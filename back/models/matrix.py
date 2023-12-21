import math
import re
import pandas as pd
import numpy as np

import copy
from services.utils import get_states, alphabet


class Matrix:
    ''' Class Matrix is used to store relevant matrix data. '''

    def __init__(
        self,
        title: str = 'TPM'
    ) -> None:
        self._digitos: dict[str: int] = {'A': '1', 'B': '0', 'C': '0'}
        self._future: str = ['A', 'B', 'C']
        self._current: str = ['A', 'B', 'C']
        self._alpha: np.array = np.array([
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0],
        ])
        self._title: str = title

#sirve para moverme libremente entre la matriz
    def as_dataframe(self) -> pd.DataFrame:
        ''' Return the dataframe data with it's states. '''
        num_row_vars: int = int(
            math.log2(self._alpha.shape[0])
        )
        num_col_vars: int = int(
            math.log2(self._alpha.shape[1])
        )
       # print("aqui"+num_col_vars, num_row_vars)

        col_states: list[str] = get_states(num_col_vars)
        row_states: list[str] = get_states(num_row_vars)

        return pd.DataFrame(
            self._alpha, columns=col_states,
            index=row_states
        )

    def set_digitos(self, digitos: str) -> None:
        ''' Set the evaluation state. '''
        # print(self._current, self._future)
        if len(digitos) != len(self._current):
            raise Exception(
                'La cantidad de dígitos no es igual a la cantidad de variables.'
            )
        if bool(re.match("^[01]+$", digitos)) is False:
            raise Exception(
                'Los dígitos no son binarios.'
            )
        # print('digitos::', digitos, self._current)
        self._digitos = {
            self._current[i]: digitos[i]
            for i in range(len(digitos))
        }

    def get_digitos(self) -> dict[str: int]:
        ''' Get the evaluation state. '''
        return self._digitos

    def set_data(self, data: np.array) -> None:
        ''' Set the matrix data. '''
        self._alpha = data
        num_col_vars: int = int(
            math.log2(self._alpha.shape[1])
        )
        num_row_vars: int = int(
            math.log2(self._alpha.shape[0])
        )
        self._current: str = alphabet(num_row_vars)
        self._future: str = alphabet(num_col_vars)

    def get_data(self) -> np.array:
        ''' Return the matrix data. '''
        return self._alpha

    def set_future(self, future: list[str]) -> None:
        ''' Set the future state. '''
        self._future = future

    def get_future(self) -> list[str]:
        ''' Get the future state. '''
        return self._future

    def set_current(self, current: list[str]) -> None:
        ''' Set the current state. '''
        self._current = current

    def get_current(self) -> list[str]:
        ''' Get the current state. '''
        return self._current

    def margin_col(self, states: str) -> None:
        self.transpose()
        self.margin_row(states, False)
        self.transpose()

    def margin_row(self, states: str, from_row=True) -> None:
        ''' Drop the ungiven channels from the matrix. '''
        actual_matrix: pd.DataFrame = self.as_dataframe()

        '''
        Si no hay estados entonces todo se marginaliza y se colapsa en una sola fila.
        '''
        states = [s for s in states]
        if states == [] or states == '':
            vector_sum = np.sum(self._alpha, axis=0)
            collapsed: pd.DataFrame = pd.DataFrame(
                vector_sum.reshape(1, -1), columns=actual_matrix.columns, index=['0']
            ) / actual_matrix.shape[0]

            self._alpha = collapsed.values

            # print('states::', states)
            self._current = states
            return

        '''
        Nos dan una cantidad definida de variables a marginalizar, podemos saber
        el tamaño de la matriz resultante para llenarla inicialmente con ceros y luego
        con los datos de la marginalización.
        '''
        new_states: list[str] = get_states(len(states))
        new_data: np.array = np.zeros((
            len(new_states), actual_matrix.shape[1]
        ))
        new_matrix: pd.DataFrame = pd.DataFrame(
            new_data, columns=actual_matrix.columns, index=new_states
        )

        '''
        La idea es que tenemos las cadenas ABC, queremos quedarnos con las que nos pasan, por ejemplo AB.
        Entonces es que obtenemos los índices de las letras dadas respecto a las del sistema original para luego seleccionarlas en cada índice del dataframe.
        '''
        new_indices = self.find_indices(self._current, states)
        max_cell_sum: int = 0

        for row in actual_matrix.index:
            for col in actual_matrix.columns:
                selected_row = self.select_chars_at_indices(row, new_indices)
                new_matrix.at[selected_row, col] += actual_matrix.at[row, col]
                if new_matrix.at[selected_row, col] > max_cell_sum:
                    max_cell_sum = new_matrix.at[selected_row, col]

        if from_row:
            # ! División por filas O columnas ! #
            self._alpha = new_matrix.values / max_cell_sum

            # ! ¿By max or by size? ! #
            # new_matrix = new_matrix / max_cell_sum
        else:
            self._alpha = new_matrix.values / \
                actual_matrix.shape[1]  # División por columnas

        self._current = states
        if from_row:
            self._digitos = {
                f'{k}': f'{v}'
                for k, v in self._digitos.items()
                if k in states
            }

    def select_chars_at_indices(self, cadena, indices) -> str:
        ''' Select the chars at the given indices. '''
        return ''.join([cadena[i] for i in indices])

    def select_serie(self) -> np.array:
        ''' Select the serie at the given digito. '''
        '''
        implementar para poder localizar los indices
        que sí se pueden tomar al momento de seleccionar el dígito en la
        posible partición de subsistemas

        De una matriz como C|ABC=101 una posible partición es en los subsistemas
        El usuario ingresa el dígito de la current string
        Luego se itera en un dictionary comprehension sobre las variables del current y se asignan los dígitos
        Luego en la iteración de los subsistemas particionados se selecciona la clave por la que esté iterándose
        y se selecciona para entonces obtener el selector del dígito.

        }
        '''
        digits: dict[str:int] = self.get_digitos()
        concat_digits: str = ''.join(digits.values())
        matrix_information = self.as_dataframe()

        estado_current: str = ''.join(self.get_current())

        if concat_digits == '' or estado_current == '':
            return self.get_data()

        return matrix_information.loc[[concat_digits]].values

    def find_indices(self, s1, s2):
        return [s1.index(char) for char in s2]

    def transpose(self):
        ''' Transpose the matrix with it's keys. '''
        self._alpha: np.array = self._alpha.transpose()
        self._future, self._current = self._current, self._future

    def copy(self):
        ''' Create a deep copy of this Matrix object. '''
        return copy.deepcopy(self)

    def get_title(self) -> str:
        ''' Get the matrix title. '''
        return self._title

    def set_title(self, title: str) -> None:
        ''' Set the matrix title. '''
        self._title = title

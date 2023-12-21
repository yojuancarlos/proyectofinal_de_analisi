import pandas as pd
from scipy.stats import wasserstein_distance
import numpy as np
from services.utils import get_states
from models.matrix import Matrix
from services.utils import combinator, get_states


class AlgoritmoPD:
    ''' Class Algoritmo is used to solve TPM. '''

    def __init__(self) -> None:
        self._tabla_resultados = {}
        self._arreglo_original_final: np.array = None
        self._mejor_particion: np.array = None

    def get_mejor_particion(self) -> np.array:
        ''' Return the best decomposition. '''
        return self._mejor_particion

    def get_arreglo_original_final(self) -> np.array:
        ''' Return the original matrix. '''
        return self._arreglo_original_final

    def run(self, matriz_original: Matrix):
        ''' Run the algorithm. '''
        '''
        1. Hallar la TPM original (marginalizando si requiere: enviar de front?)
        y seleccionar en su digito.
        '''

        # !! Marginalización de prueba !! #
        # matriz_original.margin_row(['A', 'C'])

        # print(matriz_original)

        digits: dict[str:int] = matriz_original.get_digitos()
        concat_digits: str = ''.join(digits.values())

        matrix_information = matriz_original.as_dataframe()
        tpm_original = matrix_information.loc[[concat_digits]]
        # print(tpm_original)
        self._arreglo_original_final: np.array = tpm_original.values

        print()
        '''
        Así es cómo se manejará los sistemas, de un sistema se pueden generar 02 subsistemas representados (particiones)
        com tuplas, cada una tendrá el estado futuro y presente del sistema propio (tupla misma), estas tuplas tienen
        entonces las listas de caracteres por los que se va a hacer la marginalización.
        '''

        subsistemas: list[
            list[(list[str], list[str]),
                 (list[str], list[str])]
        ] = self.obtener_particiones(matriz_original)

        emd_minima, mejor_descomp = self.hallar_emd(
            matriz_original, tpm_original.values, subsistemas
        )

        # print('EMD mínima:', emd_minima)
        # print('Mejor descomposición:', mejor_descomp)

        return emd_minima, mejor_descomp

    def hallar_emd(
        self, matriz_original: Matrix,
        matriz_tpm: np.array, subsistemas: list[
            list[(list[str], list[str]),
                 (list[str], list[str])]
        ]
    ) -> (tuple[float, tuple[list[str], list[str]]],
          tuple[list[str], list[str]]):
        ''' Calculate the EMD. '''
        future = tuple(matriz_original.get_future())
        current = tuple(matriz_original.get_current())
        llave_matriz = (future, current)

        print(llave_matriz, self._tabla_resultados)

        if llave_matriz in self._tabla_resultados:
            return self._tabla_resultados[llave_matriz]

        emd_minimo = float('inf')
        mejor_descomposicion: tuple[list[str], list[str]] = None
        '''
        Se iteran todas las posibles descomposiciones en 02 subsistemas y se calcula la EMD
        '''
        for posible_descomposicion in subsistemas:

            primer_subsistema: np.array = self.calculo_distribucion(
                matriz_original, posible_descomposicion[0]
            )
            segundo_subsistema: np.array = self.calculo_distribucion(
                matriz_original, posible_descomposicion[1]
            )
            distribucion_combinada: np.array = np.kron(
                primer_subsistema, segundo_subsistema
            )
            # Cálculo de la EMD.

            # print(matriz_tpm)
            # print(distribucion_combinada)
            # i += 1
            # print(i)

            emd = wasserstein_distance(
                matriz_tpm.flatten(), distribucion_combinada.flatten()
            )

            if emd < emd_minimo:
                emd_minimo = emd
                mejor_descomposicion = posible_descomposicion
                self._mejor_particion = distribucion_combinada

        self._tabla_resultados[llave_matriz] = (
            emd_minimo, mejor_descomposicion)
        return emd_minimo, mejor_descomposicion

    def obtener_particiones(self, sistema_original: Matrix):
        '''
        2. Descomponer en 02 subsistemas. A partir del subsistema original se marginaliza
        para obtener cada subsistema y se selecciona en su current_state respectivo a cada variable.
        Imagino crear cada subsistema como una nueva Matrix().
        '''
        future_states = sistema_original.get_future()
        current_states = sistema_original.get_current()

        states_first = get_states(len(future_states))
        states_last = get_states(len(current_states))

        return [
            [
                (combinator(future_states, combinar_primera)[0],
                 combinator(current_states, combinar_final)[0]),
                (combinator(future_states, combinar_primera)[1],
                 combinator(current_states, combinar_final)[1])
            ]
            for combinar_primera in states_first
            for combinar_final in states_last
        ]

    def calculo_distribucion(
        self, matriz: Matrix, estados: tuple[list[str], list[str]]
    ) -> np.array:
        ''' Calculate the distribution. '''
        # Copia de la matriz para marginalizar según los subsistemas.
        matriz_copia = matriz.copy()
        # La primera tupla es el current_state.
        matriz_copia.margin_row(estados[1])
        # La segunda tupla es el future_state.
        matriz_copia.margin_col(estados[0])

        matriz_serializada: np.array = matriz_copia.select_serie()
        return matriz_serializada

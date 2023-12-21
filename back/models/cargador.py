import pandas as pd
import numpy as np

from models.matrix import Matrix


class Cargador:
    ''' Class Cargador is used to load data. '''

    def __init__(self, ruta: str = 'database/datos.csv') -> None:
        self._ruta = ruta

    def load_csv_data(self) -> pd.DataFrame:
        ''' Load data from csv file. '''
        try:
            df = pd.read_csv(self._ruta, delimiter=';')
            matriz_datos: np.array = df.values
            # print(matriz_datos)
            return matriz_datos
        except Exception as e:
            print("Error loading data from CSV file:", e)
            return None

    def write_csv_data(self, matriz: Matrix, ruta: str) -> None:
      ''' Write data to csv file with a title row, overwriting existing file. '''
      try:
        titulo: str = matriz.get_title()
        dataframe: pd.DataFrame = matriz.as_dataframe()

        with open(ruta, 'w', newline='', encoding='utf-8') as csvfile:
          # Escribir el título
          csvfile.write(titulo + '\n')

        # Escribir el DataFrame, conservando los índices de fila y columna
        dataframe.to_csv(ruta, mode='a', sep=';', index=True, header=True, encoding='utf-8')
        print("Data written to CSV file successfully.")
      except Exception as e:
        print("Error writing data to CSV file:", e)

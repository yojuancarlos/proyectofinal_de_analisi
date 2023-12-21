from fastapi import FastAPI, APIRouter, UploadFile, File
from fastapi.responses import FileResponse, JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from os import getcwd
import time

import numpy as np
import pandas as pd

from models.matrix import Matrix
from models.cargador import Cargador
from services.algoritmo_pd import AlgoritmoPD
from services.utils import FOLDER_NAME, RUTA_MAT_DIN, RUTA_MAT_ORI, validar_digitos

app = FastAPI()
CLIENT_URL: str = 'http://localhost:4200'
app.add_middleware(
    CORSMiddleware, allow_origins=[CLIENT_URL],
    allow_credentials=True,
    allow_methods=['*'], allow_headers=['*']
)

# app.include_router(users.router, tags=['USERS-ROLES'])


@app.get('/', tags=['ROOT'])
def main():
    return {'message': 'Hello Math!'}


@app.post('/upload')
async def subir(file: UploadFile = File(...)):
    with open(f'{getcwd()}/{FOLDER_NAME}/{file.filename}', 'wb') as myfile:
        content = await file.read()
        myfile.write(content)
        myfile.close()
    return {'filename': file.filename}


@app.get('/resolver/{digitos}')
async def solve(digitos: str):
    start_time = time.time()
    if validar_digitos(digitos) is False:
        return {'message': 'Los dígitos no son binarios.'}
    cargador: Cargador = Cargador()
    # print(digito)
    arreglo_datos: np.array = cargador.load_csv_data()

    matriz_sistema: Matrix = Matrix('Sistema original')

    matriz_sistema.set_data(arreglo_datos)
    
    matriz_sistema.set_digitos(digitos)
    # print(matriz_sistema.as_dataframe())
    # return
    algoritmo = AlgoritmoPD()

    emd_minima, mejor_subsistema = algoritmo.run(matriz_sistema)

    arreglo_particion_original: np.array = algoritmo.get_arreglo_original_final()
    matriz_particion_original: Matrix = Matrix('Partición original')
    matriz_particion_original.set_data(arreglo_particion_original)

    arreglo_particion = algoritmo.get_mejor_particion()
    matriz_mejor_particion: Matrix = Matrix('Mejor partición')
    matriz_mejor_particion.set_data(arreglo_particion)

    cargador.write_csv_data(matriz_mejor_particion, RUTA_MAT_DIN)
    cargador.write_csv_data(matriz_particion_original, RUTA_MAT_ORI)

    subir(file=File(RUTA_MAT_DIN))
    subir(file=File(RUTA_MAT_ORI))
    end_time = time.time()  # Finaliza el contador de tiempo
    execution_time = end_time - start_time  # Calcula el tiempo de ejecución
    print(f"Tiempo de ejecución para '/some_endpoint': {execution_time} segundos")

    return JSONResponse(
        
        content={
            'message': 'EMD mínima encontrada.',
            'emd_minima': emd_minima,
            'mejor_particion': mejor_subsistema
        },
        
        status_code=200
    )


@app.get('/download/{filename}')
async def bajar(filename: str):
    return FileResponse(
        f'{getcwd()}/{FOLDER_NAME}/{filename}',
        media_type='application/octet-stream',
        filename=filename
    )

import itertools
import re
import string

FOLDER_NAME: str = 'database'
RUTA_MAT_DIN: str = 'database/solucion_matriz_dinamica.csv'
RUTA_MAT_ORI: str = 'database/solucion_matriz_original.csv'


def alphabet(n: int) -> list[str]:
    """
    Generate a list of Excel-style column names up to a given size.

    :param size: The size up to which to generate the column names.
    :return: A list of strings representing the Excel-style column names.
    """
    result: list[str] = []
    for length in range(1, n + 1):
        for combination in itertools.product(
            string.ascii_uppercase, repeat=length
        ):
            result.append(''.join(combination))
            if len(result) == n:
                return result
    return result


def combinator(STR1: list[str], STR2: list[str]):
    ''' Combinator function. '''
    ones, zeros = [], []
    for char, flag in zip(STR1, STR2):
        if flag == '1':
            ones.append(char)
        else:
            zeros.append(char)
    return ones, zeros


def get_states(size: int, binaries: list[str] = ['0', '1']):
    return [''.join(combination) for combination in itertools.product(binaries, repeat=size)]


def validar_digitos(digitos: str) -> bool:
    ''' Validate digits. '''
    return bool(re.match("^[01]+$", digitos))


def parser(chain: str) -> list[str]:
    ''' Parser function. '''
    return list(chain)

# crypto_utils.py

import numpy as np

def encrypt_number(number: int) -> str:
    """
    Cifra un número de 6 dígitos usando las reglas indicadas.

    Args:
        number (int): Número entero de 6 dígitos.

    Returns:
        str: Número cifrado como cadena.
    """
    digits = np.array([int(d) for d in str(number).zfill(6)])
    digits = (digits + 7) % 10

    # Intercambiar posiciones: 1↔3, 2↔4, 5↔6
    digits[[0, 2]] = digits[[2, 0]]
    digits[[1, 3]] = digits[[3, 1]]
    digits[[4, 5]] = digits[[5, 4]]

    return ''.join(str(d) for d in digits)


def decrypt_number(encrypted: str) -> str:
    """
    Descifra un número cifrado y devuelve el original.

    Args:
        encrypted (str): Número cifrado (6 dígitos).

    Returns:
        str: Número original como cadena.
    """
    digits = np.array([int(d) for d in encrypted])

    # Revertir los intercambios: 1↔3, 2↔4, 5↔6
    digits[[0, 2]] = digits[[2, 0]]
    digits[[1, 3]] = digits[[3, 1]]
    digits[[4, 5]] = digits[[5, 4]]

    digits = (digits - 7 + 10) % 10

    return ''.join(str(d) for d in digits)

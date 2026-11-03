import numpy as np

def calculate(numbers):
    # Validar que la lista contenga exactamente 9 números
    if len(numbers) < 9:
        raise ValueError("List must contain nine numbers.")
    
    # 1. Convertir la lista en una matriz NumPy de 3x3
    matrix = np.array(numbers).reshape(3, 3)
    
    # 2. Construir el diccionario con los cálculos solicitados
    # axis=0 -> columnas (eje vertical)
    # axis=1 -> filas (eje horizontal)
    # sin axis -> matriz aplanada
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }
    
    return calculations
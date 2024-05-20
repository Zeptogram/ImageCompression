import numpy as np
import math
from scipy.fft import dct, dctn
import os
import matplotlib.pyplot as plt


def dct_custom(vector):
    # Inizializzo le variabili
    n = len(vector)
    pi = math.pi
    dtc = []
    cos_vect = []  
    # K = 0 a n-1
    for k in range(n):
        # Vettori della base dei coseni
        wk = []
        for i in range(n):
            # Calcolo le componenti wki come cos(pi * k * (2 * i + 1) / (2 * n))
            wki = math.cos(pi * k * (2 * i + 1) / (2 * n))
            # Costruisco il vettore wk
            wk.append(wki)
        # Normalizzazione ortho per avere il confronto con
        # la dct della libreria
        if k == 0:
            # Calcolo i coefficenti ak = (v * wk) / (wk * wk)
            ak = np.dot(vector, wk) / math.sqrt(n)   # wk * wk
        else:
            ak = np.dot(vector, wk) / math.sqrt(n/2) # wk * wk
        # Salvo le basi
        cos_vect.append(wk)
        # Aggiungo alla lista gli ak
        dtc.append(ak)
    #plot_cosine_base(cos_vect)
    return dtc



def dct2_custom(matrix):
    # Creo una matrice di appoggio
    dct_matrix_row = np.zeros_like(matrix, dtype=float)
    # Applico la DCT alle righe della matrice
    for i in range(len(matrix)):
        dct_matrix_row[i, :] = dct_custom(matrix[i, :])
    # Applico la DCT alle colonne della matrice dct righe
    dct_matrix_col = dct_matrix_row.T
    for i in range(len(dct_matrix_col)):
        dct_matrix_col[i, :] = dct_custom(dct_matrix_col[i, :])
    # Rifaccio la traposta e ritorno la matrice
    return dct_matrix_col.T

def dct_library(vector):
    return dct(vector, 2, norm='ortho')


def dct2_library(matrix):
    return dctn(matrix, 2, norm='ortho')



# Per debugging stampa delle basi dei coseni per vedere se sono corrette
def plot_cosine_base(base):
    n = len(base[0])  # Lunghezza della base
    num_base = len(base)
    ncols = 3  # Numero di colonne nella griglia
    nrows = -(-num_base // ncols)  # Calcolo del numero di righe
    fig, axes = plt.subplots(nrows, ncols, figsize=(12, 8))
    for i, wk in enumerate(base):
        row = i // ncols
        col = i % ncols
        axes[row, col].bar(range(n), wk, label=f'k={i}')
        axes[row, col].set_xlabel('Indice i fino a n')
        axes[row, col].set_ylabel('Valore')
        axes[row, col].set_title(f'Basi dei Coseni per k={i} oscillazioni')
        axes[row, col].legend()
    plt.tight_layout()
    plt.show()

def write_results_to_file(dtype, result):
    # Verifica se il file "dct_results" esiste già
    file_name = "dct_results.txt"
    file_exists = os.path.exists(file_name)
    # Se il file non esiste, crea un nuovo file "dct_results.txt"
    if not file_exists:
        with open(file_name, "w") as file:
            file.write("====[ RISULTATI DCT E DCT2 ]====\n\n")
    # Scrivi i dati nella tupla nel file
    with open(file_name, "a") as file:
        file.write('=== {} ===\n'.format(dtype))
        file.write('Result: {}\n'.format(result))
        file.write("")
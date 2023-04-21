import numpy as np
import pandas as pd


# np.random.rand(rows, columns) - NumPy Matrix of Random Floats

# generates int matrix
def generate_matrix(mk, kn, a, z):
    return np.random.randint(a, z, (mk, kn))


# write matrix into dataframe and save the dataframe in the csv file
def save_in_cvs(matrix, file_address):
    dataframe = pd.DataFrame(matrix)
    dataframe.to_csv(file_address, index=False, header=False)


# extract matrix from csv files
def take_matrix_from_csv(file_address):
    file = open(file_address)
    matrix = np.loadtxt(file, delimiter=",", dtype='int')
    file.close()
    return matrix
from functions import take_matrix_from_csv
import numpy as np
from time import time

MATRIX_A_FILE = "matrix_A.csv"
MATRIX_B_FILE = "matrix_B.csv"
matrix_A = take_matrix_from_csv(MATRIX_A_FILE)
matrix_B = take_matrix_from_csv(MATRIX_B_FILE)

# multiple launch multiplication calculation
yes = ['да', 'yes', 'YES', 'y', 'Y', 'ДА', 'Да', 'Yes']
repeat = 'yes'
while repeat in yes:
    start = time()
    # multiplication of two matrices
    matrix_C = np.dot(matrix_A, matrix_B)
    time_par = time() - start
    # осуществить запись в файл данных + подсчет статистики
    print('Время выполнения умножения матриц составило {:.2f} секунд'.format(time_par))
    repeat = input('Повторить процесс?: ')
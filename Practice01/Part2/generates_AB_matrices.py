from functions import generate_matrix, save_in_cvs

M = 700
K = 400
N = 900
MATRIX_A_FILE = "matrix_A.csv"
MATRIX_B_FILE = "matrix_B.csv"
start_value = int(input("Введите диапазон значений элементов матрицы - от: "))
end_value = int(input("Введите диапазон значений элементов матрицы - до: "))
# generating matrixes A and B
matrix_A = generate_matrix(M, K, start_value, end_value)
matrix_B = generate_matrix(K, N, start_value, end_value)
# Saving to a csv.file
save_in_cvs(matrix_A, MATRIX_A_FILE)
save_in_cvs(matrix_B, MATRIX_B_FILE)

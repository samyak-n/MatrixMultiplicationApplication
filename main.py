'''
Main file for the Matrix Multiplication software.
'''
import tkinter as tk
from tkinter import filedialog
from matrix_operations import MatrixOperations
from matrix_gui import MatrixGUI
def run_experiment(matrix_operations):
    # Define the parameters for the experiment
    matrix_sizes = [8, 16, 32, 64, 128, 256, 512, 1024]
    repeats = 10
    # Perform the runtime experiment
    results = []
    for size in matrix_sizes:
        total_time_iterative = 0
        total_time_divide_and_conquer = 0
        total_time_strassen = 0
        for _ in range(repeats):
            # Generate random matrices
            matrix1 = matrix_operations.generate_random_matrix(size)
            matrix2 = matrix_operations.generate_random_matrix(size)
            # Measure the execution time for each algorithm
            time_iterative = matrix_operations.time_execution(matrix_operations.iterative_matrix_multiplication, matrix1, matrix2)
            time_divide_and_conquer = matrix_operations.time_execution(matrix_operations.divide_and_conquer_matrix_multiplication, matrix1, matrix2)
            time_strassen = matrix_operations.time_execution(matrix_operations.strassen_algorithm, matrix1, matrix2)
            # Accumulate the total execution time
            total_time_iterative += time_iterative
            total_time_divide_and_conquer += time_divide_and_conquer
            total_time_strassen += time_strassen
        # Calculate the average execution time for each algorithm
        average_time_iterative = total_time_iterative / repeats
        average_time_divide_and_conquer = total_time_divide_and_conquer / repeats
        average_time_strassen = total_time_strassen / repeats
        # Append the results to the list
        results.append([size, average_time_iterative, average_time_divide_and_conquer, average_time_strassen])
    # Save the results to a CSV file
    with open('results.csv', 'w') as file:
        file.write('Matrix Size,Iterative Time,Divide-and-Conquer Time,Strassen Time\n')
        for result in results:
            file.write(','.join(map(str, result)) + '\n')
def main():
    root = tk.Tk()
    matrix_operations = MatrixOperations()
    matrix_gui = MatrixGUI(root, matrix_operations)
    matrix_gui.run()
    # Run the experiment after the GUI is closed
    run_experiment(matrix_operations)
if __name__ == "__main__":
    main()
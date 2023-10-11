'''
Module for the Matrix GUI.
'''
import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog
class MatrixGUI:
    def __init__(self, root, matrix_operations):
        self.root = root
        self.matrix_operations = matrix_operations
        self.matrix1 = None
        self.matrix2 = None
        self.root.title("Matrix Multiplication")
        self.root.geometry("400x300")
        self.label_matrix1 = tk.Label(self.root, text="Matrix 1")
        self.label_matrix1.pack()
        self.button_load_matrix1 = tk.Button(self.root, text="Load Matrix 1", command=self.load_matrix1)
        self.button_load_matrix1.pack()
        self.label_matrix2 = tk.Label(self.root, text="Matrix 2")
        self.label_matrix2.pack()
        self.button_load_matrix2 = tk.Button(self.root, text="Load Matrix 2", command=self.load_matrix2)
        self.button_load_matrix2.pack()
        self.button_multiply = tk.Button(self.root, text="Multiply", command=self.multiply_matrices)
        self.button_multiply.pack()
    def load_matrix1(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.matrix1 = self.matrix_operations.load_matrix(filename)
            messagebox.showinfo("Success", "Matrix 1 loaded successfully.")
    def load_matrix2(self):
        filename = filedialog.askopenfilename()
        if filename:
            self.matrix2 = self.matrix_operations.load_matrix(filename)
            messagebox.showinfo("Success", "Matrix 2 loaded successfully.")
    def multiply_matrices(self):
        if self.matrix1 is None or self.matrix2 is None:
            messagebox.showerror("Error", "Please load both matrices.")
        else:
            result = self.matrix_operations.iterative_matrix_multiplication(self.matrix1, self.matrix2)
            messagebox.showinfo("Result", str(result))
    def run(self):
        self.root.mainloop()
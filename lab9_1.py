import numpy as np
import itertools

def generate_permutations(n):
    """
    creates a list of all permutations of numbers from 0 to n-1.
    """
    return list(itertools.permutations(range(n)))

def calculate_product(matrix, permutation):
    """
    calculates the product of matrix elements for a specific permutation.
    """
    product = 1
    for i in range(len(matrix)):
        product *= matrix[i][permutation[i]]  
        
    if count_inversions(permutation) % 2 == 1: # the sign of the product depends on the amount of inversions in the permutation
        product *= -1  
    
    return product

def count_inversions(permutation):
    """
    counts the number of inversions in the permutation
    """
    inversion = 0
    for i in range(len(permutation)):
        for j in range(i + 1, len(permutation)):
            if permutation[i] > permutation[j]:
                inversion += 1
    return inversion

def calculate_determinant(matrix):
    """
    calculates the determinant of a matrix using the method of permutations
    """
    n = len(matrix)
    permutations = generate_permutations(n)
    det = 0
    for i in permutations:
        det += calculate_product(matrix, i)
    return det

def main():
    """
    function to get the matrix size from user, create a random matrix, and calculate a determinant.
    """
    try:
        dim = int(input("Enter the size of a matrix: "))
        if dim <= 0 or dim > 5:
            raise ValueError
    except ValueError:
        print('Error! Enter a positive integer that is not bigger than 5.')
        return

    matrix = np.random.randint(10, size=(dim, dim))
    print(matrix)
    print('det =', calculate_determinant(matrix))

main()

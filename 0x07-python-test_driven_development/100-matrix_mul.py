#!/usr/bin/python3

def matrix_mul(m_a, m_b):
    """ Validate m_a and m_b as lists of lists """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if not all(isinstance(row, list) for row in m_a) or not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_a must be a list of lists and m_b must be a list of lists")

    """ Validate m_a and m_b are not empty """
    if not m_a or not m_b:
        raise ValueError("m_a can't be empty and m_b can't be empty")

    """ Validate m_a and m_b contain only integers or floats """
    for row in m_a + m_b:
        if not all(isinstance(num, (int, float)) for num in row):
            raise TypeError("m_a should contain only integers or floats and m_b should contain only integers or floats")

    """ Validate m_a and m_b are rectangular matrices (all rows have the same size) """
    num_cols_a = len(m_a[0])
    num_cols_b = len(m_b[0])
    if not all(len(row) == num_cols_a for row in m_a) or not all(len(row) == num_cols_b for row in m_b):
        raise TypeError("Each row of m_a must be of the same size and each row of m_b must be of the same size")

    """ Validate that m_a and m_b can be multiplied (number of columns in m_a is equal to number of rows in m_b) """
    if num_cols_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    """ Perform matrix multiplication """
    result = [[0 for _ in range(len(m_b[0]))] for _ in range(len(m_a))]
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for k in range(len(m_b)):
                result[i][j] += m_a[i][k] * m_b[k][j]

    return result


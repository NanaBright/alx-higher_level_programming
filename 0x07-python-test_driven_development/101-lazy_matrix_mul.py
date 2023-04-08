#!/usr/bin/python3

import numpy as np

def lazy_matrix_mul(m_a, m_b):
    try:
        # Convert input matrices to NumPy arrays
        m_a = np.array(m_a)
        m_b = np.array(m_b)

        # Perform matrix multiplication using dot product
        result = np.dot(m_a, m_b)

        return result.tolist()  # Convert the result back to a regular Python list

    except ValueError as ve:
        raise ValueError("m_a and m_b can't be multiplied") from ve
    except Exception as e:
        raise type(e)("An error occurred during matrix multiplication") from e

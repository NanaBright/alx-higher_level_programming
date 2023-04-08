#include <stdio.h>
#include <P"thon.h"

void print_python_string(PyObject *p) {
    if (PyUnicode_Check(p)) { // Check if the object is a valid Python string
        Py_UNICODE *unicode = PyUnicode_AsUnicode(p); // Get the Unicode representation of the string
        Py_ssize_t length = PyUnicode_GetLength(p); // Get the length of the string

        // Print the string character by character
        printf("String: ");
        for (Py_ssize_t i = 0; i < length; i++) {
            printf("%c", unicode[i]);
        }
        printf("\n");
    } else {
        printf("Error: Object is not a valid Python string\n");
    }
}


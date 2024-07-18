import array as arr
import os
import sys
import matplotlib.pyplot as plt
import numpy as np
from collections import Counter
import datetime


def graph_function():
    x_axis_points = np.array([1, 10])
    y_axis_points = np.array([1, 10])

    plt.plot(x_axis_points, y_axis_points)
    plt.grid()
    plt.show()


def get_the_paths():
    code_path = os.getcwd()
    print(code_path + ' - With help of getcwd()')

    code_directory_path = os.path.dirname(sys.argv[0])
    print(code_directory_path + ' - Directory name with help of sys.argv[0]')
    code_file_path = os.path.abspath(sys.argv[0])
    print(code_file_path + ' - File name with help of sys.argv[0]')

    python_directory_path = os.path.dirname(sys.executable)
    print(python_directory_path + ' - Python executable installation directory path using sys.executable')
    python_file_path = os.path.abspath(sys.executable)
    print(python_file_path + ' - Python executable installation absolute path using sys.executable')


def types_in_python():
    ar = arr.array('i', [1, 3, 4, 4])
    li = [1, 2, 3, 'a']
    tup = (1, 2, 3, 4, 5)
    print(ar, li, tup)
    print(type(ar), type(li), type(tup))


def two_sum_input():
    length_of_list = int(input('Enter the length of list '))
    numbers = list()
    for i in range(0, length_of_list):
        numbers.append(int(input('Enter value at list in ' + str(i + 1) + ' position ')))
    target = int(input('Enter target value '))
    return target, numbers


def two_sum(f_target: int, f_numbers: list[int]):
    hash_var = dict()
    for i in range(len(f_numbers)):
        temp_num = f_target - f_numbers[i]
        if temp_num in hash_var:
            return [hash_var[temp_num], i]
        hash_var[f_numbers[i]] = i


if __name__ == '__main__':
    # get_the_paths()
    # types_in_python()
    # print(two_sum(*two_sum_input()))
    # graph_function()
    test_var = 3.123123
    test_var1 = round(test_var, 5)
    #print(f'This is the string {test_var:.2f} and {test_var1}')
    red1 = 'This is the masterpiece of code that you are writing Champ'
    my_counter = Counter(red1)
    print(my_counter)
    print(my_counter.items())


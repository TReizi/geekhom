from termcolor import colored, cprint
from typing import List
class Matrix:
    def __init__(self, matrix_data: List[List]):
        self.__matrix = matrix_data

        m_rows = len(self.__matrix)
        self.__matrix_size = frozenset([(m_rows, len(row)) for row in self.__matrix])
        if len(self.__matrix_size) != 1:
            raise ValueError("Invalid matrix size")

    def __add__(self, other: "Matrix") -> "Matrix":
        if not isinstance(other, Matrix):
            raise TypeError(f"'{other.__class__.__name__}' "
                            f"incompatible object type")
        if self.__matrix_size != other.__matrix_size:
            raise ValueError(f"Matrix sizes difference")

        result = []

        for item in zip(self.__matrix, other.__matrix):
            result.append([sum([j, k]) for j, k in zip(*item)])
        return Matrix(result)

    def __str__(self) -> str:
        return '\n'.join(['\t'.join(map(str, row)) for row in self.__matrix])


if __name__ == '__main__':

    matrix1 = Matrix([[10, 30], [50, 90]])
    print(colored('Первая матрица', 'red', attrs=['underline']))
    print(colored(matrix1, 'red', attrs=['underline']))
    matrix2 = Matrix([[50, 100], [320, 440]])
    print(colored('Вторая матрица', 'green', attrs=['underline']))
    print(colored(matrix2, 'green', attrs=['underline']))
    #Не понравилось просто как выглядит)
    #cprint('Результат сложения двух матриц ', 'green', 'on_blue')
    #cprint(matrix1 + matrix2 , 'green', 'on_red')
    print(f'Результат сложения двух матриц \n{(matrix1 + matrix2 )}')

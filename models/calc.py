from random import randint

class Calc:
    def __init__(self: object, dificulty: int) -> None:
        self.__dificulty: int = dificulty
        self.__value1: int = self.generate_value
        self.__value2: int = self.generate_value
        self.__operation: int = randint(1, 3)
        self.__result: int = self.generate_result

    
    @property
    def dificulty(self: object) -> int:
        return self.__dificulty

    @property
    def value1(self: object) -> int:
        return self.__value1

    @property
    def value2(self: object) -> int:
        return self.__value2

    @property
    def operation(self: object) -> int:
        return self.__operation

    @property
    def result(self: object) -> int:
        return self.__result

    def __str__(self: object) -> str:
        op: str = ''
        if self.operation == 1:
            op = 'Somar'
        elif self.operation == 2:
            op = 'Subtrair'
        elif self.operation == 3:
            op = 'Multiplicar'
        else:
            op = 'Operação desconhecida'
        return f'Valor 1: {self.value1}\nValor 2: {self.value2}\nDificuldade: {self.dificulty}\nOperação: {op}'

    @property
    def generate_value(self: object) -> int:
        values = {
            1: randint(0,10),
            2: randint(0,100),
            3: randint(0,1000),
            4: randint(0,10000)
        }

        try:
            return values[self.dificulty]
        except Exception as e:
            print(f'Dificuldade inválida, Erro: {e}')

    @property
    def generate_result(self: object) -> int:
         operations = {
            1: self.value1 + self.value2,
            2: self.value1 - self.value2,
            3: self.value1 * self.value2
        }

        try:
            return operations[self.operation]
        except Exception as e:
            print(f'Dificuldade inválida')

    def check_result(self: object, answer: int) -> bool:
        correct: bool = False
        if self.result == answer:
            correct = True
        else:
            print('Resposta incorreta')

        return correct

    def show_operation(self: object) -> None:
        pass






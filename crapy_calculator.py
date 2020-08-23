import time

class CalcError(Exception):
    pass

class Calculator:
    """
    Crappy calculator
    """
    def add(self, a, b):
        """
        Addition. Max execution time 1 sec.
        Does not like when a == 100.
        :param a: int or float
        :param b: int or float
        :return: int or float
        """
        if a == 100:
            raise CalcError()
        return a + b

    def subtr(self, a, b):
        """
        Subtraction. Max execution time 1 sec.
        :param a: int or float
        :param b: int or float
        :return: int or float
        """
        return a - b

    def multiply(self, a, b):

        """
        Multiplication. Max execution time 1 sec.
        If a == 100 calculates for 3 sec.
        :param a: int or float
        :param b: int or float
        :return: int or float
        """
        if a == 100:
            time.sleep(3)
        return a * b

    def divide(self, a, b):
        """
        Division. Max execution time 1 sec.
        When division by 0 returns None, does not rais an error, outputs "div_by_0"
        :param a: int or float
        :param b: int or float
        :return: int or float
        """
        if b == 0:
            print("div_by_0")
        else:
            return a / b


if __name__ == '__main__':
    calc = Calculator()
    operations = [calc.add,
                  calc.subtr,
                  calc.multiply,
                  calc.divide
                  ]
    operation = ""
    while operation != "q":
        for i, operation in enumerate(operations, start=1):
            print(f"{i}: {operation.__name__}")
        print("q: quit")
        operation = input("Выберете операцию: ")
        if operation in ["1","2","3","4"]:
            op = int(operation)
            a = float(input("Введите a:"))
            b = float(input("Введите b:"))
            print(operations[op - 1](a, b),'\n')
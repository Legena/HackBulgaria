from random import randint


class Expression():
    def generate_expression():
        signs = ['+', '-', '*', '/']
        choice = randint(1, 4)
        sign = signs[choice - 1]
        left_number = randint(0, 100)
        right_number = randint(0, 100)
        answer = 0
        if sign == '+':
            answer = left_number + right_number
        elif sign == '-':
            answer = left_number - right_number
        elif sign == '*':
            answer = left_number * right_number
        else:
            answer = round(left_number / right_number, 2)
        return (left_number, right_number, sign, answer)
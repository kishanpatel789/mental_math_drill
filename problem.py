import random

class Problem():
    valid_operators = ['+', '-', '*', '/']

    def __init__(self, first_num, second_num, operator) -> None:
        if isinstance(first_num, int) and isinstance(second_num, int):
            self.first_num = first_num
            self.second_num = second_num
        else:
            raise TypeError(f"First number and second number should be integers.")
        
        if operator in self.__class__.valid_operators:
            self.operator = operator
        else:
            raise ValueError(f"Operator should be one of {self.__class__.valid_operators}. Recieved '{operator}'.")
        
        if operator == '+':
            self.answer = first_num + second_num
        elif operator == '-':
            self.answer = first_num - second_num
        elif operator == '*':
            self.answer = first_num * second_num
        elif operator == '/':
            self.answer = first_num / second_num
        else:
            self.answer = None

    def render(self):
        first_str = str(self.first_num)
        second_str = str(self.second_num)
        max_num_len = max(len(first_str), len(second_str))
        output = f"{first_str.rjust(max_num_len + 3)}\n"
        output += f"{self.operator} {second_str.rjust(max_num_len + 1)}\n"
        output += f"{'‾'*(max_num_len + 3)}"

        return output

def generate_problems(num_probs: int):
    problems = []

    for _ in range(num_probs):
        operator = random.choice(Problem.valid_operators)
        first_num = random.randint(2, 999)
        second_num = random.randint(2, 999)
        prob = Problem(first_num, second_num, operator)
        problems.append(prob)

    return problems
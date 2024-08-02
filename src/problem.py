import random

class Problem():
    valid_operators = ['+', '-', '*', '/']

    def __init__(self, first_num, second_num, operator) -> None:
        if isinstance(first_num, int) and isinstance(second_num, int):
            self.first_num = first_num
            self.second_num = second_num

            first_str = str(self.first_num)
            second_str = str(self.second_num)

            self.max_num_len = max(len(first_str), len(second_str))
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

        self.display_components = [
            f"{first_str.rjust(self.max_num_len + 2)}",
            f"{self.operator} {second_str.rjust(self.max_num_len)}",
            f"{'‾'*(self.max_num_len + 2)}",
        ]

    def render(self):
        return '\n'.join(self.display_components)
    
    def print(self):
        print(self.render())

def generate_problems(num_probs: int, operators = ['+', '-', '*', '/']):

    if not all(o in Problem.valid_operators for o in operators):
        raise ValueError(f"Operators must be subset of '{Problem.valid_operators}'. Received '{operators}'.")
    
    if len(operators) == 0:
        raise ValueError(f"Must choose at least one operator from the following: '{Problem.valid_operators}'. Received '{operators}'.")


    problems = []
    for _ in range(num_probs):
        operator = random.choice(operators)
        first_num = random.randint(2, 999)
        second_num = random.randint(2, 999)
        prob = Problem(first_num, second_num, operator)
        problems.append(prob)

    return problems
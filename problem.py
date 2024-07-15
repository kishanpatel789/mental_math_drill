class Problem():
    def __init__(self, first_num, second_num, operator) -> None:
        if isinstance(first_num, int) and isinstance(second_num, int):
            self.first_num = first_num
            self.second_num = second_num
        else:
            raise TypeError(f"First number and second number should be integers.")
        
        if operator in ('+', '-', '*', '/'):
            self.operator = operator
        else:
            raise ValueError(f"Operator should be one of '+', '-', '*', '/'. Recieved '{operator}'.")
        
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

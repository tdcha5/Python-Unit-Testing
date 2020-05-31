availableOperations = ["Add", "Subtract", "Divide","Multiply"]

def calculate(operator, x, y):
    if operator == "Add":
        return x + y
    if operator == "Subtract":
        return x - y
    if operator == "Divide":
        if y == 0:
            return ValueError('Cannot divide by zero')
        return x / y    
    if operator == "Multiply":
        return x * y
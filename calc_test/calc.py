
def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    if y == 0:
        raise ValueError('Cannot divide by zero!')
    return x / y


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
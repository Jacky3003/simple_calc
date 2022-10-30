def basic_calculator(a, b, operator):
    if(a.isnumeric() and b.isnumeric()):
        a = float(a)
        b = float(b)
        if(operator == '+'):
            result = a + b
        elif(operator == '-'):
            result = a - b
        elif (operator == 'x'):
            result = a*b
        elif(operator == '/'):
            result = a/b
        elif(operator == 'mod'):
            result = a%b
        elif(operator == "*"):
            result = a**b
        else:
            result = "Please enter a valid value."
    else:
        result = 'Please enter a valid value.'
    return result
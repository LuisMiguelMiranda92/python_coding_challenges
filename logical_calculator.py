"""
Given an array of Boolean values and a logical operator, return a Boolean result based on sequentially applying the operator to the values in the array.

Examples
booleans = [True, True, False], operator = "AND"
True AND True -> True
True AND False -> False
return False
booleans = [True, True, False], operator = "OR"
True OR True -> True
True OR False -> True
return True
booleans = [True, True, False], operator = "XOR"
True XOR True -> False
False XOR False -> False
return False

"""
def logical_calc(array, op):
    
    if op == 'AND':
        value=True
        for i in range(len(array)):
            if array[i] == True and value == True:
                value = True
            elif array[i] == True and value == False:
                value = False
            elif array[i] == False and value == True:
                value = False
            elif array[i] == False and value == False:
                value = False
    if op == 'OR':
        value=False
        for i in range(len(array)):
            if array[i] == True and value == True:
                value = True
            elif array[i] == True and value == False:
                value = True
            elif array[i] == False and value == True:
                value = True
            elif array[i] == False and value == False:
                value = False
    if op == 'XOR':
        value=False
        for i in range(len(array)):
            if array[i] == True and value == True:
                value = False
            elif array[i] == True and value == False:
                value = True
            elif array[i] == False and value == True:
                value = True
            elif array[i] == False and value == False:
                value = False
                
    return value

"""
or
def logical_calc(array, op):
    if op == 'AND':
        return all(array)
    elif op == 'OR':
        return any(array)
    if op == 'XOR':
        value=False
        for i in range(len(array)):
            if array[i] == True and value == True:
                value = False
            elif array[i] == True and value == False:
                value = True
            elif array[i] == False and value == True:
                value = True
            elif array[i] == False and value == False:
                value = False
                
    return value

"""
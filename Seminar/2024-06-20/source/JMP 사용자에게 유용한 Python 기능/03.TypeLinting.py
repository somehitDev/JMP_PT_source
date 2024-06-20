# -*- coding: utf-8 -*-

def fn_add(a:int, b:int) -> int:
    """
    add a:int and b:int

    return int
    """
    return a + b

def fn_sub(a:int, b:int) -> int:
    """
    sub a:int and b:int

    return int
    """
    return a - b

def fn_multiply(a:int, b:int) -> int:
    """
    multiply a:int and b:int

    return int
    """
    return a * b

def fn_divide(a:int, b:int) -> float:
    """
    divide a:int and b:int

    return float
    """
    return a / b

def fn_equal(a:float, b:float) -> bool:
    """
    check equal a:int and b:int

    return bool
    """
    return a == b


var_a, var_b = 1, 2

print(f"fn_add: {fn_add(var_a, var_b)}")
print(f"fn_sub: {fn_sub(var_a, var_b)}")
print(f"fn_multiply: {fn_multiply(var_a, var_b)}")
print(f"fn_divide: {fn_divide(var_a, var_b)}")
print(f"fn_equal: {fn_equal(var_a, var_b)}")

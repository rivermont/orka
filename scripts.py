
###################
# TEMP CONVERSION #
###################


def convert(amount, unit_from, unit_to):
    if unit_from.lower() == 'c':
        if unit_to.lower() == 'f':
            return c_to_f(amount)
        elif unit_to.lower == 'k':
            return c_to_k(amount)
        else:
            return "Error"
    elif unit_from.lower() == 'f':
        if unit_to.lower() == 'c':
            return f_to_c(amount)
        elif unit_to.lower() == 'k':
            return f_to_k(amount)
        else:
            return "Error"
    elif unit_from.lower() == 'k':
        if unit_to.lower() == 'c':
            return k_to_c(amount)
        elif unit_to.lower() == 'f':
            return k_to_f(amount)
        else:
            return "Error"
    else:
        return "Error"


def f_to_c(temp):
    """
    Converts Fahrenheit to Celsius.
    """
    return (temp - 32) * 5/9


def c_to_f(temp):
    """
    Converts Celsius to Fahrenheit.
    """
    return temp * 9/5 + 32


def c_to_k(temp):
    """
    Converts Celsius to Kelvin.
    """
    return temp + 273.15


def k_to_c(temp):
    """
    Converts Kelvin to Celsius.
    """
    return temp - 273.15


def f_to_k(temp):
    """
    Converts Fahrenheit to Kelvin.
    """
    return (temp + 459.67) * 5/9


def k_to_f(temp):
    """
    Converts Kelvin to Fahrenheit.
    """
    return temp * 9/5 + 459.67

def es_parentesis(caracter):
    """
    (str of len == 1) -> str

    >>> es_parentesis('(')
    'Es parentesis'
    >>> es_parentesis('x')
    'No es parentesis'
    >>> es_parentesis('xa')
    Traceback (most recent call last):
    ..
    TypeError: xa no es parentesis

    :param caracter: srt el catacter a evaluar
    :return: srt el mensaje de la validacion
    """

    if len(caracter) !=1:
        raise TypeError(str(caracter) + ' no es un parentesis')
    elif caracter in '()': # caracter == '(' or caracter
        return 'Es parentesis'
    return  'No es parentesis'
pass

def es_par(num):
    """

    num -> bool

    Determina si el numero es par

    >>> es_par(0)
    true

    >>> es_par(7)
    false

    :param num: el numero a evaluar
    :return: true si es par false de lo contrario
    """
    return num % 2 != 0


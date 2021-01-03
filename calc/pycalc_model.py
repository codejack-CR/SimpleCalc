import re


ERROR_MSGS = ["ERROR", "NOT A VALID EXPRESSION"]


def evaluate(expr):
    try:
        if re.search('[a-zA-Z]', expr):
            result = ERROR_MSGS[1]
        else:
            result = str(eval(expr))
    except Exception:
        result = ERROR_MSGS[0]
    return result

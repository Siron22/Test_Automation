""""
def decorator():
pass

@decorator
def func():
pass

func = decorator(func)
==============================
def decorator():
pass

@decorator(param)
def func():
pass

func = decorator(param)(func)


"""

def bold_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<b>{func(*args, **kwargs)}</b>"
    return wrapper


def italic_decorator(func):
    def wrapper(*args, **kwargs):
        return f"<i>{func(*args, **kwargs)}</i>"
    return wrapper


def style_decorator(style):
    def decorator(func):
        def wrapper(*args, **kwargs):
            return f"<{style}>{func(*args, **kwargs)}</{style}>"
        return wrapper
    return decorator



# @italic_decorator
# @bold_decorator

@style_decorator('b')
@style_decorator('i')
def greetings(name):
    return f"Hello, {name}"

print(greetings("Andrew"))


"""
<b>text</b> 
<i>text</i>
"""

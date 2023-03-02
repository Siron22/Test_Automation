#https://www.tutorialspoint.com/execute_python3_online.php
# Python 3.10

def print_hello(language):
    match language:
        case "spanish":
            print("Hola")
        case "english":
            print("Hello")
        case "german":
            print("Hallo")
        case _:
            print("Can't translate")


print_hello("english")  # Hello
print_hello("german")  # Hallo
print_hello("spanish")  # Hola
print_hello("haramamburu")  # Can't translate
# 1
def caching_fibonacci():
    
    cache = {}

    def fibonacci(n):
        if n <= 0:
            return 0
        if n == 1:
            return 1
        if n in cache:
            return cache[n]
        cache[n] = fibonacci(n-1) + fibonacci(n-2)
        return cache[n]
        
    return fibonacci
numbers = caching_fibonacci()
print(numbers(10))


# 2
import re 

def generator_numbers (text):

    numbers = re.findall(r"\d+\.\d+", text)
    for num in numbers:
        yield float(num)
def sum_profit(text: str, func):
    return sum(func(text))
        
text = "Загальний дохід працівника складається з декількох частин: 1000.01 як основний дохід, доповнений додатковими надходженнями" \
" 27.45 і 324.00 доларів."

total_income = sum_profit(text, generator_numbers)
print(f"Загальний дохід: {total_income}")


# 4

def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please"
        except KeyError:
            return "Contact not found"
        except IndexError:
            return "Not enough arguments"
    return inner

contacts = {}
    
@input_error
def add_contact(args,contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added"
    
@input_error
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return f"Contact {name} changed."

@input_error
def get_phone(args,contacts):
    name = args[0]
    return contacts[name]
    
@input_error
def show_all (contacts):
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"
    return result.strip()
    
commands = {
    "add": add_contact,
    "change": change_contact,
    "phone": get_phone,
    "all": show_all
    }


while True:
    command_input = input("Enter a comand:").split()
    if not command_input:
        continue

    command = command_input[0]
    args = command_input[1:]

    if command in ["exit", "close", "goodbye"]:
        print("Goodbye!")
        break

    if command in commands:
        func = commands[command]
            
        if command == "all":
            print(func(contacts))
        else:
            print(func(args, contacts))

    else:
        print("Unknown command")

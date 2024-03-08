#Calculator

def add(n1,n2):
  return n1 + n2

def subtract(n1,n2):
  return n1 - n2 

def multiply(n1,n2):
  return n1*n2

def divide(n1,n2):
  return n1 / n2 

operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide 
}

def calculator():
  num1 = float(input("Whats the first num: "))
  while True:
    for operation in operations:
      print(operation)
    action = input("What's the action you want to do: ")
    num2 = float(input("Whats the second num: "))
    calculation_function = operations[action]
    answer = calculation_function(num1, num2)

    print(f"{num1} {action} {num2} = {answer}")

    do_we_continue = input(f"Would you like to continue with {answer} type 'y', or type 'n' to exit: ").lower()

    if do_we_continue == 'y':
        num1 = answer
    elif do_we_continue == 'n':
      num1 = float(input("What's next number?: "))
    else:
      break

calculator()

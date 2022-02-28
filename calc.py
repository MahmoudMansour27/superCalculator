#Keep it clean as possible all the time :)
#instructions
print("Instructions:\n1.Don't use letter as inputs\n2.Don't for get choose an operation\n")
#inputs
flag = 1
while flag == 1:
    try:
        enter1 = input("enter you first number: ")
        enter2 = input("enter you sec number: ")
        num1 = int(enter1)
        num2 = int(enter2)
        result = num1 + num2
    except ValueError as err:
        print(err)
        print("Please enter numbers :(")
    else:
        break

#main functions
def sum():
    result = num1 + num2
    return result
def sub():
    result = num1 - num2
    return result
def mul():
    result = num1 * num2
    return result
def div():
    result = num1 / num2
    return result
def rem():
    result = num1 % num2
    return result
def Pow():
    result = pow(num1, num2)
    return result
def Max():
    results = max(num1, num2)
    return results
def Min():
    results = min(num1, num2)
    return results
#calculator main loop
while 1 == 1:
    print("\nchoose an operation \"type the number or the complete word\":\n1.Summation\n2.Subtraction\n3.Multiplication\n4.Division\n5.Remainder\n6.Power\n7.Maximum number\n8.Minimum number")
    inputChoice = input("Operation is: ")
    choice = inputChoice.lower()
    if choice in ["1", "sum", "Summation", "summation", "جمع"]:
        print(sum())
    elif choice in ["2", "sub", "Subtraction", "subtraction", "طرح"]:
        print(sub())
    elif choice in ["3", "mul", "Multiplication", "multiplication", "ضرب"]:
        print(mul())
    elif choice in ["4", "div", "Division", "division", "قسمة"]:
        print(div())
    elif choice in ["5", "rem", "Remainder", "remainder", "باقى القسمة"]:
        print(rem())
    elif choice in ["6", "pow", "Power", "power", "الاس"]:
        print(Pow())
    elif choice in ["7", "max", "Maximum number", "maximum number", "الاكبر"]:
        print(Max())
    elif choice in ["8", "min", "Minimum number", "minimum number", "الاصغر"]:
        print(Min())
    else:
        print("undefined operation :(")
    again = input("Do you want to calculate again?\n1.Yes\n2.No\n")
    if again in ["1", "yes", "y", "yep"]:
        continue
    else:
        print("Thank you for using my calculator :)\n-I will be very thankful about your feedback")
        break




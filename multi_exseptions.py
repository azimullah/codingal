try:
    num = eval(int(input("Enter two numbers, separated by comma : ")))
    result = num1 / num2
    print("The result is", result)


except ZeroDivisionError :
    print("divison by zero is error")
except SyntaxError:
    print("comma is missing.Enter numberts separated by comma like this 1,2")
except:
        print("wrong input")
else:
        print("no exception ")
finally:
     print("this will execute no matter what")
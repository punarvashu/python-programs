#Exercise 2
#Design a calculator which will correctly solve all the problem except the following ones:
#   45 * 3 = 555, 56 + 9 = 77, 56 / 2 = 4

print("Welcome To Calculator")
print("Enter First Number")
num1=int(input())
print("Enter Second Number")
num2=int(input())
print("Choose + to add"
            "- to sustract"
            "* to multiply"
            "/ to divide")
sign=input()
print("you choose  " ,sign)
if num1==56 and num2==9:
    print("Answer is 77")
elif sign== "+" :
    result=num1+num2
    print("your answer is ", result)
elif sign== "-":
    result=num1-num2
    print("your answer is ",result)
elif num1==45 and num2==3:
    print("your answer is 555")
elif sign=="*":
    result=num1*num2
    print("your answer is ",result)
elif num1==56 and num2==2:
    print("your answer is 4")
elif sign=="/":
     result=num1/num2
     print("your answer is ",result)
print("\n Thanku for using calculator")
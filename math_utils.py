def find_max_number(num1, num2, num3):
    if num1 > num2 >= num3 or num1 > num3 >= num2:
      return num1
    elif num2 > num1 >= num3 or num2 > num3 >= num1:
      return num2
    elif num3 > num1 >= num2 or num3 > num2 >= num1:
      return num3
    elif num1 == num3 or num1 == num2 or num2 == num3 and num1 == num3 :
      return "equal numbers:", num1
    elif num1 == num3 or num1 == num2 or num2 == num3 and num2 == num1 :
      return "equal numbers:", num2
    elif num1 == num3 or num1 == num2 or num2 == num3 and num2 == num3 :
      return "equal numbers:", num2

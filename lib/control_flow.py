#!/usr/bin/env python3

def admin_login(username, password):
    user_admin =  username == "admin" or username == "ADMIN" 
    user_password = password == "12345"
    return "Access granted" if user_admin and user_password else "Access denied"
    
def hows_the_weather(temperature):
    if temperature > 85: 
        weather = "It's too dang hot out there!"
    elif temperature > 39 and temperature < 66:
        weather = "It's a little chilly out there!"
    elif temperature > 65: 
        weather = "It's perfect out there!"
    else:
        weather = "It's brisk out there!"
    return weather

def fizzbuzz(num):
    num_three = num % 3
    num_five = num % 5
    num_three_bool = num_three == 0
    num_five_bool =  num_five == 0 
    if num_three_bool and num_five_bool:
        return "FizzBuzz"
    elif num_three_bool:
        return "Fizz"
    elif num_five_bool:
        return "Buzz"
    else:
        return num

def calculator(operation, num1, num2):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "/":
        return num1 / num2
    elif operation == "*":
        return num1 * num2
    else:
        print("Invalid operation!")
        return None

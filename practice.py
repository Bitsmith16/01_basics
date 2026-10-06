# Write a program that converts number of years to the weeks. 
# if the input was 2, then the output should be 2 * 52 = 104, because we have 52 weeks 
# in 1 year.

# Example Input 2
# Example Output 2 * 52 = 104
#====================================================================
# year = int(input("Enter number of years: "))
# weeks = year * 52

# print("There are " + str(weeks) +" weeks in " + str(year)+ " years" )

#-------------------------------------------------------------------------------------------
# #Group Name Generator
# print("Welcome to the Group Name Generator!")

# color = input("Whats your favourite color?\n")
# animal = input("Whats your favourite animal?\n")

# # Entering animal is singular but the output is plural so we add an 's' at the end of the animal name.
# print(f"Your group name could be {color} {animal}s") 

#------------------------------------------------------------------------------------------
# # Gross Pay Calculator
# print("Welcome to the Gross Pay Calculator!")

# hours = float(input("Enter the number of hours worked: "))
# rate = float(input("Enter the hourly rate: "))  
# pay = hours * rate
# pay = round(pay, 2)
# print(f"Your gross pay is ${pay}")
#------------------------------------------------------------------------------------------
# Celsius to Fahrenheit Converter
# print("Welcome to the Temperature (celcius to farenheit) converter!")

# while True:
#     scale =input("Choose a temerature scale C or F which you want to convert to:")
#     if scale.upper() == "C":
#         celcius = float(input ("Enter the temperature in celcius: "))
#         farenheit = (celcius * 9/5) + 32
#         print(f"{celcius}°C is equal to {farenheit}°F")
#         break
#     elif scale.upper() == "F":
#         farenheit = float(input ("Enter the temperature in farenheit: "))
#         celcius = (farenheit - 32) * 5/9
#         print(f"{farenheit}°F is equal to {celcius}°C")
#         break
#     else:
#         print("Invalid input. Please enter C or F.")  
#------------------------------------------------------------------------------------------
# # Trip Cost Calculator
# print("Welcome to the Trip cost Calculator")

# day = int(input("Enter Trip duration(in days): "))
# hotel = float(input("How much hotel cost per night:$"))
# flight = float(input("Enter flight price: $"))
# car = float (input("Enter Rental Car price: $"))
# misc = float(input("Enter any other cost involved: $"))

# total_cost= round((day * hotel) + flight + (day * car)+ misc,2)

# print(f"Your total trip cost:${total_cost}")
#------------------------------------------------------------------------------------------
#Even or Odd Number Checker
# print("Welcome to program that determine given number is Even or odd")

# num = int(input("Enter a number: "))

# if num%2==0:
#     print(f"{num} is Even")
# else:
#     print(f"{num} is Odd")
#------------------------------------------------------------------------------------------
# #BMI Calculator
# print("Welcome to the BMI Calculator")
# height = float(input("Enter your height in m: "))
# weight =  float(input("Enter your weight in kg: "))
# # TODO
# BMI = round(weight/(height ** 2), 2)

# if BMI <= 18.5:
#     print(f"Your BMI is {BMI}. You are underweight")
# elif BMI>18.5 and BMI <= 25:
#     print(f"Your BMI is {BMI}. Your weight is normal")
# elif BMI >25 and BMI <=30:
#      print(f"Your BMI is {BMI}. You are overweight")
# else:
#     print(f"Your BMI is {BMI}. You are Obese")
#------------------------------------------------------------------------------------------

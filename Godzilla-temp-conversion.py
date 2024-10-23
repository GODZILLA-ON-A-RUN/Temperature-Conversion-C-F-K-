# Godzilla
# Computer Science 20
# October 21, 2024

# Temperature Conversion Program
# Purpose: To convert temperature from celcius to fahrenheit


# take info from user
unit = input("Do you wanna convert to C(celsius) or to F(fahrenheit) or to K(Kelvin)?") 
unit_2 = input("What unit is your current temperature in (C/F/K)?")
temp = input("Enter the temperature")

# Convert data type
temp = float(temp)

# Opperation
# Celsius to Fahrenheit and Fahrenheit to Celsius
if unit == "C" and unit_2 =="F":
    temp = ((temp - 32) * 5 / 9)
    print(f"The temperature is {temp}° Celsius")
elif unit == "c" and unit_2 == "f":
    temp = ((temp - 32) * 5 / 9)
    print(f"The temperature is {temp}° Celsius")    
elif unit == "F" and unit_2 == "C":
    temp = ((9 * temp) / 5 + 32 )
    print(f"The temperature is {temp}° Fahrenheit")
elif unit == "f" and unit_2 == "c":
    temp = ((9 * temp) / 5 + 32 )
    print(f"The temperature is {temp}° Fahrenheit")
# Celsius to Kelvin and Kelvin to Celsius
elif unit == "C" and unit_2 == "K":
    temp = (temp - 273.15)
    print(f"The temperature is {temp}° Celsius")
elif unit == "c" and unit_2 == "k":
    temp = (temp - 273.15)
    print(f"The temperature is {temp}° Celsius")
elif unit == "K" and unit_2 == "C":
    temp = (temp + 273.15)
    print(f"The temperature is {temp} Kelvin")
elif unit == "k" and unit_2 == "c":
    temp = (temp + 273.15)
    print(f"The temperature is {temp} Kelvin")    
# Fahrenheit to Kelvin and Kelvin to Fahrenheit
elif unit == "F" and unit_2 == "K":
    temp = (temp - 273.15) * 9/5 + 32
    print(f"The temperature is {temp}° Fahrenheit")
elif unit == "f" and unit_2 == "k":
    temp = (temp - 273.15) * 9/5 + 32
    print(f"The temperature is {temp}° Fahrenheit")
elif unit == "K" and unit_2 == "F":
    temp = (temp - 32) * 5/9 + 273.15
    print(f"The temperature is {temp} Kelvin")
elif unit == "k" and unit_2 == "f":
    temp = (temp - 32) * 5/9 + 273.15
    print(f"The temperature is {temp} Kelvin")
    
else:
    print("Please provide a vaild unit of temperature measurement")


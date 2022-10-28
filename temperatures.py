import functions as func
import os
from functions import colors 


# Clear the Console

os.system("cls")

# Get the first Unit (Einheit)
code_1 = func.get_unit_code("Enter the Temperature unit (Celcius (C), Fahrenheit (F) oder Kelvin (K)) for the temperature you have: ")
name_1 = func.get_unit_name(code_1)


# Get the secound Unit (Einheit)
code_2 = func.get_unit_code("Enter the Temperature unit (Celcius (C), Fahrenheit (F) oder Kelvin (K)) for the temperature you wanna \nknow: ")
name_2 = func.get_unit_name(code_2)

# Get the Temperature 1

temperature_1 = func.get_temperature_1(name_1)

# Get the Temperature 2

temperature_2 = func.calculate_temperature_2( code_2, temperature_1)

# Log the Result

print(colors.OKBLUE,temperature_1,"°",name_1,"are",temperature_2,"°",name_2,".")

# Go On or Not?

func.go_on_or_not()

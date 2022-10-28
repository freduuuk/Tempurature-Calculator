from concurrent.futures import process
import time
import sys
class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
units = ["C", "F", "K"]

def get_unit_code(inputname):

    while True:
        unit = input(inputname)
        if unit.upper() in units:
            if unit.upper() == "C":
                return  1
            elif unit.upper() == "F":
                return  2
            elif unit.upper() == "K":
                return  3
        else:
            print(colors.FAIL, "Keine richtige Einheit angegeben. Programm startet neu...")
            time.sleep(1.5)
            False

def get_unit_name(code):
    if code > 3:
        print(colors.FAIL,"Not a valid Code... Returning...")
    elif code == 1:
        return "Celcius"
    elif code == 2:
        return "Fahrenheit"
    elif code == 3:
        return "Kelvin"
    
def get_temperature_1(unit_name_1):

    temperature_1 = input("Please Enter the temperature in ° "+unit_name_1 +": ")
    while True:
        try:
            temperature_1 = float(temperature_1)
            return temperature_1
        except ValueError:
            print(colors.FAIL,"Please enter a valid number for the temperature!")
            break

def calculate_temperature_2 (code_2,temperature_1):

    if code_2 == 1:
        code_2 = 0

    if code_2 == 2:
        code_2 = 32
    
    if code_2 == 3:
        code_2 = 173.15    

    if code_2:
        return temperature_1 *1.8 +32
    return temperature_1 + code_2

def go_on_or_not():
    number = input( "Enter 1 to do another calculation, Enter 2 to close this window!\n")
    while True:
        try:
            number = float(number)
            break
        except ValueError:
            print(colors.FAIL,"Please enter 1 or 2!")
            break
    if number == 1:
        import temperatures
    else:
        sys.exit()
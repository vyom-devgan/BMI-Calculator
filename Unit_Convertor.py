import decimal
def convertor(value, unit):
    value = float(decimal.Decimal(value))
    if unit == 'in' or unit == 'inches':
        return 'Height in meters is', float(value/39.37)
    
    if unit == 'lbs' or unit == 'pounds':
        return 'Weight in kilograms is', float(value/2.204622)

value = input("What is the value that you would like to convert? ")
unit = input("What unit are you inputting?\nHeight = inches\nWeight = lbs")

convertor(value, unit)

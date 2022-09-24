import decimal
def bmi():
    print("Welcome to the BMI calculator")
    w = input("What is the weight of the person? ")
    h = input("What is the height of the person? ")
    h = decimal.Decimal(h)*decimal.Decimal(h)
    w = decimal.Decimal(w)
    bmi = w/(h)
    bmi = float("{0:.2f}".format(bmi))

    #Conditions
    if bmi >= 18.5 and bmi <= 25:
        print("Youre BMI is ", bmi, " which classifies you as Normal Weight")
    elif bmi < 18.5:
        print("Youre BMI is ", bmi, " which classifies you as Underweight")
    elif bmi > 25:
        print("Youre BMI is ", bmi," which classifies you as Overweight")


bmi()

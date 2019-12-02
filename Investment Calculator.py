import math

print("Welcome to your investment calculator: \n")

p = float(input("How much  are your depositing: "))
i = float(input("Please enter your interest rate: "))
t = float(input("Enter investment term in years: "))
r = i/100
interest = input("Please choose interest type: (Simple or Compound): ")




if interest == "Simple":
    simple = p*(1+r*t)
    print(round(simple))

else:
    compound = p*math.pow((1+r),t)
    print(round(compound))

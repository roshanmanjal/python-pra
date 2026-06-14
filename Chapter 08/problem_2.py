# temp celsius to fahrenheit
# formula is c = 5*((f-32)/9)

def f_to_c():
    f = float(input("Enter the temp in F:- "))
    c = 5*((f-32)/9)
    return c


print(f"Temp in Celsius is := {round(f_to_c(), 2)} °C")
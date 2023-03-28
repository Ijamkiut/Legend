def convertion(a):
    return a + 273.15

celcius = float(input("What is Your Celcius to Convert? : "))

total = convertion(celcius)
print("The Kelvin For This", celcius , "Celcius is :" ,total)
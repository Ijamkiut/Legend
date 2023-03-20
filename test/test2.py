def display(name,celcius,farenheit):

    farenheit = (celcius * 9 / 5) + 32 

    print("Hello",name,"Nilai dalam farenheit ialah",farenheit)

    if(farenheit > 150):
        print("Cuaca Amat Panas,suhu nya ialah : ",farenheit)
    else:
        print("Cuaca okay jak,suhu nya ialah : ",farenheit)    
    
name = input("What is Your Name : ")
celcius = float(input("Celcius : "))

display(name,celcius,farenheit=any)
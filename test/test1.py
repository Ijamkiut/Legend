def details():


    bmi = weight / (height/100)**2
    

    print('Hi' , name , "your age is," , age , "your weight is" , weight , "and your height is" , height)
    print("Your bmi is " , round(bmi,0))

    if(bmi < 18.5):
        print("You Are underweight")
    elif(bmi < 25):
        print("You are Healthy")
    elif(bmi <= 30):
        print("You are overweight")
    elif(bmi > 30 ):
        print('You Are Obesity')  


name = input("What is Your Name : ")    
age = input("What is Your Age : ")
weight = float(input("What is Your weight : "))
height = float(input("What is Your height : "))

details()
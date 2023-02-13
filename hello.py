#naqiu naqayyoum bin kamis
#019-2347005
#naqiu.naqayyoum@gmail.com
name = input("What is Your Name : ")
weight = float(input("What is Your weight : "))
height = float(input("What is Your height : "))
greeting = "Hello" + " "+name
bmi= weight / (height*height)
print(greeting)
print (name + " " + "This is Your BMI " + " "+ str(bmi))
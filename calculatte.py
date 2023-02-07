name = input("What is Your Name : ")
tax = float(input("How Many Percent Of Tax : "))
price = float(input("How Much is The item Cost : "))
aftersales = price * tax /100
totalprice = price + aftersales
print("HI " + name + " ," + "This is your total price" + " " + "RM" + str(totalprice) + "," +"The Sales tax is : " + " " + str(tax))
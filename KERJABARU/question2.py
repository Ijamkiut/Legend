print("""
 _  _  ____  __     ___  __   _  _  ____    ____  __     ____  __    ____  _  _  __  
/ )( \(  __)(  )   / __)/  \ ( \/ )(  __)  (_  _)/  \   (  __)(  )  (  __)( \/ )(  ) 
\ /\ / ) _) / (_/\( (__(  O )/ \/ \ ) _)     )( (  O )   ) _) / (_/\ ) _)  )  (  )(  
(_/\_)(____)\____/ \___)\__/ \_)(_/(____)   (__) \__/   (__)  \____/(____)(_/\_)(__) 
""")

from prettytable import PrettyTable

# Specify the Column Names while initializing the Table
myTable = PrettyTable(["ID", "From", "To", "Depart Time","Adault Time","Child Price"])

# Add rows
myTable.add_row(["1", "Lawas", "Limbang", "6.30","40.0","30.0"])
myTable.add_row(["2", "Mukah", "Bakalalan", "7.30","28.0","13.0"])
myTable.add_row(["3", "Bintulu", "Kapit", "8.30","13.0","25.0"])
myTable.add_row(["4", "Kuching", "Sibu", "9.30","35.0","40.0"])
myTable.add_row(["5", "Miri", "Bintulu", "5.30","55.0","45.0"])

print(myTable)

name = input("Please Enter Your Name : ")
froms = input("From : ")
To = input("To : ")
Adult = int(input("Number of Adult : "))
Children = int(input("Number of Children : "))
total = (Adult*40) + (Children*30)

myTable2 = PrettyTable(["Name", "From", "To", "Number of Adult","Number of Children","Total Payment"])

myTable2.add_row([name,froms, To, Adult,Children,total])

print(myTable2)
converter = int(input('what do you want to convert : '))
totalminit = converter // 60
totalsec = converter % 60
print(str(totalminit) + 'Minute ' +str(totalsec) + 'Second')
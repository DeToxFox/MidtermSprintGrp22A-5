# hello Mak


personName = input('Enter your name: ')
tripLocal = input('Enter the trip location: ')
tripDays = int(input('Enter the number of days: '))
numKms = int(input('Enter the number of Kms traveled: '))
print()
perDiem = 56.00
lodging = 125.00
totalDiem = tripDays * perDiem
totalLodging = (tripDays - 1) * lodging
totalBasedDays = totalDiem + totalLodging

costPerKms = 0.24
totalKms = numKms * costPerKms

totalClaim = totalKms + totalBasedDays

print("Question 5: NL Chocolate Company Employee Expenses")
print('Name:                   ', personName)
print('Location Traveled:      ', tripLocal)
print('Length of Stay (days):  ', tripDays)
print('Number of Kms traveled: ', numKms)
print()
print('Total claim amount:      $', totalClaim)
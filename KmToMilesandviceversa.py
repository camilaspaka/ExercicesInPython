# Taking kilometers input from the user
miles = float(input("Enter value in miles: "))

#Enter value in kilometers: 3.5
#3.50 kilometers is equal to 2.17 miles

# conversion factor
conv_fac = 0.621371

# calculate miles
kilometers = miles / conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

Numbers = [6,5,3,8,4,2,5,4,11,43,1,17,27,90,77,62,51,47,82,86,20]
#Determine how many numbers are in the list

print(len(Numbers))
#Calculate the sum of all numbers in the list.
print()
sum = 0
for value in Numbers:
    sum = sum + value
print("The sum is:", sum)
#Use a While loop to print all the numbers in the list with their index values
print()
Sum2 = 0
while Sum2 < len(Numbers):
  print(Numbers[Sum2])
  Sum2 = Sum2 + 1

#Use a For loop and the range() function to print every other number in the list with their index values.
print()
for counter in range(0, len(Numbers), 2):
    print(Numbers[counter])

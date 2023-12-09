#Calculate average temperature

numDays = int(input("How many day's temperature? "))
total = 0
#empty array to store temperatures
temp = []
#range second parameter will go to parameter -1, that's why we use +1 so it consider param itself
for i in range(numDays):
    nextDay = int(input("Day " + str(i+1) + "'s high temp:"))
    temp.append(nextDay)
    #temp total
    total += temp[i]

#round by 2
avg = round(total/numDays,2)
print("\nAverage = " + str(avg))

above = 0
#finds how many days are above avg
for i in temp:
    if i > avg:
        above += 1

print(str(above) + " day(s) above average") 
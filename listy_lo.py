food = ['rice', 'beans']
food.append('broccoli')
print(food)
food2 = ['bread', 'pizza']
food.extend(food2)
print(food)
print(food[3], food[4])
breakfast = "eggs,fruit,orange juice"
print(breakfast.split(','))

newbreakfast = (breakfast.split(','))
print(len(newbreakfast))

numblist = []
while True:
    numb = input("Enter floating point number: ")

    if numb == "stop":
        break
    else:
        numblist.append(numb)

print(numblist)
min = numblist[0]
max = numblist[0]

for i in numblist:
    if float(i) < float(min):
        min = i
    if float(i) > float(max):
        max = i
print("Min: ", min)
print("Max: ", max)

total = float(0)
for i in numblist:
    total = float(i) + total

average = total/len(numblist)
print("Average: ", average)
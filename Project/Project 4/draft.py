import dog
import cat
import fish
import bird
import csv
list = []
with open('pets.csv', 'r') as f:
    reader = csv.reader(f)
    for i in reader:
        if i[0] == 'Dog':
            d = dog.Dog(i[1], i[2], i[3], i[4])
            list.append(d.name)
        elif i[0] == 'Cat':
            c = cat.Cat(i[1], i[2], i[3], i[4])
            list.append(c.name)
        elif i[0] == 'Fish':
            f = fish.Fish(i[1], i[2], i[3], i[4])
print(list)
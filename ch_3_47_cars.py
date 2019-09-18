#learn : sort(), sort(reverse=True), sorted(), reverse(), len()

#sort() method, sort list PERMANENTLYs
cars = ['toyota', 'bmw', 'mercedes', 'audi', 'nissan']
print(cars)

cars.sort()
print(cars)
print('\n')

cars.sort(reverse=True)
print(cars)


#sorted() method, sort list temporarily
print('\n')
cars2 = ['toyota', 'bmw', 'mercedes', 'audi', 'nissan']

print('original cars2')
print(cars2)

print('sorted() cars2')
print(sorted(cars2))

print('orignal cars2')
print(cars2)

#sorted( ,reverse=True), temporarily sort list reverse alphabetically order
print('sorted(cars2,reverse=True)')
print(sorted(cars, reverse=True))

print('orignal cars2')
print(cars2)


#len() method, identify list lenght. count start at ONE
x = len(cars)
print(x)

#reverse() method, reverse list's chronological order
print('\n')
print(cars)

cars.reverse()
print(cars)

#reverse() method for the 2nd time used at same list, revert the list to its original order
cars.reverse()
print(cars)


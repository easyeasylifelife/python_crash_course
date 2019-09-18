#chapter 3, list introduction
bicycle = ['polygon', 'thrill', 'dahon', 'element', 'trek']
print(bicycle)

#accessing list's element
print(bicycle[0:2])

#accessing list's element w/ method .title() .upper() .lower()
print(bicycle[0].title())

#accessing last item in list's element w/ [-1]
print(bicycle[-1])
print(bicycle[-3])

message = "I have a bicycle and it is called by " + bicycle[1].upper() + "."
print(message)

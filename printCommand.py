print()   # Prints Empty Line
print("Hello World!")
print("Hello master \n python programming")

a, b = 10, 9

print(a, b)

print(a, b, sep='||')

################ Print Formatting ################

# %s = string, %i = integer, %f = float

name = "Royson"
percentage = "98.9%"
marks = 98.9

print("Name is %s, and his marks are %s" % (name, percentage))
print("Name is %s, and his marks are %.2f" % (name, marks))

print("Name is {}, and his marks are {}".format(name,percentage))

print("Name is {0}, and his marks are {1}".format(name,percentage))

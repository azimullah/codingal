class parrot:

    species = bird
    def __init__(self, name, age):
        self.name = name
        self.age = age

blue = parrot("blue", 10)
woo = parrot("woo", 15)

print("Blu is a {}".format(blue.species))
print("Woo is a {}".format(woo.species))

print("{} is {} years old".format(blue.name,blue.age))
print("{} is {} years old".format(woo.name ,woo.age))
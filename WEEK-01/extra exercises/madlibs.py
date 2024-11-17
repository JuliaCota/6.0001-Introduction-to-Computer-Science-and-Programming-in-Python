# this is a madlibs code in python! it's being written in IDLE
# I'll exercise the following:
# string concatenation --- putting strings together
# If I want to create a setence with a blank space, that can be filled by the user, let's say: "My name is ______"
# name = "" # a string variable that can collect the name of the user

# there are multiple ways to do the same thing
# print("My name is " + name) # string + variable
# print("My name is {}".format(name)) # string{}.format(variable) - won't use this one for a simple concatenation like this one
# print(f"My name is {name}") # best format, in my opinion, for this one.

# I still need to get the variable value from the user, their NAME

adj1 = input("Adjective: ")
verb = input("Verb: ")
adj2 = input("Adjective: ")
famousperson = input("Famous person: ")
madlib = f"I'm so {adj1}! I really love to {verb}. Just stay {adj2} like {famousperson}"

print(madlib)

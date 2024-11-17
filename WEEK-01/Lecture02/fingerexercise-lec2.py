# FINGER EXERCISE - Write a program that examines three variables--x, y, and z-- and prints the largest odd number among them. If none of them are odd, it should print a message to that effect
#
#x = 5
#y = 7
#z = 2
#
# examine variables
#print #largest odd number
#
# if none are odd
#    print("none of them are odd")

x = 0
y = 1
z = 2

if x%2 != 0 and y%2 != 0 and z%2 != 0:
    print('all of them are odd')
    if x > y and y > z:
        print(f'X, {x} is the largest odd number')
    elif y > x:
        print(f'Y, {y} is the largest odd number')
    else:
        print(f'Z, {z} is the largest odd number')
elif x%2 != 0 or y%2 != 0 or z%2 != 0:
    print('there are odd numbers')
    
    if x%2 != 0:
        print('X is odd')
        if x > y and x > z:
            print('X is the largest odd number')
        else:
            print('')
    else:
        print('X is even')
        
    if y%2 != 0:
        print('Y is odd')
        if y > z and y > x:
            print('Y is the largest odd number')
        else:
            print('')
    else:
        print('Y is even')
        
    if z%2 != 0:
        print('Z is odd')
        if z > y and z > x:
            print('Z is the largest odd number')
        else:
            print('')
    else:
        print('Z is even')

# I can't make this work rn, later on I will come back to it

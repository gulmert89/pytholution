# List of prime numbers up to a user defined point #

ep = int(input("Enter the end point: "))    #ep: end point
pl = []    #pl: prime list

for i in range(1,ep):
    for divider in range(2,i):
        if i%divider==0 and i!=2:
            break
    else:
        pl.append(i)
        
print("List of the prime numbers up to",ep,"is:\n",pl)

# Note to myself:
# The meaning of "else" aligned with the "for" above: If none of "if" values are satisfied for all the "for" values, do the "else".
# Loved this usage of "else".

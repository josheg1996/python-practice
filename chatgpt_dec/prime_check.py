def prime(y):
    x = int(y)
    for i in range(2,x):
        if x%i == 0:
            print ("False (since %d is not a prime number)" % (x))
            break
        if i == x-1:
            print ("True (since %d is a prime number)" % (x))
a = input("Gimme number:")
prime(a)



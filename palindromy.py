def czy_to_palindrom(x):
    y = len(x)
    z = 0
    for i in range (0,y):
        tyl = (x[-1-i])
        przod = (x[i])
        if tyl == przod:
            z= z + 1
    if z == y:
        print("palindrom")
    else:
        print ("nie palindrom")

czy_to_palindrom("test")
    

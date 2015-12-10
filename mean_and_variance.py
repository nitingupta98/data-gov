try:

    data = []
    while 1:
        x = int(input("Enter data and press -1 to stop:"))
        if x == -1:
            break
        data.append(x)
    
    mean = lambda data: float(sum(data))/len(data) 
    variance = lambda data :  sum([(i-mean(data))**2 for i in data])/len(data)
    print ("Mean :" , mean(data))
    print ("Variance :", variance(data))
    
except ZeroDivisionError:
    print 'enter atleast 1 value to compute  mean and variance'

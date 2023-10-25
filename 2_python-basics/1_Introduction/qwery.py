from data import warehouse1
a = dict()
for i in warehouse1:
        
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
            
        #if i == dict1:
        #dict1.values += 1

print(a)


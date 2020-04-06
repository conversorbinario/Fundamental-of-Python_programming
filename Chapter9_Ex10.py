#Exercise 11

def sumfile(filename):
    file = open(filename) #by default, 'r' mpde. We are creating a new object
    addsto=0
    for n in file:
        n.split() 
        addsto+=int(n)
    return addsto
        
sum_integers=sumfile('createdtext.txt')
print(sum_integers)
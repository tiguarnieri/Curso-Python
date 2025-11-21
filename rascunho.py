x =1

def escopo():
    x=10

    def escopo_interno():
        y=2
        print (x, y)
    
    escopo_interno()

escopo()
print(x)
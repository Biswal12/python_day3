class Shoe:
    def __init__(self,price,material):
        self.price = price
        self.material = material

s1=Shoe(1000,"canvas")
print("the unique id of the object",id(s1))
#print(s1)
class Fruit(object):
    """Fruit"""
    number=0
    indexes=0
    types = 'Fruit'
    def __init__(self,size,taste):
        """General"""
        self.taste=taste
        self.size=size
        Fruit.number+=1
        Fruit.indexes+=1
    def describe(self):
        """Description"""
        print(self.taste)
        print(self.size)
    def cut(self,parts):
        print(f"{self.name} is cut into {parts}")
        print(f"It's {self.taste}!!")
class Apple(Fruit):
    """Apple"""
    def __init__(self,amount,size,taste,color):
        super().__init__(size, taste)
        self.amount=amount
        self.name = 'Apple'
        self.color=color

    def cut(self,parts):
        super().cut(parts)
        return 'Nice apple!'
    def describe(self):
         super().describe()
         return 'Great'
    def pie(self):
        return f"We made apple pie"
class Citrus(Apple):
    def __init__(self,size, taste,color):
        super().__init__(size, taste, color)
        self.name = 'Orange'
    def cut(self, parts):
        super().cut()
        return  f'Nice {self.name}!'
    def describe(self):
        return super().describe()
    def pie(self):
        return f"We made {self.name} pie"
    def juice(self):
        return (f"We made {self.name} juice")

lst=[]
a=Apple(2,'Small','Good','Red')
print(a.indexes)
a1=Apple(3,'Small','Good','Red')
print(a1.number)
fruits = [Apple(f"{i}",'Big','TAsty','REd') for i in range(10)]
print(fruits)



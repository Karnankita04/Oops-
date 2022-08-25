class FAMILY_MEMBERS:

    raise_amt = 500
    def __init__(self,name,roll,pocket_money):
        self.a = name
        self.b = roll
        self.c = pocket_money
    def increase(self):
        self.c = int(self.c + 100)
    def new(self):  
        self.c = int(self.c + a.raise_amt) # class variables can be accessed by either instance of the class or the class itself
    
a = FAMILY_MEMBERS('Ankita','Daughter',200)
c = FAMILY_MEMBERS('RAchna','Mother',200)
b = FAMILY_MEMBERS('Himanshu','son',100)
d = FAMILY_MEMBERS('Sharma uncle','neighbour',0)

print(a.a)

print(a.b)

print(a.c)

a.increase()
print(a.c)
a.new()
print(a.c)
print(FAMILY_MEMBERS.__dict__)
print(a.__dict__)





# print(c)




# class second:
#     def hello(self,):






# x = second(2400,'teacher')

class Singleton():

    moje_nova_promenna_pro_a = 'test'
    instance = None

    def __new__(cls):
        if not cls.instance:
            cls.instance = cls
            return Singleton()
        return cls.instance
    

a = Singleton()
b = Singleton()

print(a is b) #Musi vypsat true

a.moje_nova_promenna_pro_a = "Test"
print(a.moje_nova_promenna_pro_a) #Musi vypsat test
print(b.moje_nova_promenna_pro_a) #Musi vypsat take test
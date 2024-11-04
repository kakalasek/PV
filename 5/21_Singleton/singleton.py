class Singleton():

    moje_nova_promenna_pro_a = 'test'
    instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.instance:
            cls.instance = object.__new__(cls, *args, **kwargs)

        return cls.instance

    def __init__(self):
        self._num = 22

a = Singleton()
b = Singleton()

print(a is b) #Musi vypsat true

print(a._num)
print(b._num)
print(id(a))
print(id(b))

a.moje_nova_promenna_pro_a = "Test"
print(a.moje_nova_promenna_pro_a) #Musi vypsat test
print(b.moje_nova_promenna_pro_a) #Musi vypsat take test
class A:
    def __init__(self):
        self.a_variable = True

    def test(self):
        print("A")

class B:
    def __init__(self):
        self.b_variable = True

    def test(self):
        print("B")

class C(A, B):
    def __init__(self):
        # super().__init__()
        A.__init__(self)
        B.__init__(self) 

    def test(self):
        return super().test()

if __name__ == "__main__":
    # Experiment 1
    c = C()
    c.test()

    # Experiment 2
    try:
        print(c.a_variable)
    except:
        print("A was not executed")

    try:
        print(c.b_variable)
    except:
        print("B was not executed")





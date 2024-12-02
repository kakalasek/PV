def wrapper_repeat(f):
    def twice():
        f()
        f()
    return twice

@wrapper_repeat
def helloworld():
    print("hello world")

helloworld()
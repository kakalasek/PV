"""
A string is mainly for characters .. so not really, you cant embed a different collection. I mean in a way, yes, but it will get converted to string. So NO is the right answer for me
"""
print("A basic proof is to just try to add a collection to it .. see what happens")
try:
    string_s = "s"
    string_s += ('1',)
except:
    print("As I said, it does not really work. It does the same for all the other collection, trust me .. I dont want to make a case for each of them ..")
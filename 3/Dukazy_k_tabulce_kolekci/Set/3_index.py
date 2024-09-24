"""
Set is unindexed. That should speak for itself
"""
try:
    s = {1, "two", 3.33}
    print("Trying to acces a set element with an index in 1 .. 2 .. 3 ...")
    print(s[2])
except:
    print("Hm, an exception has been thrown .. what could that mean? I guess the set really is unindexed")
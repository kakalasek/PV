"""
String is a little discutable. You write a None there .. but I dont think it counts tho. The easy answer is NO.
If it is somehow possible, I dont think I even want to find out .. why would I ever do that?
"""
try:
    no_none = "None"

    print("If I try to add None .. well, theres gonna be an exception. See for yourself")

    no_none += None
except:
    print("Told ya, an exception has occured")
rain: bool = False
wind: bool = True
fog: bool = True

if not rain and not wind and not fog:
    print("Very nice wheater, umbrella is not needed")
elif (fog or rain) and not wind:
    print("Get yourself an umbrella")
elif wind and not rain:
    print("Get yourself a hat")
    if fog:
        print("And some bright clothes")
elif rain and wind and fog:
    print("Stay home")
elif rain and wind:
    print("Prepare for storm")
else:
    print("Figure this out yourself")
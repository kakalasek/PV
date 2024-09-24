"""
List once again works like expected. You can, without any problems, put a None value there. Heck, you can even put a lot of them there ..
"""
I_am_about_to_be_noned =[]
for i in range (0, 10000):
    I_am_about_to_be_noned.append(None)

print(f"{I_am_about_to_be_noned}\nThis surely was a long output. Thats why I am writing this down here. Yes, you can put None into a list :)")
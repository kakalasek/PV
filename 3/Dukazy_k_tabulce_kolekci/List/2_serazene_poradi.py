"""
If we insert a few numbers into a list in an ordered manner, we can say they are ordered. Couldnt be said so easily about objects. And the list does not do it on its own, so NO
"""
a_perfectly_ordered_list = [0,1,1,2,3,5,8,13]
print(f"A perfectly ordered list: {a_perfectly_ordered_list}")
a_perfectly_ordered_list.append(-300)
print(f"Not so perfectly ordered list: {a_perfectly_ordered_list}")
a_perfectly_ordered_list.append({"Shoot": "me"})
print(f"Everything is ruined now: {a_perfectly_ordered_list}")
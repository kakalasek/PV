"""
Dictionary, as always, is kinda special. It does not care about equal elements as its values, but equal keys, oh that is a different story ..
"""
proffesional_equal_key_killing_machine = {"please dont overwrite me": "Oh yes you will be", "please dont overwrite me": "You already were"}
print(f"Only the second value will be displayed here: {proffesional_equal_key_killing_machine}")
print(f"Just to showcase that equal values are okay: {{'a': 1, 'b': 1}}")
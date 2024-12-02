"""
Still .. what even is from smallest to biggest at this point? Well, you can kinda define it yourself, the fact is, dict does not really care, so the accurate answer is NO
"""
can_this_even_be_considered_ordered = {"aaa": "battery", "E": "probably not a battery", None: "how does this even work?"}
print(f"A perfectly ordered dict in my opinion: {can_this_even_be_considered_ordered}")
can_this_even_be_considered_ordered["Patrik"] = "Dyntr"
print(f"Now this ruins it all: {can_this_even_be_considered_ordered}")
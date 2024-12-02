import math

germination = 0.8
dead_plants = 0.08
target_number_of_plants = 14513
seeds_in_bag = 100

germinated_plants = germination * seeds_in_bag

dead_plants_num = germinated_plants * dead_plants

number_of_bags = math.ceil(target_number_of_plants/(germinated_plants - dead_plants_num))

print(number_of_bags)
num_of_line = 0
with open('helloworld.txt', 'r') as file:
    # content = file.read()
    # file.seek(0)
    # one_line = file.readline()
    # file.seek(0)
    # first_three = file.read(3)
    for line in file:
        num_of_line += 1
        print(f"{num_of_line} {line} ", end='')
    print()


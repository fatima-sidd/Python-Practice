roll_number = [47, 64, 69, 37, 76, 83, 95, 97]
sample_dict = {'Jhon':47, 'Emma':69, 'Kelly':76, 'Jason':97}

values = sample_dict.values()

res = []
for roll in roll_number:
    if roll in values:
        res.append(roll)

print(res)
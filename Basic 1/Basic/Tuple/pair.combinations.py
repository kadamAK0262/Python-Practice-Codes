tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')

def generate_pair_combinations(tuple1, tuple2):
    pair_combinations = [(item1, item2) for item1 in tuple1 for item2 in tuple2]
    return pair_combinations


pairs = generate_pair_combinations(tuple1, tuple2)

print("Tuple 1:", tuple1)
print("Tuple 2:", tuple2)
print("All pair combinations:", pairs)

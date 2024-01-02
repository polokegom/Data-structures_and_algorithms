import random;

random_data = []

for k in range(1,30):
    rand = random.randint(1, 100);
    random_data.append(rand);
print("Random Dataset:");
print(random_data);


def quicksort(dataset):
    if len(dataset) <= 1:
        return dataset
    else:
        pivot = dataset[random.randint(1,30)]
        left = [value for value in dataset[1:] if value < pivot]
        right = [value for value in dataset[1:] if value >= pivot]
        return quicksort(left) + [pivot] + quicksort(right)

print("\nOrdered Dataset:");
print(quicksort(random_data));



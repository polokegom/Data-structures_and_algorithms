import random;

random_data = []

for k in range(1,30):
    rand = random.randint(1, 100);
    random_data.append(rand);
print("Random Dataset:");
print(random_data);


def bubblesort(dataset):

    for k in range(len(dataset) - 1):
        for j in range (len(dataset) - 1):
            if (dataset[j] > dataset[j+1]):
                dataset[j], dataset[j+1] = dataset[j+1], dataset[j];

bubblesort(random_data);
print("\nOrdered Dataset:");
print(random_data);



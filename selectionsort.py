import random;

random_data = []

for k in range(1,30):
    rand = random.randint(1, 100);
    random_data.append(rand);
print("Random Dataset:");
print(random_data);


def selectionSort(dataset):

    for k in range(len(dataset) ):
        for j in range(k, len(dataset) ):
            if (dataset[k] > dataset[j]):
                dataset[k], dataset[j] = dataset[j], dataset[k];

selectionSort(random_data);
print("\nOrdered Dataset:");
print(random_data);



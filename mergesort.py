import random;

random_data = []

for k in range(1,30):
    rand = random.randint(1, 100);
    random_data.append(rand);
print("Random Dataset:");
print(random_data);


def mergesort(dataset):
  
  if len(dataset) > 1:
        mid_value = len(dataset)//2
        left = dataset[:mid_value]
        right = dataset[mid_value:]

        mergesort(left)
        mergesort(right)

        j = k = l = 0
        while l < len(left) and j < len(right):
            if left[l] < right[j]:
                dataset[k] = left[l]
                l += 1
            else:
                dataset[k] = right[j]
                j += 1
            k += 1

        while l < len(left):
            dataset[k] = left[l]
            l += 1; k += 1
        while j < len(right):
            dataset[k] = right[j]
            j += 1; k += 1

mergesort(random_data);
print("\nOrdered Dataset:");
print(random_data);



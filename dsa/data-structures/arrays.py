import random

class Array:
    def __init__(self, size):
        self.size = size
        self.items = [None] * size
    
    def insert(self, index, value):
        if 0 <= index < self.size:
            self.items[index] = value
        else:
            raise IndexError("Index out of range")
        
    def get(self, index):
        if 0 <= index < self.size:
            return self.items[index]
        else:
            raise IndexError("Index out of range")
    
    def delete(self, index):
        if 0 <= index < self.size:
            self.items[index] = None
        else:
            raise IndexError("Index out of range")
    
    def __str__(self):
        return ' '.join([str(item) if item is not None else '_' for item in self.items])
        

def visualize_array(arr):
    print("\nArray Visualization:")
    print("+---" * arr.size + "+")
    print("|" + "|".join([f"{item:^3}" if item is not None else " _ " for item in arr.items]) + "|" )
    print("+---" * arr.size + "+")

#Example Usage
if __name__ == "__main__":
    arr = Array(10)

    print ("Initial array")
    visualize_array(arr)

    # insert some random values
    for _ in range(5):
        index = random.randint(0, 9)
        value = random.randint(0, 99)
        arr.insert(index, value)
        print(f"Inserted {value} at index {index}")
        visualize_array(arr)

    
    # Get a value
    index = random.randint(0, 9)
    value = arr.get(index)
    print(f"\nValue at index {index}: {value}")
    visualize_array(arr)


    # Delete a value
    index = random.randint(0, 9)
    arr.delete(index)
    print(f"\nDeleted value at index {index}")
    visualize_array(arr)   
class Queue:
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return IndexError("Queue is empty")

    def front(self):
        if not self.is_empty():
            return self.items[0]
        return IndexError("Queue is empty")
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

def visualize_queue(queue):
    print("\nQueue Visualization:")
    if queue.is_empty():
        print("Empty Queue")
        return
    
    print("Front", end="")
    for item in queue.items:
        print(f" <- [{item}]", end="")
    print(" <- Rear")

# Example usage
if __name__ == "__main__":
    queue = Queue()
    
    print("\nEnqueuing elements into the queue:")
    for i in range(1, 6):
        queue.enqueue(i)
        print(f"Enqueued {i}")
        visualize_queue(queue)

    
    print("\nFront element of the queue:")
    front_element = queue.front()
    print(f"Front element: {front_element}")
    visualize_queue(queue)

    print("\nDequeuing elements from the queue:")
    for _ in range(3):
        dequeued_item = queue.dequeue()
        print(f"Dequeued: {dequeued_item}")
        visualize_queue(queue)
    
    print(f"\nCurrent queue size: {queue.size()}")
    print("\nIs queue empty?", queue.is_empty())
    
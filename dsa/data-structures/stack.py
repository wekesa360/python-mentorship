class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return IndexError("Stack is empty")

    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)
    

def visualize_stack(stack):
    print("\nStack Visualization:")
    if stack.is_empty():
        print("Empty Stack")
        return
    
    print("Top")
    for item in reversed(stack.items):
        print(f"| {item} |")
        print("+----+")
    print("Bottom")


# Example usage
if __name__ == "__main__":
    stack = Stack()
    
    print("\nPushing elements onto the stack:")
    for i in range(1, 6):
        stack.push(i)
        print(f"Pushed {i}")
        visualize_stack(stack)

    
    print("\nPeeking at the top element:")
    top_element = stack.peek()
    print(f"Top element: {top_element}")
    visualize_stack(stack)

    print("\nPopping elements from the stack:")
    for _ in range(3):
        popped_item = stack.pop()
        print(f"Popped: {popped_item}")
        visualize_stack(stack)
    
    print(f"\nCurrent stack size: {stack.size()}")
    print(f"\nIs stack empty? {stack.is_empty()}")

            
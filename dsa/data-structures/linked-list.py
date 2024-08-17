class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
    
    def delete(self, data):
        if not self.head:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        current = self.head
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
    
    def search(self, data):
        current = self.head
        index =  0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1
    
    def __str__(self):
        elements = []
        current = self.head
        while current:
            elements.append(str(current.data))
            current = current.next
        return '->'.join(elements)
    
def visualize_linked_list(linked_list):
    print("\nLinked List Visualization:")
    current = linked_list.head
    while current:
        print(f"+---+   ", end="")
        current = current.next
    print()


    current = linked_list.head
    while current:
        print(f"{current.data} |--> ", end="")
        current = current.next
    print("None")

    current = linked_list.head
    while current:
        print(f"+---+   ", end="")
        current = current.next
    print()


# Example usage
if __name__ == "__main__":
    ll = LinkedList()

    print("Inserting elements at the beginning:")
    for i in range(5, 0, -1):
        ll.insert_at_beginning(i)
        visualize_linked_list(ll)
    
    print("Inserting elements at the end:")
    for i in range(6, 8):
        ll.insert_at_end(i)
        visualize_linked_list(ll)

    print("\nSearching for element 4:")
    index = ll.search(4)
    print(f"Element found at index: {index}")
    visualize_linked_list(ll)


    print("\nDeleting element 3:")
    ll.delete(3)
    visualize_linked_list(ll)




    


    
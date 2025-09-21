# Import the Node class you created in node.py
from node import Node

# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        node = Node(value)
        if self.rear is None:
            # empty queue
            self.front = self.rear = node
        else:
            self.rear.next = node
            self.rear = node

    def dequeue(self):
        if self.front is None:
            return None
        node = self.front
        self.front = self.front.next
        if self.front is None:  # queue became empty
            self.rear = None
        return node.value

    def peek(self):
        return None if self.front is None else self.front.value

    def print_queue(self):
        if self.front is None:
            print("Queue is empty.")
            return
        curr = self.front
        while curr:
            print(f"- {curr.value}")
            curr = curr.next


def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ").strip()
            if name == "":
                print("Name cannot be empty.")
            else:
                queue.enqueue(name)
                print(f"{name} added to the queue.")

        elif choice == "2":
            helped = queue.dequeue()
            if helped is None:
                print("No customers to help.")
            else:
                print(f"Helped: {helped}")

        elif choice == "3":
            nxt = queue.peek()
            if nxt is None:
                print("No customers in queue.")
            else:
                print(f"Next customer: {nxt}")

        elif choice == "4":
            print("\nWaiting customers:")
            queue.print_queue()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    run_help_desk()


'''Why is a stack the right choice for undo/redo?: Stack is the right choice for undo/redo because it follows the Last In, First Out (LIFO) principle. 
This means that the most recent action performed by the user is the first one to be undone. 
When a user performs an action, it is pushed onto the undo stack. 
If they decide to undo that action, it is popped from the stack and reversed. 
If they then want to redo that action, it can be pushed onto a redo stack and popped from there when needed.
This structure allows for easy tracking of actions in the order they were performed and ensures that the most recent actions are addressed first.

Why is a queue better suited for the help desk?: A queue is better suited for the help desk because it follows the First In, First Out (FIFO) principle. 
This means that the first customer to arrive at the help desk is the first one to be served.

How do your implementations differ from Python’s built-in lists?: They give each Object a node that can be tracked much more easily and efficiently. '''
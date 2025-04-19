# distributed  global avearge method
import random

class Node:
    def __init__(self, id, value):
        self.id = id
        self.value = value

    def communicate(self, other):
        # Take average of both nodes
        average = (self.value + other.value) / 2
        print(f"Node {self.id} and Node {other.id} exchanged: New value = {average:.2f}")
        self.value = other.value = average

# Create nodes with initial random values
nodes = [Node(i, random.randint(1, 100)) for i in range(5)]

print("Initial values:")
for node in nodes:
    print(f"Node {node.id}: {node.value}")

# Perform gossip-based averaging
for round in range(10):
    print(f"\nRound {round + 1}:")
    a, b = random.sample(nodes, 2)
    a.communicate(b)

print("\nFinal values:")
for node in nodes:
    print(f"Node {node.id}: {node.value:.2f}")

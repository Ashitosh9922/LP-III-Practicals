class Node:
    """Huffman Tree Node"""

    def __init__(self, freq, sym, left=None, right=None):
        self.freq = freq      # frequency of character
        self.sym = sym        # symbol (character)
        self.left = left      # left child
        self.right = right    # right child
        self.huff = ""        # 0 or 1 assigned later


def print_code(node, code=""):
    """Recursively print Huffman codes"""
    new_code = code + str(node.huff)

    if node.left:
        print_code(node.left, new_code)
    if node.right:
        print_code(node.right, new_code)

    # If it's a leaf node, print its code
    if not node.left and not node.right:
        print(f"{node.sym} -> {new_code}")


# Step 1: Input string
text = input("Enter a string: ")

# Step 2: Count frequency of each character
freqs = {}
for ch in text:
    if ch in freqs:
        freqs[ch] += 1
    else:
        freqs[ch] = 1

# Step 3: Create nodes for each character
nodes = []
for ch in freqs:
    nodes.append(Node(freqs[ch], ch))

# Step 4: Build Huffman Tree
while len(nodes) > 1:
    # Sort by frequency (smallest first)
    nodes.sort(key=lambda x: x.freq)

    # Pick two smallest nodes
    left = nodes[0]
    right = nodes[1]

    # Assign binary values
    left.huff = 0
    right.huff = 1

    # Create new combined node
    new_node = Node(left.freq + right.freq, left.sym + right.sym, left, right)

    # Replace the two smallest nodes with their parent node
    nodes.remove(left)
    nodes.remove(right)
    nodes.append(new_node)

# Step 5: Display results
print("\nCharacters:", list(freqs.keys()))
print("Frequencies:", list(freqs.values()))
print("\nHuffman Codes:")
print_code(nodes[0])

"""
SAMPLE OUTPUT:

Enter a string: hello

Characters: ['h', 'e', 'l', 'o']
Frequencies: [1, 1, 2, 1]

Huffman Codes:
h -> 00
e -> 01
o -> 10
l -> 11

--------------------------------------------
EXPLANATION:
1️⃣ Count how many times each letter appears.
2️⃣ Each letter becomes a node in the tree.
3️⃣ Combine two smallest frequency nodes → parent.
4️⃣ Assign 0 (left) and 1 (right).
5️⃣ Continue until one root node remains.
6️⃣ Print Huffman codes for all characters.
--------------------------------------------
"""


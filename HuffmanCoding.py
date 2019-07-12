import sys
import collections as c
import typing as t

class Value:
    def __init__(self,charater,frequency):
        self.character=charater
        self.frequency=frequency

    def __eq__(self, other):
        """Overrides the default """
        if not isinstance(other, Value):
            return False
        return (self.character==other.character and self.frequency== other.frequency)



class Node(object):

    def __init__(self,value=None):
        self.value = value
        self.left = None
        self.right = None

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, left):
        self.left = left

    def set_right_child(self, right):
        self.right = right

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left != None

    def has_right_child(self):
        return self.right != None

    # define __repr_ to decide what a print statement displays for a Node object
    def __repr__(self):
        return f"Node({self.get_value()})"

    def __str__(self):
        return f"Node({self.get_value()})"

    def __eq__(self, other):
        """Overrides the default """
        if not isinstance(other, Node):
            return False
        return (self.value == other.value and self.left==other.left and self.right==other.right)


class Tree():
    def __init__(self, value=None):
        self.root = Node(value)

    def get_root(self):
        return self.root

    def __eq__(self, other):
        """Overrides the default """
        if not isinstance(other, Tree):
            return False
        return (self.root == other.root)

# Take a string and determine the relevant frequencies of the characters.
# Build and sort a list of tuples from lowest to highest frequencies.
# Build the Huffman Tree by assigning a binary code to each letter, using shorter codes for the more frequent letters. (This is the heart of the Huffman algorithm.)
# Trim the Huffman Tree (remove the frequencies from the previously built tree).
# Encode the text into its compressed form.
# Decode the text from its compressed form.

# Data Structure to add the character and frequency to the tree


# return dictionary: num
# of repetitions of each chr in data
def frequencies(data: str) -> t.Dict[chr, int]:
    dict = c.defaultdict(int)
    for elem in data:
        dict[elem] += 1
    return dict


# return dictionary: key(frequency), list[trees of Node]
def build_priority(dict: t.Dict[chr, int]) -> t.List[ Tree]:
    # transform dictionary to List of trees
    tree_list = [Tree( Value(char, freq)) for char, freq in dict.items()]
    return tree_list


def print_tree(bt: Tree, value: str):
    if bt == None:
        return
    if bt.root == None:
        return
    print("Node " + value, (bt.root.value.character, bt.root.value.frequency))
    if bt.root.left is not None:
        print_tree(bt.root.left, "Left")
    if bt.root.right is not None:
        print_tree(bt.root.right, "Right")


def merge(tree_list: t.List[Tree]) -> Tree:
    if tree_list == []: return None
    tree_list = sorted(tree_list, key=lambda x: x.root.value.frequency)
    while (len(tree_list) > 1):
        bt_merged = Tree( Value('', tree_list[0].root.value.frequency + tree_list[1].root.value.frequency))
        bt_merged.root.left = tree_list[0]
        bt_merged.root.right = tree_list[1]
        tree_list.pop(0)
        tree_list.pop(0)
        tree_list.append(bt_merged)
    bt_merged = tree_list.pop(0)
    return bt_merged


def traverse_tree(bt: Tree, elem: str, encode: str, output: t.List):
    if bt == None:
        return
    if bt.root == None:
        return
    if bt.root.value.character == elem:
        output.append(encode)
        return

    traverse_tree(bt.root.left, elem, encode + '0', output)
    traverse_tree(bt.root.right, elem, encode + '1', output)


def huffman_encoding(data):
    dic = frequencies(data)
    group = build_priority(dic)
    bt = merge(group)
    output = []
    for elem in data:
        traverse_tree(bt, elem, '', output)
    return ''.join(output), bt


def traverse_decode(copy_inmutable: Tree, data_list: t.List, output: t.List, parent: Tree):
    if copy_inmutable == None:
        return
    if copy_inmutable.root.value.character != "":
        output.append(copy_inmutable.root.value.character)
        if (len(data_list) > 0):
            traverse_decode(parent, data_list, output, parent)
        return
    if (len(data_list) > 0):
        elem = data_list.pop(0)
        if elem == '0':
            traverse_decode(copy_inmutable.root.left, data_list, output, parent)
        if elem == '1':
            traverse_decode(copy_inmutable.root.right, data_list, output, parent)
    return


def huffman_decoding(encode: str, tree: Tree):
    output = []
    bin_encode = list(encode)
    if bin_encode == [] and tree != None and tree.root != None:
        return '0' * tree.root.value.frequency
    if bin_encode != []:
        traverse_decode(tree, bin_encode, output, tree)
        return ''.join(output)
    return ''


if __name__ == "__main__":
    codes = {}
#basic Test1
    a_great_sentence = "The bird is the word"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the decoded data is: {}\n".format(decoded_data))

# basic Test2
    a_great_sentence = ""

    print("\n","The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The content of the decoded data is: {}\n".format(decoded_data))

#basic Test3
    a_great_sentence = "aaa"

    print("\n","The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The content of the decoded data is: {}\n".format(decoded_data))

#basic Test4
    a_great_sentence = "Mississippi"

    print("\n","The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The content of the decoded data is: {}\n".format(decoded_data))


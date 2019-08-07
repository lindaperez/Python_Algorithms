# ***** Building a Trie in Python *****#

# ***** PROBLEM DESCRIPTION ********#
#Before we start let us reiterate the key components of a Trie or Prefix Tree. A trie is a tree-like data structure that stores a dynamic set of strings. Tries are commonly used to facilitate operations like predictive text or autocomplete features on mobile phones or web search.
#Before we move into the autocomplete function we need to create a working trie for storing strings. We will create two classes:
#A Trie class that contains the root node (empty string)
#A TrieNode class that exposes the general functionality of the Trie,
# like inserting a word or finding the node which represents a prefix.
# Give it a try by implementing the TrieNode and Trie classes below!
## Represents a single node in the Trie
import collections
from typing import List

class TrieNode:
    def __init__(self):
        ## Initialize this node in the Trie
        self.end_word = False
        self.word = {}


    def insert(self, char):
        ## Add a child node in this Trie
        if char not in self.word:
            self.word[char] = TrieNode()

    def print_node(self):
        node = self.word
        for key,elem in node.items():
            print(key,':',elem.end_word)
            if elem!=None:
                elem.print_node()


## The Trie itself containing the root node and insert/find functions
class Trie:
    def __init__(self):
        ## Initialize this Trie (add a root node)
        self.root = TrieNode()


    def insert(self, word):
        ## Add a word to the Trie
        current_node = self.root
        for char in word:
            if char not in current_node.word:
                current_node.insert(char)
            current_node = current_node.word[char]
        current_node.end_word = True


    def print_trie(self):
        node = self.root
        node.print_node()


    def find(self, prefix):
        current_node= self.root
        for char in prefix:
            if char in current_node.word:
                current_node = current_node.word[char]
            else:
                return None
        return current_node

    def suffixes(self, suffix = ''):
        ## Recursive function that collects the suffix for
        ## all complete words below this point
        output=''
        ans =[]
        if suffix!='':
            current_node=self.find(suffix)
            if current_node==None:
                return []
            else:
                #current_node.print_node()
                self.suff(current_node,output,ans)
        return ans

    def suff(self, current_node: TrieNode, output:str, ans):
        for key,elem in current_node.word.items():
            if elem.end_word == True:
                ans.append(output+key)
            self.suff(elem, output+key, ans)
        return




## Find the Trie node that represents this prefix


root = TrieNode()
#root.insert('c')
#root.insert('d')
#root.insert('e')
#root.insert('c')


t = Trie()

t.insert("lunes")
t.insert("luna")
t.insert("lunesa")
t.insert("luz")


print(t.suffixes("lun"))

#print(t.suffixes('l'))

MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

#MyTrie.find("an").print_node()
print(MyTrie.suffixes("")) #return empty list
print(MyTrie.suffixes("an")) #return all word staring with an
print(MyTrie.suffixes("f")) #return all word staring with f
print(MyTrie.suffixes("tri")) #return all word staring with tri
print(MyTrie.suffixes("id"))  #return empty list



# ***** Router Using a Trie  *****#

# ***** PROBLEM DESCRIPTION ********#/
# For this exercise we are going to implement an HTTPRouter like you would
# find in a typical web server using the Trie data structure we learned previously.

# There are many different implementations of HTTP Routers such as regular
# expressions or simple string matching, but the Trie is an excellent and very
# efficient data structure for this purpose.

# The purpose of an HTTP Router is to take a URL path like "/", "/about",
# or "/blog/2019-01-15/my-awesome-blog-post" and figure out what content
# to return. In a dynamic web server, the content will often come from a
# block of code called a handler.

import collections
# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
from typing import List


class RouteTrieNode:
    def __init__(self):
        # Initialize the node with children as before, plus a handler
        self.trie = {}
        self.handler = None

    def insert(self, word: str, handler=None):
        # Insert the node as before
        if word not in self.trie:
            self.trie[word] = RouteTrieNode()
            self.handler = handler


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self):
        # Initialize the trie with an root node and a handler, this is the root path or home page node
        self.root = RouteTrieNode()

    def insert(self, elements: List[str], handler=None):
        # Similar to our previous example you will want to recursively add nodes
        # Make sure you assign the handler to only the leaf (deepest) node of this path
        current_node = self.root
        for elem in elements:
            if elem not in current_node.trie:
                current_node.insert(elem, None)
            current_node = current_node.trie[elem]
        current_node.handler = handler

    def find(self, elements: List[str], handler=None) -> str:
        # Starting at the root, navigate the Trie to find a match for this path
        # Return the handler for a match, or None for no match

        current_node = self.root

        for elem in elements:
            if elem not in current_node.trie:
                return None
            current_node = current_node.trie[elem]

        return current_node.handler


# The Router class will wrap the Trie and handle
class Router:
    def __init__(self):
        # Create a new RouteTrie for holding our routes
        # You could also add a handler for 404 page not found responses as well!
        self.route = RouteTrie()

    def add_handler(self, path: str, handler=None):
        # Add a handler for a path
        # You will need to split the path and pass the pass parts
        # as a list to the RouteTrie
        path_list = self.split_path(path)
        self.route.insert(path_list, handler)

    def lookup(self, path: str):
        # lookup path (by parts) and return the associated handler
        # you can return None if it's not found or
        # return the "not found" handler if you added one
        # bonus points if a path works with and without a trailing slash
        # e.g. /about and /about/ both return the /about handler
        path_list = self.split_path(path)
        hand = self.route.find(path_list)

        return 'not found' if hand is None else hand

    def split_path(self, path) -> List[str]:
        # you need to split the path into parts for
        # both the add_handler and loopup functions,
        # so it should be placed in a function here
        n = len(path) - 1
        if path[n] == '/':
            path_list = path[:n].split('/')
        else:
            path_list = path.split('/')

        return path_list



r = Router()
path1=r.split_path("classroom.udacity.com/nanodegrees/nd256/parts/modules/lessons/project/")
assert (path1==['classroom.udacity.com', 'nanodegrees', 'nd256', 'parts', 'modules', 'lessons', 'project'])
#['classroom.udacity.com', 'nanodegrees', 'nd256', 'parts', 'modules', 'lessons', 'project'
print("Pass" if
      path1==['classroom.udacity.com', 'nanodegrees', 'nd256', 'parts', 'modules', 'lessons', 'project']
      else 'Fail')


path2=r.split_path("classroom.udacity.com/nanodegrees/nd256/parts/modules/lessons/project")
assert (path1==['classroom.udacity.com', 'nanodegrees', 'nd256', 'parts', 'modules', 'lessons', 'project'])
#['classroom.udacity.com', 'nanodegrees', 'nd256', 'parts', 'modules', 'lessons', 'project'
print("Pass" if
      path2==['classroom.udacity.com', 'nanodegrees', 'nd256', 'parts', 'modules', 'lessons', 'project']
      else 'Fail')

r.add_handler("classroom.udacity.com/nanodegrees/nd256/parts/modules/lessons/project","Problems vs Algorithms")
res=r.lookup("classroom.udacity.com/nanodegrees/nd256/parts/modules/lessons/project/")
print("Pass" if res=="Problems vs Algorithms" else "Fail")
assert (res=="Problems vs Algorithms")

r.add_handler("classroom.udacity.com/nanodegrees/nd256/parts/modules/lessons/project","Problems vs Algorithms")
res=r.lookup("classroom.udacity.com/nanodegrees/nd256/parts/modules/lessons/project")
print("Pass" if res=="Problems vs Algorithms" else "Fail")
assert (res=="Problems vs Algorithms")

r.add_handler("classroom.udacity.com/nanodegrees/nd256/parts/modules/lessons","Lessons")
res=r.lookup("classroom.udacity.com/nanodegrees/nd256/parts/modules/lessons")
print("Pass" if res=="Lessons" else "Fail")
assert (res=="Lessons")
import queue

#Node for Linked List Structure
class DLinkedListNode:
    def __init__(self, key=None,value=None):
        self.key=key
        self.value=value
        self.prev=None
        self.next=None

    def set_value(self,value):
        self.value=value

    def get_value(self):
        return self.value

    def get_key(self):
        return self.key

# LRU_Cache contains the double linkedlist (head, tail capacity and size)
class LRU_Cache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.head = None
        self.tail = None
        self.capacity = capacity
        self.size = 0

    def add_node(self, node: DLinkedListNode):
        if not self.head:
            self.head = node
            self.tail = node
        else:
            node.next = self.head
            node.prev = None

            if self.head:
                self.head.prev= node
            self.head = node
        self.size += 1
        return
    def remove_node(self, node: DLinkedListNode):
        if self.head ==None:
            return
        if node == self.head and node ==self.tail:
            self.head = None
            self.tail = None

        elif node ==self.head:
            node.next.prev = None
            self.head = node.next

        elif node ==self.tail:
            node.prev.next = None
            self.tail = node.prev

        elif node !=self.head and node!= self.tail:
            if node.next == None or node.prev == None:
                return
            else:
                prev = node.prev
                node.prev.next = node.next
                node.next.prev = prev
        self.size-=1
        return

    def get(self, key: int) -> int:
        if key in self.dict:
            value = self.dict[key].get_value()
            self.remove_node(self.dict[key])
            self.add_node(self.dict[key])
            return value
        return -1


    def set(self, key: int, value: int) -> None:
        if self.capacity>0:
            if key in self.dict:
                    self.dict[key].set_value(value)
                    self.remove_node(self.dict[key])
                    self.add_node(self.dict[key])
            else:
                node = DLinkedListNode(key, value)
                self.dict[key]=node
                if self.capacity==self.size:
                    del self.dict[self.tail.get_key()]
                    self.remove_node(self.tail)
                self.add_node(node)

        return


##### LRU Cache Test ########
#####Test_1
# #Capacity 0

obj = LRU_Cache(0)
obj.set(1, 1);
assert (obj.size==0)

#####Test_1
# #Capacity 1
# Should be always size 1 because capacity is 1 and should be save just one node in every set
obj = LRU_Cache(1)
obj.set(1, 1);
assert (obj.size==1 and obj.head.key==1 and obj.head.value==1 )
assert (obj.tail.key==1 and obj.tail.value==1 )
obj.set(1, 2);
assert (obj.size==1 and obj.head.key==1 and obj.head.value==2)
assert (obj.tail.key==1 and obj.tail.value==2 )
obj.set(1, 3);
assert (obj.size==1 and obj.head.key==1 and obj.head.value==3 )
assert (obj.tail.key==1 and obj.tail.value==3 )
obj.set(2, 3);
assert (obj.size==1 and obj.head.key==2 and obj.head.value==3 )
assert (obj.tail.key==2 and obj.tail.value==3 )


#####Test_2 ########
# #Capacity 5
our_cache = LRU_Cache(5)
our_cache.set(1, 1);
our_cache.set(2, 2);
our_cache.set(3, 3);
our_cache.set(4, 4);
res=our_cache.get(1)       # returns 1
assert (res==1)
res=our_cache.get(2)       # returns 2
assert (res==2)
res=our_cache.get(9)      # returns -1 because 9 is not present in the cache
assert (res==-1)
our_cache.set(5, 5)
our_cache.set(6, 6)
res=our_cache.get(3)      # returns -1 because the cache reached it's capacity and 3 was the least recently used entry
assert (res==-1)

#####Test_3 ########
obj2 = LRU_Cache(10)
obj2.set(10,13)
obj2.set(3,17)
obj2.set(6,11)
obj2.set(10,5)
obj2.set(9,10)
assert (obj2.get(13)==-1)   #returns -1 is not present
obj2.set(2,19)
assert (obj2.get(2)==19)    #returns 19
assert (obj2.get(3)==17)    #returns 17
obj2.set(5,25)
assert (obj2.get(8)==-1)    #returns -1 is not present
obj2.set(9,22)
obj2.set(5,5)
obj2.set(1,30)
assert (obj2.get(11)==-1)
obj2.set(9,12)
assert (obj2.get(7)==-1)
assert (obj2.get(5)==5)     #returns 5 is it updated
assert (obj2.get(8)==-1)
assert (obj2.get(9)==12)
obj2.set(4,30)
obj2.set(9,3)
assert (obj2.get(9)==3)
assert (obj2.get(10)==5)
assert (obj2.get(10)==5)
obj2.set(6,14)
obj2.set(2,13)
obj2.set(8,17)
obj2.set(7,11)
obj2.set(18,17)
obj2.set(17,11)
obj2.set(12,13)
res=obj2.get(3)         # returns -1 because the cache reached it's capacity
assert (res==-1)
res=obj2.get(10)        # returns -1 because the cache reached it's capacity
#print([(value.key,value.value ) for key, value in obj2.dict.items()])


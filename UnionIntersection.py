class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string


    def append(self, value):

        if self.head is None:
            self.head = Node(value)
            return

        node = self.head
        while node.next:
            node = node.next

        node.next = Node(value)

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next

        return size

def union(llist_1, llist_2):
    if llist_1==None or llist_1.head==None:
        return llist_2
    if llist_2==None or llist_2.head ==None:
        return llist_1
    set_ = set()
    remove_repet(llist_1, set_)
    remove_repet(llist_2, set_)
    head = llist_1.head
    while(head.next!=None):
        head = head.next
    head.next = llist_2.head
    return llist_1
    pass

def intersection(llist_1, llist_2):
    set_1=set()
    set_2 = set()
    remove_repet(llist_1, set_1)
    remove_repet(llist_2, set_2)
    remove_uniques(llist_1,set_2)
    return llist_1
    pass

def remove_repet(list_,set_):
    head =list_.head
    prev = None
    while head!=None:
        if head.value in set_:
            if prev!=None:
                prev.next =head.next
            else:
                list_.head = head.next
        else:
            prev = head
            set_.add(head.value)
        head = head.next
    return

def remove_uniques(list_,set_):
    head = list_.head
    prev = None
    while(head!=None):
        if head.value in set_:
            prev = head
        else:
            if prev != None:
                prev.next = head.next
            else:
                list_.head = head.next
        head = head.next
    return




# Test
linked_list_1 = LinkedList()
linked_list_2 = LinkedList()
linked_list_3 = LinkedList()
linked_list_4 = LinkedList()
linked_list_5 = LinkedList()
linked_list_6 = LinkedList()
linked_list_7 = LinkedList()
linked_list_8 = LinkedList()
linked_list_9 = LinkedList()
linked_list_10 = LinkedList()
linked_list_11 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
element_3 = [1,2,3,4]
element_4 = [5,6,7,8]


for i in element_1:
    linked_list_1.append(i)
    linked_list_3.append(i)

for i in element_2:
    linked_list_2.append(i)
    linked_list_4.append(i)

for i in element_3:
    linked_list_5.append(i)
    linked_list_6.append(i)
    linked_list_7.append(i)
    linked_list_8.append(i)

for i in element_4:
    linked_list_9.append(i)
    linked_list_10.append(i)

print("\n Test #1 diferent lists")
print("\n Union between list:",linked_list_1,"\n with this list:",linked_list_2)
print ("\n The Union Result is", union(linked_list_1,linked_list_2))

print("\n Intersection between list:",linked_list_3,"\n with this list:",linked_list_4)
print ("\n The Intersection Result is", intersection(linked_list_3,linked_list_4))

print("\n Test #2 same lists")
print("\n Union between list:",linked_list_5,"\n with this list:",linked_list_6)
print ("\n The Union Result is", union(linked_list_5,linked_list_6))

print("\n Intersection between list:",linked_list_7,"\n with this list:",linked_list_8)
print ("\n The Intersection Result is", intersection(linked_list_7,linked_list_8))

print("\n Test #3 different lists")
print("\n Union between list:",linked_list_5,"\n with this list:",linked_list_9)
print ("\n The Union Result is", union(linked_list_5,linked_list_9))

print("\n Intersection between list:",linked_list_7,"\n with this list:",linked_list_10)
print ("\n The Intersection Result is", intersection(linked_list_7,linked_list_10))

print("\n Test #4 Empty Lists" )
print("\n Union between list:",LinkedList(),"\n with this list:",LinkedList())
print ("\n The Union Result is", union(LinkedList(),LinkedList()))

print("\n Intersection between list:",LinkedList(),"\n with this list:",LinkedList())
print ("\n The Intersection Result is", intersection(LinkedList(),LinkedList()))

class Group(object):
    def __init__(self, _name):
        self.name = _name
        self.groups = []
        self.users = []

    def add_group(self, group):
        self.groups.append(group)

    def add_user(self, user):
        self.users.append(user)

    def get_groups(self):
        return self.groups

    def get_users(self):
        return self.users

    def get_name(self):
        return self.name

    def print_group(self):
        if self.groups!=None:
            print("--",self.name)
            for elem in self.groups:
                print("---",elem.name)
    def print_users(self):
        if self.groups!=None:
            print("Group:", self.name)
            print("Users:",self.users)
        for elem in self.groups:
            elem.print_users()


def is_user_in_group(user, group):
    """
    Return True if user is in the group, False otherwise.

    Args:
      user(str): user name/id
      group(class:Group): group to check user membership against
    """
    if group != None:
        for elem in group.users:
            if elem==user:
                return True
        for elem in group.groups:
            result=is_user_in_group(user,elem)
            if result==True:
                return True
    return False

##Test 1 ## no childs                              ###########################################
parent = Group("parent")

#Create  User
user_ = "User_1"
#Asociated User
parent.add_user(user_)
print("Test #1 no childs")
print("Belongs User_1 user to parent?",is_user_in_group("User_1", parent))

##Test 2 ## child and 1 subchild                   ###########################################
parent = Group("parent")
child  = Group("child")
sub_child = Group("subchild")

#Asociate parent to child
parent.add_group(child)
#Asociate child to sub_child
child.add_group(sub_child)

#Create  User
user_ = "User_1"
#Asociated User
sub_child.add_user(user_)
print("Test #2  1 child and 1 subchild")
print("Belongs User_1 user to subchild?",is_user_in_group("User_1", sub_child))
print("Belongs User_1 user to child?",is_user_in_group("User_1", child))
print("Belongs User_1 user to parent?",is_user_in_group("User_1", parent))

##Test ## 3 multiple childs and multiple subchilds ###########################################
parent = Group("parent")
child_1  = Group("child_1")
sub_child_1_1= Group("Administrator")
child_2  = Group("child_2")
sub_child_1_2 = Group("Domain Admins")
child_3 = Group("child_3")
sub_child_2_3 = Group("Enterprise Admins")
sub_child_2_4 = Group("Remote Desktop")
sub_child_3_5 = Group("Event Log Readers")

#Asociating parent to childs
parent.add_group(child_1)
parent.add_group(child_2)
parent.add_group(child_3)

#Asociating child to sub_childs
child_1.add_group(sub_child_1_1)
child_1.add_group(sub_child_1_2)
child_2.add_group(sub_child_2_3)
child_2.add_group(sub_child_2_4)
child_3.add_group(sub_child_3_5)

#Create  Users
user_1_1 = "Adam"
user_1_2 = "Angel"
user_1_3 = "David"
user_2_4 = "Victor"
user_2_5 = "Matthew"
user_2_6 = "Linda"
user_2_7 = "Albert"
user_3_8 = "Mary"

#Asociating Users

sub_child_1_1.add_user(user_1_1) #Adam is an Administrator
sub_child_1_1.add_user(user_1_2) #Angel is an Administrator
sub_child_1_2.add_user(user_1_3) #David is a Domain Admin
sub_child_2_3.add_user(user_2_4) #Victor Enterprise Admin
sub_child_2_3.add_user(user_2_5) #Mattthew Enterprise Admin
sub_child_2_3.add_user(user_2_6) #Linda Enterprise Admin
sub_child_2_4.add_user(user_2_7) #Albert is a Remote Desktop
sub_child_3_5.add_user(user_3_8) #Mary is a Event Log Reader


print("Test #3  multiple childs and multiple subchilds")

print("Belongs Adam user to Administrator Group?",is_user_in_group("Adam", sub_child_1_1)) #Returns True Because Adam is just an Administrator
print("Belongs Adam user to Domain Admins?",is_user_in_group("Adam", sub_child_1_2)) #Returns False Because Adam is just an Administrator


print("Belongs Angel user to Administrator Group?",is_user_in_group("Angel", sub_child_1_1)) #Returns True Because Angel is just an Administrator
print("Belongs Angel user to Domain Admins?",is_user_in_group("Angel", sub_child_1_2)) #Returns False Because Angel is just an Administrator

print("Belongs Linda user to Enterprise Admins?",is_user_in_group("Linda", sub_child_2_3)) #Returns True Because Linda is just an Enterprise Admin
print("Belongs Linda user to Remote Desktop?",is_user_in_group("Linda", sub_child_2_4)) #Returns False Because Linda is an Enterprise Admin

print("Belongs Linda user to child2?",is_user_in_group("Linda", child_2)) #Returns True Because Linda is in Group Category  child2
print("Belongs Linda user to child1?",is_user_in_group("Linda", child_1)) #Returns False Because Linda is not in Group Category child1

print("Belongs Linda user to parent?",is_user_in_group("Linda", parent)) #Returns True Because Linda is in Group Category  child2 - sub_child_2_3
print("Belongs Linda user to child2?",is_user_in_group("Linda", child_3)) #Returns False Because Linda is in Group Category child2

#Blockchain
#A Blockchain is a sequential chain of records, similar to a linked list.
#Each block contains some information and how it is connected related
#to the other blocks in the chain. Each block contains a cryptographic hash
#of the previous block, a timestamp, and transaction data. For our blockchain
#we will be using a  SHA-256 hash, the Greenwich Mean Time when the block was
#created, and text strings as the data.

#Solution: Having a block structure and a calc_hash "sha256()" encode what we need to do is
# create the blockchain list and a methods for example add a block to the chain

import hashlib
import datetime

class Node:
    def __init__(self, block):
        self.block= block
        self.next = None

class BlockChain():
    def __init__(self, timestamp=None,data=None):
        if timestamp==None:
            timestamp = datetime.datetime.now()
        if data ==None:
            data=''
        self.head = Node(Block(timestamp,data,None))
        self.last=self.head
        self.size = 1

    def add_block(self, timestamp,data):
        if self.head==None:
            self.head = Node(Block(self,timestamp,data))
            self.size += 1
            return True
        else:
            self.last.next = Node(Block(timestamp,data,self.last.block.hash))
            self.last = self.last.next
            self.size += 1
            return True
        return False

    def print_block_chain(self):
        if self.head ==None:
            return
        head = self.head
        while head!=None:
            Block.print_block(head.block)
            head = head.next
        return
    def verifyBlockChain(self):
        if self.head ==None:
            return
        head = self.head
        hash = self.head.block.hash
        while head!=None:
            prev = head.block.previous_hash
            if hash!=prev and prev!=None:
                print(hash, head.block.previous_hash)
                return False
            hash =head.block.hash
            head = head.next
        return True

class Block:
    def __init__(self, timestamp, data, previous_hash):
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calc_hash()

    def calc_hash(self):
          sha = hashlib.sha256()

          hash_str = self.data.encode('utf-8')

          sha.update(hash_str)

          return sha.hexdigest()

    def print_block(self):
        print(self.timestamp.strftime("\n Time: %b-%d-%Y %H:%M:%S"), "\n Data:"+self.data)

        return


if __name__ == "__main__":

    #test 1 empty blockchain
    print("\n Test#1")
    print("\n Creating an empty Blockchain..")
    BC = BlockChain()
    print("\n Blockchain is Ok?",BC.verifyBlockChain())

    #test 2 add a blocn
    print("\n Test#2 \n")
    print(" Adding block: ","111")
    BC.add_block(datetime.datetime.now(),"111")
    print("\n Blockchain is Ok prevHash==Hash?",BC.verifyBlockChain())

    #test 3 add several blocks
    print("\n Test#3")
    print("\n Creating the Blockchain... with block","242315245 \n")
    BC = BlockChain(datetime.datetime.now(),"242315245")
    print(" Adding block: ","2525234")
    BC.add_block(datetime.datetime.now(),"2525234")
    print(" Adding block: ","07698")
    BC.add_block(datetime.datetime.now(),"07698")
    print(" Adding block: ","98987")
    BC.add_block(datetime.datetime.now(),"98987")
    print("\nPrinting Blockchain")
    BC.print_block_chain()
    print("\n Blockchain is Ok? all prevHash are linked with hash:",BC.verifyBlockChain())

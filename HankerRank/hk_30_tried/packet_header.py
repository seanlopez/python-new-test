class Node:
    def __init__(self,name):
        self.name = name
        self.next = None

class Encapu:
    head_list = []
    def display(self,head):
        current = head
        while current:
            print(current.name,end=" ")
            current = current.next

    def insert(self,name,head):
        if head == None:
            self.head = Node(name)
            self.head_list.append(self.head)
        else:
            self.name = Node(name)
            self.head_list[len(self.head_list)-1].next = self.name
            self.head_list.append(self.name)

        return self.head

if __name__=="__main__":
    my_packet = Encapu()
    header_num = 4   #设置4层
    head = None
    for i in range(header_num):
        name = input()
        head = my_packet.insert(name,head)
    my_packet.display(head)


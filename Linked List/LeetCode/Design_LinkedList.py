class Node():
    def __init__(self, data,next_node = None):
        self.data = data
        self.next = next_node
    
class MyLinkedList():

    def __init__(self, head=None):
        self.head = head

    def get(self, index: int) -> int:
        
        if self.head is None:
            return -1
        
        current_node = self.head
        get_cnt = -1
        while current_node:
            get_cnt += 1
            if get_cnt == index:
                return current_node.data
            current_node = current_node.next
        
        return -1
                   
    def addAtHead(self, val: int) -> None:
        
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return
        
        new_node.next = self.head
        self.head = new_node
        
    def addAtTail(self, val: int) -> None:
        
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next:
            current_node = current_node.next

        current_node.next = new_node
        new_node.next = None
        
    def addAtIndex(self, index: int, val: int) -> None:
        
        new_node = Node(val)
        
        if self.head is None:
            self.head = new_node
            return
        
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        index_cnt = 0
        previous_node = self.head
        current_node = self.head.next
        
        while current_node:
            index_cnt += 1
            if index_cnt == index:
                new_node.next = current_node
                previous_node.next = new_node
                return
            
            previous_node = current_node
            current_node = current_node.next
        
        if index_cnt+1 == index:
            current_node = self.head
            while current_node.next:
                current_node = current_node.next

            current_node.next = new_node
            new_node.next = None
        
    def deleteAtIndex(self, index: int) -> None:
        
        if self.head is None:
            return 
        
        if index == 0:
            self.head = self.head.next
            return

        index_cnt = 0
        previous_node = self.head
        current_node = self.head.next
        
        while current_node:
            index_cnt += 1
            if index_cnt == index:
                previous_node.next = current_node.next
                current_node is None
                return
            previous_node = current_node
            current_node = current_node.next


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)

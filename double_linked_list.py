class Node:
    def __init__(self,data):
        self.prev = None;
        self.data = data;
        self.next = None;


class DoubleLinkedList:
 
    def __init__(self):
        self.headNode = None;
        self.tailNode = None;



    def createNewNode(self,data):
        
        if (self.headNode == None):
            self.headNode = Node(data);
            
            self.tailNode = self.headNode;
            self.headNode.prev = self.tailNode;
            self.headNode.next = self.tailNode;
            self.tailNode.prev = self.headNode;
            self.tailNode.next = self.headNode;
        
        else:
            self.tailNode.next = Node(data);
            self.tailNode.next.prev = self.tailNode;
            self.tailNode.next.next = self.headNode;
            self.tailNode = self.tailNode.next;

    def searchForNode(self,data):
        isFound = False;
            
        refHeadNode = self.headNode;
        isEnd = False;
        while (not isEnd):
            if (refHeadNode.data == data):
                isFound = True
            refHeadNode = refHeadNode.next
            isEnd = refHeadNode != self.tailNode
        return isFound;
 


if __name__ == "__main__":
    dblLinkedList = DoubleLinkedList();
    dblLinkedList.createNewNode(40);
    dblLinkedList.createNewNode(30);
   
    print();
    print("Nodes that exists: ");
    print(dblLinkedList.searchForNode(30))
    print(dblLinkedList.searchForNode(40))
    print();
    print("Nodes that dont exist: ");
    print(dblLinkedList.searchForNode(20))
    print(dblLinkedList.searchForNode(50))
    print();

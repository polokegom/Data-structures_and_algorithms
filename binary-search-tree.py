import copy;
class Node:
    def __init__(self, value):
        self.left = None;   
        self.data = value;
        self.numOfData = 0;
        self.right = None;


class BinarySearchTree:

    

    def __init__(self):
        self.headNode = None;



    def createNewNode(self,data):
        


        if (self.headNode == None):
            self.headNode = Node(data);
        else:
            
            isDataInserted = False;
            refHeadNode = self.headNode;


            while (not isDataInserted):
                if (refHeadNode.data < data):
                    if (refHeadNode.right != None):
                        refHeadNode = refHeadNode.right
                    else:
                        refHeadNode.right = Node(data)
                        isDataInserted = True;
                if (refHeadNode.data > data):
                    if (refHeadNode.left != None):
                        refHeadNode = refHeadNode.left
                    else:
                        refHeadNode.left = Node(data)
                        isDataInserted = True
                if (refHeadNode.data == data):
                    refHeadNode.numOfData += 1;

    def searchForNode(self,data):
            isFound = False;
            
            refHeadNode = self.headNode;

            while (not isFound):
                if (refHeadNode == None) :
                    isFound = True
                    return None
                if (refHeadNode.data == data):
                    isFound = True
                    return refHeadNode;
                               
                if (refHeadNode.data < data):
                    refHeadNode = refHeadNode.right;
                else:
                    
                    if (refHeadNode.data > data):
                        refHeadNode = refHeadNode.left;
 


if __name__ == "__main__":
    bfs = BinarySearchTree();
    bfs.createNewNode(40);
    bfs.createNewNode(30);

    print();
    print("Nodes that exists: ");
    print(bfs.searchForNode(30))
    print(bfs.searchForNode(40))
    print();
    print("Nodes that dont exist: ");
    print(bfs.searchForNode(20))
    print(bfs.searchForNode(50))
    print();
    
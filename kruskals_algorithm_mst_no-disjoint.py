class Vertex:
    def __init__(self, storage):
        self.Vertex1 = None;
        self.storage = storage;
        self.nextVertex = [];

class Edge:
    def __init__(self,edge,vertex, vertex2):
        self.vertex = vertex;
        self.edge = edge;
        self.vertex2 = vertex2;
    


class Graph:


    def __init__(self):
        ''''''
        self.startNode = None;
        self.allEdges= []


    def addNewEdge(self, vec1, vec2, edge):
        ''''''
        if (self.startNode == None):
            self.startNode = vec1;
        self.allEdges.append( Edge(edge, vec1, vec2));
        vec1.nextVertex.append( self.allEdges[len(self.allEdges) - 1]);


    def isCycle(self, listOfEdges, newEdge):
        tempNode = newEdge.vertex;

        ''''listOfVertices = [] + listOfEdges[0].vertex;
        for vertex in listOfEdges:
            listOfVertices.append(vertex.vertex2);
        '''

        #Transverse graph and view cycle
        tempListOfValidEdges = [] +listOfEdges
        tempListOfValidEdges.append(newEdge);
        pastVertices = []
        liveVertices = []
        liveVertices.append(tempNode);
        nextVertices = []
        isCycleFound = False;
        isPathFlowing = False;
        while (liveVertices):
            nextVertices.clear();
            for presentVertex in liveVertices:
                if (presentVertex.nextVertex != []):
                    pastVertices.append(presentVertex); 
                    for next in  presentVertex.nextVertex:
                        isPathFlowing = (next in tempListOfValidEdges);
                        if ((not next.vertex2 in pastVertices) and (next.vertex2 != None) and (isPathFlowing)):                           
                           nextVertices.append(next.vertex2);
                        isCycleFound = (next.vertex2 in pastVertices)
                        if(isCycleFound):
                            nextVertices.clear();
                            liveVertices.clear();
             
            liveVertices.clear();
            liveVertices += nextVertices;
        return isCycleFound;


    def makingMinSpanningTree(self):
        

        tempNode = self.startNode;

        #Transversal code
        #Sort to Asc
        sortedEdges = [] + self.allEdges;
        minSpanTree = []
        for k in range( len(sortedEdges)):
            for j in range(len(sortedEdges)):
                if (sortedEdges[k].edge < sortedEdges[j].edge):
                    sortedEdges[k],sortedEdges[j] = sortedEdges[j], sortedEdges[k]
        for ordEdge in sortedEdges:
            if not self.isCycle(minSpanTree, ordEdge):
                minSpanTree.append(ordEdge);
        return minSpanTree;

    def printGraph(self):
        ''''''
        tempNode = self.startNode;

        #Transversal code
        pastVertices = []
        liveVertices = []
        liveVertices.append(tempNode);
        nextVertices = []
        while (liveVertices):
            printGraph = '';
            nextVertices.clear();
            for presentVertex in liveVertices:
                ''''''
                if (presentVertex.nextVertex != []):
                    printGraph = '['+ str(presentVertex.storage) + '] (Head)=>';
                    pastVertices.append(presentVertex); 
                    for next in  presentVertex.nextVertex:
                        if ((not next.vertex2 in pastVertices) and (next.vertex2 != None)):
                            nextVertices.append(next.vertex2);
                        printGraph += ' [' +  next.vertex2.storage +  '] (tail; Edge:' + str(next.edge) + '), ';
                    
                    printGraph = printGraph[:-2];
                    print(printGraph);
            liveVertices.clear();
            liveVertices += nextVertices;

                

if __name__ == "__main__":
    a = Vertex("A");
    b = Vertex("B");
    c = Vertex("C");
    d = Vertex("D");
    e = Vertex("E");
    f = Vertex("F");
    print("Finished loading Vertex...");
    graph = Graph();
    graph.addNewEdge(a,b,3);
    graph.addNewEdge(b,c,2);
    graph.addNewEdge(c,d,4);
    graph.addNewEdge(c,a,4);



    print("Finished loading Graph...");
    print()
    print("Edges of Graph:")    
    graph.printGraph();

    print()
    print("===========================")




   

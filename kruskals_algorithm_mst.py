class Vertex:
    def __init__(self, storage):
        self.Vertex1 = None;
        self.storage = storage;
        self.nextVertex = [];


class Edge:
    def __init__(self,edge, vertex2):
        self.edge = edge;
        self.vertex2 = vertex2;


class Graph:


    def __init__(self):
        ''''''
        self.startNode = None;

    def addNewEdge(self, vec1, vec2, edge):
        ''''''
        if (self.startNode == None):
            self.startNode = vec1;
        vec1.nextVertex.append( Edge(edge, vec2));    
    
    def printMinSpanningTree(self):
        ''''''

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
    graph.addNewEdge(a,c,4);


    print("Finished loading Graph...");
    print()

    print("Edges of Graph:")
    print()
   
    graph.printGraph();




   

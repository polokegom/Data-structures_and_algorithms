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
        self.startNode.nextVertex.push( Edge(edge, vec2));    
    
    def printMinSpanningTree(self):
        ''''''

    def printGraph(self):
        ''''''
        tempNode = self.baseNode;

        #Transversal code
        pastVertices = []
        liveVertices = []
        liveVertices.push(tempNode);
        nextVertices = []
        while (liveVertices):
            printGraph = '';
            nextVertices.clear();
            for presentVertex in liveVertices:
                ''''''

                printGraph = ' (Head):';
                pastVertices.push(presentVertex); 
                for nextVertex in  liveVertices.vertex2:
                    if (pastVertices in nextVertex):
                        nextVertices.push(nextVertex);
                    printGraph += ' ' +  nextVertex.data +  ' (tail; Edge:' + nextVertex.edge + '), ';
                
                printGraph = printGraph[:-2]  + "\n";
                print(printGraph);
            liveVertices.clear();
            liveVertices += nextVertices;

                



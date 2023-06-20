
class Graph:
    class Node:

        def __init__(self, b1, b2, b3, prev = None, next = None):
            self.b1 = b1
            self.b2 = b2
            self.b3 = b3
            self.prev = prev
            self.visited = False
            self.neighbors = []

        def __hash__(self):
            return int(self.b1)*1000000 + int(self.b2)*1000 + int(self.b3)

        def __repr__(self):
            return '(' + str(self.b1) + ',' + str(self.b2) + ',' + str(self.b3) + ')'


    def __init__(self, m1, m2, m3):
        self.maxNode = Graph.Node(m1, m2, m3)
        self.vertices = {}


    def find(self,amount):
        if int(amount) == 0:
            print('The path is: [' + str(Graph.Node(0,0,0)) + ']')
            return
        self.createBucketGraph()
        self.vertices[hash(Graph.Node(0,0,0))].neighbors.append(Graph.Node(self.maxNode.b1,0,0))
        self.vertices[hash(Graph.Node(0,0,0))].neighbors.append(Graph.Node(0,self.maxNode.b2,0))
        self.vertices[hash(Graph.Node(0,0,0))].neighbors.append(Graph.Node(0,0,self.maxNode.b3))
        for n in self.vertices:
            temp = self.vertices[hash(n)]
        path = self.breadthFirstSearch(amount)
        print('The path is: ' + str(path))

    def createBucketGraph(self):
        # queue (0,0,0) then find permutations of buckets that can be made, add those to queue if they aren't in graph, remove first node, go to next node and repeat process, go until nothing in queue
        queue=[]
        self.vertices[hash(Graph.Node(0,0,0))] = Graph.Node(0,0,0)
        queue.append(Graph.Node(0,0,0))
        while(len(queue)!=0):
            perms = self.getPermutaions(queue.pop(0))
            for n in perms:
                if not hash(n) in self.vertices.keys():
                    self.vertices[hash(n)] = n
                    queue.append(n)
    
    
    def getPermutaions(self,n):
        #find permutations of Node n using one move (fill, empty, transfer) (12 possibilities)
        n1 = n.b1
        n2 = n.b2
        n3 = n.b3
        l = []
        l.append(Graph.Node(0,n2,n3))
        l.append(Graph.Node(n1,0,n3))
        l.append(Graph.Node(n1,n2,0))
        l.append(Graph.Node(self.maxNode.b1,n2,n3))
        l.append(Graph.Node(n1,self.maxNode.b2,n3))
        l.append(Graph.Node(n1,n2,self.maxNode.b3))
        if(int(self.maxNode.b2) >= int(n1)+int(n2)): #1 -> 2
            l.append(Graph.Node(0,int(n2)+int(n1),n3))
        else:
            l.append(Graph.Node((int(n1)+int(n2))-int(self.maxNode.b2),int(self.maxNode.b2),n3))
        
        if(int(self.maxNode.b3) >= int(n1)+int(n3)): # 1 -> 3
            l.append(Graph.Node(0,n2,int(n3)+int(n1)))
        else:
            l.append(Graph.Node((int(n1)+int(n3))-int(self.maxNode.b3),n2,int(self.maxNode.b3)))
       
        if(int(self.maxNode.b1) >= int(n1)+int(n2)): # 2 -> 1
            l.append(Graph.Node(int(n2)+int(n1),0,n3))
        else:
            l.append(Graph.Node(int(self.maxNode.b1),(int(n1)+int(n2))-int(self.maxNode.b1),n3))
        
        if(int(self.maxNode.b3) >= int(n3)+int(n2)): # 2 -> 3
            l.append(Graph.Node(n1,0,int(n3)+int(n2)))
        else:
            l.append(Graph.Node(n1,(int(n2)+int(n3))-int(self.maxNode.b3),int(self.maxNode.b3)))
        
        if(int(self.maxNode.b1) >= int(n1)+int(n3)): # 3 -> 1
            l.append(Graph.Node(int(n1)+int(n3),n2,0))
        else:
            l.append(Graph.Node(int(self.maxNode.b1),n2,(int(n1)+int(n3))-int(self.maxNode.b1)))
        
        if(int(self.maxNode.b2) >= int(n3)+int(n2)): # 3 -> 2
            l.append(Graph.Node(n1,int(n2)+int(n3),0))
        else:
            l.append(Graph.Node(n1,int(self.maxNode.b2),(int(n2)+int(n3))-int(self.maxNode.b2)))
        for node in l:
            if(hash(node) != hash(n)) and ((node in n.neighbors) == False):
                n.neighbors.append(node)
        return l
    
    def breadthFirstSearch(self, amount):
        #make queue and add a node then go through neighbors, add to queue, remove original until found
        queue=[]
        queue.append(self.vertices[hash(Graph.Node(0,0,0))])
        queue[0].visited = True
        while(len(queue)!=0):
            node = queue[0]
            neighborhood = node.neighbors
            for n in neighborhood:
                temp = self.vertices[hash(n)]
                if temp.visited == False:
                    if(node.prev!=temp):
                        temp.prev = node
                    if int(temp.b1) == int(amount) or int(temp.b2) == int(amount) or int(temp.b3) == int(amount):
                        return self.getPath(temp)
                    queue.append(temp)
                    temp.visited = True
            queue.pop(0)
        return ["No Possible Path"]


    def getPath(self,node):
        l = []
        while hash(node) != 0:
            l.append(node)
            node = node.prev
        l.append(node)
        lst = []
        for i in l:
            lst.insert(0,i)
        return lst

# RUNTIME CODE
size1,size2,size3,target = -1,-1,-1,-1
while int(size1) <= 0:
    size1 = input('Input a positive integer for the size of jar 1: ')
while int(size2) <= 0:
    size2 = input('Input a positive integer for the size of jar 2: ')
while int(size3) <= 0:
    size3 = input('Input a positive integer for the size of jar 3: ')
while int(target) < 0 or (int(target) > int(size1) and int(target) > int(size2) and int(target) > int(size3)):
    target = input('Input a positive integer for the target less or equal to the size of the largest bucket: ')
print('Finding quickest path to a fill of ' + str(target) + ' with buckets of size ' + str(size1) + ' ' + str(size2) + ' ' + str(size3))
g = Graph(size1,size2,size3)
g.find(target)


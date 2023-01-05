import dummy_data

def uniform( start, goal):                                  # function for BFS 
    global parentInPath                                       #list to mark node by their parent so you can traverse back from the goal node to path node by parent
    parentInPath = {} 
    visited = []                                                # List for visited nodes.
    PriortyQueue = []                                           # Initialize a queue
    global path
    path = []
    graph = dummy_data.modifiedgraph
    visited.append(start)                                    #adding initial node to the list
    parentInPath[start] = start
  
    firstParent = [0,str(start)]                                #making the parent node as start with 0 distance
    PriortyQueue.append(firstParent)
   

    while PriortyQueue:                                     # Creating loop to visit each node inside this queue
        parent = PriortyQueue.pop(0)                        #removing the first list that was first entered to use it as parent
        
        if(  str(parent[1]).isnumeric()):                   #swapping the first and second field in each child list so the heuristic distance appear first then the node char
           parent[0],parent[1]= parent[1],parent[0]
        
        if parent[1] == goal:                               #queting if the goal node is reached
            getPath(parent[1])
            path.reverse()

            return path                              #returing the sum of real distance

        for child in graph[parent[1]]:                      #expanding to child nodes
            
            
            if( str(child[1])[:1].isnumeric()):             #swapping the first and second field in each child list so the heuristic distance appear first then the node char
                child[0],child[1]= child[1],child[0]
                #print("i got here")
            #print(50*'#')
            #print(child)
            if child[1] not in visited:                     #condition for checking to work with only unvisited nodes
             
             child[0] = child[0]+parent[0]                  
             
             visited.append(child[1])                       #adding this node to the queue
             parentInPath[child[1]] = parent[1]
             PriortyQueue.append(child)
             PriortyQueue.sort()                            #sorting the priority queue


def getPath(node):                                           #genrating the path after finding the goal node
    if parentInPath[node] != node:
        path.append(node)
        getPath(parentInPath[node])
    else:
        path.append(node)
        return   


import dummy_data


def Bfs_Algorithm():
    
    if(int(len(queue))==int(0)):
        return
    
    while queue:
        first=queue.pop(0)
        
        for i in dummy_data.graph[first].keys():
            if(vis[i]==False):
                queue.append(i)
                parent[i] = first
                vis[i] = True
        


def getPath(node):
    if parent[node] != node:
        ans.append(node)
        getPath(parent[node])
    else:
        ans.append(node)
        return



# function will be used outside this class to get path
def bfs_algorithm(start,end):
    global source
    global destination
    global ans
    global queue
    global vis
    global parent
    source = start
    destination = end
    
    queue = []
    parent = {}
    vis={
        "ashmoun":False,
        "bajour":False,
        "berkh_elsab3":False,
        "menouf":False,
        "elsadat":False,
        "srs_ellyan":False,
        "tla":False,
        "elshohada":False,
        "shebin_elkom":False,
        "quesna":False
    }

    ans = []


    

    # assign parent[start] = start to stop at it 
    # when generating the actual path at getPath function
    
    parent[start] = start

    queue.append(start)
    vis[source] = True

    Bfs_Algorithm()
    # print(parent)
    getPath(end)
    
    
    return ans


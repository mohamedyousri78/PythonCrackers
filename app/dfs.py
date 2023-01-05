import dummy_data


def Dfs_Algorithm(node):
    
   
    vis[node] = True  
    if vis[destination] == True:
        return  
    for i in dummy_data.graph[node].keys():
        if(vis[i]==False):
            parent[i] = node
            Dfs_Algorithm(i)
        


def getPath(node):
    if parent[node] != node:
        ans.append(node)
        getPath(parent[node])
    else:
        ans.append(node)
        return



# function will be used outside this class to get path
def dfs_algorithm(start,end):
    global source
    global destination
    global ans
    global vis
    global parent
    source = start
    destination = end
    

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

    vis[source] = True

    Dfs_Algorithm(source)
    # print(parent)
    getPath(end)
    
    
    return ans


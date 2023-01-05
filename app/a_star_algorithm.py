import dummy_data

# init the shortest distance map with big value
shortest_dis={}
def init():
    shortest_dis['ashmoun']=10000000.0
    shortest_dis['bajour']=10000000.0
    shortest_dis['berkh_elsab3']=10000000.0
    shortest_dis['menouf']=10000000.0
    shortest_dis['elsadat']=10000000.0
    shortest_dis['srs_ellyan']=10000000.0
    shortest_dis['tla']=10000000.0
    shortest_dis['elshohada']=10000000.0
    shortest_dis['shebin_elkom']=10000000.0
    shortest_dis['quesna']=10000000.0

opened = []
closed = []
def A_search(source,destination):

    if(int(len(opened))==int(0)):      # check if there is any data to be processed
        return

    first=opened[0]           # get the smallest distance
    for j in opened:
        if(list(first.keys())[0]>list(j.keys())[0]):
            first=j


    dis=list(first.keys())[0]       #get key for the map


    heurstic_dis=dummy_data.heurstic_data[destination][first[dis]]     # get heurstic distance between new source and distination

    real=dis-heurstic_dis       # get real distance by subtract heurstic data


    parent=first[dis]                                      # check neighbours
    for f in dummy_data.graph[first[dis]]:
        current_real_distance = dummy_data.graph[parent][f]
        heurstic_dis = dummy_data.heurstic_data[destination][f]

        total_value= float(current_real_distance) + float(real) + float(heurstic_dis)  #check if the new path is smaller than the previous paths
        if( total_value < float(shortest_dis[f]) ):  #update shortest path and add for opened

            opened.append({ total_value : f})
            shortest_dis[f]=total_value

    closed.append(first[dis])   #update opened and closed lists
    opened.remove(first)


    A_search(source,destination) # repeat

source=""
destination=""

ans=[]
path=[]

def dfs(source,value,total_distance):  #generate path

    if(total_distance>value):  #check current cost
        return

    if(source==destination):   #save valid answer
        ans.clear()
        for i in path:
            ans.append(i)

    for i in dummy_data.graph[source]:      # process children
        if(path.count(i)==0):
            path.append(i)
            dfs(i,value,total_distance+dummy_data.graph[source][i])
            path.remove(i)

# function will be used outside this class to get path
def Astar(start,end):
    init()
    global source
    global destination
    global opened
    global closed
    global ans
    global path
    global shortest_dis
    source= start
    destination= end
    path = []
    ans=[]
    opened.append({dummy_data.heurstic_data[destination][source]: source})
    shortest_dis[source]= dummy_data.heurstic_data[destination][source]
    closed=[]
    A_search(start,end)
    path.append(source)
    total_value = shortest_dis[end]
    dfs(source, float(total_value), float(0.0))
    return ans


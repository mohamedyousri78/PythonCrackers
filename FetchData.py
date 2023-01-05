import requests
import copy 
data = {
    "ashmoun": 150563,
  "bajour": 151060,
  "berkh_elsab3": 99946,
  "menouf": 188472,
  "elsadat": 95514,
  "srs_ellyan": 119284,
  "tla": 157868,
  "elshohada": 93690,
  "shebin_elkom": 93110,
  "quesna": 195273
}
graph = {} 
for sourse_name , sourse in data.items() : 
    g = {}

    for dist_name , dist in data.items() : 

        res = requests.get(f'https://eg.toponavi.com/{sourse}-{dist}')
        response = res.text.split("\n")
        sum = 9284982 
        for i in response : 
            sum = sum - 1 
            if sum == 0 : 
                distance = int(i.strip()[0:2]) 
                g[dist_name] = distance 
               # print(f'{sourse_name} to {dist_name} = {distance}')
            if i.startswith("<div id=\"tn_slider\">") : 
                sum = 14 ; 
    graph[sourse_name] = copy.deepcopy(g)

print(graph)
#print(response)
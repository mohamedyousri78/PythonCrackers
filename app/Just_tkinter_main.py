from tkinter import *
import bfs 
import dfs 
import dummy_data
import a_star_algorithm
import uniformSearch
import tkintermapview as tkintermapview
from PIL import ImageTk,Image



data = [
 "ashmoun" ,
  "bajour",
 "berkh_elsab3",
  "menouf",
  "elsadat",
  "srs_ellyan",
  "tla",
  "elshohada",
  "shebin_elkom",
  "quesna"
]

algorithms = [
	"DFS",
	"BFS",
	"Uniform Cost",
	"A_Star",
]


selectAlgo='DFS'
startingCity='ashmoun'
goalCity='none'

def click():
    global selectAlgo
    selectAlgo=clicked1.get()
    global startingCity
    startingCity=clicked2.get()
    global goalCity
    goalCity=clicked3.get()
    # Delete all previous markers.
    # delete all markers before drawing the new path.
    map_widget.delete_all_marker()
    applyAlgorithm()
root = Tk()
root.title('searching task')
screenWidth = 800
screenHight = 600
mapHight = screenHight - 80
root.geometry(f"{screenWidth}x{screenHight}")


frame = LabelFrame(root,text='main panel',width=screenWidth,height=200,padx=200)
frame.grid(row=0,column=0)


map_widget = tkintermapview.TkinterMapView(root, width=screenWidth, height=mapHight)
# Set Coordinates
#map_widget.set_position(36.1699, -115.1396) # Vegas Baby!

# Set Address
map_widget.set_address("Menoufia, Egypt")

# Set A Zoom Level
map_widget.set_zoom(10)
map_widget.grid(row=1,column=0)


algo=Label(frame,text="Algorithm")
algo.grid(row=0,column=2)


clicked1 = StringVar()
clicked1.set(algorithms[0])
drop1 = OptionMenu(frame, clicked1, *algorithms)
drop1.grid(row=1,column=2)

src=Label(frame,text="from")
src.grid(row=0,column=0)
clicked2 = StringVar()
clicked2.set(data[0])
drop2 = OptionMenu(frame, clicked2, *data)
drop2.grid(row=1,column=0)

algo=Label(frame,text="to")
algo.grid(row=0,column=1)
clicked3 = StringVar()
clicked3.set(data[0])
drop3 = OptionMenu(frame, clicked3, *data)
drop3.grid(row=1,column=1)




start = Button(frame, text="start",padx=30,pady=15,bg='#8E8EE5',command=click)
start.grid(row=0, column=3,rowspan=2)




def getPostion(algoResult):
    path=[]
    for i in algoResult:
        marker = map_widget.set_marker(deg_x=dummy_data.degr_x[i],deg_y=dummy_data.degr_y[i])
        path.append(marker.position)
        if i != startingCity and i != goalCity:  
            marker.delete()
    return path
path_1 = map_widget.set_path([(30.2941595,30.9756935),(30.2941595,30.9756935)])
path_1.delete()

def drawPath(path):
    if (len(path) > 0):
        global path_1
        path_1 = map_widget.set_path(path)


def applyAlgorithm():
    path_1.delete()
    if selectAlgo!='default':
        if selectAlgo=='A_Star':
            if(startingCity!= goalCity):
                generatedPath = a_star_algorithm.Astar(startingCity,goalCity)
                path = getPostion(generatedPath)
        elif selectAlgo == 'BFS':
            if(startingCity!= goalCity):
                generatedPath = bfs.bfs_algorithm(startingCity,goalCity)
                path = getPostion(generatedPath)
        elif selectAlgo == 'DFS':
            if(startingCity!= goalCity):
                generatedPath = dfs.dfs_algorithm(startingCity,goalCity)
                path = getPostion(generatedPath)
        elif selectAlgo == 'Uniform Cost':
            if(startingCity!= goalCity):
                generatedPath = uniformSearch.uniform(startingCity,goalCity)
                path = getPostion(generatedPath)

        drawPath(path)
        
        
       



root.mainloop()

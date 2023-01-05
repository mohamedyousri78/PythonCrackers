from tkinter import *
import tkintermapview as tkintermapview
import customtkinter
from tkinter import *
import bfs 
import dfs 
import dummy_data
import a_star_algorithm
import uniformSearch

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("green")  # Themes: blue (default), dark-blue, green


data = dummy_data.data                  
algorithms = dummy_data.algorithms

def click():
    global selectAlgo
    selectAlgo=clicked1.get()
    global startingCity
    startingCity=clicked2.get()
    global goalCity
    goalCity=clicked3.get()
    # Delete all previous markers.
    map_widget.delete_all_marker()
    applyAlgorithm()
def getPostion(algoResult):
    path=[]
    for i in algoResult:
        marker = map_widget.set_marker(deg_x=dummy_data.degr_x[i],deg_y=dummy_data.degr_y[i])
        path.append(marker.position)
        if i != startingCity and i != goalCity:
            marker.delete()
    return path

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

Croot =  customtkinter.CTk()                                #creating main window
Croot.title('Path Finder')
Croot.geometry(f"{800}x{800}")

buttonFrame = customtkinter.CTkFrame(master=Croot,width=800,height=200)                 #create frame for buttons
buttonFrame.pack( padx=20, pady=20)
Mapframe = customtkinter.CTkFrame(master=Croot,width=800,height=600)                    #create frame for map
Mapframe.pack(after= buttonFrame, padx=20, pady=20)
map_widget = tkintermapview.TkinterMapView(Mapframe, width=800, height=600)



map_widget.set_address("Menoufia, Egypt")

# # Set A Zoom Level
map_widget.set_zoom(10)
map_widget.grid(row=1,column=0)


#three menus to get input


algo= customtkinter.CTkLabel(master=buttonFrame,text="Algorithm")   #button to select algorithm
algo.grid(row=0,column=2)                                           #packing it in specified frame
clicked1 = customtkinter.StringVar(value=algorithms[0])

drop1 = customtkinter.CTkComboBox(master=buttonFrame, variable=clicked1, values=algorithms)
drop1.grid(row=1,column=2)



src= customtkinter.CTkLabel(master=buttonFrame,text="from")
src.grid(row=0,column=0)
clicked2 = customtkinter.StringVar(value=data[0])

drop2 = customtkinter.CTkComboBox(master=buttonFrame, variable=clicked2, values=data)
drop2.grid(row=1,column=0)



algo= customtkinter.CTkLabel(master=buttonFrame,text="to")
algo.grid(row=0,column=1)
clicked3 = customtkinter.StringVar(value=data[1])

drop3 = customtkinter.CTkComboBox(master=buttonFrame, variable=clicked3, values=data)
drop3.grid(row=1,column=1)



#button to start funcationality
start = customtkinter.CTkButton(master=buttonFrame, text="start",command=click)
start.grid(row=1, column=3,rowspan=2,columnspan=2)

#setting initial position
path_1 = map_widget.set_path([(30.2941595,30.9756935),(30.2941595,30.9756935)])
path_1.delete()

Croot.mainloop()
import tkinter
from operator import itemgetter
from tkinter import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

from main import Main

tk = Tk() # makes a new window
tk.geometry(f'{tk.winfo_screenwidth()}x{tk.winfo_screenheight()}')
tk.title("Vancouver Env Stats")




# aqi_percentage = Main.aqi_percentage()
# pop_percentage = Main.population_percentage()
# tphos_percentage = Main.tphos_percentage()

# def compare_percentages():
#     sorted_percentages =[[aqi_percentage, 'aqi_percentage'], [pop_percentage, 'population_percentage'], [tphos_percentage,'tphos_percentage']].sort()
#     output =sorted_percentages[0][0]
#     return output
#     #f'1) {sorted_percentages[0][1]} : {sorted_percentages[0][0]}'
# output = compare_percentages()
# priorityLabelText = StringVar()

# priorityLabelText.set("Top Priority: "+ str(output))
# priorityLabel = Label(topFrame, textvariable=priorityLabelText)
# priorityLabel.pack(side=TOP)

leftFrame = Frame(tk, borderwidth = 2,background = 'green')
leftFrame.pack(side = LEFT, fill = X, expand = 1)
rightFrame = Frame(tk, borderwidth=2, background='blue')
rightFrame.pack(side = RIGHT,fill=X, expand = 1)


#application icon
winIcon = PhotoImage(file = 'logo.png') 
tk.iconphoto(False, winIcon) 

# time = [2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054] # NEED TO GET X and Y LISTS
# #get time and respective variable lists w/values from main
# y = Main.graph_values('property') #GRAPH TO DISPLAY IS BY CHOICE OF USER
# ax.plot(time, y)
# graph = FigureCanvasTkAgg(fig, master=leftFrame)
# graph.draw()
# graph.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

# update_graph('population_change')

#DROPDOWN MENU in left frame graph value chooser
optionsY = ['population', 'aqi', 'tphos', 'population_change', 'aqi_change', 'tphos_change']
chosenY = StringVar(value='population_change')
# chosenY.set('population')
dropMenuY = OptionMenu(leftFrame, chosenY, *optionsY)
dropMenuY.pack(side=TOP, fill=BOTH)

fig = Figure(figsize=(5, 4), dpi=100)
graph = FigureCanvasTkAgg(fig, master=leftFrame)
ax = fig.add_subplot()

def update_graph():
    global leftFrame, chosenY, graph
    value = str(chosenY.get())
    #get time and respective variable lists w/values from main
    time = [2043, 2044, 2045, 2046, 2047, 2048, 2049, 2050, 2051, 2052, 2053, 2054] # NEED TO GET X and Y LISTS
    y = Main.graph_values(value) #GRAPH TO DISPLAY IS BY CHOICE OF USER
    ax.cla()
    if value == 'tphos':
        ax.plot(time, [.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05,.05])
    elif value == 'population':
        ax.plot(time, [524500, 524500,524500,524500,524500,524500,524500,524500,524500,524500,524500,524500])
    elif value == 'aqi':
        ax.plot(time, [150, 150,150,150,150,150,150,150,150,150,150,150])
    ax.plot(time, y)
    graph.draw()
    graph.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)

update_graph()

submit_button = tkinter.Button(leftFrame, text='Submit', background = 'green', command = update_graph) 
submit_button.pack(side = BOTTOM) 
#TEXT ENTRY BOX
input1 = StringVar()
input2 = StringVar()
textBox1 = Entry(rightFrame, width=20, textvariable=input1)
textBox2 = Entry(rightFrame, width=20, textvariable=input2)
textBox1.pack(side=TOP, fill=BOTH)
textBox2.pack(side=TOP, fill=BOTH)
#intInput1 = textBox1.get()
# intInput2 = textBox2.get()

#DROPDOWN MENU in right frame for avg change of variable
optionsChange = ['population','aqi','tphos']
chosenChange = StringVar()
chosenChange.set('population')
dropMenuChange = OptionMenu(rightFrame, chosenChange, *optionsChange)
dropMenuChange.pack(side=TOP, fill=BOTH)
changeButton = Button(rightFrame, text="Submit", command= Main.compare_years)
changeButton.pack(side=BOTTOM)
labelText = StringVar()
labelText.set(Main.compare_value)
label = Label(rightFrame, textvariable=labelText)
label.pack(side=BOTTOM)


#EXIT BUTTON
#example button w/ a frame
#exitFrame = Frame(tk, borderwidth=2, background = 'red')
#exitFrame.pack(side = BOTTOM, fill=X, expand=1)
#button = Button(exitFrame, text="Exit", command=tk.destroy) 
#button.pack(side=BOTTOM) 


tk.mainloop() #creates the tangible window, updates the tk on click

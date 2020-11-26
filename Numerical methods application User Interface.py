# Numerical methods application User Interface

from tkinter import *
from pandas import *
from math import sin
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Data for plot
df = DataFrame({'A': range(20),
                'B': [sin(i) for i in range(20)]
                }, index=range(20))   

method = 0
isrunAppagain = False
listNum = 0

app = Tk()
app.config(bg='lightgray')
app.title("The title of the project")
app.geometry("800x600")
app.minsize(1000, 700)
app.rowconfigure(0, weight=1)
app.columnconfigure(3, weight=1)

# Defining a funtion for the button command
def diffMethodsList():
    global listNum
    listNum = 1
    # Add the names of the numerical methods for the list
    lbm.delete(0, END)
    lbm.insert(END, "First derivative: Forward 2 point")
    lbm.insert(END, "First derivative: Central 2 point")
    lbm.insert(END, "First derivative: Backward 2 point")
    lbm.insert(END, "First derivative: Forward 3 point")
    lbm.insert(END, "First derivative: Central 3 point")
    lbm.insert(END, "First derivative: Backward 3 point")

def integMethodsList():
    global listNum
    listNum = 2
    # Add the names of the numerical methods for the list
    lbm.delete(0, END)
    lbm.insert(END, "Integration 1")
    lbm.insert(END, "Integration 2")
    lbm.insert(END, "Integration 3")
    lbm.insert(END, "Integration 4")

def oneD():
    global df
    y_dot = [0] * len(df)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(0, len(x)-1, 1):
        y_dot[i] = (y[i+1] - y[i]) / h 
    y_dot = DataFrame({'A': range(len(df)),
                'B': y_dot
                }, index=range(len(df)))  
    return y_dot

def twoD():
    global df
    y_dot = [0] * len(df)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(1, len(x)-1, 1):
        y_dot[i] = (y[i+1] - y[i-1]) /(2*h)
    y_dot = DataFrame({'A': range(len(df)),
                'B': y_dot
                }, index=range(len(df)))  
    return y_dot

def threeD():
    global df
    y_dot = [0] * len(df)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(1, len(x), 1):
        y_dot[i] = (y[i] - y[i-1]) / h 
    y_dot = DataFrame({'A': range(len(df)),
                'B': y_dot
                }, index=range(len(df)))  
    return y_dot

def fourD():
    global df
    y_dot = [0] * len(df)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(0, len(x)-2, 1):
        y_dot[i] = (-y[i+2] + 4*y[i+1] - 3*y[i]) / (2*h) 
    y_dot = DataFrame({'A': range(len(df)),
                'B': y_dot
                }, index=range(len(df)))  
    return y_dot

def fiveD():
    global df
    y_dot = [0] * len(df)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(2, len(x)-2, 1):
        y_dot[i] = (y[i-2] - y[i+2] + 8*y[i+1] -8*y[i-1]) / (12*h) 
    y_dot = DataFrame({'A': range(len(df)),
                'B': y_dot
                }, index=range(len(df)))  
    return y_dot

def sixD():
    global df
    y_dot = [0] * len(df)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(2, len(x), 1):
        y_dot[i] = (3*y[i] - 4*y[i-1] + y[i-2]) / (2*h) 
    y_dot = DataFrame({'A': range(len(df)),
                'B': y_dot
                }, index=range(len(df)))  
    return y_dot


def runApp(method, listNum):
    # Process the data
    global isrunAppagain, figure2, ax2, df
    name = ''
    df2 = df.copy()
    if method == 0:
        return
    if method == (0,) and listNum == 1:
        df2 = oneD()
        name = 'First derivative: Forward'
    if method == (1,) and listNum == 1:
        df2 = twoD()
        name = 'First derivative: Backward'
    if method == (2,) and listNum == 1:
        df2 = threeD()
        name = 'First derivative: Central'
    if method == (3,) and listNum == 1:
        df2 = fourD()
        name = 'First derivative: Forward 3 point' 
    if method == (4,) and listNum == 1:
        df2 = fiveD()
        name = 'First derivative: Central 3 point'   
    if method == (5,) and listNum == 1:
        df2 = sixD()
        name = 'First derivative: Backward 3 point'        

    if method == (0,) and listNum == 2:
        df2 = oneI()
        name = 'Integration: mid-point Orthogonal'
    if method == (1,) and listNum == 2:
        df2 = twoI()
        name = 'Integration: Trapezoid'
    if method == (2,) and listNum == 2:
        df2 = threeI()
        name = 'Integration: Simpsons'
    if method == (3,) and listNum == 2:
        df2 = fourI()
        name = 'Integration: ' 
    if method == (4,) and listNum == 2:
        df2 = fiveI()
        name = 'Integration: '   
    if method == (5,) and listNum == 2:
        df2 = sixI()
        name = 'Integration: '  

    if isrunAppagain==False:
        isrunAppagain = True
        df2 = df.loc[0:,'B']
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        figure2.canvas.draw_idle()
    else:
        ax2.cla()
        df2 = df2.loc[0:,'B']
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        ax2.set_title(name)
        figure2.canvas.draw_idle()
    


# Frame for the listbox and the scrollbar
fr_lbm_sbm = Frame(app)
fr_lbm_sbm.grid(row=0, column=0, sticky=N+S)

lbl1 = Label(fr_lbm_sbm, text='Methods', fg='black', font=('Helvetica', 16, 'bold'))
lbl1.pack(side=TOP)

#Scrollbar for the listbox of methods - sbm
scrollbar = Scrollbar(fr_lbm_sbm, orient='vertical')
scrollbar.pack(side=RIGHT, fill=Y)

# Listbox of methods - lbm
lbm = Listbox(fr_lbm_sbm, yscrollcommand=scrollbar.set, font=('Helvetica', 14))
lbm.pack(expand=True, fill=BOTH)

scrollbar.config(command=lbm.yview)

# frame within the other frame
fr2_bt = Frame(fr_lbm_sbm)
fr2_bt.pack(side=BOTTOM, fill=X)

bt1 = Button(fr2_bt, text="Differentiation methods", font=('Helvetica',14), command=diffMethodsList)
bt1.pack(side=LEFT, fill=Y)
bt2 = Button(fr2_bt, text="Integration methods", font=('Helvetica',14), command=integMethodsList)
bt2.pack(side=RIGHT, fill=Y)


# Middle frame for graphs
fr_plot = Frame(app)
fr_plot.grid(row=0, column=1, sticky=N+S) 

figure1 = plt.Figure(figsize=(5,4), dpi=80)
ax1 = figure1.add_subplot()
line1 = FigureCanvasTkAgg(figure1, fr_plot)
line1.get_tk_widget().pack(side=TOP, fill=BOTH)
df1 = df.iloc[:,1]
df1.plot(kind='line', legend=True, ax=ax1, color='r', marker='o', fontsize=10)
ax1.set_title('Initial data')

bt3 = Button(fr_plot, text='Run', font=('Helvetica', 14), command=lambda: runApp(lbm.curselection(), listNum))
bt3.pack()

figure2 = plt.Figure(figsize=(5,4), dpi=80)
ax2 = figure2.add_subplot()
line2 = FigureCanvasTkAgg(figure2, fr_plot)
line2.get_tk_widget().pack(side=BOTTOM, fill=X)
ax2.set_title('Processed data')

#lbl3 = Label(fr_plot, text='Plot 2. Processed data.', fg='black', font=('Helvetica', 12, 'italic'))
#lbl3.pack(side=BOTTOM)



app.mainloop()

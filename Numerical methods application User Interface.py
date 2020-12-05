# Numerical methods application User Interface

from tkinter import *
from pandas import *
from numpy import arange
from math import sin, cos, pi
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Data for plot
df = DataFrame({'A': range(10),
                'B': [sin(i) for i in range(10)] #[1, 2,1,10,5,3,3,4,5,6]#
                }, index=range(10))   

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
    lbm.delete(0, END)
    lbm.insert(END, "Integration 1")
    lbm.insert(END, "Integration 2")
    lbm.insert(END, "Integration 3")
    lbm.insert(END, "Integration 4")

def interpMethodsList():
    global listNum
    listNum = 3
    lbm.delete(0, END)
    lbm.insert(END, "Interpolation: Linear")
    lbm.insert(END, "Interpolation: Cosine")
    lbm.insert(END, 'Interpolation: Cubic')
    lbm.insert(END, 'Interpolation: Hermite')

def oneDiff():
    global df
    y_dot = [0] * (len(df)-1)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(0, len(x)-1, 1):
        y_dot[i] = (y[i+1] - y[i]) / h 
    y_dot = DataFrame({'A': range(len(y_dot)),
                'B': y_dot
                }, index=range(len(y_dot)))  
    return y_dot

def twoDiff():
    global df
    y_dot = [0] * (len(df)-1)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(1, len(x)-1, 1):
        y_dot[i] = (y[i+1] - y[i-1]) /(2*h)
    y_dot = DataFrame({'A': range(len(y_dot)),
                'B': y_dot
                }, index=range(len(y_dot)))  
    return y_dot

def threeDiff():
    global df
    y_dot = [0] * (len(df)-1)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(1, len(x), 1):
        y_dot[i] = (y[i] - y[i-1]) / h 
    y_dot = DataFrame({'A': range(len(y_dot)),
                'B': y_dot
                }, index=range(len(y_dot)))  
    return y_dot

def fourDiff():
    global df
    y_dot = [0] * (len(df)-1)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(0, len(x)-2, 1):
        y_dot[i] = (-y[i+2] + 4*y[i+1] - 3*y[i]) / (2*h) 
    y_dot = DataFrame({'A': range(len(y_dot)),
                'B': y_dot
                }, index=range(len(y_dot)))  
    return y_dot

def fiveDiff():
    global df
    y_dot = [0] * (len(df)-1)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(2, len(x)-2, 1):
        y_dot[i] = (y[i-2] - y[i+2] + 8*y[i+1] -8*y[i-1]) / (12*h) 
    y_dot = DataFrame({'A': range(len(y_dot)),
                'B': y_dot
                }, index=range(len(y_dot)))  
    return y_dot

def sixDiff():
    global df
    y_dot = [0] * (len(df)-1)
    x = df['A']
    y = df['B']
    h = x[1] - x[0] # step
    for i in range(2, len(x), 1):
        y_dot[i] = (3*y[i] - 4*y[i-1] + y[i-2]) / (2*h) 
    y_dot = DataFrame({'A': range(len(y_dot)),
                'B': y_dot
                }, index=range(len(y_dot)))  
    return y_dot


def oneInterp():
    # Linear interpolation
    global df
    step = 10
    x = df['A']
    y = df['B']
    y_int = [0] * (len(df)-1) * step
    c = 0
    for i in range(0, len(x)-1, 1):
        for h in range(step):
            mu = (x[i]+h/step)
            y_int[c] = (y[i]*(x[i+1]-mu) + y[i+1]*(mu-x[i])) / (x[i+1]-x[i])
            #print(f'c={c} i={i} y_int={y_int[c]} len={len(y_int)}')
            c += 1
    y_int = DataFrame({'A': [i/step for i in range(len(y_int))] ,
                'B': y_int
                })#, index=range(len(y_int)))
    return y_int

def twoInterp():
    # Cosine Interpolation
    global df
    step = 10
    x = df['A']
    y = df['B']
    y_int = [0] * (len(df)-1) * step
    c = 0
    for i in range(0, len(x)-1, 1):
        for h in range(step):
            x_now = (h/step)#+x[i]
            mu2 = (1-cos(x_now*pi))/2
            y_int[c] = y[i]+(y[i+1]-y[i])*mu2
            c += 1               
    y_int = DataFrame({'A': [i/step for i in range(len(y_int))] ,
                'B': y_int
                })#, index=range(len(y_int)))
    return y_int

def threeInterp():
    # Cubic Interpolation
    global df
    step = 10
    x = df['A']
    y = df['B']
    y_int = [0] * (len(df)-3) * step
    k = 0
    for i in range(0, len(x)-3, 1):
        c = y[i+2]-y[i]
        d = y[i+1]
        a = y[i+3]-y[i+2]-y[i]+y[i+1] 
        for h in range(step):
            b = y[i]-y[i+1]-a
            y_int[k] = a*(h/step)**3 + b*(h/step)**2 + c*(h/step) + d
            k += 1               
    y_int = DataFrame({'A': [i/step for i in range(len(y_int))] ,
                'B': y_int
                })#, index=range(len(y_int)))
    return y_int

def fourInterp():
    #Tension: 1 is high, 0 normal, -1 is low
    #Bias: 0 is even, positive is towards first segment, negative towards the other
    tension = 0
    bias = 0
    global df
    step = 10
    x = df['A']
    y = df['B']
    y_int = [0] * (len(df)-3) * step
    c = 0
    for i in range(0, len(x)-3, 1):
        for h in range(step):
            mu =  (h/step)
            mu2 = mu*mu
            mu3 = mu2*mu
            m0  = (y[i+1]-y[i])*(1+bias)*(1-tension)/2
            m0 += (y[i+2]-y[i+1])*(1-bias)*(1-tension)/2
            m1  = (y[i+2]-y[i+1])*(1+bias)*(1-tension)/2
            m1 += (y[i+3]-y[i+2])*(1-bias)*(1-tension)/2
            a0 =  2*mu3 - 3*mu2 + 1
            a1 =    mu3 - 2*mu2 + mu
            a2 =    mu3 -   mu2
            a3 = -2*mu3 + 3*mu2
            y_int[c] = a0*y[i+1]+a1*m0+a2*m1+a3*y[i+2]
            c += 1               
    y_int = DataFrame({'A': [i/step for i in range(len(y_int))] ,
                'B': y_int
                })#, index=range(len(y_int)))
    return y_int

def runApp(method, listNum):
    # Process the data
    global isrunAppagain, figure2, ax2, df
    name = ''
    df2 = df.copy()
    if method == 0:
        return
    if method == (0,) and listNum == 1:
        df2 = oneDiff()
        name = 'First derivative: Forward'
    if method == (1,) and listNum == 1:
        df2 = twoDiff()
        name = 'First derivative: Backward'
    if method == (2,) and listNum == 1:
        df2 = threeDiff()
        name = 'First derivative: Central'
    if method == (3,) and listNum == 1:
        df2 = fourDiff()
        name = 'First derivative: Forward 3 point' 
    if method == (4,) and listNum == 1:
        df2 = fiveDiff()
        name = 'First derivative: Central 3 point'   
    if method == (5,) and listNum == 1:
        df2 = sixDiff()
        name = 'First derivative: Backward 3 point'        

    if method == (0,) and listNum == 2:
        df2 = oneInteg()
        name = 'Integration: mid-point Orthogonal'
    if method == (1,) and listNum == 2:
        df2 = twoInteg()
        name = 'Integration: Trapezoid'
    if method == (2,) and listNum == 2:
        df2 = threeInteg()
        name = 'Integration: Simpsons'
    if method == (3,) and listNum == 2:
        df2 = fourInteg()
        name = 'Integration: ' 
    if method == (4,) and listNum == 2:
        df2 = fiveInteg()
        name = 'Integration: '   
    if method == (5,) and listNum == 2:
        df2 = sixInteg()
        name = 'Integration: '  

    if method == (0,) and listNum == 3:
        df2 = oneInterp()
        print(df2)
        name = 'Interpolation: Linear'
    if method == (1,) and listNum == 3:
        df2 = twoInterp()
        name = 'Interpolation: Cosine'
    if method == (2,) and listNum == 3:
        df2 = threeInterp()
        name = 'Integration: Cubic'
    if method == (3,) and listNum == 3:
        df2 = fourInterp()
        name = 'Integration: ' 
    if method == (4,) and listNum == 3:
        df2 = fiveInterp()
        name = 'Integration: '   
    if method == (5,) and listNum == 3:
        df2 = sixInterp()
        name = 'Integration: '  

    if isrunAppagain==False:
        isrunAppagain = True
        df2 = df.loc[0:,'B']
        df2.plot(kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
        figure2.canvas.draw_idle()
    else:
        ax2.cla()
        df2 = df2.loc[0:,'B']
        df2.plot( kind='line', legend=True, ax=ax2, color='r', marker='o', fontsize=10)
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
bt1.pack(side=LEFT)
bt2 = Button(fr2_bt, text="Integration methods", font=('Helvetica',14), command=integMethodsList)
bt2.pack(side=LEFT)
bt3 = Button(fr2_bt, text='Interpolation methods', font=('Helvetica', 14), command=interpMethodsList)
bt3.pack(side=RIGHT)
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

bt4 = Button(fr_plot, text='Run', font=('Helvetica', 14), command=lambda: runApp(lbm.curselection(), listNum))
bt4.pack()

figure2 = plt.Figure(figsize=(5,4), dpi=80)
ax2 = figure2.add_subplot()
line2 = FigureCanvasTkAgg(figure2, fr_plot)
line2.get_tk_widget().pack(side=BOTTOM, fill=X)
ax2.set_title('Processed data')

#lbl3 = Label(fr_plot, text='Plot 2. Processed data.', fg='black', font=('Helvetica', 12, 'italic'))
#lbl3.pack(side=BOTTOM)



app.mainloop()

# Statistical & Numerical Methods With A User Interface
A python application with graphical user interface (GUI) for the calculation and presentation of statistical and numerical methods.

### Actual implementation
The user interface is created using the tkinter library, the plots that apear are created using the matplotlib and to be specific the FigureCanvasTkAgg function to draw the plot onto a canvas.
Finally, the numerical methods are coded using pandas for the use of dataframes and the math library for basic trigonometric functions: sin, cos, and the number pi.
Each method displayed has a corresponding function body that has access to the data displayed by the upper graph and then returns the transformed data that are then used to update the lower graph.
The buttons run and reload performe two basic operations, running the selected numerical method from the Methods list and showing the results on the bottom graph, and replacing the data that feed into the top graph with the data of the bottom graph, respectively.

### Features list
- The aim is to be able to drag and drop a .csv or .txt file directly onto the top graph and use that data. As of now, the dataset at hand is always the same, a simple sin wave of 1 and a half period length. (not yet)
- Allow the user to choose between different methods. (added differentiation and interpolation methods)
- Display the raw data on the top graph and the results on the bottom. (done)
- The details tab is used for showing information regardnig the method choosen and the relevant results. (not yet)

#### Libraries used:
- [tkinter]
- [pandas]
- [matplotlib]
- [math]

### Installation
To run the code you need Python3, and the libraries above installed on your computer.
To install a libray for python open the command prompt and follow the example bellow.

```sh
$ pip install pandas
```

To clone the repository, open the command prompt at the directory of choise and type:
```sh
$  git clone --recursive https://github.com/JustMakeItStudio/Statistical-and-Numerical-Methods.git
```


### Screenshots
![image](https://user-images.githubusercontent.com/71210416/114682311-a2702800-9d17-11eb-9c0c-9bbce5fbbaf4.png)
Starting screen.

![image](https://user-images.githubusercontent.com/71210416/114682498-d1869980-9d17-11eb-8ca7-421067c43fbe.png)
After excecuting the first derivative using the 3 point central differentiation method and pressing the reload button.

![image](https://user-images.githubusercontent.com/71210416/114689230-27f6d680-9d1e-11eb-9e39-de93cd8a0603.png)
After running the cubic interpolation method.

**Use this as you like.**

   [tkinter]: <https://docs.python.org/3/library/tk.html>
   [pandas]: <https://pandas.pydata.org/docs/index.html>
   [matplotlib]: <https://matplotlib.org/stable/contents.html>
   [math]: <https://docs.python.org/3/library/math.html>

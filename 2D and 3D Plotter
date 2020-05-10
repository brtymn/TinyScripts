from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
import math 


##########                                                     ##########
###############                                           ###############
####################    THIS PART IS FOR 3D PLOTS    ####################
###############                                           ###############
##########                                                     ##########   
## Define the function that will be used here. The function defined here will be used all throughout the plots.
def f(x, y):
    return np.sin(np.sqrt(x ** 2 + y ** 2)) ## Return the defined function.

## This plots the predefined function as points and plots.
def ThreeDimensionalPointsandLines():
    ax = plt.axes(projection='3d')

# Data for a three-dimensional line
    zline = np.linspace(0, 15, 1000)
    xline = np.sin(zline)
    yline = np.cos(zline)
    ax.plot3D(xline, yline, zline, 'gray')

# Data for three-dimensional scattered points
    zdata = 15 * np.random.random(100)
    xdata = np.sin(zdata) + 0.1 * np.random.randn(100)
    ydata = np.cos(zdata) + 0.1 * np.random.randn(100)
    ax.scatter3D(xdata, ydata, zdata, c=zdata, cmap='Greens');
    plt.show()

def ThreeDimensionalContour():
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    ax = plt.axes(projection='3d')
    ax.contour3D(X, Y, Z, 50, cmap='binary')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_zlabel('z');
    
    ax.view_init(60, 35) ## This adjusts the viewing angles, it is not mandatory but cool to use.

    plt.show()

def ThreeDimensionalWireframe():
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)

    ax = plt.axes(projection='3d')
    ax.plot_wireframe(X, Y, Z, color='black')
    ax.set_title('wireframe');

    plt.show()

def ThreeDimensionalSurface():
    x = np.linspace(-6, 6, 30)
    y = np.linspace(-6, 6, 30)

    X, Y = np.meshgrid(x, y)
    Z = f(X, Y)
    
    ax = plt.axes(projection='3d')
    ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
                cmap='viridis', edgecolor='none')
    ax.set_title('surface');

    plt.show()

def ThreeDimensionalScatter():
    theta = 2 * np.pi * np.random.random(1000)
    r = 6 * np.random.random(1000)
    x = np.ravel(r * np.sin(theta))
    y = np.ravel(r * np.cos(theta))
    z = f(x, y)

    ax = plt.axes(projection='3d')
    ax.scatter(x, y, z, c=z, cmap='viridis', linewidth=0.5);

    plt.show()

## Once the 3D function is defined at the beginning of this script, simply un-comment the 3D plot type you want and run the script.
def main3D():
    user_choice_3D = ent_3D_choice.get()

    if (user_choice_3D == "PL"):
        ThreeDimensionalPointsandLines()
    elif (user_choice_3D == "C"):
    	ThreeDimensionalContour()
    elif (user_choice_3D == "W"):
    	ThreeDimensionalWireframe()
    elif (user_choice_3D == "S"):
    	ThreeDimensionalSurface()
    elif (user_choice_3D == "SC"):
    	ThreeDimensionalScatter()


##########                                                     ##########
###############                                           ###############
####################    THIS PART IS FOR 2D PLOTS    ####################
###############                                           ###############
##########                                                     ##########  


def TwoDimensionalLine():
    fig = plt.figure()
    ax = plt.axes()

    x = np.linspace(0, 10, 1000)
    ax.plot(x, np.sin(x)); ## Input the actual funtion here.
    plt.show()

def TwoDimensionalScatter():
    x = np.linspace(0, 10, 30)
    y = np.sin(x)

    plt.plot(x, y, 'o', color='black');
    plt.show()

def main2D():
    user_choice_2D = ent_2D_choice.get()

    if (user_choice_2D == "L"):
        TwoDimensionalLine()
    elif (user_choice_2D == "S"):
    	TwoDimensionalScatter()



def ChooseDimension():
    dimension_choice = ent_dimension.get()

    if (dimension_choice == "2D"):
        main2D()
    elif (dimension_choice == "3D"):
        main3D()
    else :
        print("??????????????")


window = tk.Tk()
window.title("PLOTTER")
first_entry = tk.Frame(master = window)

ent_dimension = tk.Entry(master = first_entry, width=10)
ent_dimension.grid(row=0, column=0, sticky="e")

    
btn_choose_dimension = tk.Button(
                       master=window,
                       text="Enter The Coice. 2D or 3D",
                        command = ChooseDimension
                         )

first_entry.grid(row=0, column=0, padx=10)
btn_choose_dimension.grid(row=0, column=1, pady=10)



second_entry = tk.Frame(master = window)

ent_3D_choice = tk.Entry(master = second_entry, width=10)
ent_3D_choice.grid(row = 1, column=0, sticky="e")

    
btn_3D_choice = tk.Button(
                       master=window,
                       text="Plot 3D Right Here. PL for points and lines plot, C for contour plot, W for wireframe plot, S for surface plot and SC for scatter plot.",
                        command = main3D
                         )

second_entry.grid(row=1, column=0, padx=10)
btn_3D_choice.grid(row=1, column=1, pady=10)



third_entry = tk.Frame(master = window)

ent_2D_choice = tk.Entry(master = third_entry, width=10)
ent_2D_choice.grid(row = 1, column=0, sticky="e")

    
btn_2D_choice = tk.Button(
                       master=window,
                       text="Plot 2D Right Here. L for line plot and S for scatter plot.",
                        command = main2D
                         )

third_entry.grid(row=2, column=0, padx=10)
btn_2D_choice.grid(row=2, column=1, pady=10)

window.mainloop()

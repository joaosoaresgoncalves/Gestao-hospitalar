# -*- coding: utf-8 -*-
"""
Created on Thu Jun  9 14:10:56 2022

@author: marti
"""

import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
import matplotlib
from Classes.equipamento import Equipamento

def Graph():

    Y = Equipamento.para_o_graf()
    print(Y)
    X = ["doações", "tecnológico", "clínico", "cirurgia"]
    
    
    # Plot the data using bar() method
    plt.bar(X, Y, color='g')
    plt.title("Quantidades dos diferentes tipos")
    plt.xlabel("Nome do equipamento")
    plt.ylabel("Quantidade total")
    
    # This defines the Python GUI backend to use for matplotlib
    matplotlib.use('TkAgg')
    
    # Initialize an instance of Tk
    #root = tk.Tk()
    
    # # Initialize matplotlib figure for graphing purposes
    # fig = plt.figure(1)
    
    # # Special type of "canvas" to allow for matplotlib graphing
    # canvas = FigureCanvasTkAgg(fig, master=root)
    # plot_widget = canvas.get_tk_widget()
    
    
    # #Add the plot to the tkinter widget
    # plot_widget.grid(row=0, column=0)
    
    
   # root.mainloop()
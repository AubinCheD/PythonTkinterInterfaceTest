#from tkinter import *
#from tkinter.messagebox import *

import tkinter as tk
import tkinter.messagebox as tk_mb
import tkinter.ttk as tk_ttk

class Window(tk.Tk):  #faire hériter de Tk ????
    #docstring
    """(docstring) Classe Fenetre"""
    
    #attributs de classe (constantes)
    
    
    
    #dans init, mettre les attributs d'instance
    def __init__(self):
        tk.Tk.__init__(self)	# On dérive de Tk, on reprend sa méthode d'instanciation
        self.populationSize = 0
        self.evalutionMethod = ""
        self.mutationMethod = ""
        self.crossoverMethod = ""
        self.selectionMethod = ""
        
        self.endAfterGen = False
        self.endAfterTime = False
        self.endWhenExtremumReached = False
        
        self.enableMutation = True
        self.enableCrossover = True
        
        self.mutationRate = 0.000
        self.crossoverRate = 0.000
        
        self.menuBar = tk.Menu(self)
        self.mainPanedWindow = tk.PanedWindow(self, orient=tk.HORIZONTAL)
        
        
        #self.panedWindowGeneticMethods(self.mainPanedWindow, orient=VERTICAL)
        self.initMenuBar()
        
        self.config(menu = self.menuBar)

    def alert(self):
        tk_mb.showinfo("alert", "ok")

    def initMenuBar(self):
            
        menuFile = tk.Menu(self.menuBar, tearoff=0)
        menuFile.add_command(label="Quit", command=self.destroy)
        self.menuBar.add_cascade(label="File", menu=menuFile)
        
        menuEdit = tk.Menu(self.menuBar, tearoff=0)
        menuEdit.add_command(label="Copy", command=self.alert)
        menuEdit.add_command(label="Paste", command=self.alert)
        menuEdit.add_command(label="Cut", command=self.alert)
        self.menuBar.add_cascade(label="Edit", menu=menuEdit)
        
        menuHelp = tk.Menu(self.menuBar, tearoff=0)
        menuHelp.add_command(label="About", command=self.alert)
        self.menuBar.add_cascade(label="Help", menu=menuHelp)


    #def initPanedWindows(self):
        
    def initPanedWindowGeneticMethods(self):
        
        panedWindowGeneticMethods = tk.PanedWindow(self.mainPanedWindow, orient=tk.VERTICAL)
        
        
        
        
        comboBox1 = tk_ttk.Combobox(panedWindowGeneticMethods, state=tk_ttk.READONLY, )
        
        #panedWindowGeneticMethods
        
        self.mainPanedWindow.add(panedWindowGeneticMethods)
       


fenetre = Window()
fenetre.mainloop()

del fenetre
#fenetre.mainloop()
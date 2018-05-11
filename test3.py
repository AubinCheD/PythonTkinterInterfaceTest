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
        self.evaluationMethod = tk.StringVar()
        #self.valueSelectedEvalMethod	= StringVar()
        self.mutationMethod = tk.StringVar()
        self.crossoverMethod = tk.StringVar()
        self.selectionMethod = tk.StringVar()
        
        self.endAfterGen4 = tk.IntVar()
        self.endAfterTime4 = tk.IntVar()
        self.endAfterValue4 = tk.IntVar()
        self.endAfterGen3 = tk.BooleanVar()
        self.endAfterTime3 = tk.BooleanVar()
        self.endAfterValue3 = tk.BooleanVar()
        self.endAfterGen2 = 1
        self.endAfterTime2 = 2         ################## WWWWWWWWWWTTTTTTTTTTFFFFFFFF
        self.endAfterValue2 = 3
        self.endAfterGen = False
        self.endAfterTime = False
        self.endAfterValue = False
        
        self.endAfterGen_value = tk.IntVar()
        self.endAfterTime_value = tk.IntVar()
        self.endAfterValue_value = tk.IntVar()
        
        
        self.enableMutation = True
        self.enableCrossover = True
        
        self.mutationRate = 0.000
        self.crossoverRate = 0.000
        
        self.menuBar = tk.Menu(self)
        self.mainPanedWindow = tk.PanedWindow(self, orient=tk.VERTICAL)
        
        
        #self.panedWindowGeneticMethods(self.mainPanedWindow, orient=VERTICAL)
        self.initMenuBar()
        self.config(menu = self.menuBar)

        #self.initPanedWindowGeneticMethods()
        self.initLabelframeGeneticMethods()
        self.initLabelframeEndConditions()
        
        self.mainPanedWindow.pack()
        
        #comboBox1 = self.initCombobox(tk.StringVar(), ('fitnessFun1', 'fitnessFun2', 'fitnessFun3'), 'readonly')
        #comboBox1.grid()
        
        

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
        
        panedWindowEvaluation = tk.PanedWindow(panedWindowGeneticMethods, orient=tk.HORIZONTAL)
        
        frameMutation = tk_ttk.Labelframe(panedWindowGeneticMethods, text='Pane1', width=100, height=100)
        
        labelTest= tk.Label(panedWindowGeneticMethods, text = self.evalutionMethod)
        
        labelEvaluation = tk.Label(panedWindowEvaluation, text = "Fitness Function")
        labelMutation = tk.Label(frameMutation, text = "Mutation Method")
        labelCrossover = tk.Label(panedWindowGeneticMethods, text = "Crossover Method")
        labelSelection = tk.Label(panedWindowGeneticMethods, text = "Selection Method")

        comboBoxEvaluation = self.initCombobox(panedWindowEvaluation, self.evalutionMethod, ('fitnessFun1', 'fitnessFun2', 'fitnessFun3'), 'readonly')
        comboBoxMutation = self.initCombobox(frameMutation, tk.StringVar(), ('mutFun1', 'mutFun2', 'mutFun3'), 'readonly')
        comboBoxCrossover = self.initCombobox(panedWindowGeneticMethods, tk.StringVar(), ('CrossFun1', 'CrossoverFun2', 'CrossoverFun3'), 'readonly')
        comboBoxSelection = self.initCombobox(panedWindowGeneticMethods, tk.StringVar(), ('selecFun1', 'selecFun2', 'selecFun3'), 'readonly')
        

        comboBoxEvaluation.grid()
        comboBoxMutation.grid()
        comboBoxCrossover.grid()
        comboBoxSelection.grid()
        
        panedWindowEvaluation.add(labelEvaluation)
        panedWindowEvaluation.add(comboBoxEvaluation)
        
        panedWindowGeneticMethods.add(panedWindowEvaluation)
        
        #frameMutation.pack()
        #frameMutation.add(labelMutation)
        #frameMutation.add(comboBoxMutation)
        
        
        #panedWindowGeneticMethods.add(labelMutation)
        #panedWindowGeneticMethods.add(comboBoxMutation)
        
        panedWindowGeneticMethods.add(labelCrossover)
        panedWindowGeneticMethods.add(comboBoxCrossover)
        panedWindowGeneticMethods.add(labelSelection)
        panedWindowGeneticMethods.add(comboBoxSelection)
        
        panedWindowGeneticMethods.pack()
        
        self.mainPanedWindow.add(panedWindowGeneticMethods)
        
        
        
        
    def initLabelframeGeneticMethods(self):
        
        labelframeGeneticMethods = tk_ttk.Labelframe(self.mainPanedWindow, text='Genetic Algorithm', width=500, height=400)
        
        panedWindowPopulation = tk.PanedWindow(labelframeGeneticMethods, orient=tk.HORIZONTAL)
        panedWindowEvaluation = tk.PanedWindow(labelframeGeneticMethods, orient=tk.HORIZONTAL)
        panedWindowMutation = tk.PanedWindow(labelframeGeneticMethods, orient=tk.HORIZONTAL)
        panedWindowCrossover = tk.PanedWindow(labelframeGeneticMethods, orient=tk.HORIZONTAL)
        panedWindowSelection = tk.PanedWindow(labelframeGeneticMethods, orient=tk.HORIZONTAL)
        
        labelPopulation = tk.Label(panedWindowPopulation, text = "Initial Population Size : ")
        labelEvaluation = tk.Label(panedWindowEvaluation, text = "Fitness Function : ")
        labelMutation = tk.Label(panedWindowMutation, text = "Mutation Method  : ")
        labelCrossover = tk.Label(panedWindowCrossover, text = "Crossover Method : ")
        labelSelection = tk.Label(panedWindowSelection, text = "Selection Method : ")

        self.labelTest= tk.Label(labelframeGeneticMethods, text = "selected : ")
        labelTest2= tk.Label(labelframeGeneticMethods, text = "selected : ")

        spinboxPopulation = tk.Spinbox(panedWindowPopulation, from_ = 0, to = 5000)    #changer les tk.StingVar(); ajouter une variable
        
        comboBoxEvaluation = self.initCombobox(panedWindowEvaluation, self.evaluationMethod, ('fitnessFun1', 'fitnessFun2', 'fitnessFun3'), 'readonly')
        comboBoxMutation = self.initCombobox(panedWindowMutation, tk.StringVar(), ('mutFun1', 'mutFun2', 'mutFun3'), 'readonly')
        comboBoxCrossover = self.initCombobox(panedWindowCrossover, tk.StringVar(), ('CrossFun1', 'CrossoverFun2', 'CrossoverFun3'), 'readonly')
        comboBoxSelection = self.initCombobox(panedWindowSelection, tk.StringVar(), ('selecFun1', 'selecFun2', 'selecFun3'), 'readonly')
        
        test = ""
        
        def value():
            return self.evaluationMethod
            
        def on_selection(event):  # Just to test
            labelTest.configure(text="selected : " + event)
            
        def on_selection2(event=None):  # Just to test
            labelTest.configure(text="selected : " + value())
        
        def on_selection3(label, test, event=None):  # Just to test
            print ("1 ; " + test + " | " + label.cget("text"))
            label.configure(text="selected : " + self.evaluationMethod.get())
            test = test + "bla"
            print("2 ; " + test + " | " + label.cget("text"))
            
        def on_selection4(event=None):  # Just to test
            self.labelTest.configure(text="selected : " + self.evaluationMethod.get())
        
        comboBoxEvaluation.bind('<<ComboboxSelected>>', on_selection4)  #works
        comboBoxEvaluation.bind('<<ComboboxSelected>>', on_selection3(self.labelTest, test)) # doesn't work

        #comboBoxEvaluation.grid()
        #comboBoxMutation.grid()
        #comboBoxCrossover.grid()
        #comboBoxSelection.grid()
        
        panedWindowPopulation.add(labelPopulation)
        panedWindowPopulation.add(spinboxPopulation)
        
        panedWindowEvaluation.add(labelEvaluation)
        panedWindowEvaluation.add(comboBoxEvaluation)
        
        panedWindowMutation.add(labelMutation)
        panedWindowMutation.add(comboBoxMutation)
        
        panedWindowCrossover.add(labelCrossover)
        panedWindowCrossover.add(comboBoxCrossover)
        
        panedWindowSelection.add(labelSelection)
        panedWindowSelection.add(comboBoxSelection)
    
        
        #panedWindowGeneticMethods.add(panedWindowEvaluation)
        
        #frameMutation.pack()
        #frameMutation.add(labelMutation)
        #frameMutation.add(comboBoxMutation)
        
        
        #panedWindowGeneticMethods.add(labelMutation)
        #panedWindowGeneticMethods.add(comboBoxMutation)
        
        #panedWindowGeneticMethods.add(labelCrossover)
        #panedWindowGeneticMethods.add(comboBoxCrossover)
        #panedWindowGeneticMethods.add(labelSelection)
        #panedWindowGeneticMethods.add(comboBoxSelection)
        
        panedWindowPopulation.grid()
        panedWindowEvaluation.grid()
        panedWindowMutation.grid()
        panedWindowCrossover.grid()
        panedWindowSelection.grid()
        self.labelTest.grid()
        labelTest2.grid()
        
        labelframeGeneticMethods.pack()
        
        self.mainPanedWindow.add(labelframeGeneticMethods)
        
    
    
    def initLabelframeEndConditions(self):
        labelframeEndConditions = tk_ttk.Labelframe(self.mainPanedWindow, text='End Conditions', width=500, height=400)
        
        panedWindowEndAfterGen = tk.PanedWindow(labelframeEndConditions, orient=tk.HORIZONTAL)
        panedWindowEndAfterTime = tk.PanedWindow(labelframeEndConditions, orient=tk.HORIZONTAL)
        panedWindowEndAfterValue = tk.PanedWindow(labelframeEndConditions, orient=tk.HORIZONTAL)
        
        
        checkButtonEndAfterGen = tk_ttk.Checkbutton(panedWindowEndAfterGen, text=" Ends after a number of generation ?", variable = self.endAfterGen4)               #offvalue=False, onvalue=True
        checkButtonEndAfterTime = tk_ttk.Checkbutton(panedWindowEndAfterTime, text=" Ends after time ?", variable = self.endAfterTime4)
        checkButtonEndAfterValue = tk_ttk.Checkbutton(panedWindowEndAfterValue, text=" Ends after value is reached ?", variable = self.endAfterValue4)
    
        #checkButtonEndAfterGenerations.pack() #don't need it here
        
        
        
        spinboxEndAfterGen = tk.Spinbox(panedWindowEndAfterGen, from_ = 0, to = 5000, textvariable = self.endAfterGen_value)
        spinboxEndAfterTime = tk.Spinbox(panedWindowEndAfterTime, from_ = 0, to = 5000, textvariable = self.endAfterTime_value)
        spinboxEndAfterValue = tk.Spinbox(panedWindowEndAfterValue, from_ = 0, to = 5000, textvariable = self.endAfterValue_value)
        
        
        panedWindowEndAfterGen.add(checkButtonEndAfterGen)
        panedWindowEndAfterGen.add(spinboxEndAfterGen)
        
        panedWindowEndAfterTime.add(checkButtonEndAfterTime)
        panedWindowEndAfterTime.add(spinboxEndAfterTime)
        
        panedWindowEndAfterValue.add(checkButtonEndAfterValue)
        panedWindowEndAfterValue.add(spinboxEndAfterValue)
        
        panedWindowEndAfterGen.grid()
        panedWindowEndAfterTime.grid()
        panedWindowEndAfterValue.grid()
        
        labelframeEndConditions.pack()
        
        self.mainPanedWindow.add(labelframeEndConditions)
        
    

    def initCombobox(self, root, varType, listOfAttributes, visibilityState):
        
        return tk_ttk.Combobox(root, textvariable = varType, values = listOfAttributes, state = visibilityState)
        


fenetre = Window()
fenetre.mainloop()

del fenetre
#fenetre.mainloop()
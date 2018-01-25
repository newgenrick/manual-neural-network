# -*- coding: utf-8 -*-
import numpy as np

'''the following lines contains definition of basic operations class that will
    be used by the other basic operations'''
class operations():
    def __init__(self,input_nodes=[]):
        self.input_nodes = input_nodes
        self.output_nodes = []
        for input_node in input_nodes:
            self.output_nodes.append(self)
        _default_graph.operations.append(self)
    def calculate():
        pass
    

'''the following lines contain basic operations such as add multiply
   and matmultiply each of these operations inherit from operations class'''
class add(operations):
    def __init__(self,x,y):
        super().__init__([x,y])
    
    def calculate(self,x_var,y_var):
        self.inputs = [x_var,y_var]
        return x_var + y_var

class multiply(operations):
    def __init__(self,x,y):
        super().__init__([x,y])
    
    def calculate(self,x_var,y_var):
        self.inputs = [x_var,y_var]
        return x_var * y_var

class matmul(operations):
    def __init__(self,x,y):
        super().__init__([x,y])
    
    def calculate(self,x_var,y_var):
        self.inputs = [x_var,y_var]
        return x_var.dot(y_var)

'''the following lines of code contains different types of nodes that are 
    going to be there in our neural net such as placeholder and variables  '''
class Placeholder():
    def __init__(self):
        self.output_nodes = []
        _default_graph.placeholders.append(self)

class Variables():
    def __init__(self,initial = None):
        self.output_nodes = []
        self.value = initial
        _default_graph.variables.append(self)

'''the following lines contains the graph class definition which handles or 
   connects all the components of all the nodes'''
class Graph():
    def __init__(self):
        self.variables = []
        self.placeholders = []
        self.operations = []

    def set_defaut_graph(self):
        global _default_graph
        _default_graph = self



        
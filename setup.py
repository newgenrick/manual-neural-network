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

class Variable():
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
'''traverse postorder is a very interesting function ,in which we get an 
    operation node as an argument and we trace it backwords to cal all the 
    values(inputs) to that node in the correct order'''
def traverse_postorder(operation):
    nodes_postorder = []
    def recurse(node):
        if isinstance(node, operations):
            for input_node in node.input_nodes:
                recurse(input_node)
        nodes_postorder.append(node)
    recurse(operation)
    return nodes_postorder
        
    
'''A session runs the graph data transfer and computation when triggered on 
    a operational node'''
class Session():
    def run(self,operation,feed_dict = {}):
        nodes_postorder = traverse_postorder(operation)
        print(nodes_postorder)
        
        for node in nodes_postorder:
            if type(node) == Placeholder:
                node.output = feed_dict[node]
            elif type(node) == Variable:
                node.output = node.value
            else:
                node.inputs = [input_node.output for input_node in node.input_nodes]
                node.output = node.calculate(*node.inputs)
            if type(node.output) == list:
                node.output = np.array(node.output)
        return operation.output
                
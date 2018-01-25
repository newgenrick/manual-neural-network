# -*- coding: utf-8 -*-
import numpy as np

class operations():
    def __init__(self,input_nodes=[]):
        self.input_nodes = input_nodes
        self.output_nodes = []
    def calculate():
        pass


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
        

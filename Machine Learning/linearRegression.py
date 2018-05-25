import numpy as np
import matplotlib.pyplot as plt
import pandas as pd 

def error(b,m,x,y):
    finalError=0
    for i in range(len(x)):
        finalError +=(y [i]-(m*x[i]+b))**2
    return finalError/len(x)

def gradient_descent(init_m,init_b,x,y):
    learning_rate=0.001
    num_iterations=1000
    b=init_b
    m=init_m
    for i in range(num_iterations):
        b,m=step(init_b,init_m,x,y)
        init_b=init_b-(learning_rate*b)
        init_m=init_m-(learning_rate*m)
    return [init_b, init_m]

def step(b,m,x,y):
    m_gradient=0
    b_gradient=0
    for i in range(len(x)):
        b_gradient += -(2/len(x))*(y[i]-((m*x[i])+b))
        m_gradient += -x[i]*(2/len(x))*(y[i]-((m*x[i])+b))
        
    return [b_gradient,m_gradient]
 
def linearRegression():
#collecting the data
    dataset = pd.read_csv('lactic.csv')
    X = dataset.iloc[:,1].values
    Y = dataset.iloc[:,-1].values
    print(X)
    
    
    in_b=0
    in_m=0
    print('Starting at b={0},m={1},error = {2} '.format(in_b,in_m,error(in_b,in_m,X,Y)))
    [b,m]=gradient_descent(in_m,in_b,X,Y)
    print('Finally at b={0},m={1},error = {2} '.format(b,m,error(b,m,X,Y)))
    
    #plotting the graph
    y_vals=[m*x+b for x in range(20)]
    x_vals = range(20)
    
    plt.scatter(X,Y)
    plt.plot(x_vals,y_vals,linewidth=3)
    plt.show()
    
if __name__=='__main__':
    linearRegression()

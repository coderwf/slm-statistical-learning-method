
#产生点集数据

import numpy as np
import matplotlib.pyplot as plt

"""
二维线性可分两类数据
k,b分别为y=kx+b的k和b
x_scale,y_scale为数据的距离线的两个方向的距离值
num为生成的点的数目
"""

def rand_2d_linear_2c(k:np.float64=1,b:np.float64=0,x_scale:np.float64=5,y_scale:np.float64=5,num:int=100) :
    assert num > 0 , "num must > 0"
    left  = list()
    right = list()
    for i in range(num) :
        x = np.random.uniform(-x_scale,x_scale)
        y = k * x + b
        f = np.random.uniform(-y_scale,y_scale)
        if f > 0 :
            left.append([x,y+f])
        else :
            right.append([x,y+f])
    return np.array(left) , np.array(right)

"""
将数据集plot出来
"""

def plot_rand_2d_linear_2c(left:np.array,right:np.array) :
    plt.figure(figsize=(10,10))
    plt.plot(left[:,0],left[:,1],"ro")
    plt.plot(right[:,0], right[:,1],"go")
    plt.grid(True)
    plt.xlabel("X")
    plt.ylabel("Y")
    plt.title("Scatter plot")
    plt.show()


if __name__ == "__main__" :
    l , r = rand_2d_linear_2c(x_scale=2,y_scale=5,num=300)
    print(l)
    plot_rand_2d_linear_2c(l,r)
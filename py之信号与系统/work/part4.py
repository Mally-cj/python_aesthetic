import numpy as np
import matplotlib.pyplot as plt

import deputy
import scipy.signal
from scipy import  integrate
from sympy import DiracDelta
from matplotlib.ticker import  FormatStrFormatter
from matplotlib.pyplot import MultipleLocator
import imageio
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def h(t):
    return (t>=0)*t*(t<=2)

def f0(t):
    return (t>=0)*0.5*(t<=1)

def f(t,t0):
    t=-t+t0
    return (t>=0)*0.5*(t<=1)


def test1():
    x=np.arange(-4,10,0.1)
    y=h(x,3)
    for i in range(len(y)):
        print(x[i],":",y[i])
    plt.plot(x,y,lw=2)
    plt.show()


def func1(t=3):
    image_list=[]
    ge=0.1   #time的时间间隔,不能取1
    time=np.arange(-0.5,3.5,ge)
    tt=0
    x = np.arange(-6, 10, ge)
    data_list=np.zeros(len(time))

    yes=np.zeros(6)
    print(yes)
    for i in range(len(time)):
        # plt.text(0,0,"hello",fontsize=20,color="gray",alpha=0.5)
        plt.title("hello")
        y1=h(x)
        y2=f(x,time[i])
        y_int=np.sum(y1*y2)*ge
        t=np.arange(-5,time[i],ge)

        data_list[i]=y_int
        # print(time[i],":",y_int)
        ax1=plt.subplot(121)
        ax1.plot(x, y1, lw=2)  #函数曲线)
        ax1.plot(x, y2, lw=2)
        ax1.fill(x, y1, 'r', alpha=0.5, label='y1')
        ax1.fill(x, y2, 'b', alpha=0.5, label='y2')
        ax1.legend(loc=("upper left"))
        plt.title("卷积过程")
        ax2=plt.subplot(122)
        plt.title("h(t)*f(t)")
        #画分隔线
        if time[i]>=1.00: plt.axvline(x=1,ls="--", c="dimgray",alpha=0.3)  # 添加垂直直线
        if time[i]>=2.00: plt.axvline(x=2,ls="--", c="dimgray",alpha=0.4)  # 添加垂直直线




        # 画分段函数

        ### 画各个阶段的函数式
        plt.text(-4.7, 0.9, "0<t:y=0", weight="bold", color="b",alpha=0.8)
        if time[i]>0: plt.text(-4.7, 0.8, r"$0\leq t\leq 1:y=\frac{1}{4}t^2$", weight="bold", color="b",alpha=0.8)
        if time[i]>1: plt.text(-4.7, 0.7, r"$1<t\leq2:y=\frac{1}{2}t-\frac{1}{4}$", weight="bold", color="b",alpha=0.8)
        if time[i]>2:
            plt.text(-4.7, 0.6, r"$2<t\leq3:$", weight="bold", color="b",alpha=0.8)
            plt.text(-4.7, 0.5, r"$y=\frac{1}{4}t^2+\frac{1}{2}t+\frac{3}{4}$", weight="bold", color="b",alpha=0.8)
        if time[i]>3:plt.text(-4.7, 0.4, "$3<t:y=0$", weight="bold", color="b",alpha=0.8)

        ###
        x_major_locator = MultipleLocator(1)
        ax = plt.gca()
        # ax为两条坐标轴的实例
        ax.xaxis.set_major_locator(x_major_locator)

        ax2.plot(time,data_list,'b')
        plt.suptitle("卷积演示",fontsize=25)

        plt.xlim(-5,5)
        plt.ylim(0,1)
        # plt.plot(y1,y3)
        # plt.show()
        plt.savefig('tem.png')


        image_list.append((imageio.imread('tem.png')))
        plt.close()
        deputy.read("tem.png")

        image_list.append(imageio.imread('tem.png'))

    imageio.mimsave('卷积.gif', image_list, duration=1)


# func1()


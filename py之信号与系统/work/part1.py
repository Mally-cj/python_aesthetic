import numpy as np
import matplotlib.pyplot as plt
import deputy
from sympy import DiracDelta
plt.rcParams['font.sans-serif']=['SimHei']			#展现图表里的中文字体
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号


def make_dirac():
    # 画dirac
    scope=0.01   #冲激范围
    xie=100
    x=np.arange(-10,10, 0.01,np.float)
    y=np.zeros(x.shape,np.float32)
    for i in range(len(x)):
        if x[i]>scope:break
        if x[i]<-scope:continue

        if x[i]>=0 :
                y[i]=(x[i]-scope)*(-xie)
        elif x[i]<0:
            y[i]=(x[i]+scope)*xie
    plt.text(0.2, 0.6, "(1)", weight="bold", color="b")
    plt.title("画冲激函数",fontdict={"size":"xx-large","color":"b"})
    plt.plot(x, y, lw=2, label=r"$\delta(t)$",c="b")
    plt.legend()
    plt.savefig("dirac.png")
    deputy.read("dirac.png",5)
    plt.show()

def make_step_func():
    qi = -10  # 坐标轴的起始位置
    mo = -qi
    num = 1000  # 样本数量

    x = np.linspace(qi, mo, num)
    y=x>0
    plt.title("画阶跃函数",fontdict={"size":"xx-large","color":"c"})
    plt.plot(x, y, lw=2, label=r"$\varepsilon(t)$",c="c")
    plt.legend()
    plt.savefig("step.png")
    deputy.read("step.png",5)
    plt.show()


def make_rope_func():
    qi = -10  # 坐标轴的起始位置
    mo = -qi
    num = 1000  # 样本数量

    x = np.linspace(qi, mo, num)
    y = (x > 0) * x
    plt.title("斜坡函数", fontdict={"size": "xx-large", "color": "deepskyblue"})
    plt.plot(x, y, lw=2, label="r(t)", c="deepskyblue")
    plt.legend()
    plt.savefig("rope.png")
    deputy.read("rope.png",5)
    plt.show()
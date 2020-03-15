import numpy as np
import matplotlib.pyplot as plt
import imageio
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
    deputy.read("dirac.png",3)
    plt.show()

def make_step_func(spe=1):
    qi = -10  # 坐标轴的起始位置
    mo = -qi
    num = 1000  # 样本数量

    x = np.linspace(qi, mo, num)
    y=x>0
    plt.title("画阶跃函数",fontdict={"size":"xx-large","color":"c"})
    plt.plot(x, y, lw=2, label=r"$\varepsilon(t)$",c="c")
    plt.legend()
    plt.savefig("step.png")
    if spe==1:deputy.read("step.png",3)
    plt.show()


def make_rope_func(spe=1):
    qi = -10  # 坐标轴的起始位置
    mo = -qi
    num = 1000  # 样本数量

    x = np.linspace(qi, mo, num)
    y = (x > 0) * x
    plt.title("斜坡函数", fontdict={"size": "xx-large", "color": "deepskyblue"})
    plt.plot(x, y, lw=2, label="r(t)", c="deepskyblue")
    plt.legend()
    plt.savefig("rope.png")
    if spe==1: deputy.read("rope.png",3)
    plt.show()

def dirac_step():
    # 画dirac
    ge=0.5
    x=np.arange(-10,10,ge)
    image_list=[]
    make_step_func(0)
    for i in range(5):image_list.append(imageio.imread('dirac.png'))

    for i in range(len(x)):
        title="冲激函数"+r"$\Rightarrow$"+"阶跃函数"
        plt.title(title,c="b",fontsize=18)
        plt.text(-9,0.8,r"$\delta(t)=\int_{-∞}^{∞} \varepsilon(t) \, dx$",c="b",fontsize=18,alpha=0.6)
        plt.axhline(y=0,ls="-",color="b",alpha=0.3)  # 添加垂直直线
        if x[i]<0:continue
        plt.xlim(-10,10)
        for d in range (40):
            if x[i]>=ge*d:
                plt.vlines(ge*d,0,1,linestyles='-',colors="b")
            if d*ge>x[i]:break
        plt.plot()
        plt.savefig("dirac_step.png")
        deputy.read("dirac_step.png",-1)
        plt.close()
        image_list.append(imageio.imread('dirac_step.png'))
    for i in range(5):image_list.append(imageio.imread('step.png'))

    imageio.mimsave('dirac_step.gif', image_list, duration=0.5)

def step_rope(spe=1):
    # 画dirac
    ge=0.5
    x=np.arange(-10,10,ge)
    image_list=[]
    make_rope_func(0)
    for i in range(5):image_list.append(imageio.imread('step.png'))

    for i in range(len(x)):
        title="阶跃函数"+r"$\Rightarrow$"+"斜坡函数"
        plt.title(title,c="c",fontsize=20)
        plt.text(-9,5,r"$ r(t)=\int_{-∞}^{∞}\delta(t)\,dx$",c="c",fontsize=18,alpha=0.6)
        plt.axhline(y=0,ls="-",color="c",alpha=0.3)  # 添加垂直直线
        if x[i]<0:continue
        plt.xlim(-10,10)
        plt.ylim(0,10)
        for d in range (40):
            if x[i]>=ge*d:
                plt.vlines(ge*d,0,ge*d,linestyles='-',colors="c")
            if d*ge>x[i]:break
        plt.plot()
        name="step_rope"
        plt.savefig(name+".png")
        deputy.read(name+".png",-1)
        plt.close()
        image_list.append(imageio.imread(name+'.png'))
    for i in range(5):image_list.append(imageio.imread('rope.png'))
    imageio.mimsave('step_rope.gif', image_list, duration=0.5)



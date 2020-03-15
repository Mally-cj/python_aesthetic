import numpy as np
import matplotlib.pyplot as plt
import cv2
import deputy
import imageio
plt.rcParams['font.sans-serif']=['SimHei']
plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号

def combin1():
    name="对比图1"
    def x0(t,i=0):
        t=t
        t=t-i
        return t
        #表示激励

    #原函數为y=u(-t)
    def f1(t,i):
        return x0(t,i)

    qi,mo=-10,10  # 坐标轴的起始位置
    ylim_min,ylim_max=-4,200     #y轴的范围
    num = 1000  # 样本数量
    image_list = []
    t1 = 6
    t0 = 5

    x = np.linspace(qi, mo)

    for i in range(0, t0 + 1):
        plt.title("hello")
        #picture 1
        x1=t1-i  # 点动
        ax1=plt.subplot(1,2,1)
        ax1.set_title('函数不变，t变')
        ax1.plot(x, f1(x,0), lw=2, label="y(t)")

        ax1.legend()
        ax1.set(ylim=(-10,15))
        plt.plot(x1, f1(x1,0), 'bo')       #标出移动的点
        ax1.annotate('(%d,%d)' % (x1,f1(x1,0)), xy=(x1 ,f1(x1,0)))

        if (i == t0):
            y1=f1(x1,0)
            ax1.annotate("y值为%lf"%y1, xy=(x1-2, y1+2), xytext=(x1-3, y1 + 1),color='b')

        ax1.annotate('y=f(t)', xy=(1,1),xytext=(t1-5, t1-7))    #曲线的注释

        #picture 2
        x2=t1     #点不动
        y2 = f1(x2, i)
        ax2 = plt.subplot(1,2,2)
        ax2.set_title('函数变，t不变')
        ax2.plot(x, f1(x, i), lw=2, label="y=y(t-t0)",color="darkviolet")  #函数曲线
        ax2.legend()    #显示图标
        plt.annotate('y=f(t-%d)' % i, xy=(1,1),xytext=(t1-3, t1-7)) #给函数图像做注释
        ax2.set(ylim=(-10,15))
        ax2.plot(x2, y2, 'p',color="purple")  # 标出移动的点
        ax2.annotate('(%d,%d)' % (x2,y2), xy=(x2, y2))


        if i == t0:
            ax2.annotate('y值为%lf'%(y2), xy=(x2-1, y2-1), xytext=(x2-5, y2 + 1),color='darkorchid')


        plt.savefig('comb1.png')
        plt.close()  # 这样会清楚旧图
        image_list.append(imageio.imread('comb1.png'))
        deputy.read("comb1.png",1)
    imageio.mimsave('对比图1.gif', image_list, duration=1)

def combin2():
    name="对比图2"
    def x0(t,i=0):
        t=-t
        t=t-i
        return t
        #表示激励

    #原函數为y=u(-t)
    def f1(t,i):
        return x0(t,i)

    qi,mo=-10,10  # 坐标轴的起始位置
    ylim_min,ylim_max=-4,200     #y轴的范围
    num = 1000  # 样本数量
    image_list = []
    t1 = 6
    t0 = 5

    x = np.linspace(qi, mo)

    for i in range(0, t0 + 1):
        plt.title("hello")
        #picture 1
        x1=t1-i  # 点动
        ax1=plt.subplot(1,2,1)
        ax1.set_title('函数不变，t变')
        ax1.plot(x, f1(x,0), lw=2, label="y(-t)")

        ax1.legend()
        ax1.set(ylim=(-15,10))
        plt.plot(x1, f1(x1,0), 'bo')       #标出移动的点
        ax1.annotate('(%d,%d)' % (x1,f1(x1,0)), xy=(x1 ,f1(x1,0)))

        if (i == t0):
            y1=f1(x1,0)
            ax1.annotate("y值为%lf"%y1, xy=(x1-2, y1+4), xytext=(x1-3, y1 + 1),color='b')

        ax1.annotate('y=f(-t)', xy=(2,-4),xytext=(-5, -3))    #曲线的注释

        #picture 2
        x2=t1     #点不动
        y2 = f1(x2, i)
        ax2 = plt.subplot(1,2,2)
        ax2.set_title('函数变，t不变')
        ax2.plot(x, f1(x, i), lw=2, label="y=y(-t-t0)",color="darkviolet")  #函数曲线
        ax2.legend()    #显示图标
        plt.annotate('y=f(-t-%d)' % i, xy=(1,6),xytext=(t1-3, t1-7)) #给函数图像做注释
        ax2.set(ylim=(-15,10))
        ax2.plot(x2, y2, 'p',color="purple")  # 标出移动的点
        ax2.annotate('(%d,%d)' % (x2,y2), xy=(x2, y2))


        if i == t0:
            ax2.annotate('y值为%lf'%(y2), xy=(x2-1, y2-1), xytext=(x2-5, y2 + 1),color='darkorchid')


        plt.savefig('comb2.png')
        plt.close()  # 这样会清楚旧图
        image_list.append(imageio.imread('comb2.png'))
        deputy.read("comb2.png",2)


    imageio.mimsave(name+'.gif', image_list, duration=1)
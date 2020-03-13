import numpy as np
import matplotlib.pyplot as plt
import cv2
import imageio

#制作单独的演示图片
def sig_f1():
    def f1(t,t0):
        return (t>0)*t

    qi,mo = -10,10  # 坐标轴的起始位置
    num = 1000  # 样本数量
    x=np.linspace(qi,mo)
    image_list = []
    t1=6
    t0=4

    for i in range(0,t0+1):
        plt.title('点动，函数不变', fontsize=24)
        plt.xlim(qi, mo)
        x1=t1-i
        y1=f1(x1,0)
        plt.plot(x, f1(x,0), lw=2, label="f(t)")
        plt.plot(x1,y1,'bo')
        if(i==t0):
            plt.annotate('arrive', xy=(x1, y1), xytext=(x1, y1+3), arrowprops=dict(facecolor='red', shrink=0.01))

        plt.annotate('(%d,%d)' % (x1, y1), xy=(x1 + 2, y1), xytext=(x1, y1 + 0.4))

        plt.savefig('single1.png')
        plt.close()  # 这样会清楚旧图
        image_list.append(imageio.imread('single1.png'))
        img = cv2.imread('single1.png')
    imageio.mimsave('single1.gif', image_list, duration=1)


def sig_f2():
    def f1(t,t0):
        t=t-t0
        return (t>0)*t

    qi,mo = -10,10  # 坐标轴的起始位置
    num = 1000  # 样本数量
    x=np.linspace(qi,mo)
    image_list = []
    t1=6
    t0=4

    for i in range(0,t0+1):
        plt.title('函数右移，点不变', fontsize=24)
        plt.xlim(qi, mo)
        x1=t1
        y1=f1(x1,i)
        plt.plot(x, f1(x,i), lw=2, label="f(t-t0)")
        plt.plot(x1,y1,'bo')
        if(i==t0):
            plt.annotate('!', xy=(x1, y1), xytext=(x1, y1+3), arrowprops=dict(facecolor='red', shrink=0.01))

        plt.annotate('(%d,%d)' % (x1, y1), xy=(x1 + 0.3, y1), xytext=(x1, y1 + 0.4))

        plt.savefig('single2.png')
        plt.close()  # 这样会清楚旧图
        image_list.append(imageio.imread('single2.png'))
        img = cv2.imread('single2.png')
    imageio.mimsave('single2.gif', image_list, duration=1)
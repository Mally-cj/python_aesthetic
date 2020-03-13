def ori_f1():
    # fig = plt.figure(figsize=(16,9))
    # ax = fig.add_subplot(111)

    qi = -10  # 坐标轴的起始位置
    mo = -qi
    num = 1000  # 样本数量
    image_list = []
    t1=6
    t0=4
    for i in range(0,t0+1):
        plt.title('f(t)原图移动', fontsize=24)
        plt.xlim(qi, mo, 0.1)
        plt.ylim(-4,12)
        x1=t1-i
        y1=x1
        x = np.linspace(qi, mo)
        y = (x > 0) * x
        plt.plot(x, y, lw=2, label="u(t)")
        plt.plot(x1,y1,'bo')
        if(i==t0):
            plt.annotate('arrive', xy=(x1, y1), xytext=(x1, y1+3), arrowprops=dict(facecolor='red', shrink=0.01))

        plt.annotate('(%d,%d)' % (x1, y1), xy=(x1 + 2, y1), xytext=(x1, y1 + 0.4))

        plt.savefig('temp.png')
        # set(gca,'xtiock')
        plt.close()     #这样会清楚旧图
        image_list.append(imageio.imread('temp.png'))
        img=cv2.imread('temp.png')
        print(img.shape)
    imageio.mimsave('pic.gif', image_list, duration=1)

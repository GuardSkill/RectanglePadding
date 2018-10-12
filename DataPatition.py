# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import numpy

# ax1.xlabel("Financial expenditure")
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\FZSTK.TTF')


fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal',autoscale_on=True,ylim=(0,100),xlim=(0,200))

# data=[1/16,1/16,1/8,2/8,1/6,1/3]                           #各种数据
# data=[12,13,14,56,64,24,100,32,80,66,40]
data={"支出1": 1/16, "支出2": 1/16, "支出3": 1/8, "支出4": 1/16, "支出5": 2/8, "支出6": 1/6, "支出7": 1/3}
data={"支出1":22, "支出2": 33, "支出3": 41, "支出4": 42, "支出5": 32, "支出6": 13, "支出7": 31,"支出8": 42, "支出9": 32, "支出10": 13, "支出11": 31,}
list=sorted(data.items(),key = lambda kv: kv[1],reverse=True)     #list dictionary
print(list)

def sumofdata(a):
    sum=0
    for key,value in a:
        sum=sum+value
    return sum

def Patition(data,width,height,x,y):
    while(data.__len__()>0):
        randxory=random.randint(0, 1)
        randpop=random.randint(0,data.__len__()-1)          #random choose a part of data
        values=list(data.values())
        labels=list(data.keys())
        if randxory==0:
            patch_x=(width-x)*values[randpop]/sum(values)
            ax1.add_patch(
                patches.Rectangle(
                    (x,y),  # position of (x,y)
                    patch_x,  # width
                    height-y,  # height
                    label=labels[randpop],
                    facecolor=numpy.random.rand(3,)        #random color
                )
            )
            plt.text(x, y,labels[randpop],fontproperties = myfont)
            x=x+patch_x
        else:
            patch_y=(height-y)*values[randpop]/sum(values)
            ax1.add_patch(
                patches.Rectangle(
                    (x,y),  # position of (x,y)
                    width-x,  # width
                    patch_y,  # height
                    label=labels[randpop],
                    facecolor=numpy.random.rand(3, )      #random color
                )
            )
            plt.text(x, y, labels[randpop], fontproperties=myfont)
            y=y+patch_y
        data.pop(labels[randpop])
#Patition(data,100,100,0,0)

def PatitionRecursion(data,width,height,x,y):
    if(data.__len__()>1):
        sum=sumofdata(data)
        n=random.randint(1, data.__len__()-1)
        a = data[0:n]
        sum1=sumofdata(a)
        for i in a:
            data.remove(i)
        sum2=sumofdata(data)
        L1 = width * sum1 / sum
        L2=height * sum1 / sum
        if(width>height):
            PatitionRecursion(a,L1 , height, x, y)
            PatitionRecursion(data, width-L1, height, x+L1, y)
        else:
            PatitionRecursion(a, width, L2, x, y)
            PatitionRecursion(data, width, height-L2, x , y+ L2)
    else:
        ax1.add_patch(
            patches.Rectangle(
                (x, y),  # position of (x,y)
                width,  # width
                height,  # height
                facecolor=numpy.random.rand(3, )  # random color
            )
        )
        plt.text(x, y,data[0][0], fontproperties=myfont)



PatitionRecursion(list,200,100,0,0)
#plt.legend(prop=zhfont1)
plt.show(prop=myfont)
fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')


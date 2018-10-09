# -*- coding:utf-8 -*-
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import random
import numpy

#ax1.xlabel("Financial expenditure")
myfont = matplotlib.font_manager.FontProperties(fname='C:\Windows\Fonts\FZSTK.TTF')

fig1 = plt.figure()
ax1 = fig1.add_subplot(111, aspect='equal',autoscale_on=True,ylim=(0,100),xlim=(0,100))

#data=[1/16,1/16,1/8,2/8,1/6,1/3]                           #各种数据
#data=[12,13,14,56,64,24,100,32,80,66,40]
data={"支出1": 1/16, "支出2": 1/16, "支出3": 1/8, "支出4": 1/16, "支出5": 2/8, "支出6": 1/6, "支出7": 1/3}
print(list(data.keys()))

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
Patition(data,100,100,0,0)


#plt.legend(prop=zhfont1)
plt.show(prop=myfont)
#fig1.savefig('rect1.png', dpi=90, bbox_inches='tight')


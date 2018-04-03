from tkinter import *
reset=True
def buttonCallBack(event):
    #global全局变量
    global label
    global reset
    #widgt产生事件的组件。这是一个合法的Tkinter组件实例，而不是一个名字。所有的事件都归于此类。
    num=event.widget['text']
    #清零C操作
    if num=='C':
        label['text']="0"
        return
    #运算操作
    if num in "=":
        label['text']=str(eval(label['text']))
        reset=True
        return
    s=label['text']
    #输入零重置
    if s=='0' or reset==True:
        s=""
        reset=False
    #字符串输入
    label['text']=s+num
#主窗口
root=Tk()
root.wm_title("计算器")
#显示栏1
#Label——该配件处理文本或图像的显示
#输入框
label=Label(root,text="0",background="white",anchor="e")
label['width']=35
label['height']=2
label.grid(row=1,columnspan=4,sticky=W)
#按钮
showText="789/456*123-0.C+"
#计算器前4行
for i in range(4):
    for j in range(4):
        b=Button(root,text=showText[i*4+j],width=7)
        #grid
        #Grid 管理器把一个master widget的所有可用空间分成格状的很多小份，
        #每一份叫做一个cell，用row，column，rowspan，columnspan就可以确定一个cell。
        b.grid(row=i+2,column=j)
        #使用了frame组件的bind方法去把一个callback函数和一个叫做<Button-1>的时间映射在一起
        #当Button 1被按下的时候移动鼠标（B2代表中键，B3代表右键），
        #鼠标指针的当前位置将会以event对象的x y 成员的形式传递给callback
        #x,y当前的鼠标位置，单位：像素。
        b.bind("<Button-1>",buttonCallBack)
#计算器第五行“（）”
showText="()"
for i in range(2):
    b=Button(root,text=showText[i],width=7)
    b.grid(row=6,column=2+i)
    b.bind("<Button-1>",buttonCallBack)
#计算器第5行“=”
b=Button(root,text="=")
#columnspan指明占了几列   sticky组件紧靠单元格的某一角
b.grid(row=6,columnspan=2,sticky="we")
b.bind("<Button-1>",buttonCallBack)
#加入服务

root.mainloop()
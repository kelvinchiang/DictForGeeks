# -*- coding: utf-8 -*-
"""
DictForGeeks is an useful dict tools for the geeks who want to change and save
New words and phrases any time.English and Chinese both supported.
It is totally free, you can use or modify for any purpose.
Write by Python, GUI is Tkinter. 
Hope you like it.

Usage:
    First it will create a txt file called "DictForGeeksdata" where the source code is.
    The next time you start this code will read this file as the database for your Dict.
    
"""
import os
from Tkinter import *
#处理响应函数
#查询窗口的变化的响应函数
def callback(sv):
    word=entry.get().strip()
    t1.delete(0.0,END)
    lbox.delete(0,END)
    Tip(0)
    datalist=list(data)
    datalist.sort()
    for i in datalist:
        if i>=word:
            lbox.insert(END,str(i).decode('gbk'))

    if word in data:
        t1.insert(INSERT,str(data[word]).decode('gbk'))
    elif len(entry.get().strip())!=0:
        t1.insert(INSERT,str_cannotfind)
#解释框改变时，将状态设为空
def TextChange(event):
    Tip(0)
#将Listbox中选中的项加载到查询窗口
def printList(event):
    lbox_v=lbox.get(lbox.curselection())
    e.set(lbox_v)
#保存
def Save():
    word=entry.get().strip()
    answer=t1.get(0.0,END).strip()
    if len(word)==0 or len(answer)==0:
        Tip(3)
    elif answer==str_cannotfind.decode('utf-8'):
        Tip(2)
    elif word in data:
        if answer==data[word]:
            Tip(4)
        else:
            data[word]=answer
            Tip(1)
    elif word not in data:
        data[word]=answer
        Tip(1)
    SaveInFile()

#写入文本文件
def SaveInFile():
    s = '' 
    for k in data: 
        s += '%s~%s\n' % (k,data[k]) 
    fout = open(fname,'w') 
    fout.write(s) 
    fout.close() 
#提示项   
def Tip(n):
    if n==0:
        tip.set(str_null)
    if n==1:
        tip.set(str_saveok)
    if n==2:
        tip.set(str_saveerror)
    if n==3:
        tip.set(str_wordempty)
    if n==4:
        tip.set(str_repeat)
        
#主程序从这里开始
fname = 'DictForGeeksdata' 
data={}
if fname in os.listdir('.'): 
    for line in open(fname,'r').readlines():
        line=line.strip()
        if '~' in line:
            key=line.split('~')[0].decode('gbk')
            value=line.split('~')[1]
            data[key]=value
        if '~' not in line:
            value=value+'\n'+line
            data[key]=value

#从这里开始写UI
root=Tk()
root.title('DictForGeeks')
root.geometry('400x400')
#查询标签
lb1=Label(root,text='查询:')
lb1.place(x=100,y=20)
#状态标签
tip=StringVar()
lb2=Label(root,fg="blue",textvariable=tip)
lb2.place(x=40,y=350)
#参考列表框
lbox = Listbox(root)
lbox.place(x=140,y=40)
lbox.bind('<Double-Button-1>',printList)
#输出显示窗口
t1=Text(root,height=10,width=30)
t1.bind("<Key>",TextChange)
t1.place(x=80,y=100)


    
#查询窗口
e=StringVar()
e.trace("w", lambda name, index, mode: callback(e))
entry=Entry(root,textvariable=e)
entry.place(x=140,y=20)
entry.focus_set()

#按钮
btn1=Button(root,text='保存',command=Save,bg='PeachPuff')
btn1.place(x=340,y=160)
#这里声明常用的字符串
str_cannotfind="没有找到该单词!"
str_saveok="保存成功!"
str_saveerror="保存失败，请修改解释!"
str_wordempty="保存失败，单词或解释为空!"
str_repeat="保存失败，重复保存!"
str_null=""

#主循环
root.mainloop()

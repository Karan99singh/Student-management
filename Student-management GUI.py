import tkinter as tk
import tkinter.messagebox as tkm
import tkinter.ttk as ttk

#list1 = [{"name":"yoyo","age":"21","standard":"3","gender":"male","feestatus":"paid","rollno":"10"},{"name":"nono","age":"34","standard":"4","gender":"male","feestatus":"unpaid","rollno":"15"}]
dic1= {}
list1 = []
yo=0
fle = open(r"C:\Users\Karan Singh\Documents\pythonexercises\studentfile.txt","a")
fle.close()
with open(r"C:\Users\Karan Singh\Documents\pythonexercises\studentfile.txt","r") as reader:
    for line in reader.readlines():
        kstart = line.find("*")
        kend = line.find("*",kstart+1)
        vstart = line.find("#")
        vend = line.find("#",vstart+1)
        dic1[line[kstart+1:kend]] = line[vstart+1:vend]
        yo += 1
        if yo == 6:
            list1.append(dic1)
            dic1 = {}
            yo = 0


root = tk.Tk()

def lablemaker():
    labelwin = tk.Tk()
    dictlabel = {}
    listlabel = []
    rowc=0
    columnc=0
    nums = 1
    for item in list1:
        spacelabel = tk.Label(labelwin,text=f"\nStudent {nums}") 
        spacelabel.grid(row=rowc)
        rowc+=1
        for key,val in item.items():
            dictlabel[key] = tk.Label(labelwin)
            
            dictlabel[key].config(text= f"{key} : {val}")
            dictlabel[key].grid(row = rowc ,column = columnc)
            rowc += 1
        rowc +=3
        nums += 1  
        listlabel.append(dictlabel)
        dictlabel.clear()
    rowc=0
    columnc=0
    nums = 1
    dictlabel.clear()
    listlabel.clear()
    labelwin.mainloop()
def searchfunc():
    sear = searchvar.get()
    searclass = searchclassvar.get()
    searroll = searchrollvar.get()
    searchbox.delete(0,"end")
    search_class.delete(0,"end")
    search_roll.delete(0,"end")
    for item in list1:
        if item["standard"] == searclass:
            if item["name"] == sear:
                if item["rollno"] == searroll:
                    infodia(item)
                else:
                   rollcheck =  tkm.askyesno("Continue","Rollno did't match ")
                   if rollcheck == True:
                        try:
                           infodia(item)
                        except:
                            pass


def infodia(item):
    dialogue = tk.Tk()
    dialabel = tk.Label(dialogue,text=f"name : {item['name']} \n age : {item['age']} \n class : {item['standard']} \n Rollno : {item['rollno']} \n Fee Status : {item['feestatus']}")
    dialabel.grid(rowspan=2)
    diabutton1 = tk.Button(dialogue,text="edit info",command= lambda :editor(item))
    diabutton1.grid(row=4)
    dialogue.mainloop()

def editor(item):
    editing = tk.Tk()
    label1 = tk.Label(editing,text="new name ")
    label2 = tk.Label(editing,text="new age ")
    label3 = tk.Label(editing,text="new class ")
    label4 = tk.Label(editing,text="new rollno ")
    label5 = tk.Label(editing,text="Gender")
    label6 = tk.Label(editing,text="Fee status")
    label1.grid(row=0)
    label2.grid(row=1)
    label3.grid(row=2)
    label4.grid(row=3)
    label5.grid(row=4)
    label6.grid(row=5)
    entry1var = tk.StringVar(editing,value=item["name"])
    entry2var = tk.StringVar(editing,value=item["age"])
    entry3var = tk.StringVar(editing,value=item["standard"])
    entry4var = tk.StringVar(editing,value=item["rollno"])
    entry5var = tk.StringVar(editing)
    entry6var = tk.StringVar(editing)#,value=item["feestatus"])
    entry1 = tk.Entry(editing,width = 20,textvariable = entry1var)
    entry2 = tk.Entry(editing,width = 20,textvariable = entry2var)
    entry3 = tk.Entry(editing,width = 20,textvariable = entry3var)
    entry4 = tk.Entry(editing,width = 20,textvariable = entry4var)
    entry5 = ttk.Combobox(editing,width=20,textvariable = entry5var,state="readonly")#,values=["Male","Female"])
    entry5["values"] = ("male","female")
    if item["gender"] == "male":
        entry5.current(0)
    else:
        entry5.current(1)
   
    entry6 = ttk.Combobox(editing,width = 20,textvariable = entry6var,state="readonly")
    entry6["values"] = ("paid","unpaid")
    if item["feestatus"] == "paid":
        entry6.current(0)
    else:
        entry6.current(1)
    entry1.grid(row=0,column=2)
    entry2.grid(row=1,column=2)
    entry3.grid(row=2,column=2)
    entry4.grid(row=3,column=2)
    entry5.grid(row=4,column=2)
    entry6.grid(row=5,column=2)
    
    applybutton = tk.Button(editing,text="Apply",command = lambda :applyconfig(item,entry1var,entry2var,entry3var,entry4var,entry5var,entry6var))
    applybutton.grid(row = 7)
    
    deletebutton = tk.Button(editing,text="Delete",command = lambda :deleter(item))
    deletebutton.grid(row = 7,column =2)
    
    editing.mainloop()

def adder():
    dictadd = {}
    list1.append(dictadd)
    indexing = list1.index(dictadd)
    adding = tk.Tk()
    label1 = tk.Label(adding,text="Name ")
    label2 = tk.Label(adding,text="Age ")
    label3 = tk.Label(adding,text="Class ")
    label4 = tk.Label(adding,text="Rollno ")
    label5 = tk.Label(adding,text="Gender")
    label6 = tk.Label(adding,text="Fee status")
    label1.grid(row=0)
    label2.grid(row=1)
    label3.grid(row=2)
    label4.grid(row=3)
    label5.grid(row=4)
    label6.grid(row=5)
    entry1var = tk.StringVar(adding,value="Empty")
    entry2var = tk.StringVar(adding,value="Empty")
    entry3var = tk.StringVar(adding,value="Empty")
    entry4var = tk.StringVar(adding,value="Empty")
    entry5var = tk.StringVar(adding)
    entry6var = tk.StringVar(adding)
    entry1 = tk.Entry(adding,width = 20,textvariable = entry1var)
    entry2 = tk.Entry(adding,width = 20,textvariable = entry2var)
    entry3 = tk.Entry(adding,width = 20,textvariable = entry3var)
    entry4 = tk.Entry(adding,width = 20,textvariable = entry4var)
    entry5 = ttk.Combobox(adding,width=20,textvariable = entry5var,state="readonly")#,values=["Male","Female"])
    entry5["values"] = ("male","female")
    entry5.current(0)
    
    
    entry6 = ttk.Combobox(adding,width = 20,textvariable = entry6var,state="readonly")
    entry6["values"] = ("paid","unpaid")
    entry6.current(1)
    entry1.grid(row=0,column=2)
    entry2.grid(row=1,column=2)
    entry3.grid(row=2,column=2)
    entry4.grid(row=3,column=2)
    entry5.grid(row=4,column=2)
    entry6.grid(row=5,column=2)
    
    applybutton = tk.Button(adding,text="Add",command = lambda :applyconfig(list1[indexing],entry1var,entry2var,entry3var,entry4var,entry5var,entry6var))
    applybutton.grid(row = 7)
    
    adding.mainloop()

def deleter(item):
    yesno = tkm.askyesno("Delete","Are you sure you want to delete ")
    if yesno == True:
        delfile = list1.pop(list1.index(item))
            

def applyconfig(item,entry1var,entry2var,entry3var,entry4var,entry5var,entry6var):
    item["name"] = entry1var.get()
    item["age"] = entry2var.get()
    item["standard"] = entry3var.get()
    item["rollno"] = entry4var.get()
    item["gender"] = entry5var.get()
    item["feestatus"] = entry6var.get()

def saver():
    with open(r"C:\Users\Karan Singh\Documents\pythonexercises\studentfile.txt","a") as writer:
            for i in list1:
                for key,item in i.items():
                    writer.write(f"*{key}*:#{item}# \n")
            

def totalstudents():
    totstu = tk.Tk()
    totalstr = str(len(list1))
    totallable = tk.Label(totstu,text=f"total students : {totalstr}")
    totallable.pack()
    totstu.mainloop()

button1 = tk.Button(root,text="Show All",command=lablemaker)
button1.grid(row=5,column=1)
Mainlabel = tk.Label(root,text="Search")
labelname = tk.Label(root,text = "Name")
labelclass = tk.Label(root,text="Class")
labelroll = tk.Label(root,text="Roll")
Mainlabel.grid(row=0,column=1)
labelname.grid(row=1,column=0)
labelclass.grid(row=2,column=0)
labelroll.grid(row=3,column=0)
searchvar = tk.StringVar()
searchbox = tk.Entry(root,width = 20, textvariable = searchvar)
searchbox.grid(row=1,column=1)
searchclassvar = tk.StringVar()
search_class = tk.Entry(root,width=20,textvariable=searchclassvar)
search_class.grid(row=2,column=1)
searchrollvar = tk.StringVar()
search_roll = tk.Entry(root,width=20,textvariable = searchrollvar)
search_roll.grid(row=3,column=1)
searchbutton = tk.Button(root,text="search",command = searchfunc)
searchbutton.grid(row=5)

menu1 = tk.Menu(root)
root.config(menu=menu1)
submen = tk.Menu(menu1)
menu1.add_cascade(label="file",menu=submen)
submen.add_command(label="add",command = adder)
submen.add_command(label="count students",command=totalstudents)
submen.add_command(label="save",command=saver)
submen.add_command(label="quit",command = root.quit)


root.mainloop()
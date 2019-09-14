def data(a):
    def datatype(func):
        def wrapper(*args):
            typelist = [type(i)==a for i in args]
            if all(typelist):
                return func(*args)
            else:
                print("invalid input")
        return wrapper            
    return datatype        


@data(str)
def dictmaker(name,age,standard):
    dic1 = {"name":name,"age":age,"standard":standard}
    return dic1



dic1= {}
list1 = []
yo = 0


print("LOADING --- studentfile.txt")
fle = open(r"C:\Users\Karan Singh\Documents\pythonexercises\studentfile.txt","w")
fle.close()
with open(r"C:\Users\Karan Singh\Documents\pythonexercises\studentfile.txt","r") as reader:
    for line in reader.readlines():
        kstart = line.find("*")
        kend = line.find("*",kstart+1)
        vstart = line.find("#")
        vend = line.find("#",vstart+1)
        dic1[line[kstart+1:kend]] = line[vstart+1:vend]
        yo += 1
        if yo == 3:
            list1.append(dic1)
            dic1 = {}
            yo = 0
       

while True:
    while True:
        try:
            num = int(input("\nWhat you want to do \n1.input\n2.search\n3.edit\n4.print\n5.save to file \ninput value:   "))
        except ValueError:
            print("\n    wrong input try again")
        except:
            print("\n    unexpected error")
        else:
            break
        
    if num == 1:
        while True:
            try:
                val = int(input(("how many student you want to add : ")))
            except ValueError:
                print("\n    wrong input try again")
            except:
                print("\n    unexpected error")
            else:
                break
        for i in range(val):
            print(f"\n    Student {i+1}")
            temp1 = (input("enter name : "))
            temp2 = (input("enter age : "))
            temp3 = (input("enter standard : "))
            dic1 = dictmaker(temp1,temp2,temp3)
            list1.append(dic1)


    elif num == 2:
        search = input("\nEnter student name: ")
        for i in list1:
            if i["name"] == search:
                for key,value in i.items():
                    print(f"{key}: {value}")
                break
        
                
    elif num == 3:
        while True:
            try:
                option = int(input("\n1.new stuent \n2.edit old \n value :  "))
            except ValueError:
                print("\n    wrong input try again")
            except:
                print("\n    unexpected error")
            else:
                break
        if option == 2:
            search = input("Enter student name: ")
            for i in list1:
                if i["name"] == search:
                    for key,value in i.items():
                        print(f"{key}: {value}")
                        i[key] = input(f"enter new {key} : ")

    
        elif option == 1:
            temp1 = (input("enter name : "))
            temp2 = (input("enter age : "))
            temp3 = (input("enter standard : "))
            dic1 = dictmaker(temp1,temp2,temp3)
            list1.append(dic1)
        else:
            print("Wrong input\n")


    elif num == 4:
        for i in  range(0,len(list1)):
            print(f"\n   Student {i+1}")
            for key,val in list1[i].items():
                print(f"{key} : {val}")
                    
        ex = input("\nInput x to exit or any key to continue :  ")
        if ex == "x" or ex == "X":
            break

    elif num == 5:
        with open(r"C:\Users\Karan Singh\Documents\pythonexercises\studentfile.txt","a") as writer:
            for i in list1:
                for key,item in i.items():
                    writer.write(f"*{key}*:#{item}# \n")
            print("Save sucessful")

        ex = input("\nInput x to exit or any key to continue :  ")
        if ex == "x" or ex == "X":
            break
            

    else:
        print("\nInvalid input\n")

            

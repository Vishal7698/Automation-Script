
"""algorithm to print the names and the count of the same name in the same order which they occur as u ask them"""
def StudentNameCount(Name):
    Count={}
    for Student in Name:                #complexity of for loop is O(n)
        if Student not in Count:        #Dictionary uses a hash lookup i.e its complexity should always O(1)
            Count[Student]=1
        else:
            Count[Student]+=1

    for name,count in Count.items():    #complexity of for loop is O(n)
        print("{} : {}".format(name,count))




if __name__ == '__main__':
    no=int(input("Enter the number of Students"))
    name=list()
    for i in range(1,(no+1)):           #complexity of for loop is O(n)
        name.append(input("enter the {} name ".format(i)))

    #name=['Alok', 'amit', 'suresh' , 'amit', 'vidya', 'sindhu', 'vidya', 'vidya', 'alok']
    StudentNameCount(name)
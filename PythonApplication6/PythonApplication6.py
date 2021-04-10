#names=['amir','jack']
#names.append('arshak')
#names.append('mina')
#for i in names:
#    print(i)


class Student:
    def __init__(self,name,surname,age):
        self.__name=name
        self.__surName=surname
        self.__age=age

    def GetSurname(self):
        return self.__surName


#s1=Student('arshak','Kalantri',11)
#s2=Student('amir','fallah',25)

#students=[s1,s2]

#for item in students:
#    print(item.GetSurname())

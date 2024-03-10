import relation
import lefttree as l

class Group:
    def __init__(self, name):
        self.__peopleList = {0:name}
        self.__relation_List = l.tritree([name],1)
    def __init__(self, name, number):
        self.__peopleList = {}
        count = 0
        for item in name:
            self.__peopleList[count]=item
            count+=1
        relation_List = []
        for x in range(number):
            for s in range(x+1, number):
                rel = relation.Relations(name[x], name[s])
                relation_List.append(rel)
        self.__relation_List = l.tritree(relation_List, len(self.__peopleList))

    def addPerson(self, name):
        relation_List = []
        for x in self.__peopleList:
            rel = relation.Relations(self.__peopleList[x], name)
            relation_List.append(rel)
        self.__relation_List.add(relation_List)

    def printRelations(self):
        print(self.__relation_List)



class main:
    x = Group(["john", "Amy", "Ghar", "Tom"], 4)
    x.addPerson("harry")

    x.printRelations()

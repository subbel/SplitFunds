
class treeNode:

    def __init__(self, *args):
        self.up = None
        self.down = None
        self.left = None
        self.right = None
        if(len(args)==0):
            self.data = None
        else:
            self.data = args[0]

    def getdata(self):
        return self.data

class tritree:
    def __init__(self, list, side):
        self.size = len(list)
        self.side = side
        self.head = treeNode(list.pop(0))
        current = self.head
        for i in range(self.side-2):
            right = current
            for j in range(i+2,self.side):
                right.right = treeNode(list.pop(0))
                right = right.right
            current.down = treeNode(list.pop(0))
            current = current.down

    def __str__(self):
        current = self.head
        value = ""
        while(current!=None):
            value += str(current.data) + "\n"
            child = current
            while(child.right!=None):
                child = child.right
                value += str(child.data)+"\n"
                # print(value)
            current = current.down
        return value

    def rowlength(self, current):
        count = 0
        while(current!=None):
            current = current.right
            count += 1
        return count

    def get(self, indexx, indexy):
        if (indexx > indexy):
            swap = indexx
            indexx = indexy
            indexy = swap
        if (indexx >= self.side-1 or indexy >= self.side ):
            raise "Index out of bounds"
        if (indexy == indexx):
            raise "Wrong Coordinates"
        current = self.head
        for x in range(indexx):
            current = current.down
        for x in range(indexy-indexx-1):
            current = current.right
        return current

    def add(self, list):
        if (len(list)!=self.side):
            raise "length of list is not accurate must be of size" + str(self.side)
        current = self.head
        while current.down is not None:
            right = current
            while right.right!=None:
                right = right.right
            right.right = treeNode(list.pop(0))
            # print(right)
            current = current.down
        current.right = treeNode(list.pop(0))
        current.down = treeNode(list.pop(0))
        self.size += self.side
        self.side +=1
        # return self



# class Main:
#     x = tritree([1,2,3,1,1,1,1,4,5,6],5)
#     print(x)
#     x.add([1,1,1,1,1])
#     x.add([1,1,1,1,1,1])
#     print(x.size)
#     print(x)

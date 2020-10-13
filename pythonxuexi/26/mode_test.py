class People():
    def __init__(self, name, hp,occu):
        self.__name = name#变量被称作属性,这个属性不能直接修改，只能通过方法修改
        self.hp = hp
        self.occu = occu

    def print_role(self):#定义一个方法
        print("name is %s :hp is  %s:occu is %s" % (self.__name, self.hp,self.occu))
    def updateName(self,newname):
        self.__name = newname

class Monster():
    "定义怪物类"
    pass


user1 = People("tanxiumei", 100,'war')
user2 = People("tangdan", 90,'master')
user1.print_role()
user1.updateName("liliang")
user1.print_role()
user1.name = "lihuiwen"
user1.print_role()

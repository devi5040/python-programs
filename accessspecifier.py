#lex_auth_01275045546160947226
class Athlete:
    def __init__(self,name,gender):
        self.__name=name
        self.__gender=gender
    def set_name(self,name):
        self.__name=name
    def set_gender(self,gender):
        self.__gender=gender
    def get_name(self):
        print('name is ',self.__name)
    def get_gender(self):
        print('Gender is ',self.__gender)
    def running(self):
        if(self.__gender=="girl"):
            print("150mtr running")
        else:
            print("200mtr running")
a1=Athlete("Maria","girl")
a1.running()
                                        
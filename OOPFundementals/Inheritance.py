class Musicians():
    def __init__(self,name):
        self.name = name
        print("Musician Just Created")

    def test1(self):
        print("test1")

    def test2(self):
        print("test2")

james_hetfield = Musicians("James Hetfield")

class MusicianPlus(Musicians):
    def __init__(self,name):
        Musicians.__init__(self,name)
        print("MusicianPlus Just Created")

lars = MusicianPlus("lars")
lars.test1()
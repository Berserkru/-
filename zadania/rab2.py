class curs():
    def __init__(self, python, teacher, time):
       self.python = python
       self.teacher = teacher
       self.time = time
    def description(self):
     print ("курс -", self.python, "преподаватель -", self.teacher, "Кол-во занятий -", self.time)
description = curs("python", " Alexey", 128)
description. description()
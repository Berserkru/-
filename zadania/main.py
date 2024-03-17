class PO():
    def __init__(self, name, developer, version):
       self.name = name
       self.developer = developer
       self.version = version
    def description(self):
     print ("по -", self.name, "разработчик -", self.developer, "Версия -", self.version)
description = PO("windows", "Bill Geits", "new")
description. description()
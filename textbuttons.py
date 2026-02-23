class textbutton:
    def __init__(self,value,actFunc):
        self.setValue(value)
        self.actFunc = actFunc

    def setValue(self,value):
        self.value = value

    def __str__(self):
        return str(self.value)
    
    def click(self,usrInput):
        self.actFunc(usrInput,self)
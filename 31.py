class Dam:
    def __init__(self,name,length):
        self.name=name
        self.length=length
    def get_length(self):
        return self.length
dam1=Dam("ABC dam",3.5)
print("DAM name:",dam1.name)
print("DAM length",dam1.get_length())
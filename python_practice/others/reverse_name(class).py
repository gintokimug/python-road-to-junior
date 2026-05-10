class Reverse_name:
    def __init__(self, name):
        self.name = name
        self.index =  len(name) - 1


    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index < 0:
            raise StopIteration
        else:
            letter = self.name[self.index]
            self.index -= 1
            return letter
    
my_name = Reverse_name("Павел")
for char in my_name:
    print(char)

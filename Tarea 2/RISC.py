class RISC:
    def __init__(self):
        self.memory = [{0x0000 : 1},
                       {0x0004 : 1},
                       {0x0008 : 2},
                       {0x000C : 2},
                       {0x0010 : 3},
                       {0x0014 : 3},
                       {0x0018 : 4},
                       {0x001C : 4},
                       {0x0020 : 5},
                       {0x0024 : 5},
                       {0x0028 : 6},
                       {0x002C : 6},
                       {0x0030 : 7},
                       {0x0034 : 7},
                       {0x0038 : 8},
                       {0x003C : 8},
                       {0x0040 : 9},
                       {0x0044 : 9},
                       {0x0048 : 10},
                       {0x004C : 10},
                       {0x0050 : 0}]
        
    def LOAD(self, address):
        for cell in self.memory:
            content = cell.get(address, "unknown") 
            if content != "unknown":
                return content
        return "Out of Range"
    
    def STORE(self, content, address):
        for cell in self.memory:
            if address in cell:
                cell[address] = content
        return "Out of Range"
        
    def ADD(self, add1, add2):
        sum = add1, add2
        return sum 
    
my_RISC = RISC()
R1 = my_RISC.LOAD(0x0004C)
print(R1)
my_RISC.STORE(23, 0x004C)
R1 = my_RISC.LOAD(0x0004C)
print(R1)

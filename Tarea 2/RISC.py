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
        """ Reads data from a memory address

        Args:
            address: memory address to read from

        Returns:
            content: data read from memory
            1: if address is not found
        """
        
        for cell in self.memory:
            content = cell.get(address, "unknown") 
            if content != "unknown":
                return content
        return 1
    
    def STORE(self, content, address):
        """ Writes data from a memory address

        Args:
            address: memory address to write to
            content: data to write to memory

        Returns:
            0: if sucessful
        """
        
        for cell in self.memory:
            if address in cell:
                cell[address] = content
        return 0
        
    def ADD(self, add1, add2):
        """ Adds two numbers

        Args:
            add1: first addend
            add2: second addend

        Returns:
            sum: result of addition
        """
        
        sum = add1 + add2
        return sum 
    
    
my_RISC = RISC()

# Adds each element of both arrays and stores result in address 0x0050
for i in range(10):
    R1 = my_RISC.LOAD(i*8)
    R2 = my_RISC.LOAD(i*8 + 4)
    R3 = my_RISC.ADD(R1, R2)
    my_RISC.STORE(R3, 0x0050)
    print(R3)

print(my_RISC.memory)

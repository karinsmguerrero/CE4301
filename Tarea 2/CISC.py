class CISC:
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
        
    def SUMMEM(self, address, storeAddress):
        """ Adds two consecutive numbers from memory and writes the result to memory

        Args:
            address: address of the first addend
            storeAddress: address where the result should be written

        Returns:
            sum: result of the addition
        """

        # Load first addend from memory
        for cell in self.memory:
            add1 = cell.get(address, "unknown") 
            if add1 != "unknown":
                break
        # Load consecutive addend from memory
        for cell in self.memory:
            add2 = cell.get(address + 4, "unknown")
            if add2 != "unknown":
                break
        sum = add1 + add2
        # Store sum in memory
        for cell in self.memory:
            if storeAddress in cell:
                cell[storeAddress] = sum        
        return sum
    
myCISC = CISC()
# Adds each element of both arrays and stores result in address 0x0050
for i in range(10):
    R1 = myCISC.SUMMEM(i*8, 0x0050)
    print(R1)
    
print(myCISC.memory)
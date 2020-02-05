from random import choice
import matplotlib.pyplot as plt

class plot_together():    
    """Plots the amount of steps away from perfect center (0,0)"""
    def __init__(self, walks, steps):
        """Warning.. if you type plot together with parenthese, it will auto plot
    the steps for you"""
        allWalks = []
        for i in range(walks):
            current = self.instance(steps)
            allWalks.append(current)
            print(current)
        print("Closest: %s"%min(allWalks))
        print("Furthest: %s"%max(allWalks))
        plt.plot(allWalks)
        plt.title("Num. of points away from (0, 0), total")
        plt.xlabel("Instance number")
        plt.ylabel("# Away from (0, 0)")
        plt.show()
    def instance(self, steps=10):
        """Will take a step depending on the int that you chose"""
        x,y = 0,0
        for i in range(steps):
            newInst = choice(("N","S","E","W"))
            if newInst == "N":
                y+=1
            elif newInst == "S":
                y-=1
            elif newInst == "E":
                x+=1
            elif newInst == "W":
                x-=1
        return abs(x) + abs(y)
        
class plot_separate():
    """Shows the amount (by dimension) of steps away from perfect center (0,0)"""
    def __init__(self, walks, steps):
        self.allWalks = []
        for i in range(walks):
            current = self.instance(steps)
            self.allWalks.append(current)
            print(current)
    def instance(self, steps=10):
        """Will take a step depending on the int that you chose"""
        x,y = 0,0
        for i in range(steps):
            newInst = choice(("N","S","E","W"))
            if newInst == "N":
                y+=1
            elif newInst == "S":
                y-=1
            elif newInst == "E":
                x+=1
            elif newInst == "W":
                x-=1
        return abs(x), abs(y)
    def plot(self):
        for pair in self.allWalks:
            plt.scatter(pair[1], pair[0])
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.title("Num. of points away from (0, 0), by dimension")
        plt.show()

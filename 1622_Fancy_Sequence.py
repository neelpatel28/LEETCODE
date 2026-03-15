class Fancy(object):

    def __init__(self):
        self.MOD = 10**9 + 7
        self.seq = []
        self.mul = 1
        self.add = 0

    def modinv(self, x):
        return pow(x, self.MOD - 2, self.MOD)

    def append(self, val):
        val = (val - self.add) % self.MOD
        val = val * self.modinv(self.mul) % self.MOD
        self.seq.append(val)

    def addAll(self, inc):
        self.add = (self.add + inc) % self.MOD

    def multAll(self, m):
        self.mul = (self.mul * m) % self.MOD
        self.add = (self.add * m) % self.MOD

    def getIndex(self, idx):
        if idx >= len(self.seq):
            return -1
        return (self.seq[idx] * self.mul + self.add) % self.MOD
    
obj = Fancy()
# ["Fancy","append","addAll","append","multAll","getIndex","addAll","append","multAll","getIndex","getIndex","getIndex"]
# [[],[2],[3],[7],[2],[0],[3],[10],[2],[0],[1],[2]]

obj.append(2)
obj.addAll(3)  
obj.append(7)
obj.multAll(2)
print(obj.getIndex(0))  # 20
obj.addAll(3)
obj.append(10)  
obj.multAll(2)
print(obj.getIndex(0))  # 46
print(obj.getIndex(1))  # 26
print(obj.getIndex(2))  # 20

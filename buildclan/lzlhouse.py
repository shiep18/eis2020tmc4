#!/usr/bin/python3
#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Autor:ZLL
import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create('47.100.46.95',4784)
p=46
class House():
    def __init__(self,name,x,y,z,l,w,h):
        self.name=name
        self.x=int(x)
        self.y=int(y)
        self.z=int(z)
        self.l=int(l)
        self.w=int(w)
        self.h=int(h)

    def SetHouse(self):#(x,y,z).............
        for X in range(0,self.l):
            for Z in range(0,self.w):
                mc.setBlock(self.x + X, self.y, self.z + Z, p)# ..
                mc.setBlock(self.x + X, self.y + self.h-1, self.z + Z, p)#..
        for Y in range(1, self.h-1):
            for X in range(0,self.l):
                mc.setBlock(self.x + X, self.y + Y, self.z,p)
                mc.setBlock(self.x + X, self.y + Y, self.z + self.w-1, p)
            for Z in range(1, self.w-1):
                mc.setBlock(self.x,self.y + Y,self.z + Z, p)
                mc.setBlock(self.x + self.l -1, self.y + Y, self.z + Z, p)
        mc.setBlock(self.x + int(self.l / 2) - 1, self.y + 1, self.z,0)
        mc.setBlock(self.x + int(self.l / 2) - 1, self.y + 2, self.z, 0)
        mc.setBlock(self.x + int(self.l / 2), self.y + 1, self.z, 0)
        mc.setBlock(self.x + int(self.l / 2), self.y + 2, self.z, 0)
        Lx = [1, self.l - 2]
        Ly = [1, self.h - 2]
        Lz = [1, self.w - 2]
        for i in Lx:
            for j in Ly:
                for k in Lz:
                    mc.setBlock(self.x + i, self.y + j, self.z + k, 86)

    def InsideHouse(self,a,b,c):
        if a>self.x and a<self.x+self.l-1 and b>self.y and b<self.y+self.h-1 and c>self.z and c< self.z+self.w-1:
            mc.postToChat("You are in %s's house" % self.name)
            return True
        else:
            pass
        return False
    
    def getHouseMessage(self):
        print('housename:%s,x:%d,y:%d,z:%d,length:%d,width:%d,high:%d'%(self.name,self.x,self.y,self.z,self.l,self.w,self.h))

    def SetLight(self,flag):
        if not flag:
            light=86
        else:
            light=91
        Lx = [1, self.l - 2]
        Ly = [1, self.h - 2]
        Lz = [1, self.w - 2]
        for i in Lx:
            for j in Ly:
                for k in Lz:
                    mc.setBlock(self.x + i, self.y + j, self.z + k, light)
if __name__=='__main__':
    house1=House('BigHouse1',-174,-39,-54,10,10,10)
    house1.SetHouse()









import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create('47.100.46.95',4784)

fname = "info.csv"
f = open(fname, "r")
for line in f.readlines():
    data = line.split(",")
    for cell in data:
        if cell == "clancenter":
            center_x=data[1]
            center_y=data[2]
            center_z=data[3]
        elif cell == "wwz":
            offset_x=data[1]
            offset_y=data[2]
            offset_z=data[3]
x=int(center_x)+int(offset_x)
y=int(center_y)+int(offset_y)
z=int(center_z)+int(offset_z)


mc.setBlocks(x,y,z,x+9,y+9,z+9,45)
mc.setBlocks(x+1,y+1,z+1,x+8,y+8,z+8,0)
mc.setBlocks(x+3,y+1,z,x+5,y+5,z,0)
mc.setBlocks(x+3,y+6,z+9,x+6,y+7,z+9,20)
mc.setBlocks(x,y+9,z,x+9,y+9,z+9,89)

print("2020.5.11")

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
        elif cell == "zyt":
            offset_x=data[1]
            offset_y=data[2]
            offset_z=data[3]
x=int(center_x)+int(offset_x)
y=int(center_y)+int(offset_y)
z=int(center_z)+int(offset_z)
def build(xo=0, yo=0, zo=0, L=10, W=10, H=10, M=1):

    mc.setBlocks(xo,yo,zo,xo+L,yo+H,zo+W,1)
    mc.setBlocks(xo+1,yo+1,zo+1,xo+L-1,yo+H-1,zo+W-1,5)
    mc.setBlocks(xo+L/2,yo+1,zo,xo+L/2,yo+2,zo,5)




build(x, y, z)


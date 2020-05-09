import binvox_rw
import mcpi.minecraft as minecraft
import mcpi.block as block

mc=minecraft.Minecraft.create('47.100.46.95',4784)

fname = "stl.csv"
f = open(fname, "r")
for line in f.readlines():
    data = line.split(",")
    for cell in data:
        if cell == "clancenter":
            center_x=data[1]
            center_y=data[2]
            center_z=data[3]
        elif cell == "jsj":
            offset_x=data[1]
            offset_y=data[2]
            offset_z=data[3]
x0=int(center_x)+int(offset_x)
y0=int(center_y)+int(offset_y)
z0=int(center_z)+int(offset_z)


with open('mylogo.binvox', 'rb') as f:
    model = binvox_rw.read_as_3d_array(f)
print(model.dims)
print(model.scale)
print(model.translate)
#print(model.data)

for y in range(model.dims[1]):
    print("layer y=",y)
    layer_data=model.data[y]
    stringlayer=""
    for x in range(model.dims[0]):
        stringlayer=stringlayer+"\n"
        for z in range(model.dims[2]):
            if model.data[x][y][z] == True:
                stringlayer=stringlayer+'1'
                mc.setBlock(x0+x,y0+y,z0+z,block.STONE.id)
            else:
                stringlayer=stringlayer+'0'
                mc.setBlock(x0+x,y0+y,z0+z,block.AIR.id)

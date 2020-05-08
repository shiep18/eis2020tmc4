import os
import mcpi.minecraft as minecraft
import mcpi.block as block
import csv
import time
member=["wyb","jsj","zyt","wwz","lzl","thd"]
for i in range(6):
    if os.path.exists(member[i]+"house.py"):
        os.system("E:/Python/python.exe "+member[i]+"house.py")
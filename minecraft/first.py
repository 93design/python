from mcpi import minecraft
from mcpi import block
from time import sleep


mc = minecraft.Minecraft.create()

mc.postToChat("hallo world")

flower = 38
grass = 2

while True:
    x, y, z = mc.player.getPos()
    block_beneath = mc.getBlock(x,y-1,z)
    print(block_beneath)
   
    if block_beneath == grass:
        mc.setBlock(x,y,z,flower)
    else: 
        mc.setBlock(x,y-1,z,grass)
    sleep(0.1)
    
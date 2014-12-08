import mcpi.minecraft as minecraft,time as t
mc = minecraft.Minecraft.create()

#move player close to origin
mc.player.setPos(0,10,-1)

Black=7
red=14
orange=1
green=5

#setup empty lights
mc.setBlock(0,0,0,35,Black)
mc.setBlock(0,1,0,35,Black)
mc.setBlock(0,2,0,35,Black)
mc.setBlock(0,3,0,35,Black)
mc.setBlock(0,4,0,35,Black)
mc.setBlock(0,5,0,35,Black)


#sequence
mc.setBlock(0,5,0,35,red)
time.sleep(5)
mc.setBlock(0,4,0,35,orange)

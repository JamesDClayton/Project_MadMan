from panda3d.core import *
from panda3d.core import loadPrcFile
if __debug__:
        loadPrcFile("config/config.prc")
from math import pi, sin, cos
 
from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class MadManDungeon(ShowBase):
    def __init__(self):
        #initial setup
        ShowBase.__init__(self)
        #world background
        self.win.setClearColor((0,0,0,1))

        #load the world map
        self.environ = loader.loadModel("models/dungeon")
        self.environ.reparentTo(render)

        #################################################
        #                 Lights                        #
        #################################################

        #ambient
        #ambient = AmbientLight('ambient')
        #ambient.setColor((.1,.1,.1,1))
        #amb = render.attachNewNode(ambient)
        #render.setLight(amb)

        #pointlights
        pointlight1 = PointLight('pointlight1')
        pointlight2 = PointLight('pointlight2')
        pointlight3 = PointLight('pointlight3')
        pointlight4 = PointLight('pointlight4')
        pointlight5 = PointLight('pointlight5')
 


        
        pointlight1.setColor((.4,.4,.4,1))
        pointlight2.setColor((.4,.4,.4,1))
        pointlight3.setColor((.4,.4,.4,1))
        pointlight4.setColor((.4,.4,.4,1))
        pointlight5.setColor((.4,.4,.4,1))

        
        pl1 = render.attachNewNode(pointlight1)
        pl2 = render.attachNewNode(pointlight2)
        pl3 = render.attachNewNode(pointlight3)
        pl4 = render.attachNewNode(pointlight4)
        pl5 = render.attachNewNode(pointlight5)

        
        pl1.setPos(render.find("**/Pot").getPos())
        pl2.setPos(render.find("**/Pot.004").getPos())
        pl3.setPos(render.find("**/Pot.002").getPos())
        pl4.setPos(0,0,26)
        pl5.setPos(-182,-34,26)

        
        
        render.setLight(pl1)
        render.setLight(pl2)
        render.setLight(pl3)
        render.setLight(pl4)
        render.setLight(pl5)

        
        # Use a 512x512 resolution shadow map
        pointlight1.setShadowCaster(True, 512, 512)
        # Enable the shader generator for the receiving nodes
        render.setShaderAuto()
app = MadManDungeon()
app.run()

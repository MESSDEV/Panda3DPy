class Mapmanager():
   """Map management"""
   def __init__(self):
       self.model = 'block' # the cube model is in the block.egg file
       # # the following textures are used:
       self.texture = 'block.png'         
       self.colors = [
           (0.2, 0.2, 0.35, 1),
           (0.2, 0.5, 0.2, 1),
           (0.7, 0.2, 0.2, 1),
           (0.5, 0.3, 0.0, 1)
       ] #rgba
       # create the main map node:
       self.startNew()
       # self.addBlock((0,10, 0))


   def startNew(self):
       """creates the basis for the new map"""
       self .land = render.attachNewNode ( "Land" ) #the node which all the map blocks are attached to


   def getColor(self, z):
       if z < len(self.colors):
           return self.colors[z]
       else:
           return self.colors[len(self.colors) - 1]


   def addBlock(self, position):
       # create building blocks
       self.block = loader.loadModel(self.model)
       self.block.setTexture(loader.loadTexture(self.texture))
       self.block.setPos(position)
       self.color = self.getColor(int(position[2]))
       self.block.setColor(self.color)
       self.block.reparentTo(self.land)


   def clear(self):
       "" "resets the map" ""
       self.land.removeNode()
       self.startNew()


   def loadLand(self, filename):
       "" "creates a land map from a text file, returns its dimensions" ""
       self.clear()
       with open(filename) as file:
           y = 0
           for line in file:
               x = 0
               line = line.split(' ')
               for z in line:
                   for z0 in range(int(z)+1):
                       block = self.addBlock((x, y, z0))
                   x += 1
               y += 1

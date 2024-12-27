from kivy.uix.gesturesurface import Line
from kivy.uix.behaviors.touchripple import Color
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.effectwidget import Rectangle
import random

gridWidth = 16
gridHeight = 25

objectList = [[[int(gridWidth/2),gridHeight-1],[int(gridWidth/2),gridHeight-2],[int(gridWidth/2),gridHeight-3],[int(gridWidth/2),gridHeight-4]], # straight line
[[int(gridWidth/2),gridHeight-1],[int(gridWidth/2),gridHeight-2],[int(gridWidth/2),gridHeight-3],[int(gridWidth/2)-1,gridHeight-3]], # L left
[[int(gridWidth/2),gridHeight-1],[int(gridWidth/2),gridHeight-2],[int(gridWidth/2)-1,gridHeight-2],[int(gridWidth/2)-1,gridHeight-1]], # square
[[int(gridWidth/2),gridHeight-1],[int(gridWidth/2),gridHeight-2],[int(gridWidth/2)+1,gridHeight-2],[int(gridWidth/2)+1,gridHeight-3]], # rotated z
[[int(gridWidth/2),gridHeight-1],[int(gridWidth/2),gridHeight-2],[int(gridWidth/2)+1,gridHeight-2],[int(gridWidth/2)+1,gridHeight-3]], # rotated s
[[int(gridWidth/2),gridHeight-1],[int(gridWidth/2),gridHeight-2],[int(gridWidth/2),gridHeight-3],[int(gridWidth/2)+1,gridHeight-3]], # L right
[[int(gridWidth/2),gridHeight-1],[int(gridWidth/2),gridHeight-2],[int(gridWidth/2),gridHeight-3],[int(gridWidth/2)-1,gridHeight-2]]] # T

# the class of the main grid
class MainGrid(GridLayout):
    def setup(self):
        self.gameGrid = []
        self.moveTiles = []
        self.staticTiles = []
        for i in range(gridHeight):
            self.gameGrid.append([])
            for j in range(gridWidth):
                self.gameGrid[i].append(0)
        self.changeSize()
        self.spawnObject()
        self.clockEvent = Clock.schedule_interval(self.update, 1)
    def changeSize(self):
        self.sizeTile = self.size[1] / (gridHeight + gridHeight/5)
    def draw(self):
        self.ids.tetrisCanvas.canvas.clear()
        for i in range(gridHeight - 1):
            # drawing the horizontal grid lines
            self.ids.tetrisCanvas.canvas.add(Color(rgba=(0, 0, 0, 1)))
            self.ids.tetrisCanvas.canvas.add(Line(points=[self.size[0]/2-gridWidth*self.sizeTile/2, i*self.sizeTile, self.size[0]/2+gridWidth*self.sizeTile/2, i*self.sizeTile]))
            for j in range(gridWidth):
                # drawing the vertical grid lines
                self.ids.tetrisCanvas.canvas.add(Color(rgba=(0, 0, 0, 1)))
                self.ids.tetrisCanvas.canvas.add(Line(points=[j*self.sizeTile+self.size[0]/2-gridWidth*self.sizeTile/2, 0, j*self.sizeTile+self.size[0]/2-gridWidth*self.sizeTile/2, gridHeight*self.sizeTile]))
                # drawing the tiles
                if self.gameGrid[i][j] == 0:
                    self.ids.tetrisCanvas.canvas.add(Color(rgba=(1, 1, 1, 1)))
                    self.ids.tetrisCanvas.canvas.add(Rectangle(pos=(j*self.sizeTile+self.size[0]/2-self.sizeTile*gridWidth/2, i*self.sizeTile), size = (self.sizeTile, self.sizeTile)))
                else:
                    self.ids.tetrisCanvas.canvas.add(Color(rgba=(1, 0, 0, 1)))
                    self.ids.tetrisCanvas.canvas.add(Rectangle(pos=(j*self.sizeTile+self.size[0]/2-self.sizeTile*gridWidth/2, i*self.sizeTile), size =(self.sizeTile, self.sizeTile)))
    def spawnObject(self):
        if len(self.moveTiles) == 0:
            self.choice = random.choice(objectList)
            #print(self.choice)
            for tile in self.choice:
                #print(tile[1])
                #print(tile[0])
                #print(len(self.gameGrid))
                if self.gameGrid[tile[1]][tile[0]] == 1:
                    self.gameOver()
                    break
            for tile in self.choice:
                self.moveTiles.append([tile[1], tile[0]]) # I somehow managed to the tiles in reverse order, however it should still work
                self.gameGrid[tile[1]][tile[0]] = 1
    def gameOver(self):
        self.clockEvent.cancel()
        print("game over")
    def update(self, dt):
        self.move()
        self.draw()
        self.spawnObject()
        self.checkLines()
    def move(self):
        #print(self.moveTiles)
        for i in range(gridHeight):
            for j in range(gridWidth):
                if self.gameGrid[i][j] == 1 and [i, j] in self.moveTiles:
                    if i <= 0 or [i-1, j] in self.staticTiles:
                        for tile in self.moveTiles:
                            self.staticTiles.append(tile)
                            print(self.staticTiles)
                        self.moveTiles = []
        for i in range(gridHeight):
            for j in range(gridWidth):
                #if self.gameGrid[i][j] == 1:
                #    print(str([i, j]) + " is the tile")
                #    print("this condition works")
                #if [i, j] in self.moveTiles:
                    #print("this condition also works ----------------")
                if self.gameGrid[i][j] == 1 and [i, j] in self.moveTiles:
                    #print("works here")
                    if [i-1, j] not in self.staticTiles:
                        self.gameGrid[i][j] = 0
                        self.gameGrid[i-1][j] = 1
                        self.moveTiles.remove([i, j])
                        self.moveTiles.append([i-1, j])
        #print(self.gameGrid)
    def checkLines(self):
        for i in range(gridHeight):
            if 0 not in self.gameGrid[i]:
                self.gameGrid.pop(i)
                self.gameGrid.insert(0, [0 for i in range(gridWidth)])
                print("line removed")
    def settings(self):
        print("settings")

# the app class
class TetrisApp(App):
    def build(self):
        return MainGrid()
    
# running the app
if __name__ == '__main__':
    TetrisApp().run()
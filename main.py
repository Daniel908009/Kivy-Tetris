from kivy.uix.behaviors.touchripple import Color
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.effectwidget import Rectangle

gridWidth = 15
gridHeight = 25

# the class of the main grid
class MainGrid(GridLayout):
    def setup(self):
        print("setup")
        self.gameGrid = []
        for i in range(gridHeight):
            self.gameGrid.append([])
            for j in range(gridWidth):
                self.gameGrid[i].append(0)
        self.changeSize()
        # this is just for testing
        self.gameGrid[0][0] = 1
        self.gameGrid[2][2] = 1
        self.clockEvent = Clock.schedule_interval(self.update, 1)
    def changeSize(self):
        self.sizeTile = self.size[1] / (gridHeight + gridHeight/5)
        print("size changed to", self.sizeTile)
    def draw(self):
        print("draw")
        self.ids.tetrisCanvas.canvas.clear()
        for i in range(gridHeight):
            for j in range(gridWidth):
                if self.gameGrid[i][j] == 0:
                    #print("drawing white")
                    self.ids.tetrisCanvas.canvas.add(Color(rgba=(1, 1, 1, 1)))
                    self.ids.tetrisCanvas.canvas.add(Rectangle(pos=(j*self.sizeTile+self.size[0]/2-self.sizeTile*gridWidth/2, i*self.sizeTile), size = (self.sizeTile, self.sizeTile)))
                else:
                    print("drawing red")
                    self.ids.tetrisCanvas.canvas.add(Color(rgba=(1, 0, 0, 1)))
                    self.ids.tetrisCanvas.canvas.add(Rectangle(pos=(j*self.sizeTile+self.size[0]/2-self.sizeTile*gridWidth/2, i*self.sizeTile), size =(self.sizeTile, self.sizeTile)))
    def update(self, dt):
        #print("update")
        # some moving logic will be here
        self.draw()
    def settings(self):
        print("settings")

# the app class
class TetrisApp(App):
    def build(self):
        return MainGrid()
    
# running the app
if __name__ == '__main__':
    TetrisApp().run()
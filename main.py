from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.clock import Clock
from kivy.uix.effectwidget import Rectangle

# the class of the main grid
class MainGrid(GridLayout):
    def setup(self):
        print("setup")
        self.gameGrid = []
        for i in range(30):
            self.gameGrid.append([])
            for j in range(10):
                self.gameGrid[i].append(0)
    def draw(self):
        print("draw")
        self.ids.tetrisCanvas.canvas.clear()
        #self.ids.tetrisCanvas.canvas.add(Rectangle(pos=(0,0), size=(100,100)))
    def start(self):
        print("start")
        self.clockEvent = Clock.schedule_interval(self.update, 1)
    def update(self, dt):
        print("update")
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
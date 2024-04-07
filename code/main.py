import pyxel

class App :
    def __init__(self) -> None:
        pyxel.init(200,200,title="Jeu des triangle")
        pyxel.run(self.update,self.draw)
    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q):
            quit()
    def draw(self) :
        pyxel.cls(0)
        texte : str = "Bienvennu dans le jeu des triagles"
        pyxel.text(34,35,texte,pyxel.frame_count % 16)
        
App()
import pyxel
class English :
    def draw(self):
        pyxel.cls(0)
        pyxel.text(55,60,"Tape E to play in english",pyxel.frame_count % 16)
class French :
    def draw(self):
        pyxel.cls(0)
        pyxel.text(70,80,"F pour jouer en français.",pyxel.frame_count % 16)
class App :
    def __init__(self) -> None:
        pyxel.init(200,200,title="Jeu des triangle")
        pyxel.run(self.update,self.draw)
    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q):
            quit()
#TODO : faire en sorte que quand on clique sur E ou F, ça amène vers un autre écran
        elif pyxel.btnp(pyxel.KEY_E):
            English()
        elif pyxel.btnp(pyxel.KEY_F):
            French()
    def draw(self) :
        pyxel.cls(0)
        pyxel.text(34,35,"Tape E to play in english",pyxel.frame_count % 16)
        pyxel.text(40,45,"F pour jouer en français.",pyxel.frame_count % 16)
        
App()
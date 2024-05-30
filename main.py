import pyxel

class English :
    def __init__(self) -> None:
        pyxel.run(self.update, self.draw)

    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q):
            quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(40,80,"Welcome to the triangle game!!", pyxel.frame_count % 16)



class French :
    def __init__(self) -> None:
        pyxel.run(self.update, self.draw)

    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q):
            quit()

    def draw(self):
        pyxel.cls(0)
        pyxel.text(30,80,"Bienvenue sur le jeu des triangles!!", pyxel.frame_count % 16)




class App :
    def __init__(self) -> None:
        pyxel.init(200,200,title="Jeu des triangles")
        pyxel.run(self.update, self.draw)

    def update(self) :
        if pyxel.btnp(pyxel.KEY_Q):
            quit()
            
#TODO : faire en sorte que quand on clique sur E ou F, ça amène vers un autre écran
#DID IT :D -Ines
        elif pyxel.btnp(pyxel.KEY_E):
            English()
        elif pyxel.btnp(pyxel.KEY_F):
            French()

    def draw(self) :
        pyxel.cls(0)
        pyxel.text(44,35,"Press E to play in English",pyxel.frame_count % 16)
        pyxel.text(40,45,"Tapez F pour jouer en Francais",pyxel.frame_count % 16)
        
App()
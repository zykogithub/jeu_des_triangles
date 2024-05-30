import pyxel

class Penta :
    def __init__(self,cote : int) -> None:
        self.cote : int =cote
class Rect (Penta) :
    def __init__(self) -> None:
        super.__init__(4)
class Tri (Rect):
    def __init__(self) -> None:
        super().__init__(3)
# TODO : faire update et draw pour chaque forme
# TODO : dans le moule jeu, caster d'une classe à l'autre en cas de toucher
# TODO : permettre de savoir qui attaque et qui défend, vrai question
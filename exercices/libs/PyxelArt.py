from PIL import Image, ImageDraw, ImageFont
import sys
import inspect

class PyxelArt :
    
    def __init__(self, w, h, s=20):
        self.w = w
        self.h = h
        self.s = s
        self.i = 1
        self.l = False
        self.correctionDetaille = False # Mettre a True pour une correction détaillée (numéro de ligne du programme coloriant la case)
        self.lines = []
        self.font = ImageFont.truetype("../ressources/font/LiberationMono-Bold.ttf", self.s)
        self.font = ImageFont.truetype("../ressources/font/LiberationMono-Bold.ttf", int(self.s*0.75))
        self.output = Image.new('RGB', ((w+1)*(self.s+1), (h+1)*(self.s+1)), (255,255,255))
        self.draw = ImageDraw.Draw(self.output)
        for x in range(0,w+1) :
            self.draw.line([
                (x+1)*(self.s+1)-1,
                0,
                (x+1)*(self.s+1)-1,
                (h+1)*(self.s+1)
            ], fill=(0,0,0))
        for x in range(0,w) :
            self.draw.text(((x+2)*(self.s+1)-1-self.s/2,self.s/2), str(x), fill=(0, 0, 0), anchor="mm", font=self.font)
        for y in range(0,h+1) :
            self.draw.line([
                0,
                (y+1)*(self.s+1)-1,  
                (w+1)*(self.s+1),
                (y+1)*(self.s+1)-1
            ], fill=(0,0,0))
        for y in range(0,h) :
            self.draw.text((self.s/2,(y+2)*(self.s+1)-1-self.s/2), str(y), fill=(0, 0, 0), anchor="mm", font=self.font)
        if self.correctionDetaille :
            with open(sys.argv[0], 'rb') as c:
                    code = c.readlines()
                    longueur = len(code)
                    code = code[1:] # on retire la première (import)
                    while code[0] == '' or code[0] == b'\r\n' or code[0] == b'\n' :
                        code = code [1:]
                    self.shift = longueur-len(code)
    def colorier(self, x, y) :
        if self.correctionDetaille :
            line = inspect.currentframe().f_back.f_lineno
            if not line in self.lines :
                self.lines.append(line)
            color = 'hsl(%d, 100%%, 75%%)' % (int(self.lines.index(line)/15*360))
        else :
            color = (150, 150, 150)
        self.draw.rectangle([
            (x+1)*(self.s+1),
            (y+1)*(self.s+1),
            (x+1)*(self.s+1)+self.s-1,
            (y+1)*(self.s+1)+self.s-1
        ], fill=color)
        if self.correctionDetaille :
            self.draw.text(((x+1.5)*(self.s+1),(y+1.5)*(self.s+1)), str(line-self.shift), fill=(0, 0, 0), anchor="mm", font=self.font)
    def show(self) :
        if __file__.split('\\')[0] in ('generer_moodle.py', 'generer_pronote.py') : return
        self.output.show()
        
    def save(self, name=None) :
        if __file__.split('\\')[0] in ('generer_moodle.py', 'generer_pronote.py') : return
        if name == None :
            name = sys.argv[0].split('.')[0].replace('\\','/').split('/')[-1]
        if self.correctionDetaille :
            self.output.save("corrections/" + str(name) + "_cd.png")
        else :
            self.output.save("corrections/" + str(name) + ".png")
        
    def ss(self, name=None) :
        self.save(name)
        self.show()
        
        
pa = PyxelArt(9,9)

for f in [f for f in dir(PyxelArt) if not f.startswith('_')] :
    globals()[f] = getattr(pa, f)
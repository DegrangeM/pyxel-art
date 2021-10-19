from PIL import Image, ImageDraw, ImageFont
import sys

class PyxelArt :
    
    def __init__(self, w, h, s=20):
        self.w = w
        self.h = h
        self.s = s
        self.i = 1
        self.l = False
        self.step = False
        self.font = ImageFont.truetype("../ressources/font/LiberationMono-Bold.ttf", self.s)
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
    def colorier(self, x, y) :
        self.draw.rectangle([
            (x+1)*(self.s+1),
            (y+1)*(self.s+1),
            (x+1)*(self.s+1)+self.s-1,
            (y+1)*(self.s+1)+self.s-1
        ], fill=(150,150,150))
    def show(self) :
        if __file__.split('\\')[0] in ('generer_moodle.py', 'generer_pronote.py') : return
        self.output.show()
        
    def save(self, name=None) :
        if __file__.split('\\')[0] in ('generer_moodle.py', 'generer_pronote.py') : return
        if name == None :
            name = sys.argv[0].split('.')[0].replace('\\','/').split('/')[-1]
        self.output.save("corrections/" + str(name) + ".png")
        
    def ss(self, name=None) :
        self.save(name)
        self.show()
        
        
pa = PyxelArt(9,9)

for f in [f for f in dir(PyxelArt) if not f.startswith('_')] :
    globals()[f] = getattr(pa, f)
from skimage import novice,data
class MyPic():
    def __init__(self,filename):
        self.pic = novice.open(data.data_dir + "/" + filename)
    def threshold(self,p):
        if p > 255:
            return 255
        else:
            return int(p)
    def show(self):
        self.pic.show()
    def sum(self):
        (r,g,b,a) = (0,0,0,0)
        for p in self.pic:
            r += p.red
            g += p.green
            b += p.blue
            a += p.alpha
        return (r,g,b,a)
    def grey(self):
        for p in self.pic:
            (r,g,b) = (p.red, p.green, p.blue)
            grey = self.threshold((r+g+b)/3)
            (p.red, p.green, p.blue) = (grey,grey,grey)
    def bluered(self):
        for y in range(self.pic.height):
            for x in range(self.pic.width):
                if x < self.pic.width // 2:
                    self.pic[x,y].blue = 255
                else:
                    self.pic[x,y].red = 255
    def sepia(self):
        for p in self.pic:
            (r,g,b) = (p.red,p.green,p.blue)
            p.red = self.threshold(r * .393 + g *.769 + b * .189)
            p.green = r * .349 + g *.686 + b * .168
            p.blue = r * .272 + g *.534 + b * .131


pic = MyPic("chelsea.png")
pic.sepia()
pic.show()

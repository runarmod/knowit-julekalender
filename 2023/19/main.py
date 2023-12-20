farger = """#61FA11
#575947
#6E41C1
#0CD1AD
#F0C38B
#C9D2E0
#F515A7
#7E662A
#0189DA
#CBA3C2
#2FCDAA
#E5E81E
#E06162
#5176F2
#7D99B6""".split(
    "\n"
)

farger = open("kuler.txt").read().strip().split("\n")


class Kule:
    def __init__(self, hex):
        self.hex = hex
        self.dec = int(hex[1:], 16)
        self.left = None
        self.right = None
        self.parent = None

    def set_parent(self, parent):
        self.parent = parent

    def __le__(self, other):
        return self.dec <= other.dec

    def place_child(self, child):
        if child <= self:
            if self.left:
                self.left.place_child(child)
            else:
                self.left = child
                child.set_parent(self)
        else:
            if self.right:
                self.right.place_child(child)
            else:
                self.right = child
                child.set_parent(self)


root = Kule(farger[0])
halvor = None
alvhild = None
favorites = ["#811A89", "#8EAA54"]

for line in farger[1:]:
    kule = Kule(line)
    if line == favorites[0]:
        halvor = kule
    elif line == favorites[1]:
        alvhild = kule
    root.place_child(kule)
    
halvor_parents = []
alvhild_parents = []
while halvor.parent:
    halvor_parents.append(halvor.parent)
    halvor = halvor.parent
while alvhild.parent:
    alvhild_parents.append(alvhild.parent)
    alvhild = alvhild.parent
    
for parent in halvor_parents:
    if parent in alvhild_parents:
        print("Felles forelder:", parent.hex)
        break

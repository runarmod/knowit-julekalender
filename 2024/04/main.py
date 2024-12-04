import numpy as np
from PIL import Image

Image.fromarray((np.array(Image.open("santa.png")) & 1) * 255).save("solution.png")
print("HAMAR JULEBRUS ER HELT OK")

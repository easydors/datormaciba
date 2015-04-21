# Fails bilde.py
# Autors: Artis Erglis

import numpy, Image

masivs = numpy.random.rand(300,300,3) * 255
bilde = Image.fromarray(masivs.astype('uint8')).convert('RGBA')
bilde.save('bilde.png')

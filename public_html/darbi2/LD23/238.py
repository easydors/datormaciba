# Fails 238.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
bilde= Image("9x9", "#E65555")

# Izgatavojam mainiigos x un y
x=y=0

for i in range(1,7):
    bilde.pixelColor(4,i,'#55E696')
for i in range(3,6):
    bilde.pixelColor(i,2,'#55E696')
for i in range(2,7):
    bilde.pixelColor(i,3,'#55E696')
for i in range(2,7):
    bilde.pixelColor(i,0,'#55E696')
for i in range(3,6):
    bilde.pixelColor(i,7,'#55E696')
for i in range(2,5):
    bilde.pixelColor(8,i,'#55E696')
for i in range(2,5):
    bilde.pixelColor(0,i,'#55E696')
for i in range(5,7):
    bilde.pixelColor(i/3,i,'#55E696')
bilde.pixelColor(1,1, '#55E696')
bilde.pixelColor(7,1, '#55E696')
bilde.pixelColor(7,5, '#55E696')
bilde.pixelColor(6,6, '#55E696')

# 9x9 pixles palielina lidz 200x200
bilde.scale("200x200")

# Objektu 'bilde' ieraksta failaa
bilde.write("238.png")

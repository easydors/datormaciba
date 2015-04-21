# Fails: 232.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
# Objekta izmeers 16x16 pixels
bilde=Image("16x16", "#22aaff")

# Izgatavojam mainiigos x un y
x=y=0

bilde.pixelColor(1,15, "#22ff44")
bilde.pixelColor(1,15, "#22ff44")
bilde.pixelColor(1,14
                 , "#22ff44")
bilde.pixelColor(14,15, "#22ff44")
bilde.pixelColor(14,14, "#22ff44")
for i in range (11,15):
    bilde.pixelColor(2,i, "#22ff44")
for i in range (9,12):
    bilde.pixelColor(3,i, "#22ff44")
for i in range (7,10):
    bilde.pixelColor(4,i, "#22ff44")
for i in range (5,8):
    bilde.pixelColor(5,i, "#22ff44")
for i in range (3,6):
    bilde.pixelColor(6,i, "#22ff44")
for i in range (2,4):
    bilde.pixelColor(7,i, "#22ff44")
for i in range (2,4):
    bilde.pixelColor(8,i, "#22ff44")
for i in range (3,6):
    bilde.pixelColor(9,i, "#22ff44")
for i in range (5,8):
    bilde.pixelColor(10,i, "#22ff44")
for i in range (7,10):
    bilde.pixelColor(11,i, "#22ff44")
for i in range (9,12):
    bilde.pixelColor(12,i, "#22ff44")
for i in range (11,15):
    bilde.pixelColor(13,i, "#22ff44")
for i in range (4,12):
    bilde.pixelColor(i,10, "#22ff44")


# 16x16 pixels palielina lidz 300x300
bilde.scale("300x300")

# Objektu 'bilde' ieraksata failaa
bilde.write("232.png")

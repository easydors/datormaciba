# Fails 236.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
bilde= Image("8x8","#B31301")

# Izgatavojam mainiigos x un y
x=y=0

for i in range(0,4):
    bilde.pixelColor(i,1, "#CFFE00")
for i in range(0,4):
    bilde.pixelColor(i,7, "#CFFE00")
for i in range (2,4):
    bilde.pixelColor(i,3,"#CFFE00")
for i in range (2,4):
    bilde.pixelColor(i,5,"#CFFE00")
bilde.pixelColor(4,2, "#CFFE00")
bilde.pixelColor(4,4, "#CFFE00")
bilde.pixelColor(4,6, "#CFFE00")

# 8x8 pixles palielina lidz 200x200
bilde.scale("200x200")

# Objektu 'bilde' ieraksta failaa
bilde.write("236.png")

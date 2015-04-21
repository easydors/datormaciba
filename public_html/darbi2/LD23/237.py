# Fails 237.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
bilde = Image("16x16", "#00FF33")

# Izgatavojam mainiigos x un y
x=y=0

for a in range(0,7):
    bilde.pixelColor(a,8,"#000066")
for a in range(9,16):
    bilde.pixelColor(a,8,"#000066")
for a in range(6,11):
    bilde.pixelColor(9,a,"#FFFF66")
for a in range(6,11):
    bilde.pixelColor(7,a,"#FFFF66")

# 16x16 pixles palielina lidz 200x200
bilde.scale("200x200")

# Objektu 'bilde' ieraksta failaa
bilde.write("237.png")

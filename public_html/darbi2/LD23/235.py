# Fails 235.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
bilde = Image("16x16", "#3A0CC1")

# Izgatavojam mainiigos x un y
x=y=0

for a in range(0,5):
    bilde.pixelColor(8,a,"#0CC170")
for a in range(11,16):
    bilde.pixelColor(8,a,"#0CC170")
for a in range(6,10):
    bilde.pixelColor(a,5,"#E64634")
for a in range(6,10):
    bilde.pixelColor(a,11,"#E64634")
for a in range(5,12):
    bilde.pixelColor(6,a,"#E64634")
for a in range(5,12):
    bilde.pixelColor(10,a,"#E64634")

# 16x16 pixles palielina lidz 200x200
bilde.scale("200x200")

# Objektu 'bilde' ieraksta failaa
bilde.write("235.png")

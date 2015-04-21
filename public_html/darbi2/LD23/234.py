#Fails 234.py
#Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
bilde = Image("16x16", "#A96969")

# Izgatavojam mainiigos x un y
x=y=0

for a in range(0,5):
    bilde.pixelColor(a,8,"#4C3AB6")
for a in range(11,16):
    bilde.pixelColor(a,8,"#4C3AB6")
for a in range(6,11):
    bilde.pixelColor(5,a,"#F9F113")
for a in range(6,11):
    bilde.pixelColor(11,a,"#F9F113")
for a in range(5,12):
    bilde.pixelColor(a,6,"#F9F113")
for a in range(5,12):
    bilde.pixelColor(a,11,"#F9F113")

# 3x3 pixels palielina liidz 200x200
bilde.scale("200x200")

# Objektu 'bilde' ieraksta failaa
bilde.write("234.png")

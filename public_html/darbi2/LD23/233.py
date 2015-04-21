# Fails 233.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
# Objekta izmeers 32x32 pixels
bilde=Image("12x12", "#006699")

# Izgatavojam mainiigos x un y
x=y=0

bilde.pixelColor(1,4,"#22ff44")
bilde.pixelColor(1,5, "#22ff44")
bilde.pixelColor(1,6, "#22ff44")
bilde.pixelColor(1,7, "#22ff44")
bilde.pixelColor(1,8, "#22ff44")
bilde.pixelColor(1,9, "#22ff44")
bilde.pixelColor(2,3, "#22ff44")
bilde.pixelColor(2,6, "#22ff44")
bilde.pixelColor(3,3, "#22ff44")
bilde.pixelColor(3,6, "#22ff44")
bilde.pixelColor(4,3, "#22ff44")
bilde.pixelColor(4,6, "#22ff44")
bilde.pixelColor(5,4, "#22ff44")
bilde.pixelColor(5,5, "#22ff44")
bilde.pixelColor(5,6, "#22ff44")
bilde.pixelColor(5,7, "#22ff44")
bilde.pixelColor(5,8, "#22ff44")
bilde.pixelColor(5,9, "#22ff44")
bilde.pixelColor(7,3, "#22ff44")
bilde.pixelColor(7,4, "#22ff44")
bilde.pixelColor(7,5, "#22ff44")
bilde.pixelColor(7,6, "#22ff44")
bilde.pixelColor(7,7, "#22ff44")
bilde.pixelColor(7,8, "#22ff44")
bilde.pixelColor(7,9, "#22ff44")
bilde.pixelColor(8,3, "#22ff44")
bilde.pixelColor(8,6, "#22ff44")
bilde.pixelColor(8,9, "#22ff44")
bilde.pixelColor(9,3, "#22ff44")
bilde.pixelColor(9,6, "#22ff44")
bilde.pixelColor(9,9, "#22ff44")
bilde.pixelColor(10,3, "#22ff44")
bilde.pixelColor(10,9, "#22ff44")

# 12x12 pixels palielina lidz 300x300
bilde.scale("300x300")

# Objektu 'bilde' ieraksata failaa
bilde.write("233.png")

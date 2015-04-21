# Fails: 231.py
# Autors: Artis Erglis

from PythonMagick import Image

# Izgatavojam jaunu objektu - bilde
# Objekta izmeers 3x3 pixels
bilde = Image ( "3x3", "#22aaff" )

# Izgatavojam mainiigos x un y
x = y = 0

# Uzstaada objekta 'bolde' x,y pixela kraasu
bilde.pixelColor ( x,y, "#eeff22")

# 3x3 pixels palielina lidz 200x200
bilde.scale ( "200x200" )

# Objektu 'bilde' ieraksata failaa
bilde.write ( "231.png" )

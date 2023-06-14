import qrcode as qr

img = qr.make("Hi!")
img.save("imagenes_prueba/hi.jpg")

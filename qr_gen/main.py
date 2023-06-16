from data_management import *

text_qr, name_img, menu_var, go = "", "", "", True

folder, extension = search_data()

print("Hello! Welcome to link/text convert to QRcode")

while go:
    print("If you want create a QR, type 1")
    print("If you want change the save path, type 2")
    print("If you want change the image extension, type 3")
    print("If you want out, type *")
    menu_var = input("--> ")
    go, extension, folder = menu(go, extension, folder, menu_var, text_qr, name_img)

print("Thanks for ussing, see you latter.")

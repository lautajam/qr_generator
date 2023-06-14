from qr_generator import create_qr

text_qr, name_img, folder, extension, menu_var, go = "", "", "img_test", ".jpg", "", True
exts_img = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff']

print("Hello! Welcome to link/text convert to QRcode")

def menu(extension, menu_var, go):
    if menu_var.lower() == "x":
        go = False
    elif menu_var == "1":
        create_qr(text_qr, name_img, folder, extension, go)
    elif menu_var == "2":
        while go:
            print("Please, write a image extension valid:")
            extension = input("--> ")
            if extension in exts_img:
                go = False
        go = True
    return go, extension


while go:
    print("If you want create a QR, type 1")
    print("If you want change the save path, type 2")
    print("If you want change the image extension, type 3")
    print("If you want out, type X")
    menu_var = input("--> ")
    go, extension = menu(extension, menu_var, go)

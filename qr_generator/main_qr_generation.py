from qr_generator import create_qr
import os

text_qr, name_img, folder, extension, menu_var, go = "", "", "img_test", ".jpg", "", True
exts_img = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg', '.tiff']

print("Hello! Welcome to link/text convert to QRcode")

# Call the create_qr, change the path to save the image and change the image extension
def menu(go, extension, folder, menu_var):

    if menu_var.lower() == "x":
        go = False

    # Create the QR
    elif menu_var == "1":
        create_qr(text_qr, name_img, folder, extension, go)
    
    # Check if the folder exist and change the path to save the image
    elif menu_var == "2":
        while go:
            print("Please, type in the path to save the image")
            folder = input("--> ")
            if os.path.exists(folder) == False:
                print("Folder doesn´t exist, plase try again.")
            else:
                go = False
        go = True

    # Check if the extension is qualified (is inside the list) and place the extension as ordered
    elif menu_var == "3":
        while go:
            exten = ""
            for ext in exts_img:
                if ext != exts_img[len(exts_img) - 1]:
                    exten += ext + ", "
                else:
                    exten += ext
            print("(Valid extensions:", exten + ")")
            print("Please, write a image extension valid:")
            extension = input("--> ")
            if extension not in exts_img:
                print("The extension is invalid, plase try again.")
            else:
                go = False
        go = True

    return go, extension, folder

while go:
    print("If you want create a QR, type 1")
    print("If you want change the save path, type 2")
    print("If you want change the image extension, type 3")
    print("If you want out, type X")
    menu_var = input("--> ")
    go, extension, folder = menu(go, extension, folder, menu_var)

print("Thanks for ussing, see you latter.")

from qr_generator import create_qr
import os

text_qr, name_img, menu_var, go = "", "", "", True
exts_img = ['jpg', 'jpeg', 'png', 'gif', 'bmp', 'svg', 'tiff']

# Reads the data.txt and extract the data it contains
def file_lecture ():
    file_data = open("qr_generator\data.txt", "r+")
    lines = file_data.readlines()
    file_data.close()
    lines = [elemento.strip('\n') for elemento in lines]
    return lines

# Call the create_qr, change the path to save the image and change the image extension
def menu(go, extension, folder, menu_var):

    if menu_var == "*":
        go = False

    # Create the QR
    elif menu_var == "1":
        create_qr(text_qr, name_img, folder, extension, go)
    
    # Check if the folder exist and change the path to save the image
    elif menu_var == "2":
        while go:
            print("Your path now is: '" + folder + "'")
            print("If you want out, type *")
            print("Please, type in the path to save the image")
            folder = input("--> ")
            # Check if the folder isn't exist, in this case, the folder is the saved one.
            if os.path.exists(folder) == False and folder != "*":
                print("Folder doesn´t exist, plase try again.")
                folder = file_lecture()[0]
            # Checks if the folder exists, in this case, the extension is the one typed in
            elif os.path.exists(folder) == True and folder != "*":
                lines = file_lecture()
                # Check the folder position in txt
                if lines[0] in exts_img:
                    lines[1] = folder
                else:
                    lines[0] = folder
                file_data = open("qr_generator\data.txt", "w")
                file_data.writelines(folder + "\n" + "." + extension)
                file_data.close()
                go = False
            # Check if * was typed, if so, exit
            else:
                folder = file_lecture()[0]
                go = False

        go = True

    # Check if the extension is qualified (is inside the list) and place the extension as ordered
    elif menu_var == "3":
        while go:
            exten = ""
            # Print the valid extension
            for ext in exts_img:
                if ext != exts_img[len(exts_img) - 1]:
                    exten += ext + ", "
                else:
                    exten += ext
            print("(Valid extensions:", exten + ")")
            print("Your extension now is: '" + extension + "'")
            print("If you want out, type *")
            print("Please, write a image extension valid:")
            extension = input("--> ")
            # Check if the extension is not valid, in this case, the extension is the saved one.
            if extension not in exts_img and extension != "*":
                print("The extension is invalid, plase try again.")
                extension = file_lecture()[1]
            # Check if the extension is valid, in this case, the extension is the typed
            elif extension in exts_img and extension != "*":
                lines = file_lecture()
                # Check the extension position in txt
                if lines[0] in exts_img:
                    lines[0] = extension
                else:
                    lines[1] = extension
                file_data = open("qr_generator\data.txt", "w")
                file_data.writelines(folder + "\n" + "." + extension)
                file_data.close()
                go = False
            # Check if * was typed, if so, exit
            else:
                extension = file_lecture()[1]
                go = False

        go = True

    else:
        print("Please, type a valid character")

    return go, extension, folder

# Checks if the file data.txt exists, if it exists it opens and reads it, if it does not exist it creates it.
def search_data():
    folder = ""
    extension = ""
    # Check if the data.txt file exists
    if os.path.exists("qr_generator\data.txt"):
        lines = file_lecture()
        # Check the extension and folder position in txt
        if lines[0] in exts_img:
            folder = lines[1]
            extension = lines[0]
        else:
            folder = lines[0]
            extension = lines[1]
        print(lines)
    # If data.txt doesn't exists, creates it
    else:
        file_data = open("qr_generator\data.txt", "w")
    # ACA SIGO
    if os.path.exists("qr_generator\QR_folder"):
        folder = "QR_folder"
    else:
        os.mkdir('qr_generator\QR_folder')
        folder = "qr_generator\QR_folder"
    extension = ".jpg"
    file_data.writelines(folder + "\n" + extension)
    file_data.close()
    
    return folder, extension
    
#  MAIN

folder, extension = search_data()

print("Hello! Welcome to link/text convert to QRcode")

while go:
    print("If you want create a QR, type 1")
    print("If you want change the save path, type 2")
    print("If you want change the image extension, type 3")
    print("If you want out, type *")
    menu_var = input("--> ")
    go, extension, folder = menu(go, extension, folder, menu_var)

print("Thanks for ussing, see you latter.")

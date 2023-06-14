import qrcode as qr
import os, time

text_qr, name_img, folder, extension, go = "", "", "img_test", ".jpg", True

# Ask for name and link/text and validate data
def input_data(text_qr, name_img):
        
        max_charqr, max_charname = 2953, 255

        print("Type here your link/text that you want to convert to QRcode: ")
        text_qr = input("--> ")

        # Validates that the data entered does not exceed the allowed limit
        if len(text_qr) > max_charqr:
            print("The link/text exceeds the limit, please write a link/text of less than 2953 characters.")
            while go:
                try:
                  print("Type here your link/text that you want to convert to QRcode:")
                  text_qr = input("--> ")
                  if len(text_qr) <= max_charqr:
                    go = False
                except:
                  print("Something went wrong! Try again")
        go = True

        print("Type here your name that you want to named the QRcode:")
        name_img = input("--> ")

        if len(name_img) > max_charname:
            print("The name exceeds the limit, please write a name of less than 255 characters.")
            while go:
                try:
                  print("Write here your name that you want to named the QRcode:")
                  name_img = input("--> ")
                  if len(name_img) <= max_charname:
                    go = False
                except:
                  print("Something went wrong! Try again")
        go = True
        return text_qr, name_img

# Check that the file has been created
def validate_creation(folder, name_img, extension, go):
        time.sleep(0.1)
        ruta_archivo = os.path.join(folder, name_img + extension)
        if os.path.exists(ruta_archivo):
            go = False
        else:
            True
        return go

# Main
print("Hello! Welcome to link/text convert to QRcode")

while go:
    try:
        text_qr, name_img = input_data(text_qr, name_img)
        img = qr.make(text_qr)
        path = folder + "/" + name_img + extension
        img.save(path)
        go = validate_creation(folder, name_img, extension, go)
    except:
        print("An exception occurred")
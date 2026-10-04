import pywhatkit as pwk

def send_whatsapp(number,image_path,message):

    pwk.sendwhats_image(
        "+91"+number,
        image_path,
        message
    )
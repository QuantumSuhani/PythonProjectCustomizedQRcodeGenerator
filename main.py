import qrcode
from PIL import Image #Image is the class of PIL which is used to manipulate images

qr=qrcode.QRCode(version=1,#it is used acc to  the type of qrcode for short links lower verssion for long links higher version will be used
                 error_correction=qrcode.constants.ERROR_CORRECT_H,#it means if qrcode is damage upto 30% it can be scaned
                 box_size=10,border=4,)#defining the number of borders and size of qrcode
qr.add_data("https://youtube.com/shorts/27FCzUlVQ04")#storing the given data of qr code
qr.make(fit=True)#means if the link is too long for version 1 it will dynamically go for the higher version
img=qr.make_image(fill_color="brown",back_color="pink")
img.save("my.png")

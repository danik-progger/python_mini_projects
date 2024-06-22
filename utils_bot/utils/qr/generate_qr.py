import qrcode

def create_qr(link):
    img = qrcode.make(link)
    img.save("./utils/qr/qr.png")
    
if __name__ == "__main__":
    create_qr("https://www.youtube.com/watch?v=0hydJFMJZcM&ab_channel=МихаилГребенюк")
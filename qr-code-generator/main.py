from flask import Flask, render_template, request
import qrcode
from io import BytesIO
from base64 import b64encode

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def generateQR():
    memory = BytesIO()

    link = request.form.get('link')
    final_img_src = ""
    show_qr = ""

    if link:
        qrcode.make(link).save(memory)

        memory.seek(0)

        final_img_src = "data:image/png;base64," + \
            b64encode(memory.getvalue()).decode('ascii')
        show_qr = "show_qr"

    return render_template('index.html', src=final_img_src, show=show_qr)

if __name__ == '__main__':
    app.run()
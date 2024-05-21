from flask import Flask, render_template, request
from base64 import b64encode
import requests
from io import BytesIO


app = Flask(__name__)


def shorten_url(long_url):
    r = requests.get(f"https://ulvis.net/api.php?url={long_url}")
    if (r.status_code == requests.codes.ok):
        link = r.text
        print("Link shortened", link)
        return link
    else:
        return "Something went wrong"


@app.route('/', methods=['POST'])
def generateLink():
    link = request.form.get('link')
    show = ""

    if link != "":
        link = shorten_url(link)
        show = "show-link"
    print("POST", show)
    return render_template('index.html', link=link, show=show)


if __name__ == '__main__':
    app.run()

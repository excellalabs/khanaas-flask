from flask import render_template
from flask import abort
from api import api

urls = {
    'kirk': 'http://www.khanaas.com/images/kirk.jpg',
    'spock': 'http://www.khanaas.com/images/spock.jpg'
}


def get_image_url_or_404(key):
    key = key.lower()
    if urls.has_key(key):
        return urls[key]
    else:
        abort(404)


@api.route('/')
@api.route('/index')
def home():
    return render_template('home.html',
                           img_url=get_image_url_or_404('kirk'))

@api.route('/<character>/<input_phrase>')
def kirk(character, input_phrase):
    img_url = get_image_url_or_404(character)
    last_char = input_phrase[-1]
    return render_template('khanaas_template.html',
                           img_url=img_url,
                           phrase=(input_phrase + last_char*5))

from flask import Blueprint

from routes.util import POST
from flask import request
import os

FILENAME = 'image.jpg'

blueprint = Blueprint(
    name='images',
    import_name=__name__,
    url_prefix='/images',
)


@blueprint.route('', methods=[POST])
def update_rating():
    if 'file' not in request.files:
        return {'error': 'no file'}
    file = request.files['file']
    # if file.filename != FILENAME:
    #     return {'error': 'you upload wrong file'}
    current_directory = os.getcwd()
    upload_path = os.path.join(current_directory, FILENAME)
    file.save(upload_path)
    return {'messaeg': 'success'}
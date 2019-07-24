from flask import Blueprint

blueprint = Blueprint(
    name='',
    import_name=__name__,
)


@blueprint.route('/')
def home():
    return {
        'data': 'success'
    }

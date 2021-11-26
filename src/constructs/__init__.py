from flask import Blueprint

cst_bp = Blueprint('cst',__name__,template_folder='././templates/',static_folder='././statics/')


from .views import *
import json

from django.shortcuts import render
from growl.external.minify_json import json_minify
from growl.models import model_encode
from growl.models import model_encode_verbose

def error_dict(http_status_code=400):
    error_dict = _response_dict()
    error_dict['error_code'] = 1
    error_dict['error_msg'] = 'Unknown error'
    error_dict['http_status_code'] = http_status_code
    return error_dict

def success_dict(http_status_code=200):
    success_dict = _response_dict()
    success_dict['error_code'] = 0
    success_dict['error_msg'] = ''
    success_dict['http_status_code'] = http_status_code
    return success_dict

def render_json(request, json_values, verbose=False, minify=True):
    http_status = json_values['http_status_code']
    encode = model_encode
    if verbose:
        encode = model_encode_verbose
    json_dumps = json.dumps(json_values, default=encode)

    # minify json for smallest payload
    if minify:
        json_dumps = json_minify(json_dumps)

    context = {}
    context['json'] = json_dumps

    return render(request, 'growl/json.html', context, status=http_status)

###
### PRIVATE
###

def _response_dict():
    response_dict = {}
    response_dict['error_code'] = 0
    response_dict['error_msg'] = ''
    response_dict['http_status_code'] = 200
    return response_dict
from bootstrap import bootstrap
from train import train_inject_skill
from train import train_train_skill
from train import train_cancel_train_skill

def get_error_dict(http_status_code=400):
    error_dict = _get_response_dict()
    error_dict['error_code'] = 1
    error_dict['error_msg'] = 'Unknown error'
    error_dict['http_status_code'] = http_status_code
    return error_dict

def get_success_dict(http_status_code=200):
    success_dict = _response_dict()
    success_dict['error_code'] = 0
    success_dict['error_msg'] = ''
    success_dict['http_status_code'] = http_status_code
    return success_dict

###
### PRIVATE
###

def _get_response_dict(self):
    response_dict = {}
    response_dict['error_code'] = 0
    response_dict['error_msg'] = ''
    response_dict['http_status_code'] = 200
    return response_dict
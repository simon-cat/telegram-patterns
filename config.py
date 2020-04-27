import configparser

def get_param(param_name='', file_name='config.ini'):
    """Get parameter with name"""
    config = configparser.ConfigParser()
    try:
        config.read(file_name)
    except:
        return '0'
    default = config['DEFAULT']
    if param_name != '':
        return default.get(param_name, '0')
    else:
        return ''
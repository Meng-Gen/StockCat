#-*- coding: utf-8 -*-

import os
import json
import logging.config

def setup_logging(default_path='logging.json', default_level=logging.INFO, env_key='LOG_CFG'):
    path = default_path
    value = os.getenv(env_key, None)
    if value:
        path = value
    if os.path.exists(path):
        with open(path, 'rt') as file_handle:
            config = json.load(file_handle)
        logging.config.dictConfig(config)
    else:
        logging.basicConfig(level=default_level)

# app/logging_config.py
import logging
from logging.config import dictConfig

def setup_logging():
    dictConfig({
        'version': 1,
        'disable_existing_loggers': False,
        'formatters': {
            'default': {
                'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            },
        },
        'handlers': {
            'console': {
                'class': 'logging.StreamHandler',
                'formatter': 'default',
                'level': 'INFO',
            },
        },
        'loggers': {
            'app': {
                'level': 'INFO',
                'handlers': ['console'],
            },
        },
    })

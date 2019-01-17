# -*- coding: utf-8 -*-

import logging.handlers
import logging
import os

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
file_handler = logging.handlers.RotatingFileHandler(os.path.abspath('./log_calculator_tests'))
formatter = logging.Formatter(
    "%(asctime)s : func - %(funcName)-16s - %(lineno)-3s line : %(filename)-16s : %(levelname)-6s : %(message)s")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

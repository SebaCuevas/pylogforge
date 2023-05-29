"""
Custom Logger Module

A custom logging module for advanced logging functionality.
Author: Sebastián M. Cuevas
Email: sebastian.cuevas@greatgeek.net
License: MIT
"""

import os
import logging
import threading
import re

# ANSI color codes
BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE = range(8)

# The background is set with 40 plus the number of the color, and the foreground with 30
RESET_SEQ = "\033[0m"
COLOR_SEQ = "\033[1;%dm"


COLORS = {
    'WARNING': YELLOW,
    'INFO': WHITE,
    'DEBUG': BLUE,
    'CRITICAL': MAGENTA,
    'ERROR': RED
}


class LevelFilter(logging.Filter):
    def __init__(self, level):
        self.level = level

    def filter(self, record):
        return record.levelno == self.level


class CustomFormatter(logging.Formatter):
    def __init__(self, msg, use_color=True):
        logging.Formatter.__init__(self, msg)
        self.use_color = use_color

    def format(self, record):
        levelname = record.levelname
        if self.use_color and levelname in COLORS:
            levelname_color = COLOR_SEQ % (30 + COLORS[levelname]) + levelname + RESET_SEQ
            record.levelname = levelname_color

        filename = os.path.basename(record.pathname)
        filename_color = "\033[92m" + filename + "\033[0m"
        lineno_color = "\033[92m" + str(record.lineno) + "\033[0m"
        record.msg = f"{filename_color}:{lineno_color} - {record.getMessage()}"
        record.args = ()
        return logging.Formatter.format(self, record)





class PyLogForge:
    _instance = None
    _lock = threading.Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(PyLogForge, cls).__new__(cls)
        return cls._instance

    def __init__(self, name=None, console_level=logging.DEBUG, file_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.configure_from_env(console_level, file_level)

    def configure_from_env(self, console_level=logging.DEBUG, file_level=logging.INFO):
        console_level = getattr(logging, os.environ.get('LOG_CONSOLE_LEVEL', ''), console_level)
        file_level = getattr(logging, os.environ.get('LOG_FILE_LEVEL', ''), file_level)

        self.logger.setLevel(min(console_level, file_level))

        for handler in self.logger.handlers:
            self.logger.removeHandler(handler)

        console_formatter = CustomFormatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s')
        console_handler = logging.StreamHandler()
        console_handler.setLevel(console_level)
        console_handler.setFormatter(console_formatter)
        self.logger.addHandler(console_handler)

        log_dir = os.environ.get('LOG_DIR')
        if log_dir:
            os.makedirs(log_dir, exist_ok=True)

            if os.environ.get('LOG_SINGLE_FILE', '').lower() == 'true':
                file_handler = logging.FileHandler(os.path.join(log_dir, "app.log"))
                file_handler.setLevel(file_level)
                file_formatter = CleanLevelFormatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s')
                file_handler.setFormatter(file_formatter)
                self.logger.addHandler(file_handler)
            else:
                for level in (logging.DEBUG, logging.INFO, logging.WARNING, logging.ERROR, logging.CRITICAL):
                    if level >= file_level:
                        level_name = logging.getLevelName(level)
                        log_file = os.path.join(log_dir, f"{level_name.lower()}.log")
                        file_handler = logging.FileHandler(log_file)
                        file_handler.setLevel(level)
                        file_handler.addFilter(LevelFilter(level))  # Only log records at the specific level
                        file_formatter = CleanLevelFormatter('[%(asctime)s] %(name)s - %(levelname)s - %(message)s')
                        file_handler.setFormatter(file_formatter)
                        self.logger.addHandler(file_handler)


class CleanLevelFormatter(logging.Formatter):
    color_pattern = re.compile(r'\x1b\[\d{1,2}(;\d{1,2})?m')

    def format(self, record):
        record.levelname = logging.getLevelName(record.levelno)
        record.msg = self.color_pattern.sub('', record.getMessage())
        filename = os.path.basename(record.pathname)
        record.msg = f"{record.msg}"
        record.args = ()
        return super().format(record)

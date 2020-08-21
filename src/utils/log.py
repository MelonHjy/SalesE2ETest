# -*- coding: utf-8 -*-#
import logging.config, logging
import traceback

from config.global_var import g
from src.utils.create_dir import create_log_dir

local = g.root_path + '/config/Logger.conf'
log_dir = create_log_dir()
logging.config.fileConfig(local, defaults={'logdir': log_dir})
_log = logging.getLogger()
logging.getLogger("requests").setLevel(logging.WARNING)


def debug(message, *args, **kwargs):
    # 打印debug级别的日志方法
    logging.debug(message, *args, **kwargs)


def warning(message, *args, **kwargs):
    # 打印warning级别的日志方法
    logging.warning(message, *args, **kwargs)


def info(message, *args, **kwargs):
    # 打印info级别的日志方法
    logging.info(message, *args, **kwargs)


def error(message, *args, **kwargs):
    # 打印error级别的日志方法
    logging.error(message, *args, **kwargs)


def log(level, msg, *args, **kwargs):
    logging.log(level, msg, *args, **kwargs)


def exception(msg, *args):
    logging.exception(msg, *args)


def critical(msg, *args, **kwargs):
    try:
        logging.critical(msg, *args, **kwargs)
    except:
        logging.info("log failed")
        logging.info(traceback.format_exc())

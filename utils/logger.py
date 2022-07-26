# -*- coding: utf-8 -*-
import logging
import os
import socket
import traceback
from logging.handlers import TimedRotatingFileHandler


class Logger:
    def __init__(self, log_name):
        # 创建一个logger
        self.hostname = socket.gethostname()
        self.logger = logging.getLogger(log_name)
        self.logger.setLevel(logging.DEBUG)

        os.makedirs("./log", exist_ok=True)
        logname = "./log/%s.log" % log_name  # 指定输出的日志文件名

        # 创建一个handler，用于写入日志文件 file
        fh = logging.FileHandler(logname, encoding="utf-8")  # 指定utf-8格式编码，避免输出的日志文本乱码
        fh.setLevel(logging.DEBUG)

        # 创建一个handler，用于将日志输出到控制台 console
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # 创建TimedRotatingFileHandler对象,每天生成一个文件 time
        th = TimedRotatingFileHandler(
            filename=logname, when="S", backupCount=3, encoding="utf-8"
        )
        th.suffix = "%Y-%m-%d_%H-%M-%S.log"
        th.setLevel(logging.DEBUG)

        # 定义handler的输出格式
        # formatter = logging.Formatter(
        #     "%(asctime)s-%(name)s-%(levelname)s>> %(message)s"
        # )
        formatter = logging.Formatter(
            "[%(asctime)s] - %(name)s [Line:%(lineno)d] - [%(levelname)s]-[thread:%(thread)s]-[process:%(process)s] > %(message)s"
        )
        fh.setFormatter(formatter)
        ch.setFormatter(formatter)
        th.setFormatter(formatter)

        # 给logger添加handler
        # self.logger.addHandler(fh)
        self.logger.addHandler(ch)
        # self.logger.addHandler(th)

    def debug(self, msg):
        self.logger.log(logging.DEBUG, msg)

    def info(self, msg):
        self.logger.log(logging.INFO, msg)

    def error(
        self,
        msg,
        exc=None,
        send_ding=False,
        env=None,
        log_type=0,
        limit_key=None,
        redis_client=None,
    ):
        if exc:
            exception = "Exception | " + str(traceback.format_exc())
            self.logger.log(logging.ERROR, msg)
            self.logger.log(logging.ERROR, exception)
        else:
            self.logger.log(logging.ERROR, msg)

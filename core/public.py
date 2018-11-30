# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c)  2018/11/30 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""
import redis

class Redis(object):
    """Redis Object"""
    def __init__(self):
        self.client = None # redis client
        self.__init()

    def __connect(self):
        """Connect Reids conn"""

        self.client = redis.StrictRedis(
            host='localhost',
            port=6379,
            password='',
            db=0
        )

    def __init(self):
        """init redis instance 重试三次"""
        try:
            self.__connect()
        except:
            try:
                self.__connect()
            except:
                self.__connect()
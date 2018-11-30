# -*- encoding: utf-8 -*-
"""
    package.module
    ~~~~~~~~~~~~~~

    A brief description goes here.

    :copyright: (c)  2018/11/30 by zwhset.
    :license: OPS, see LICENSE_FILE for more details.
"""
import json

from public import Redis

BUILD_RUNNER_KEY = "BuildRunner"

redis = Redis()

class Build(object):

    def get_build(self, key):
        data = redis.client.hget(BUILD_RUNNER_KEY, key)
        if not data:
            return None
        try:
            return json.loads(data)
        except Exception as e:
            raise ValueError(str(e))

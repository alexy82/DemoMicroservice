# coding=utf-8
import json

import decimal

import datetime


class ExtendedJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, decimal.Decimal):
            return str(obj)
        if isinstance(obj, datetime.datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        if isinstance(obj, datetime.date):
            return obj.strftime('%Y-%m-%d')
        return json.JSONEncoder.default(self, obj)


def json_compact_dumps(params, sort_keys=True):
    return json.dumps(params, separators=(',', ':'), cls=ExtendedJsonEncoder, sort_keys=sort_keys)

import json
from flask import make_response


def convert_to_json(obj):
    return json.dumps(
        obj,
        default=lambda o: o.to_json(),
        ensure_ascii=False,
        indent=4
    )


def output_json(data, code, headers=None):
    res = make_response(convert_to_json(data), code)
    res.headers.extend(headers or {})
    return res

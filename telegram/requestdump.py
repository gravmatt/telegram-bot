from bottle import request, response, HTTPResponse
import json

class RequestDump(object):
    def apply(self, fn, context):
        def _request_dump(*args, **kwargs):
            print json.dumps(json.loads(request.body.read()), indent=4, separators=(',', ': '))
            return fn(*args, **kwargs)
        return _request_dump

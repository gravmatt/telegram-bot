from httplib import HTTPSConnection, HTTPConnection, HTTPException
from urlparse import urlparse
import json


CRLF = '\r\n'
mimetypes = {
    'png': 'image/png',
    'jpg': 'image/jpeg',
    'jpeg': 'image/jpeg',
    'gif': 'image/gif',
    'txt': 'text/plain',
    'html': 'text/html',
    'mp3': 'audio/mpeg',
    'mp4': 'video/mp4'
}
request_timeout = 10
HTTPException = HTTPException


def request(url, method='GET', body='', port=None, headers={}):
    _url = urlparse(url)
    host = _url.netloc.split(':')
    port = port if len(host) < 2 else host[1]
    conn = None
    if(_url.scheme == 'http'):
        port = int(port or 80)
        conn = HTTPConnection(host[0], port, timeout=request_timeout)
    elif(_url.scheme == 'https'):
        port = int(port or 443)
        conn = HTTPSConnection(host[0], port, timeout=request_timeout)
    else:
        raise Exception('Protocol not found. Must be http or https')
    conn.request(method, url, body, headers)
    resp = conn.getresponse()
    reason = resp.reason
    status = resp.status
    data = resp.read()
    conn.close()
    return (status, reason, data)


def multipartFormData(url, data, files=None, headers=None, boundary=None):
    import string
    _boundary = boundary or '-'*20+string.digits+string.ascii_lowercase
    _headers = headers or {}
    _headers['Content-Type'] = 'multipart/form-data; boundary=%s' % _boundary
    l = []
    for k in data:
        l.append('--' + _boundary)
        l.append('Content-Disposition: form-data; name="%s"' % k)
        l.append('')
        l.append(str(data[k]))
    for (name, filename, binary) in files:
        l.append('--' + _boundary)
        l.append('Content-Disposition: form-data; name="%s"; filename="%s"' % (name, filename))
        l.append('Content-Type: %s' % mimetypes[filename.split('.')[-1]])
        l.append('')
        l.append(binary)
    l.append('--' + _boundary + '--')
    payload = CRLF.join(l)
    _headers['Content-Length'] = len(payload)
    return request(url, method='POST', body=payload, headers=_headers)

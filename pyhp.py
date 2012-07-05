import requests
from datetime import datetime
from time import sleep

VERSION = '0.2'


class DummyRequest():
    """If we catch an exception and want to still output."""
    def __init__(self, url, status_code, error):
        self.url = url
        self.status_code = status_code
        self.error = error
        self.headers = {}


def terse_output(request):
    if request.status_code == 200:
        return '.', 'success'
    else:
        return 'X', 'error'

def full_output(request):
    now = datetime.now()


    if request.status_code == 200:
        returncode = 'success'
        error = ''
    else:
        if request.error:
            error = ' - ERROR: {}'.format(request.error)
        else:
            error = ' - ERROR'
        returncode = 'error'

    return "{}: [{}] {}{}".format(
        now.strftime('%Y-%m-%d %H:%M:%S.%f'),
        request.status_code,
        request.url,
        error
    ), returncode

def header_output(request):
    for k, v in request.headers.items():
        yield '    {}: {}'.format(
            k.upper(),
            v
        )

def pyhp(url, interval=None, show_headers=False, terse=False):
    if not interval:
        interval = 1
    while True:
        try:
            request = requests.get(url)
        except requests.exceptions.ConnectionError as e:
            request = DummyRequest(url, 'FAIL', 'Connection failed')
        if terse:
            yield terse_output(request)
        else:
            yield full_output(request)
            if show_headers:
                yield "\n".join([i for i in header_output(request)]), None

        sleep(interval)
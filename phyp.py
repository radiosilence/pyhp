import requests
from datetime import datetime
from time import sleep

def phyp(url, interval=None, show_headers=False):
    if not interval:
        interval = 1

    while True:
        now = datetime.now()
        r = requests.get(url)
        error = ''
        if r.error:
            error = ' ({})'.format(r.error)

        print "{}: [{}] {}{}".format(
            now.strftime('%Y-%m-%d %H:%M:%S.%f'),
            r.status_code,
            url,
            error
        )
        if show_headers:
            for k, v in r.headers.items():
                print '    {}: {}'.format(
                    k.upper(),
                    v
                )
        sleep(interval)
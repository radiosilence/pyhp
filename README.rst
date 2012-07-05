    httping
    =======

    a simple tool to hit websites at a given interval and display
    whether they are up or not.


    Usage:
        httping <url> [-H] [--interval=<seconds>]
        httping -h | --help

    Options:
        -h --help                Show this screen.
        -H --headers             Show the headers returned by each request.
        -i --interval=<seconds>  Time between requests, in seconds. [default: 1]

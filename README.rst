====
pyhp
====

a simple tool to hit websites at a given interval and display whether they are up or not.

:Authors:
    James Cleveland

:Version: 0.2


Installation
============

::

    pip install pyhp


Also available in the AUR_ (for Arch Linux users)

.. _AUR: http://aur.archlinux.org/packages.php?ID=60537

Usage
-----

::

    % pyhp

    Usage:
        pyhp <url> [-H] [--interval=<seconds>]
        pyhp -h | --help

    Options:
        -h --help                Show this screen.
        -H --headers             Show the headers returned by each request.
        -i --interval=<seconds>  Time between requests, in seconds. [default: 1]

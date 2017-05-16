#!/usr/bin/env python
# coding: utf-8
from twisted.internet import reactor


def test():
    print('Yeah, it works!!!')
    reactor.stop()


reactor.callLater(0, test)
reactor.run()

#!/usr/bin/env python
# coding: utf-8
import random

from twisted.internet import reactor
from twisted.web.server import Site
from twisted.web.xmlrpc import XMLRPC

PORT = 8005


class Server(XMLRPC):
    def xmlrpc_random(self):
        return random.random()


reactor.listenTCP(PORT, Site(Server()))
reactor.run()

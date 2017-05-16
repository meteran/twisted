#!/usr/bin/env python
# coding: utf-8

from twisted.internet import reactor
from twisted.internet.protocol import Protocol, Factory, connectionDone

PORT = 8010


class FileStack(Protocol):
    def connectionLost(self, reason=connectionDone):
        pass

    def dataReceived(self, data):
        pass

    def connectionMade(self):
        pass


class ServerFactory(Factory):
    protocol = FileStack


reactor.listenTCP(PORT, ServerFactory())
reactor.run()

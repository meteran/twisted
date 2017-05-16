#!/usr/bin/env python
# coding: utf-8

from twisted.internet import reactor
from twisted.internet.protocol import ClientFactory, Protocol

SERVER = {
    'HOST': "127.0.0.1",
    'PORT': 8000
}


class Client(Protocol):
    def connectionMade(self):
        pass

    def connectionLost(self, reason):
        pass

    def dataReceived(self, data):
        pass


class Factory(ClientFactory):
    protocol = Client


reactor.connectTCP(SERVER['HOST'], SERVER['PORT'], Factory())
reactor.run()

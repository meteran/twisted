#!/usr/bin/env python
# coding: utf-8

from xmlrpclib import Server

from twisted.internet import reactor, threads
from twisted.internet.protocol import ClientFactory, Protocol

SERVER = {
    'HOST': "127.0.0.1",
    'PORT': 8006,
    'ADDRESS_RPC': "http://127.0.0.1:8007"
}


class Client(Protocol):
    def connectionMade(self):
        pass

    def write(self):
        pass

    def connectionLost(self, reason):
        pass

    def dataReceived(self, data):
        pass


class Factory(ClientFactory):
    protocol = Client


reactor.connectTCP(SERVER['HOST'], SERVER['PORT'], Factory())
reactor.run()

#!/usr/bin/python
# coding: utf-8
from twisted.internet import reactor
from twisted.internet.defer import inlineCallbacks
from txmongo import lazyMongoConnectionPool


db = lazyMongoConnectionPool("127.0.0.1", 27017, pool_size=16)
collection = db.twisted.asdf


def res(result):
    print(result)
    reactor.stop()


@inlineCallbacks
def run_me():
    # d = collection.insert({"first document": None}, safe=True)
    # d.addCallback(lambda ignored: reactor.stop())
    result = yield collection.find({}, fields={"_id": 0})
    print(result)
    reactor.stop()
    d = collection.insert(...)
    d.addCallback(res)
    # d.addCallback(res)


reactor.callLater(0, run_me)
reactor.run()
#!/usr/bin/python
# coding: utf-8
from xmlrpclib import Server

ADDRESS = "http://127.0.0.1:8005"

s = Server(ADDRESS)
print s.random()
print s.add(2, 3)
print s.odd(2, 3)
print s.mul(2, 3)
print s.div(2, 3)

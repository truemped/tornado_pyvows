#!/usr/bin/env python
# -*- coding: utf-8 -*-

# tornado-pyvows extensions
# https://github.com/rafaelcaricio/tornado-pyvows

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2011 globo.com rafael@caricio.com


import tornado.web
from tornado.web import RequestHandler

class MainPageHandler(RequestHandler):
    def get(self):
        self.write("Hello, world")

    def post(self):
        self.set_header("Content-Type", "application/json")
        self.write("{\"message\":\"Hello, world\"")

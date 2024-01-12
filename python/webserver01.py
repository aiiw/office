# Create your views here.
#-*- coding: utf-8 -*-
import json

from django.shortcuts import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# import logging
# logging.basicConfig(level=logging.DEBUG)
# from spyne import Application, rpc, ServiceBase,Integer, Unicode
from spyne import Application, rpc, ServiceBase, Unicode
from spyne import Iterable
from spyne.protocol.soap import Soap11
# from spyne.protocol.json import JsonDocument
from spyne.server.django import DjangoApplication


class HelloWorldService(ServiceBase):
    @rpc(Unicode, _returns=Iterable(Unicode))
    def ess_information(ctx, data):
        dic = {"a":1,"b":2}
        return HttpResponse(json.dumps(dic))

application = Application([HelloWorldService],
    tns='spyne.examples.api',
    in_protocol=Soap11(validator='lxml'),
    out_protocol=Soap11()
)

# This module resides in a package in your Django
# project.

information_app = csrf_exempt(DjangoApplication(application))
##############################################################################
#
# Copyright (c) 2009 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""

$Id$
"""
from zope import interface
from zope.schema import getFields
from zojax.persistent.fields.field import Field


class FieldType(type):

    def __new__(cls, name, field, schema, ignoreFields=(), *args, **kw):
        bases = (Field, field)

        cdict = {'__module__': 'zojax.persistent.fields.fields',
                 'description': schema.__doc__}

        if ignoreFields:
            cdict['ignoreFields'] = ignoreFields

        tp = type.__new__(cls, str(name), bases, cdict)
        interface.classImplements(tp, schema)
        return tp

    def __init__(cls, name, field, schema, *args, **kw):
        cls.__schema__ = DataProperty(schema)


class DataProperty(object):

    def __init__(self, schema):
        self.schema = schema

    def __get__(self, inst, klass):
        return self.schema

    def __set__(self, inst, value):
        raise AttributeError("Can't set __schema__")

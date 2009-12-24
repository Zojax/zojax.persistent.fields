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
from persistent import Persistent

from zope import interface
from zope.app.container.contained import Contained
from zope.schema.fieldproperty import FieldProperty

from zojax.content.type.interfaces import IItem
from zojax.persistent.fields.interfaces import IField


class NameProperty(object):

    def __get__(self, inst, klass):
        if inst is None:
            return self

        return str(inst.__dict__['__name__'])

    def __set__(self, inst, value):
        inst.__dict__['__name__'] = value


class Field(Persistent, Contained):
    interface.implements(IField, IItem)

    __name__ = NameProperty()

    ignoreFields = ('missing_value', 'default', 'readonly', 'value_type')

    _data = {}
    def getFieldData(self):
        return dict(self._data)

    def setFieldData(self, data):
        self._data = dict(data)

    def __getattr__(self, attr):
        if attr in self._data:
            return self._data[attr]

        raise AttributeError(attr)

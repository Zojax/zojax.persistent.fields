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
from rwproperty import getproperty, setproperty
from zope import interface, schema
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary
from z3c.schema.email import RFC822MailAddress
from z3c.schema.baseurl.field import isValidBaseURL, BaseURL
from z3c.schema.baseurl.interfaces import InvalidBaseURL

from zojax.richtext.field import RichText
from zojax.widget.list.field import SimpleList
from zojax.widget.radio.field import RadioChoice

from zojax.persistent.fields import interfaces
from zojax.persistent.fields.field import Field
from zojax.persistent.fields.fieldtype import FieldType, DataProperty

import vocabulary


Bool = FieldType(
    'Bool', schema.Bool, interfaces.IBool)

Int = FieldType(
    'Int', schema.Int, interfaces.IInt)

Text = FieldType(
    'Text', schema.Text, interfaces.IText)

TextLine = FieldType(
    'TextLine', schema.TextLine, interfaces.ITextLine)

Date = FieldType(
    'Date', schema.Date, interfaces.IDate)

Datetime = FieldType(
    'Datetime', schema.Datetime, interfaces.IDatetime)

Time = FieldType(
    'Time', schema.Time, interfaces.ITime)

EMail = FieldType(
    'EMail', RFC822MailAddress, interfaces.IEmailField,
    ignoreFields = Field.ignoreFields + ('max_length', 'min_length'))

RichText = FieldType(
    'RichText', RichText, interfaces.IRichText)


class URL(Field, BaseURL):
    interface.implements(interfaces.IURLField)

    __schema__ = DataProperty(interfaces.IURLField)

    def _validate(self, value):
        if isValidBaseURL(value) and not value.endswith(':/'):
            return

        raise InvalidBaseURL(value)


class Select(Field, schema.Choice):
    interface.implements(interfaces.ISelect)

    __schema__ = DataProperty(interfaces.ISelect)

    def __init__(self, *args, **kw):
        self.explicitSelect = kw.pop('explicitSelect', False)
        super(Select, self).__init__(*args, **kw)

    @setproperty
    def values(self, values):
        self.vocabulary = SimpleVocabulary.fromValues(values)

    @getproperty
    def values(self):
        return [term.value for term in self.vocabulary]


class RadioSelect(Field, RadioChoice):
    interface.implements(interfaces.IRadioSelect)

    __schema__ = DataProperty(interfaces.IRadioSelect)

    def __init__(self, *args, **kw):
        self.horizontal = kw.pop('horizontal', False)
        super(RadioSelect, self).__init__(*args, **kw)


class VocAccess(object):

    @setproperty
    def values(self, values):
        self.value_type.vocabulary = SimpleVocabulary.fromValues(values)

    @getproperty
    def values(self):
        return [term.value for term in self.value_type.vocabulary]


class MultiSelect(Field, schema.List, VocAccess):
    interface.implements(interfaces.IMultiSelect)

    __schema__ = DataProperty(interfaces.IMultiSelect)

    missing_value = []
    ignoreFields = Field.ignoreFields + ('unique', 'max_length', 'min_length')

    def __init__(self, values=(), *args, **kw):
        kw['default'] = []
        kw['value_type'] = schema.Choice(values=values)

        super(MultiSelect, self).__init__(*args, **kw)


class MultiCheckbox(Field, schema.List, VocAccess):
    interface.implements(interfaces.IMultiCheckbox)

    __schema__ = DataProperty(interfaces.IMultiCheckbox)

    missing_value = []
    ignoreFields = Field.ignoreFields + ('unique', 'max_length', 'min_length')

    def __init__(self, values=(), *args, **kw):
        kw['default'] = []
        kw['value_type'] = schema.Choice(values=values)

        super(MultiCheckbox, self).__init__(*args, **kw)


class Country(Field, schema.Choice, schema.TextLine):
    interface.implements(interfaces.ICountry)

    __schema__ = DataProperty(interfaces.ICountry)
    ignoreFields = Field.ignoreFields + ('max_length', 'min_length')

    def __init__(self, *args, **kw):
        kw['vocabulary'] = vocabulary.countries

        super(Country, self).__init__(*args, **kw)


class State(Field, schema.Choice, schema.TextLine):
    interface.implements(interfaces.IState)

    __schema__ = DataProperty(interfaces.IState)
    ignoreFields = Field.ignoreFields + ('max_length', 'min_length')

    def __init__(self, *args, **kw):
        kw['vocabulary'] = vocabulary.states

        super(State, self).__init__(*args, **kw)


class Lines(Field, SimpleList):
    interface.implements(interfaces.ILines)

    __schema__ = DataProperty(interfaces.ILines)

    missing_value = []

    def __init__(self, values=(), *args, **kw):
        kw['default'] = []
        kw['value_type'] = schema.TextLine()

        super(Lines, self).__init__(*args, **kw)

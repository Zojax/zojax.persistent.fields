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
from zope import interface, schema
from zope.i18nmessageid import MessageFactory
from z3c.schema.email import RFC822MailAddress
from z3c.schema.baseurl.interfaces import IBaseURL
from z3c.schema.email.interfaces import IRFC822MailAddress
from zojax.richtext.field import RichText
from zojax.richtext.interfaces import IRichText
from zojax.widget.list.field import SimpleList
from zojax.widget.radio.interfaces import IRadioChoice
from zojax.content.type.interfaces import IItem, IContent, IContentType

_ = MessageFactory('zojax.persistent.fields')


class IField(IContent):
    """ field """

    __schema__ = interface.Attribute(u'Field schema')

    ignoreFields = interface.Attribute(u'Ignore fields')

    def getFieldData():
        """ return field data """

    def setFieldData(data):
        """ set field data """


class IFieldSchema(interface.Interface):
    """ additional field schema,
        depends on fields container and field content type """

    title = interface.Attribute('Title')
    weight = interface.Attribute('Weight')
    schema = interface.Attribute('Schema')


class IFieldType(interface.Interface):
    """ field content type """


class IFieldsContainer(interface.Interface):
    """ container for fields """


class IFieldWithVocabulary(interface.Interface):
    """ field with configurable vocabulary """

    values = SimpleList(
        title = _(u'Values'),
        description = _(u'Enter values for field, each line new value.'),
        value_type = schema.TextLine(),
        required = True,
        unique = True,
        missing_value = [])


class ISelect(schema.interfaces.IChoice, IFieldWithVocabulary):
    """ select """

    explicitSelect = schema.Bool(
        title=_(u'Use explicit value selection for required fields'),
        default=False)


class IRadioSelect(IRadioChoice, IFieldWithVocabulary):
    """ select using radio buttons """

    horizontal = schema.Bool(
        title=_(u'Use horizontal layout'),
        default=False)


class IMultiSelect(schema.interfaces.IList, IFieldWithVocabulary):
    """ multi select """


class IMultiCheckbox(schema.interfaces.IList, IFieldWithVocabulary):
    """ multi checkbox select """


class IBool(schema.interfaces.IBool):
    pass


class IInt(schema.interfaces.IInt):
    pass


class IText(schema.interfaces.IText):
    pass


class ITextLine(schema.interfaces.ITextLine):
    pass


class IEmailField(IRFC822MailAddress):
    """ email field """


class IURLField(IBaseURL):
    """ url field """


class IRichText(IRichText):
    """ rich text field """


class ICountry(schema.interfaces.ITextLine):
    """ Country """


class IState(schema.interfaces.ITextLine):
    """ US State """


class ILines(schema.interfaces.IField):
    """ Lines field """


class IDate(schema.interfaces.IDate):

    min = schema.Date(
        title=_(u"Start of the range"),
        required=False)

    max = schema.Date(
        title=_(u"End of the range (excluding the value itself)"),
        required=False)


class IDatetime(schema.interfaces.IDatetime):

    min = schema.Datetime(
        title=_(u"Start of the range"),
        required=False)

    max = schema.Datetime(
        title=_(u"End of the range (excluding the value itself)"),
        required=False)


class ITime(schema.interfaces.ITime):

    min = schema.Time(
        title=_(u"Start of the range"),
        required=False)

    max = schema.Time(
        title=_(u"End of the range (excluding the value itself)"),
        required=False)

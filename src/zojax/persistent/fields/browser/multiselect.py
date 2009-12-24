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
from xml.sax import saxutils

from zope import schema, component, interface
from zope.schema.interfaces import IList, ITextLine

from z3c.form import converter
from z3c.form import interfaces
from z3c.form.widget import FieldWidget
from z3c.form.browser import select

from zojax.persistent.fields.fields import MultiSelect, MultiCheckbox


class MultiSelectWidget(select.SelectWidget):

    size = 5
    multiple = True


@interface.implementer(interfaces.IFieldWidget)
@component.adapter(MultiSelect, interfaces.IFormLayer)
def MultiSelectFieldWidget(field, request):
    return FieldWidget(field, MultiSelectWidget(request))


class MultiCheckboxWidget(select.SelectWidget):

    size = 5
    multiple = True


@interface.implementer(interfaces.IFieldWidget)
@component.adapter(MultiCheckbox, interfaces.IFormLayer)
def MultiCheckboxFieldWidget(field, request):
    return FieldWidget(field, MultiCheckboxWidget(request))

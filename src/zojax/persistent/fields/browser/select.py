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
"""Select field related code

$Id$
"""
from z3c.form.browser.select import SelectWidget
from z3c.form.widget import ComputedWidgetAttribute, StaticWidgetAttribute

from zojax.persistent.fields.interfaces import ISelect, _

# Add "prompt" to adapter attributes for z3c.form 1.9
if 'prompt' not in SelectWidget._adapterValueAttributes:
    SelectWidget._adapterValueAttributes += ('prompt', )

PromptNeeded = ComputedWidgetAttribute(
    lambda value:getattr(value.field, 'explicitSelect', False),
    field=ISelect)

PromptMessage = StaticWidgetAttribute(_(u'select a value ...'))
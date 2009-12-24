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
from email.Utils import formataddr

from zope import interface, component
from zope.component import queryUtility, getMultiAdapter

from interfaces import IFormResults


class MessageTemplate(object):

    contentType = 'text/html'

    @property
    def subject(self):
        msg = u'Form has been processed'

        title = getattr(self.form, 'title', u'')
        if title:
            return u'%s: %s'%(msg, title)
        else:
            return msg

    def render(self):
        form = getMultiAdapter((self.form, self.request), IFormResults)
        form.update(self.record)
        return form.render()

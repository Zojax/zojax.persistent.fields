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
import re
import os.path

from zope import interface
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from interfaces import _

# Static DisplayLists
dirname = os.path.dirname(globals()["__file__"])
iso3166_file = file(os.path.join(dirname, 'iso3166.txt'), 'rb')

reg = re.compile("'*(\w+)")


def countryrepl(matchobj):
    str = matchobj.group(1)
    if matchobj.group(0).startswith("'"):
        return "'" + str.lower()
    return str.lower().capitalize()


countries = []
for line in iso3166_file.readlines():
    data = [unicode(v.strip()) for v in line.split(';')]
    title = reg.sub(countryrepl, data[0])
    countries.append(SimpleTerm(data[1], str(data[1]), _(title)))

countries = SimpleVocabulary(countries)


class CountriesVocabulary(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        return countries


STATE_VOCAB = ((u'', _(u'Not applicable')),
               (u'AK', _(u'AK')),
               (u'AL', _(u'AL')),
               (u'AR', _(u'AR')),
               (u'AZ', _(u'AZ')),
               (u'CA', _(u'CA')),
               (u'CO', _(u'CO')),
               (u'CT', _(u'CT')),
               (u'DC', _(u'DC')),
               (u'DE', _(u'DE')),
               (u'FL', _(u'FL')),
               (u'GA', _(u'GA')),
               (u'HI', _(u'HI')),
               (u'IA', _(u'IA')),
               (u'ID', _(u'ID')),
               (u'IL', _(u'IL')),
               (u'IN', _(u'IN')),
               (u'KS', _(u'KS')),
               (u'KY', _(u'KY')),
               (u'LA', _(u'LA')),
               (u'MA', _(u'MA')),
               (u'MD', _(u'MD')),
               (u'ME', _(u'ME')),
               (u'MI', _(u'MI')),
               (u'MN', _(u'MN')),
               (u'MO', _(u'MO')),
               (u'MS', _(u'MS')),
               (u'MT', _(u'MT')),
               (u'NC', _(u'NC')),
               (u'ND', _(u'ND')),
               (u'NE', _(u'NE')),
               (u'NH', _(u'NH')),
               (u'NJ', _(u'NJ')),
               (u'NM', _(u'NM')),
               (u'NV', _(u'NV')),
               (u'NY', _(u'NY')),
               (u'OH', _(u'OH')),
               (u'OK', _(u'OK')),
               (u'OR', _(u'OR')),
               (u'PA', _(u'PA')),
               (u'PR', _(u'PR')),
               (u'RI', _(u'RI')),
               (u'SC', _(u'SC')),
               (u'SD', _(u'SD')),
               (u'TN', _(u'TN')),
               (u'TX', _(u'TX')),
               (u'UT', _(u'UT')),
               (u'VA', _(u'VA')),
               (u'VI', _(u'VI')),
               (u'VT', _(u'VT')),
               (u'WA', _(u'WA')),
               (u'WI', _(u'WI')),
               (u'WV', _(u'WV')),
               (u'WY', _(u'WY')))

states = SimpleVocabulary(
    [SimpleTerm(item[0], item[0], item[1]) for item in STATE_VOCAB])

class StatesVocabulary(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        return states

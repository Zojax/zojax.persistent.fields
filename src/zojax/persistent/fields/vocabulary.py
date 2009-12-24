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
import os.path

from zope import interface
from zope.schema.interfaces import IVocabularyFactory
from zope.schema.vocabulary import SimpleTerm, SimpleVocabulary

from interfaces import _

# Static DisplayLists
dirname = os.path.dirname(globals()["__file__"])
iso3166_file = file(os.path.join(dirname, 'iso3166.txt'), 'rb')

countries = []
for line in iso3166_file.readlines():
    data = [unicode(v.strip()) for v in line.split(';')]
    countries.append(SimpleTerm(data[1], str(data[1]), _(data[0])))

countries = SimpleVocabulary(countries)


class CountriesVocabulary(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        return countries


STATE_VOCAB = ((u'', _(u'Not applicable')),
               (u'AL', _(u'Alabama')),
               (u'AK', _(u'Alaska')),
               (u'AZ', _(u'Arizona')),
               (u'AR', _(u'Arkansas')),
               (u'CA', _(u'California')),
               (u'CO', _(u'Colorado')),
               (u'CT', _(u'Conneticut')),
               (u'DE', _(u'Delaware')),
               (u'DC', _(u'District of Columbia')),
               (u'FL', _(u'Florida')),
               (u'GA', _(u'Georgia')),
               (u'HI', _(u'Hawaii')),
               (u'ID', _(u'Idaho')),
               (u'IL', _(u'Illinois')),
               (u'IN', _(u'Indiana')),
               (u'IA', _(u'Iowa')),
               (u'KS', _(u'Kansas')),
               (u'KY', _(u'Kentucky')),
               (u'LA', _(u'Louisiana')),
               (u'ME', _(u'Maine')),
               (u'MD', _(u'Maryland')),
               (u'MA', _(u'Massachusets')),
               (u'MI', _(u'Michagan')),
               (u'MN', _(u'Minnesota')),
               (u'MP', _(u'Mississippi')),
               (u'MS', _(u'Missouri')),
               (u'MT', _(u'Montana')),
               (u'NE', _(u'Nebraska')),
               (u'NV', _(u'Nevada')),
               (u'NH', _(u'New Hampshire')),
               (u'NJ', _(u'New Jersey')),
               (u'NM', _(u'New Mexico')),
               (u'NY', _(u'New York')),
               (u'NC', _(u'North Carolina')),
               (u'ND', _(u'North Dakota')),
               (u'OH', _(u'Ohio')),
               (u'OK', _(u'Oklahoma')),
               (u'OR', _(u'Oregon')),
               (u'PA', _(u'Pennsylvania')),
               (u'PR', _(u'Puerto Rico')),
               (u'RI', _(u'Rhode Island')),
               (u'SC', _(u'South Carolina')),
               (u'SD', _(u'South Dakota')),
               (u'TN', _(u'Tennessee')),
               (u'TX', _(u'Texas')),
               (u'UT', _(u'Utah')),
               (u'VT', _(u'Vermont')),
               (u'VI', _(u'Virginia')),
               (u'WA', _(u'Washington')),
               (u'WV', _(u'West Virginia')),
               (u'WI', _(u'Wisconsin')),
               (u'WY', _(u'Wyoming')))


states = SimpleVocabulary(
    [SimpleTerm(item[0], item[0], item[1]) for item in STATE_VOCAB])

class StatesVocabulary(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        return states

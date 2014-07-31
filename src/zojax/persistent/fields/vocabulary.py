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
               (u'AA', _(u'Armed Forces Americas')),
               (u'AE', _(u'Armed Forces Europe')),
               (u'AK', _(u'Alaska')),
               (u'AL', _(u'Alabama')),
               (u'AP', _(u'Armed Forces Pacific')),
               (u'AR', _(u'Arkansas')),
               (u'AS', _(u'American Samoa')),
               (u'AZ', _(u'Arizona')),
               (u'CA', _(u'California')),
               (u'CO', _(u'Colorado')),
               (u'CT', _(u'Connecticut')),
               (u'DC', _(u'District of Columbia')),
               (u'DE', _(u'Delaware')),
               (u'FL', _(u'Florida')),
               (u'FM', _(u'Federated Micronesia')),
               (u'GA', _(u'Georgia')),
               (u'GU', _(u'Guam')),
               (u'HI', _(u'Hawaii')),
               (u'IA', _(u'Iowa')),
               (u'ID', _(u'Idaho')),
               (u'IL', _(u'Illinois')),
               (u'IN', _(u'Indiana')),
               (u'KS', _(u'Kansas')),
               (u'KY', _(u'Kentucky')),
               (u'LA', _(u'Louisiana')),
               (u'MA', _(u'Massachusetts')),
               (u'MD', _(u'Maryland')),
               (u'ME', _(u'Maine')),
               (u'MH', _(u'Marshall Islands')),
               (u'MI', _(u'Michigan')),
               (u'MN', _(u'Minnesota')),
               (u'MO', _(u'Missouri')),
               (u'MP', _(u'Northern Mariana Islands')),
               (u'MS', _(u'Mississippi')),
               (u'MT', _(u'Montana')),
               (u'NC', _(u'North Carolina')),
               (u'ND', _(u'North Dakota')),
               (u'NE', _(u'Nebraska')),
               (u'NH', _(u'New Hampshire')),
               (u'NJ', _(u'New Jersey')),
               (u'NM', _(u'New Mexico')),
               (u'NV', _(u'Nevada')),
               (u'NY', _(u'New York')),
               (u'OH', _(u'Ohio')),
               (u'OK', _(u'Oklahoma')),
               (u'OR', _(u'Oregon')),
               (u'PA', _(u'Pennsylvania')),
               (u'PR', _(u'Puerto Rico')),
               (u'PW', _(u'Palau')),
               (u'RI', _(u'Rhode Island')),
               (u'SC', _(u'South Carolina')),
               (u'SD', _(u'South Dakota')),
               (u'TN', _(u'Tennessee')),
               (u'TX', _(u'Texas')),
               (u'UM', _(u'United States Minor Outlying Islands')),
               (u'UT', _(u'Utah')),
               (u'VA', _(u'Virginia')),
               (u'VI', _(u'US Virgin Islands')),
               (u'VT', _(u'Vermont')),
               (u'WA', _(u'Washington')),
               (u'WI', _(u'Wisconsin')),
               (u'WV', _(u'West Virginia')),
               (u'WY', _(u'Wyoming')))


states = SimpleVocabulary(
    [SimpleTerm(item[0], item[0], item[1]) for item in STATE_VOCAB])

class StatesVocabulary(object):
    interface.implements(IVocabularyFactory)

    def __call__(self, context):
        return states

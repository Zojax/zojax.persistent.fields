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
from zope import interface, event
from zope.schema import getFieldNames
from zope.component import getAdapters
from zope.traversing.browser import absoluteURL
from zope.cachedescriptors.property import Lazy
from zope.proxy import removeAllProxies
from zope.security.proxy import removeSecurityProxy
from zope.lifecycleevent import Attributes, ObjectModifiedEvent

from zojax.layoutform import button
from zojax.wizard.button import WizardButton
from zojax.wizard.step import WizardStepForm, applyChanges
from zojax.wizard.interfaces import ISaveable
from zojax.content.forms.form import Fields, AddForm
from zojax.statusmessage.interfaces import IStatusMessage
from zojax.content.type.interfaces import IContentType

from zojax.persistent.fields.interfaces import _, IField, IFieldSchema


class AddFieldForm(AddForm):

    def create(self, data):
        content = super(AddFieldForm, self).create(data)

        fieldData = {}
        for schema in self.schemas:
            for name in schema:
                if name in data:
                    fieldData[name] = data[name]

        if fieldData:
            removeSecurityProxy(content).setFieldData(fieldData)

        return content

    @Lazy
    def fields(self):
        klass = removeSecurityProxy(self.context.klass)
        fields = Fields(
            self.context.schema, IField,
            omitReadOnly=True).omit(*klass.ignoreFields)

        if self.schemas:
            fields = fields + Fields(*self.schemas)

        return fields

    def update(self):
        schemas = []
        for name, schema in getAdapters(
            (self.context.context, self.context), IFieldSchema):
            schemas.append((schema.weight, schema.title, schema.schema))

        schemas.sort()
        self.schemas = [schema for w,t,schema in schemas]

        super(AddFieldForm, self).update()


class EditFieldForm(WizardStepForm):
    interface.implements(ISaveable)

    def applyChanges(self, data):
        content = self.wizard.getContent()

        descriptions = []
        for schema in (removeAllProxies(content).__schema__, IField):
            names = []
            for name in getFieldNames(schema):
                if name in data:
                    field = schema[name].bind(content)
                    if field.get(content) != data[name]:
                        names.append(name)
                        field.set(content, data[name])

            if names:
                descriptions.append(Attributes(schema, *names))

        fieldData = {}
        oldData = content.getFieldData()
        for schema in self.schemas:
            names = []
            for name in schema:
                if name in data:
                    if oldData.get(name) != data[name]:
                        names.append(name)
                    fieldData[name] = data[name]

            if names:
                descriptions.append(Attributes(schema, *names))

        if fieldData:
            content.setFieldData(fieldData)

        if descriptions:
            event.notify(ObjectModifiedEvent(content, *descriptions))

        return bool(descriptions)

    def getContent(self):
        content = self.wizard.getContent()
        data = removeAllProxies(content.getFieldData())

        for schema in (removeAllProxies(content).__schema__, IField):
            for name in getFieldNames(schema):
                field = schema[name].bind(content)
                data[name] = field.get(content)

        return data

    @Lazy
    def fields(self):
        fields = Fields(
            self.context.__schema__, IField,
            omitReadOnly=True).omit(*self.context.ignoreFields)

        if self.schemas:
            fields = fields + Fields(*self.schemas)

        return fields

    def update(self):
        self.ct = IContentType(self.context)

        schemas = []
        for name, schema in getAdapters(
            (self.context.__parent__, self.ct), IFieldSchema):
            schemas.append((schema.weight, schema.title, schema.schema))

        schemas.sort()
        self.schemas = [schema for w,t,schema in schemas]

        super(EditFieldForm, self).update()


class ViewField(WizardStepForm):

    ignoreContext = True
    formFailedMessage = _(u'Test is failed.')
    formSuccessMessage = _(u'Test is successful.')

    @Lazy
    def fields(self):
        return Fields(self.context)

    def extractData(self, setErrors=True):
        return {}, ()

    @button.buttonAndHandler(_(u'Test'), name='test')
    def handleTest(self, action):
        data, errors = super(ViewField, self).extractData()
        if errors:
            IStatusMessage(self.request).add(self.formFailedMessage, 'warning')
        else:
            IStatusMessage(self.request).add(self.formSuccessMessage)

    def isComplete(self):
        return True


# back action
class BackButton(WizardButton):

    def actionHandler(self):
        return self.wizard.redirect('%s/'%absoluteURL(
                self.wizard.__parent__.__parent__, self.request))


backButton = BackButton(title = _(u'Back'), weight = 502)

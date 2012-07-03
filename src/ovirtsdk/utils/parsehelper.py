#
# Copyright (c) 2010 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import StringIO
from ovirtsdk.xml import params
from ovirtsdk.utils.reflectionhelper import ReflectionHelper
import sys

class ParseHelper():
    '''Provides parsing capabilities'''

    @staticmethod
    def toXml(entity):
        '''Parse entity to corresponding XML representation'''

        if ReflectionHelper.isModuleMember(sys.modules['ovirtsdk.infrastructure.brokers'],
                                           type(entity)) and hasattr(entity, 'superclass'):
            entity = entity.superclass

        type_name = type(entity).__name__.lower()
        output = StringIO.StringIO()
        entity.export(output, 0, name_=ParseHelper.getXmlTypeInstance(type_name))
        return output.getvalue()

    @staticmethod
    def getXmlWrapperType(type_name):
        tn = type_name.lower()
        for k, v in params._rootClassMap.items():
            if v.__name__.lower() == tn or k.lower() == tn:
                return v.__name__
        return type_name

    @staticmethod
    def getXmlTypeInstance(type_name):
        tn = type_name.lower()
        for k, v in params._rootClassMap.items():
            if v.__name__.lower() == tn:
                return k
        return type_name

    @staticmethod
    def getXmlType(type_name):
        if type_name and type_name != '':
            tn = type_name.lower()
            items = params._rootClassMap.items()
            for k, v in items:
                if v.__name__.lower() == tn or k.lower() == tn:
                    return v
        return None

    @staticmethod
    def getSingularXmlTypeInstance(type_name):
        instance = ParseHelper.getXmlTypeInstance(type_name)
        if instance.endswith('s'):
            return instance[0 : len(instance) - 1]
        return instance

    @staticmethod
    def toType(fromItem, toType):
        '''Encapsulates the entity with the broker instance.'''
        return toType(fromItem)

    @staticmethod
    def toCollection(toType, fromItems=[]):
        '''Encapsulates the entities collection with the broker instance collection.'''
        new_coll = []
        for item in fromItems:
            new_coll.append(ParseHelper.toType(item, toType))
        return new_coll

    @staticmethod
    def toSubType(fromItem, toType, parent):
        '''Encapsulates the sub-entity with the broker instance.'''
        return toType(parent, fromItem)

    @staticmethod
    def toSubTypeFromCollection(toType, parent, fromItems=[]):
        '''Encapsulates the sub-entity collection element with the broker instance.'''
        return toType(parent, fromItems[0]) if(fromItems is not None and len(fromItems) > 0) else None

    @staticmethod
    def toTypeFromCollection(toType, fromItems=[]):
        '''Encapsulates the entity collection element with the broker instance.'''
        #return toType(fromItems[0]) if(fromItems is not None and len(fromItems) > 0) else None
        return toType(fromItems[0] if(fromItems is not None and len(fromItems) > 0) else None)

    @staticmethod
    def toSubCollection(toType, parent, fromItems=[]):
        '''Encapsulates the sub-entities collection with the broker instance collection.'''
        new_coll = []
        for fromItem in fromItems:
            new_coll.append(ParseHelper.toSubType(fromItem, toType, parent))
        return new_coll

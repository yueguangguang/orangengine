# -*- coding: utf-8 -*-
from orangengine.models.base import BaseObject


class BaseAddressGroup(BaseObject):

    def __init__(self, name):
        """init a address group object"""

        self.name = name
        self.elements = list()

    def add(self, address):
        """add an address(group) object to the elements list"""

        self.elements.append(address)

    def __getattr__(self, item):
        """
        yeild the values of the underlying objects
        """
        if item == 'value':
            return [a.value for a in self.elements]
        else:
            raise AttributeError

    def table_value(self, with_names):
        value = "Group: " + self.name + "\n"
        for a in self.elements:
            value = value + "   " + a.table_value(with_names) + "\n"
        return value.rstrip('\n')  # remove the last new line

    def serialize(self):
        """Searialize self to a json acceptable data structure
        """

        elements = []
        for e in self.elements:
            elements.append(e.serialize())

        return {
            'name': self.name,
            'elements': elements
        }

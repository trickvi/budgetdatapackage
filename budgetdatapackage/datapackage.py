# -*- encoding: utf-8 -*-
# budgetdatapackage - Load and manage Budget data packages
# Copyright (C) 2013 Tryggvi Björgvinsson
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from __future__ import absolute_import
import datapackage
from .resource import BudgetResource


class BudgetDataPackage(datapackage.DataPackage):

    @property
    def resources(self):
        return self['resources']

    @resources.setter
    def resources(self, value):
        if not value:
            raise ValueError("resources is a required field")

        # Check if array is a list
        if type(value) != list:
            raise TypeError(
                '{0} must be a list not {1}'.format(
                    BudgetResource.__name__, type(value)))

        # We loop through the list and create Resource objects from dicts
        # or throw errors if the type is invalid
        modified_array = []
        for single_value in value:
            if isinstance(single_value, BudgetResource):
                # We don't need to do anything if it already
                # is of the correct class
                pass
            elif type(single_value) == dict:
                # We turn the single_value into kwargs and pass it into
                # the License constructor
                base = os.path.curdir if 'base' not in self else self.base
                single_value = BudgetResource(datapackage_uri=base,
                                        **single_value)
            else:
                raise TypeError('{0} type {1} is invalid'.format(
                    BudgetResource.__name__, type(single_value)))
            modified_array.append(single_value)

        self['resources'] = modified_array

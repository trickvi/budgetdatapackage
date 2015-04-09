# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

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

from .utils import Granularities, Statuses, Types, Currencies, Countries
import datapackage
import datetime
import warnings
from datapackage import compat


class BudgetResource(datapackage.Resource):

    BUDGET_DATA_PACKAGE_STANDARD = "1.0.0-alpha"
    SPECIFICATION = {'currency': compat.str,
                     'dateLastUpdated': compat.str,
                     'datePublished': compat.str,
                     'fiscalYear': compat.str,
                     'granularity': compat.str,
                     'standard': compat.str,
                     'status': compat.str,
                     'type': compat.str,
                     'location': compat.str,
                     'url': compat.str,
                     'path': compat.str,
                     'data': None,
                     'name': compat.str,
                     'format': compat.str,
                     'mediatype': compat.str,
                     'encoding': compat.str,
                     'bytes': int,
                     'hash': compat.str,
                     'schema': (dict, datapackage.schema.Schema),
                     'sources': list,
                     'licenses': list}
    REQUIRED = (('url', 'path', 'data'), 'currency', 'dateLastUpdated',
                'datePublished', 'fiscalYear', 'granularity', 'status',
                'type')

    GRANULARITIES = Granularities()
    STATUSES = Statuses()
    TYPES = Types()
    CURRENCIES = Currencies()
    COUNTRIES = Countries()

    def __init__(self, *args, **kwargs):
        self.standard = kwargs.pop('standard',
                              self.BUDGET_DATA_PACKAGE_STANDARD)
        super(BudgetResource, self).__init__(*args, **kwargs)

    @property
    def currency(self):
        return self['currency']

    @currency.setter
    def currency(self, value):
        if self.CURRENCIES.is_valid(value):
            self['currency'] = value
            return
        raise ValueError("'{0}' is not a valid currency".format(value))

    @property
    def dateLastUpdated(self):
        return datetime.datetime.strptime(
            self['dateLastUpdated'], '%Y-%m-%d').date()

    @dateLastUpdated.setter
    def dateLastUpdated(self, value):
        datetime.datetime.strptime(value, '%Y-%m-%d')
        self['dateLastUpdated'] = value

    @property
    def datePublished(self):
        return datetime.datetime.strptime(
            self['datePublished'], '%Y-%m-%d').date()

    @datePublished.setter
    def datePublished(self, value):
        datetime.datetime.strptime(value, '%Y-%m-%d')
        self['datePublished'] = value

    @property
    def fiscalYear(self):
        return self['fiscalYear']

    @fiscalYear.setter
    def fiscalYear(self, value):
        datetime.datetime.strptime(value, '%Y')
        self['fiscalYear'] = value

    @property
    def granularity(self):
        return self['granularity']

    @granularity.setter
    def granularity(self, value):
        if self.GRANULARITIES.is_valid(value):
            self['granularity'] = value
            return
        raise ValueError("'{0}' is not a valid granularity".format(value))

    @property
    def standard(self):
        return self['standard']

    @standard.setter
    def standard(self, value):
        if not value:
            raise ValueError('standard is required')

        if value != self.BUDGET_DATA_PACKAGE_STANDARD:
            warnings.warn(
                "BudgetDataPackage does not support multiple versions")

        self['standard'] = datapackage.util.verify_version(value)

    @property
    def status(self):
        return self['status']

    @status.setter
    def status(self, value):
        if self.STATUSES.is_valid(value):
            self['status'] = value
            return
        raise ValueError("'{0}' is not a valid status".format(value))

    @property
    def type(self):
        return self['type']

    @type.setter
    def type(self, value):
        if self.TYPES.is_valid(value):
            self['type'] = value
            return
        raise ValueError("'{0}' is not a valid type".format(value))

    @property
    def location(self):
        return self['location']

    @location.setter
    def location(self, value):
        if self.COUNTRIES.is_valid(value):
            self['location'] = value
            return
        raise ValueError("'{0}' is not a valid country code".format(value))

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

import os
import io
import json
from datapackage import compat


class Lookup(object):
    LOOKUP_FILE = ''

    def __init__(self, *args, **kwargs):
        if self.LOOKUP_FILE is None:
            raise NotImplementedError('Lookup file is missing')

        with io.open(self.LOOKUP_FILE) as object_list:
            self.objects = json.load(object_list)

    def is_valid(self, code):
        """Checks to see if a code is valid"""
        return code in self.objects

    def name(self, code):
        """Returns the name for this code"""
        return self.objects[code]


class Granularities(Lookup):
    LOOKUP_FILE = os.path.join(
        os.path.dirname(__file__), 'data', 'granularities.json')


class Statuses(Lookup):
    LOOKUP_FILE = os.path.join(
        os.path.dirname(__file__), 'data', 'statuses.json')


class Types(Lookup):
    LOOKUP_FILE = os.path.join(
        os.path.dirname(__file__), 'data', 'types.json')


class Currencies(Lookup):
    LOOKUP_FILE = os.path.join(
        os.path.dirname(__file__), 'data', 'currencies.json')


class Countries(Lookup):
    LOOKUP_FILE = os.path.join(
        os.path.dirname(__file__), 'data', 'countries.json')

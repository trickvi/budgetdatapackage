# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import budgetdatapackage
import datapackage
import datetime
from nose.tools import raises
from datapackage import compat


class TestBudgetDataPackage(object):

    def test_load_datapackage(self):
        bdpkg = budgetdatapackage.BudgetDataPackage('tests/test.dpkg')
        assert len(bdpkg.resources) == 1

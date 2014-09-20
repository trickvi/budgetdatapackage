import budgetdatapackage
import datapackage
import datetime
from nose.tools import raises
import sys

if sys.version_info[0] < 3:
    next = lambda x: x.next()
    bytes = str
    str = unicode


class TestBudgetDataPackage(object):

    def test_load_datapackage(self):
        bdpkg = budgetdatapackage.BudgetDataPackage('tests/test.dpkg')
        assert len(bdpkg.resources) == 1

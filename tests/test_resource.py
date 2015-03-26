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


class TestBudgetResource(object):

    def setup(self):
        self.values = {
            'currency': 'ISK',
            'dateLastUpdated': '2014-04-22',
            'datePublished': '1982-04-22',
            'fiscalYear': '2014',
            'granularity': 'transactional',
            'status': 'approved',
            'type': 'expenditure',
            'location': 'IS',
            'url': 'http://iceland.is/budgets.csv'}

    def test_create_resource(self):
        resource = budgetdatapackage.BudgetResource(**self.values)
        assert resource.currency == self.values['currency']
        last_updated = datetime.datetime.strptime(
            self.values['dateLastUpdated'], '%Y-%m-%d').date()
        assert resource.dateLastUpdated == last_updated
        published = datetime.datetime.strptime(
            self.values['datePublished'], '%Y-%m-%d').date()
        assert resource.datePublished == published
        assert resource.fiscalYear == self.values['fiscalYear']
        assert resource.granularity == self.values['granularity']
        assert resource.status == self.values['status']
        assert resource.type == self.values['type']
        assert resource.location == self.values['location']
        assert resource.url == self.values['url']
        assert resource.standard == '1.0.0-alpha'

    def test_resource_can_be_used_with_datapackage(self):
        """Checks if it's possible to create a datapackage with a
        budget resource"""
        moneys = budgetdatapackage.BudgetResource(**self.values)
        finances = datapackage.DataPackage(
            name="finances", license="PDDL", resources=[moneys])
        assert finances.name == "finances"
        assert len(finances.resources) == 1
        assert finances.resources[0].granularity == self.values['granularity']

    @raises(ValueError)
    def test_create_resource_missing_required_field(self):
        del self.values['fiscalYear']
        budgetdatapackage.BudgetResource(**self.values)

    @raises(ValueError)
    def test_bad_currency(self):
        self.values['currency'] = 'batman'
        budgetdatapackage.BudgetResource(**self.values)

    @raises(ValueError)
    def test_bad_dateLastPublished(self):
        self.values['dateLastUpdated'] = 'batman'
        budgetdatapackage.BudgetResource(**self.values)

    @raises(ValueError)
    def test_bad_datePublished(self):
        self.values['datePublished'] = 'batman'
        budgetdatapackage.BudgetResource(**self.values)

    @raises(ValueError)
    def test_bad_fiscalYear(self):
        self.values['fiscalYear'] = 'batman'
        budgetdatapackage.BudgetResource(**self.values)

    @raises(ValueError)
    def test_bad_granularity(self):
        self.values['granularity'] = 'batman'
        budgetdatapackage.BudgetResource(**self.values)

    @raises(ValueError)
    def test_bad_status(self):
        self.values['status'] = 'batman'
        budgetdatapackage.BudgetResource(**self.values)

    @raises(ValueError)
    def test_bad_type(self):
        self.values['type'] = 'batman'
        budgetdatapackage.BudgetResource(**self.values)

    @raises(ValueError)
    def test_bad_location(self):
        self.values['location'] = 'batman'
        budgetdatapackage.BudgetResource(**self.values)

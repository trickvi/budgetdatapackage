budgetdatapackage
=================

Extension of `datapackage <https://github.com/tryggvib/datapackage>`__
which provides a ``BudgetResource`` class for creating a `Budget Data
Package <https://github.com/openspending/budget-data-package>`__
resource which is a drop in replacement for ``datapackage.Resource``.

::

    from budgetdatapacakge import BudgetResource
    from datapackage import DataPackage

    # Create BudgetResource which has a lot of requirements
    budget = BudgetResource(
        currency='ISK',
        dateLastUpdated='2014-04-22',
        datePublished='1982-04-22',
        fiscalYear='2014',
        granularity='transactional',
        status='approved',
        type='expenditure',
        location='IS',
        url='http://iceland.is/budgets.csv')
    # Create Budget Data Package
    budget_dpkg = DataPackage(
        name="icelandic-budget", license="PDDL", resources=[budget])

License
-------

budgetdatapackage is available under the GNU General Public License,
version 3. See LICENCE for more details.

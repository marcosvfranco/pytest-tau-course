Plugins for pytest:

`pytest-html`:

Plugin to generate HTML reports with the test results.

Use as:
`python -m pytest --html=report.html
`

--------------
`pytest-cov`

Gives the coverage of the code

Use as: `python -m pytest --cov=stuff
`

Can add more folders repeating `--cov=folder`

`--cov-report html`
Generates a report

------------
`pytest-xdist`

Run tests in parallel

`-n [number]`

Where number is the number of parallel tests

-----------

`pytest-bdd`

Allow to write tests using BDD

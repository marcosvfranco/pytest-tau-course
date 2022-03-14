Run tests by folder

`python -m pytest tests`

Run tests by file

`python -m pytest tests/test_bla.py`

Run tests by test case

`python -m pytest tests/test_bla.py::test_math`

Run tests by token (string in the test description)

`python -m pytest -k one`

Run tests by marker 

`python -m pytest -m math`

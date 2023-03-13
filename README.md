## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) for installation.

Run the following commands:
```bash
pip install pipenv
```
```bash
pipenv install
```
```bash
pipenv shell
```


## Running the tests

Run from inside the pipenv shell

To run all tests:
```
pytest tests/
```

To run specific set - smoke, regression:
```
pytest tests/ -m smoke
```

```
pytest tests/ -m regression
```

To run specific module:
```
pytest tests/amazon_test.py
pytest tests/typicode_api_test.py
```
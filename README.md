# KHAN as a service, in Flask

This is a lightweight implementation of khanaas.com written in Python using the Flask framework.  For comparison, check out [khanaas-django](https://github.com/excellalabs/khanaas-django) for a more full-featured implementation in Django.

## Installation

1. Clone this repo

    ```shell
    git clone https://github.com/excellalabs/khanaas-flask
    ```

1. Optional: Set up a virtual environment

    ```shell
    pip install virtualenv virtualenv-wrapper
    mkvirtualenv khanaas-flask
    ```

1. Run the webapp

    ```shell
    ./run.py
    ```

You should now be able to access the API on port 5000.  For example: http://localhost:5000/kirk/test

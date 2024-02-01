# lists

Here are the tests for linked list imlementation exercise.

1. Python

    You have to create 2 files: `list_node.py` and `my_list.py` and write code to pass the tests.
    * Install pipenv
        ```shell
        pip install pipenv
        ```
    * Recreate environment
        ```shell
        pipenv install
        ```

    * Run tests
        ```shell
        pipenv run pytest -v
        ```
        or
        ```shell
        pipenv shell
        pytest -v
        ```

2. C

    You have to create file `list.c` and... I think you got it. Makefile included, so running test is a piece of cake:
    ```shell
    make
    make memcheck
    make clean
    ```
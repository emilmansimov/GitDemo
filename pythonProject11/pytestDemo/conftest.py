# import pytest
#
#
# @pytest.fixture(scope="class")
# def setup():
#     print("This print statement will get executed first")
#     yield
#     print("This statement will be executed last")
#___________________________________________________________________________________________-
# import pytest
#
#
# @pytest.fixture(scope="class")
# def setup():
#     print("This print statement will get executed first")
#     yield
#     print("This statement will be executed last")
#
#
# @pytest.fixture(params=[("firstname : Hakim", "Last name : Bekkour", "Balance : $5000"),
#                         ("firstname : Yulia", "Last name : Melnyk", "Balance : -2000")])
# def data_set(request):
#     return request.param
#__________________________________________________________________________________________________________

import pytest


@pytest.fixture(scope="class")
def setup():
    print("This print statement will get executed first")
    yield
    print("This statement will be executed last")

@pytest.fixture(params=[("Firstname : Hakim", "Lastname : Bekkour", "Balance : $5000"),
                        ("Firstname : Yuliia", "Lastname : Melnyk", "Balance : -$2000")])
def data_sets(request):
    return request.param

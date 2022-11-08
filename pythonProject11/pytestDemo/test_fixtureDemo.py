# import pytest
#
#
# @pytest.fixture
# def setup():
#     print("This print statement will get executed first")
#     yield
#     print("This statement will be executed last")
#
#
# def test_fixture_first_program(setup):
#     print("This statement will be executed as a part of fixture")
#--------------------------------------------------------------------------------------------------------
# import pytest
#
#
# @pytest.fixture
# def setup():
#     print("This print statement will get executed first")
#     yield
#     print("This statement will be executed last")
#
#
#
# def test_fixture_first_programm(setup):
#     print("This statement will be executed as part of fixture")
#import pytest
import pytest


# import pytest
#
#
# @pytest.mark.usefixtures("data_set")
# def test_multiple_data(data_set):
#     print(data_set)
#_____________________________________________________________________________________________________________

@pytest.mark.usefixtures("data_sets")
def test_multiple_data(data_sets):
    print(data_sets)


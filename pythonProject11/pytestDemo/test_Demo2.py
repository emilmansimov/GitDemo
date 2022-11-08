# import pytest
#
#
# @pytest.mark.smoke
# def test_my_very_firstProgram():
#     print("Hello World")
#
# @pytest.mark.smoke
# @pytest.mark.xfail
# def test_my_very_secondProgam():
#     message = "Hello world"
#     assert "Hello world" == message
#     print(message)
#------------------------------------------------------------------------------------------------------
# 1 py.test - This command is used to execute all tests
# 2 py.test -v: This command is used to executed our
# tests and also include the information for tests explicitly it will tell whether it passed or failed
# 3 py.test -s This command used to print the logs after execution
# 4 py.test -k: This regular command is used
# to execute certain testcases which contain keyword that we are filtering them by
import pytest

@pytest.mark.smoke
@pytest.mark.skip
def test_my_very_secondProgram():
    message = "Hello World"
    assert "ju" in message


@pytest.mark.smoke
@pytest.mark.xfail
def test_my_very_firstProgram():
    msg = "Hello World"
    assert "Hello World" == msg
    print(msg)


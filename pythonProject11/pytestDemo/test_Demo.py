# import pytest
#
#
# @pytest.mark.usefixture("setup")
# class TestFixtureDemo:
#
#
#     def test_my_very_first_car(self):
#         print("It was 1991 car that my dad bought me")
#
#
#     def test_my_second_car(self):
#         print("Wass up")
#
#
#     def test_my_very_firstProgram(self):
#         print("hey hey hey")
#
#     def test_my_very_firstProgram2(self):
#         print("hola hola hola")
#
#     def test_my_very_firstProgram3(self):
#         print("bonjour bonjour bonjour")
#----------------------------------------------------------------------------------------
import pytest

@pytest.mark.usefixtures("setup")
class TestfixtureDemo:


   def test_my_very_first_car(self):
       print("It was 1991 car that my dad bought me")


   def test_my_very_second_car(self):
       print("Wass up")

   def test_my_very_firstProgram1(self):
       print("hey hey hey")

   def test_my_very_firstProgram2(self):
       print("hola hola hola")

   def test_my_very_firstProgram3(self):
       print("bonjour bonjour bonjour")
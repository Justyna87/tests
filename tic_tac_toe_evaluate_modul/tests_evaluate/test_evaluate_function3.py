import pytest
from evaluate_function import evaluate


def test_evaluate():
   assert evaluate('xxx--o-o-o-o--x--') == True
   assert evaluate('---------ooo---x-') == True
   assert evaluate('xooxxooxxooxxoxox') == True
   assert evaluate('--o--x--o--x-o--o') == False
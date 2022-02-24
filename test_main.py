from main import *

def test_simple_work():
  assert simple_work_calc(10, 2, 2) == 36
  assert simple_work_calc(20, 3, 2) == 230
  assert simple_work_calc(30, 4, 2) == 650
  assert simple_work_calc(40, 3, 2) == 730
  assert simple_work_calc(50, 1, 2) == 97
  assert simple_work_calc(60, 2, 2) == 316

def test_work():
  assert work_calc(10, 2, 2,lambda n: 1) == 15
  assert work_calc(20, 1, 2, lambda n: n*n) == 530
  assert work_calc(30, 3, 2, lambda n: n) == 300
  assert work_calc(40, 4, 2,lambda n: n) == 2136
  assert work_calc(60, 1, 2, lambda n: n*n) == 4784
  assert work_calc(50, 3, 2, lambda n: n) == 881

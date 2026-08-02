# -*- coding: utf-8 -*- 


import numpy as np



from qiskit_optimization import QuadraticProgram
from qiskit.quantum_info import SparsePauliOp
from qiskit import QuantumCircuit
#from qiskit.primitives import Sampler  # V1 Sampler（QAOAと互換性あり）
from qiskit_aer import AerSimulator

#from qiskit_ibm_runtime import Sampler, SamplerV2
from qiskit_algorithms import QAOA
from qiskit_algorithms.optimizers import COBYLA
import matplotlib.pyplot as plt

#%%
from qiskit_optimization import QuadraticProgram

# 1. 問題の初期化
problem = QuadraticProgram("my_optimization_problem")

# 2. バイナリ変数 (0 または 1 の値をとる変数) の追加
x0 = problem.binary_var(name="x0")
x1 = problem.binary_var(name="x1")

# 3. 目的関数の設定 (最小化問題)
# 最小化したい数式: -x0 - 2*x1 + 2*x0*x1
linear_terms = {"x0": -1, "x1": -2}
quadratic_terms = {("x0", "x1"): 2}

problem.minimize(linear=linear_terms, quadratic=quadratic_terms)

print(problem.prettyprint())



#%%
from qiskit_optimization.algorithms import MinimumEigenOptimizer
from qiskit_algorithms import NumPyMinimumEigensolver

# 量子計算ではなく、古典的な厳密解（総当たり）を求めるソルバーを用意
exact_solver = MinimumEigenOptimizer(NumPyMinimumEigensolver())

# 問題を解く
result = exact_solver.solve(problem)

# 結果の取り出し
print("最適解 (x0, x1):", result.x)       # 出力: [0. 1.]
print("その時の最小値:", result.fval)    # 出力: -2.0

#%%
# qp = QuadraticProgram("pairwise-onehot")
# for i in range(4):
#     qp.binary_var(f"q{i}")

# qp.minimize(
#     linear=[4, 4, 4, 4],
#     quadratic={(0,1):4, (0,2):4, (1,2):8, (1,3):2, (2,3):2}
# )

# cost_op, offset = qp.to_ising()
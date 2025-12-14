import numpy as np

# 演示1：创建一维数组
X = np.array([1, 2])
print("一维数组X:")
print(X)
print("X的形状:", X.shape)
print()

# 演示2：创建二维数组
B = np.array([[1, 2], [3, 4], [5, 6]])
print("二维数组B:")
print(B)
print("B的形状:", B.shape)
print()

# 演示3：数组运算
y = X + 3
print("X + 3的结果:")
print(y)
print()

# 演示4：矩阵乘法
# 注意：X是一维数组，需要reshape为二维数组才能进行矩阵乘法
X_2d = X.reshape(1, 2)
result = X_2d @ B.T  # 使用@运算符进行矩阵乘法
print("X与B的矩阵乘法结果:")
print(result)

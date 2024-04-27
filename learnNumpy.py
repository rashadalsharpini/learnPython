import numpy as np
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b)
print("dimensions of a", a.ndim)
print("dimensions of b", b.ndim)
print("shape of a", a.shape)
print("shape of b", b.shape)
print("type of a", a.dtype)
print("type of b", b.dtype)
print("size of a", a.itemsize)
print("size of b", b.itemsize)
print("bytes of a", a.nbytes)
print("bytes of b", b.nbytes)
# get a specific element  [r, c]
print(b[0, 1])
print(b[1, -2])
# get a specific row  [r, :]
print(b[1, :])
# get a specific column  [:, c]
print(b[:, 1])
# 3D
c = np.array([
    [
        [1, 2, 3],
        [4, 5, 6]
    ],
    [
        [7, 8, 9],
        [10, 11, 12]
    ]
])
print(c[0, 1, 0])
# 4D
print(np.zeros((2, 3, 3, 3)))
print(np.ones((2, 3, 3, 3)))
print(np.full((2, 3, 3, 3), 12))
print(np.full(b.shape, 13))
print(np.full_like(b, 13))
print(b)
print(np.random.randint(10, size=(3, 3)))
print(np.random.randint(-5, 10, size=b.shape))
print(np.identity(5))
arr = np.array([[1, 2, 3]])
print(np.repeat(arr, 3, axis=0))

output = np.ones((5, 5))
print(output)
z = np.zeros((3, 3))
z[1, 1] = 9
print(z)
output[1:4, 1:4] = z
print(output)

a = np.array([1, 2, 3])
b = a
b[0] = 100
print(f"i am printing a {a} shit!!!!!!!!!!")  # point for the same thing

a = np.array([1, 2, 3])
b = a.copy()
b[0] = 100
print(f"i am printing a {a}")

a = np.array([1, 2, 3, 4])
b = np.array([1, 2, 3, 4])
a += b
print(a)
print(np.sin(a))

a = np.ones((2, 3))
b = np.full((3, 2), 2)
print(np.matmul(a, b))

# find the determinant
c = np.identity(3)
print(np.linalg.det(c))

before = np.array([[1, 2, 3], [4, 5, 6]])
print(before)
after = before.reshape((6, 1))
print(after)
after = before.reshape((3, 2))
print(after)
v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])
print(np.vstack([v1, v2]))
print(np.vstack([v1, v2, v1, v2]))
print(np.hstack([v1, v2]))
fileData = np.genfromtxt('data.txt', delimiter=',')
print(fileData)
print(fileData > 5)
print(fileData[fileData > 5])
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(a[[1, 2, 8]])
fileData = np.genfromtxt('data.txt', delimiter=',')
print(fileData[(fileData > 3) & (6 > fileData)])

a = np.zeros((2, 2))
for i in range(2):
    for j in range(2):
        a[i, j] = input()
print(a)

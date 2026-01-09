import numpy as np

arr = np.array([[10, 20, 30], [40, 50, 60], [70, 80, 90]])

print(arr[2, 0])

print(arr[:, 1])

print(arr.dtype)

arr_copy = arr.copy()
arr_copy[0, 0] = 100
print(arr[0, 0])

arr_view = arr.view()
arr_view[0, 0] = 500
print(arr[0, 0])

print(arr.shape)

for r in range(arr.shape[0]):
    for c in range(arr.shape[1]):
        print(f"Row {r}, Col {c}: {arr[r, c]}")

new_arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(np.vstack((arr, new_arr)))
print(np.hstack((arr, new_arr)))

print(np.hsplit(arr, 3))

print(np.where(arr == 60))

print(np.sort(arr, axis=1))

print(arr[arr > 50])

print(np.random.randint(1, 101, size=(2, 3)))

print(np.sqrt(arr))
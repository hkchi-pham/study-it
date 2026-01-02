import tensorflow as tf

# q1 - create Tensor
matrix_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matrix_b = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]

tensor_a = tf.constant(matrix_a)
tensor_b = tf.constant(matrix_b)

print(tensor_a)
print(tensor_b)

#2 - basic computation
add = tf.add(tensor_a, tensor_b)
subtract = tf.subtract(tensor_a,tensor_b)
multiply  = tf.multiply(tensor_a,tensor_b)
divide = tf.divide(tensor_a, tensor_b)

print(add)
print(subtract)
print(multiply)
print(divide)

#3 - dot product
product = tf.matmul(tensor_a, tensor_b)
print(product) 

#4 - transpose
transpose_a = tf.transpose(tensor_a)
transpose_b = tf.transpose(tensor_b)

print(transpose_a)
print(transpose_b)

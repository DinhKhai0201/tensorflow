import tensorflow as tf
x=tf.Variable(10,name="x")
y=tf.Variable(20,name="y")
f=x+y
init =tf.global_variables_initializer()
with tf.Session():
	init.run()
	result=f.eval()
print(result)
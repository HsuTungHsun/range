# range
#python function :list generator
import random

range(5) #[0, 1, 2, 3, 4]
range(3) #[0, 1, 2, 3]

for i in range(100):
	r = random.randint(1, 1000)
	#print(i)
			#print i =0
			#print i =1
			#print i =2
	
	print('hi') #print random times of 'hi'
	print('This is: ', i + 1, 'times', r)

#range advance

#range(value)
#range(start,end)
#range(start,end,step)

#range(3) 	[0, 1, 2]
#range(2, 5) [2, 3, 4]
#range(2, 10, 3) [2, 5, 8]
#range(10, 3 , -2) [10, 8, 6, 4]

for i in range(100):
	print('hi') #print 'hi' 100 times
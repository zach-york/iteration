# Make a local change
# Make another local change
# Make a change from home
<<<<<<< HEAD
# This is change [B] at school
=======
# This is change [A] from home
>>>>>>> 5e4aa6da77fea497190309f4bd93673c4b7da125

# iteration pattern

# [1, 5, 7 ,8 , 4, 3]

def iterate(list):
	# standard for loop with range
	# for i in range(0, len(list)):
	# 	print list[i]

	# for each loop
	for item in list:
		print item

def print_scores(names, scores):
	for i in range(0, len(names)):
		print names[i] , " scored " , scores[i]


# filter pattern
def congratulations(names, scores):
	for i in range(0, len(names)):
		if (scores[i] == 100):
			print "Congrats", names[i], "! You got a perfect score!"

"""
	function example
"""

def id_check(id):
	"""
		this function requires that the ID be
		passed as a string and not a number
		(i.e. float / int)
	"""
	if len(id) == 9:
		return true
	else:
		return false


student_id = str(input("Enter ID: "))

if id_check(student_id):
	print("you get a discount for being a WLU student")
else:
	print("we don't take kindly to your type around here")

 

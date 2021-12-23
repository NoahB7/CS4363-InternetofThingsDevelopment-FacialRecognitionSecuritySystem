# ************************************
# Name:			Noah Buchanan
# Problem Set:		PS1
# Due Date:		Sept 6, 2021
# ************************************

import os
#os.walk simply walks the given directory and finds all dirs and files
#file.endswith is just a boolean check to see the file type and check if 
#its a python file
for root, dirs, files in os.walk('./'):
	for file in files:
		if file.endswith('.py'):
			print(os.path.join(root, file))


print('finished')

import os
import zipfile
from shutil import copyfile
import shutil
solution_dir = 'files/solution/'
file_dir = "files/"
import zipfile
import os

print "test",solution_dir
python_files = []
for dirname, subdirs, files in os.walk(solution_dir):

	for file in files:
		if ".pptx" in file:
			continue
		print file
		with open(solution_dir+file, 'r') as fp:
			content = fp.readlines()

		python_files.append(file_dir+file)
		with open(file_dir+file, "w") as fp:
			for line in content:
				if "## Solution" in line:
					pos = len(line) - len(line.lstrip())
					line = line[:pos]+ "## PUT YOUR CODE HERE ##\n"
				#print(line.rstrip('\n'))
				fp.write(line)




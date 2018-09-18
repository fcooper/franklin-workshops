import os
import zipfile
from shutil import copyfile
import shutil
solution_dir = "files\solution\\"
file_dir = "files\\"
import zipfile
import os


python_files = []
for dirname, subdirs, files in os.walk(solution_dir):

    for file in files:
        if ".pptx" in file:
            continue

        with open(solution_dir+file, 'r') as fp:
            content = fp.readlines()

        python_files.append(file_dir+file)
        with open(file_dir+file, "w") as fp:
            for line in content:
                if "## Solution" in line:
                    pos = len(line) - len(line.lstrip())
                    line = line[:pos]+ "## PUT YOUR CODE HERE ##\n"
                print(line.rstrip('\n'))
                fp.write(line)




with zipfile.ZipFile(file_dir+'bopit.zip',
                     "w",
                     zipfile.ZIP_DEFLATED,
                     allowZip64=True) as zf:

    for file in python_files:
        zf.write(file, file)

    presentation = file_dir+"presentation_student.pptx"
    zf.write(presentation,presentation)


exit()
zf = zipfile.ZipFile("myzipfile.zip", "w")
for dirname, subdirs, files in os.walk("mydirectory"):
    zf.write(dirname)
    for filename in files:
        zf.write(os.path.join(dirname, filename))
zf.close()
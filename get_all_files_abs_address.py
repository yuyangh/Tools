import os

'''
put in the directory to work
excluded extensions are in @EXCLUDE_EXTENSIONS
result_filename 
'''
result_filename = 'AbsolutePaths.txt'
EXCLUDE_EXTENSIONS = ['.py']

fid = open(result_filename, 'w')

rootdir = os.getcwd()

pathname = []

for (dirpath, dirnames, filenames) in os.walk(rootdir):
    for filename in filenames:
        pathname += [os.path.join(dirpath, filename)]

for path in pathname:
    break_loop = False
    if result_filename in path:
        continue
    # can optimize
    for extension in EXCLUDE_EXTENSIONS:
        if extension in path:
            break_loop = True
            break
    if break_loop:
        continue
    fid.write(path + '\n')
fid.close()

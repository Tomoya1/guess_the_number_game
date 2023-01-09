def reverseFile(file1, file2):
    contents = "";
    reverseContents = "";

    # open
    with open(file1) as f:
        contents = f.read();
    # reverse
    for i in range(len(contents)):
        reverseContents = contents[i] + reverseContents;

    # write
    with open(file2, 'w') as f:
        f.write(reverseContents);


def copyFile(file1, file2):
    contents = "";

    # open
    with open(file1) as f:
        contents = f.read();
    
    # write(copy)
    with open(file2, 'w') as f:
        f.write(contents);


def duplicateContents(file, n):
    contents = "";

    with open(file) as f:
        contents = f.read();

    for i in range(int(n)):
        with open(file, 'a') as f:
            f.write('\n' + contents);


def replaceString(file, searchstring, newstring):
    contents = "";
    newcontents = "";

    with open(file) as f:
        contents = f.read();
    
    # replace
    newcontents = contents.replace(searchstring, newstring);

    with open(file, 'w') as f:
        f.write(newcontents);
    

# process separately
import sys
args = sys.argv

if args[1] == "reverse":
    reverseFile(args[2], args[3]);
elif args[1] == "copy":
    copyFile(args[2], args[3]);
elif args[1] == "duplicate-contents":
    duplicateContents(args[2], args[3]);
elif args[1] == "replace-string":
    replaceString(args[2], args[3], args[4]);

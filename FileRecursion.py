import os
l = []
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    os_dir=os.listdir(path)
    for elem in os_dir:
        if os.path.isfile(path+"/"+elem):
            if elem.startswith(suffix):
                if elem.endswith(".c"):
                    l.append(os.path.abspath(path + "/" + elem))
        elif os.path.isdir(path+"/"+elem):
            find_files(suffix,path+"/"+elem)
    return l


###Test File Recursion###
l = []
##Getting all ".c" files starting with suffix ' ' in the directory path
print("\n CALL: ","find_files(suffix=' ', path='./testdir')")
print("\n Result: ", find_files(suffix=' ', path='./testdir'),"\n")

##Getting all ".c" files starting with suffix a in the directory path outer dir
print("\n CALL: ","find_files(suffix='t1', path='./testdir')")
print("\n Result: ", find_files(suffix='t1', path='./testdir'),"\n")
l = []

##Getting all ".c" files starting with suffix a in the directory path inner dir
print("\n CALL: ","find_files(suffix='a', path='./testdir')")
print("\n Result: ", find_files(suffix='a', path='./testdir'),"\n")
l = []
##Getting all ".c" files starting with suffix  b in the directory path most inner dir
print("\n CALL: ","find_files(suffix='b', path='./testdir')")
print("\n Result: ", find_files(suffix='b', path='./testdir'),"\n")
l = []

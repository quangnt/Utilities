import os, re
import subprocess
import sys

def delete_files_by_name_without_path_in_director(modenumber, path, filenames):
    """
        Usage: Delete all files base on input filenames if they're existed. Supports 2 types:
        - Filename match exactly input filename
        - Filename match input filename pattern
        Parameters:
        + modenumber: as integer
            - value = 1: Filename match exactly input filename
            - value = 2: Filename match input filename pattern
        + path: specific directory needs to remove files
        + filenames: input filenames need to remove
        Return:
        + List of deleted files if success
        + Empty list if not success(Path is not existed or not success to delete files or files are not existed)
    """    
    delledfiles = []
    if not os.path.exists(path):
        print "Input path is not existed."
    else:        
        boolstatement = False
        t = ''
        for root, dirs, files in os.walk(path):
            for f in filenames:
                for fi in files:
                    if int(modenumber) == 1:
                        boolstatement = f in files
                        t = f
                    elif int(modenumber) == 2:
                        boolstatement = re.search(f, fi)
                        t = fi
                    if boolstatement:
                        try:
                            os.remove(os.path.join(root, t).replace("\\","/"))
                            delledfiles.append(os.path.join(root, t).replace("\\","/"))
                            print('Delete successfully {}'.format(os.path.join(root, t).replace("\\","/")))
                            if (modenumber == 1):
                                break;
                        except OSError:
                            print('Failure on deleting {}'.format(os.path.join(root, t).replace("\\","/")))
    return delledfiles

def delete_files_by_name_without_path_in_directors(modenumber, paths, filenames):
    """
        Usage: Delete all files base on input filenames. Supports 2 types:
        - Filename match exactly input filename
        - Filename match input filename pattern
        Parameters:
        + modenumber: as integer
            - value = 1: Filename match exactly input filename
            - value = 2: Filename match input filename pattern
        + paths: specific directories needs to remove files
        + filenames: input filenames need to remove
        Return:
        + List of deleted files if success
        + Empty list if not success
    """
    results = []
    for path in paths:
        result = delete_files_by_name_without_path_in_director(modenumber, path, filenames)
        results.extend(result)
    return results

def read_file_store_content_in_list(filename):
    """
        Usage: Read content of file if exist, and store its content(each line is stored as a list's member) to list.
        Parameters:
        + filename: File name needs to read
        Return:
        + empty list if file name is not existed
        + result list if file name existed.
    """
    result = []
    if not os.path.isfile(filename):
        print "Input file name is not existed"
    else:        
        with open(filename, "r") as inF:
            for line in inF:
                result.append(line.strip())
    return result        

def add_empty_deleted_files(l):
    for f in l:
        open(f, 'w').close()
        print "Added file: " + f

if __name__ == "__main__":
    if len(sys.argv) < 4 or len(sys.argv) > 4:
        print """ To run this file, needs to input following argument:
... 1. Mode number which supports 2 modes:
...    Mode number = 1: Delete all files which have exact name as input file name
...    Mode number = 2: Delete all files which have name contains input pattern name
... 2. Full file name to file contains list of directories need to delete files.
...    Content in this file is that each directory is stored in one line, there's no break line
...    Ex: I:/StagePresence/workspace
...        D:/workspace
... 3. Full file name to file contains list of filenames(without directory)need to delete
...    Content in this file is that each filename is stored in one line, there's no break line """
        sys.exit(1)
    else:
        results = []
        try:
            modenumber = int(sys.argv[1])
        except ValueError:
            print "Can't convert 1st argument to integer."
            sys.exit(1)
        pathlistfilename = str(sys.argv[2])
        namelistfilename = str(sys.argv[3])        
        if os.path.isfile(pathlistfilename) and os.path.isfile(namelistfilename):
            paths = []
            names = []                        
            paths = read_file_store_content_in_list(pathlistfilename)
            names = read_file_store_content_in_list(namelistfilename)
            print "Content of path file is: " + str(paths)
            print "Content of name file is: " + str(names)
            results = delete_files_by_name_without_path_in_directors(modenumber, paths, names)
            print "Delete files is: " + str(results)
        else:
            print 'Input file names are not existed.'
##    modenumber = 1
##    path = ['I:/Temp - Copy', 'I:/Temp - Copy (2)', 'I:/Temp - Copy (3)']
##    filenames = ['TestReport.md', 'TestReport.html', 'StagePresence.md', 'Readme.md']
##    filenames = ["StagePresence-PR_[0-9]{3}_TestReport", "StagePresence-PR_[0-9]{4}_TestReport", "StagePresence-PR_[0-9]{5}_TestReport"]
##    dellist = delete_files_by_name_without_path_in_director(modenumber, path, filenames)
##    dellist = delete_files_by_name_without_path_in_directors(modenumber, path, filenames)
##    add_deleted_files(dellist)   

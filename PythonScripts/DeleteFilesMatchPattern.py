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

if __name__ == "__main__":
    if len(sys.argv) < 2 or len(sys.argv) > 2:
        print """ To run this file, needs to input following argument:
... NODE_NAME:
...    NODE_NAME = master: Delete all old report files on master
...    [Paths, Filenames]:
            [C:/Program Files (x86)/Jenkins/jobs/StagePresence-PR/workspace, TestReport]
...    NODE_NAME = Macmini-Win10: Delete all old report files on Macmini-Win10 slave
...    [Paths, Filenames]:
            [C:/workspace/StagePresence-PR, TestReport]
            [C:/workspace/TestReport, TestReport]
            [C:/workspace/Shared, RunGUITestProject]    
"""
        sys.exit(1)
    else:
        results = []
        paths = []
        names = []
        modenumber = 2
        node_name = str(sys.argv[1]).lower()
        names.append('TestReport')
        if node_name.find('master') != -1:
            paths.append('C:/Program Files (x86)/Jenkins/jobs/StagePresence-PR/workspace')
        elif node_name.find('Macmini-Win10'.lower()) != -1:
            names.append('RunGUITestProject')
            paths.append('C:/workspace/StagePresence-PR')
            paths.append('C:/workspace/TestReport')
            paths.append('C:/workspace/Shared')        
            print "Content of path file is: " + str(paths)
            print "Content of name file is: " + str(names)
        results = delete_files_by_name_without_path_in_directors(modenumber, paths, names)       

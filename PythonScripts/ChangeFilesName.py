import os
import unittest
import re

class FileManagement(unittest.TestCase):
    def get_all_file_names_base_on_keyword(self, dictionary):
    # This function is used for changing all files' name which have their names
    # contain input keywords to new nameFormat.
    # Input parameter is a dictionary collection which have following members:
    #   + Folder: input path to specific folder
    #   + Keyword: input keywords used as condition to find files
    #   + nameFormat: common input output name after changing.
        result = []
        for file in os.listdir(dictionary['Folder']):
            satisfy = True
##            print "Length of dicitonary:" + str(len(dictionary) - 1) + " of file:" + file
            for x in range(1, len(dictionary) - 1):
##                print "+++X:" + str(x) + "\n"
                if file.lower().find(dictionary['Keyword' + str(x)].lower()) == -1:                
                    satisfy = False
                    break
            if satisfy == True:
                result.append(file)
        return result

    def find_index_of_first_digit_in_string(self, string):
        index = re.search("\d", string)
        
    
    def test_change_files_name(self):
        dictionary = {'Folder': 'I:\Temp', 'Keyword1': 'new', 'Keyword2': 'test', 'nameFormat': 'First'};
        result = self.get_all_file_names_base_on_keyword(dictionary)
        print str(result)
        
if __name__ == "__main__":
    unittest.main()

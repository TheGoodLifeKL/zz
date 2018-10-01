# A0=dict(zip(('a','b','c','d','e'),(1,2,3,4,5)))
# print(A0)
import os 
def print_directory_contents(base_file):
    for child_file in os.listdir(base_file):
        child_file_path = os.path.join(base_file,child_file)
        if os.path.isdir(child_file_path):
            print_directory_contents(child_file_path)
        else:
            print (child_file_path)

dir = input('请输入:')
print_directory_contents(dir)
        

import os
import sys


src_path_str = "C:\\temp\\bdbook\\src"
dir_add_dict = dict()
summary_dict = dict()
for dirpath,dirnames,filenames in os.walk(src_path_str, topdown=True, onerror=None, followlinks=False):
    for file_name in filenames:
        if(file_name.endswith('.md')):
            rel_path = os.path.relpath(os.path.join(dirpath, file_name), src_path_str)
            if(rel_path.find(' ')==-1):
                prefix = ""
                rel_path_list = rel_path.split('\\')
                path_deep = len(rel_path_list)
                for i in range(1, path_deep) :
                    prefix = "\t{}".format(prefix)
                if(dir_add_dict.get(rel_path_list[0]) == None and path_deep>1):
                    dir_add_dict[rel_path_list[0]] = 1
                    summary_dict["{}- [{}]".format(prefix[1:], rel_path_list[0])] = "({})".format(rel_path)
                summary_dict["{}- [{}]".format(prefix, file_name[:-3])] = "({})".format(rel_path)
            else:
                print("path [{}] contain a blank".format(rel_path))
                sys.exit()
target_path = os.path.join(src_path_str,"auto_SUMMARY.md")
print("create SUMMARY into [{}]".format(target_path))
with open(target_path, 'w') as f:
    f.write("# Summary\n\n")
    for (k,v) in summary_dict.items():
        f.write(k+v+'\n')

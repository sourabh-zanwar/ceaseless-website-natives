import os
import pandas as pd
import shutil

f_list = []

with open('output_file.txt','wb') as wfd:
    for path, dirs, files in os.walk("/Users/sourabhzanwar/Desktop/CEASELESS/ceaseless-rating/uploads"):
        for filename in files:
            if filename != '.DS_Store' and filename !='output_file.txt':
                f_list.append(str(filename))
                with open(filename,'rb') as fd:
                    shutil.copyfileobj(fd, wfd)
            


for i in range(len(f_list)):
    f_list[i] = f_list[i][:-4]
    f_list[i] = f_list[i].split('_')
    
labels = ['workerid', 'code']    
df = pd.DataFrame(f_list, columns=labels)
df.to_csv('files.csv',index=False)
df.to_excel('files.xlsx',index=False)

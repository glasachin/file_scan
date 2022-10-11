import os
import time
from odf import text, teletype
from odf.opendocument import load

txt_email_files_path = []
txt_email_file = 'txt_email_file.txt'
f = open(txt_email_file,'w')
f.close()
txt_pass_file = 'txt_pass_file.txt'
f = open(txt_pass_file,'w')
f.close()


if __name__ == "__main__":
    for (root,dirs,files) in os.walk('/home/sachin', topdown=True):
        try:
            if len(files):
                for file in files:
                    if ('.txt' in file) | ('.csv' in file):
                        file_data = open(root+'/'+file,'r').read()
                        for txt_data in file_data.split('\n'):
                            txt_data_lower = txt_data.lower()
                            if ('email' in txt_data_lower)|('e-mail' in txt_data_lower):
                                txt_email_files_path.append(root+'/'+file)
                                open(txt_email_file, 'a').write(txt_data+'\n')
                            if ('password' in txt_data_lower)|('pass' in txt_data_lower):
                                txt_email_files_path.append(root+'/'+file)
                                open(txt_pass_file, 'a').write(txt_data+'\n')

                    elif ('.odt' in file):
                        textdoc = load(root+'/'+file)
                        allparas = textdoc.getElementsByType(text.P)
                        for odt_par in allparas:
                            odt_data = teletype.extractText(odt_par)
                            odt_data_lower = odt_data.lower()






        except Exception as e:
            print(file)
            break
        # print ('--------------------------------')
        # time.sleep(1)
# print(txt_files)
print(txt_email_files_path)
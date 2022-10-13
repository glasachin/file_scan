# This file search for the Credit card number in files
import os
import time
from odf import text, teletype
from odf.opendocument import load
import re
import luhn_algo

temp_files = ['txt_email_file.txt', 'txt_pass_file.txt', 'txt_card_file.txt']
for i in temp_files:
    f = open(i,'w')
    f.close

# txt_email_files_path = []
# txt_email_file = 'txt_email_file.txt'
# f = open(txt_email_file,'w')
# f.close()
# txt_pass_file = 'txt_pass_file.txt'
# f = open(txt_pass_file,'w')
# f.close()

# txt_card_file = 'txt_card_file.txt'
# f = open(txt_card_file,'w')
# f.close()


if __name__ == "__main__":
    for (root,dirs,files) in os.walk('/home/sachin', topdown=True):
        try:
            if len(files):
                for file in files:
                    if ('.txt' in file) | ('.csv' in file):
                        # print(file)
                        # if file == 'tst_case_file.txt':
                        #     print(file)
                        file_data = open(root+'/'+file,'r').read()
                        for txt_data in file_data.split('\n'):
                            txt_data_lower = txt_data.lower()
                            
                            # ----For Cards Information-------
                            txt_file_name = temp_files[2]
                            # cards_list = [s for s in re.findall(r"\d{16}", txt_data_lower)]
                            cards_list = [s for s in re.findall(r"[\d]{16}", txt_data_lower)]
                            if len(cards_list) > 0:
                                if file in temp_files: # to skip cards from our own list
                                    # print('own file')
                                    continue
                                card_file = open(txt_file_name, 'a')
                                for i in cards_list:
                                    if int(i) == 0: #to remove 00...00 entries
                                        continue
                                    i.replace(' ','')
                                    if luhn_algo.is_luhn_valid(i):
                                        card_file.write(i+'\n')
                                        # print(root,file, i)
                                card_file.close()

                            # if ('email' in txt_data_lower)|('e-mail' in txt_data_lower):
                            #     txt_email_files_path.append(root+'/'+file)
                            #     open(txt_email_file, 'a').write(txt_data+'\n')
                            # if ('password' in txt_data_lower)|('pass' in txt_data_lower):
                            #     txt_email_files_path.append(root+'/'+file)
                            #     open(txt_pass_file, 'a').write(txt_data+'\n')

                    # elif ('.odt' in file):
                    #     textdoc = load(root+'/'+file)
                    #     allparas = textdoc.getElementsByType(text.P)
                    #     for odt_par in allparas:
                    #         odt_data = teletype.extractText(odt_par)
                    #         odt_data_lower = odt_data.lower()
                    #         if ('email' in odt_data_lower)|('e-mail' in odt_data_lower):
                    #             print('file')
                    #             txt_email_files_path.append(root+'/'+file)
                    #             open(txt_email_file, 'a').write(odt_data+'\n')
                    #         if ('password' in odt_data_lower)|('pass' in odt_data_lower):
                    #             txt_email_files_path.append(root+'/'+file)
                    #             open(txt_pass_file, 'a').write(odt_data+'\n')

        except Exception as e:
            # print(e)
            # print(file)
            continue


# a_string = "Hi this is sachin +91-7503363236123456. I live in noida"
# result = [s for s in re.findall(r"\d{16}", a_string)]
# print(result)

# This file search for the Credit card number in files
import os
import time
from odf import text, teletype
from odf.opendocument import load
import re
import luhn_algo

temp_files = ['txt_email_file.txt', 'txt_pass_file.txt', 'txt_card_file.txt', 'txt_passport_file.txt']
for i in temp_files:
    f = open(i,'w')
    f.close

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
                            # ----for email information-------
                            txt_file_name = temp_files[0]
                            regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
                            email_list = [s for s in re.findall(regex, txt_data_lower)]
                            if len(email_list) > 0:
                                if file in temp_files: # to skip cards from our own list
                                    # print('own file')
                                    continue
                                email_file = open(txt_file_name, 'a')
                                for i in email_list:
                                    # if int(i) == 0: #to remove 00...00 entries
                                    #     continue
                                    i.replace(' ','')
                                    email_file.write(i+'\n')
                                email_file.close()

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

                            # ----For Passport Information-------
                            txt_file_name = temp_files[3]
                            regex = "^[A-PR-WYa-pr-wy][1-9]\\d\\s?\\d{4}[1-9]$"
                            passport_list = [s for s in re.findall(regex, txt_data_lower)]
                            if len(passport_list) > 0:
                                if file in temp_files: # to skip cards from our own list
                                    # print('own file')
                                    continue
                                passport_file = open(txt_file_name, 'a')
                                for i in passport_list:
                                    # if int(i) == 0: #to remove 00...00 entries
                                    #     continue
                                    i.replace(' ','')
                                    passport_file.write(i+'\n')
                                passport_file.close()



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

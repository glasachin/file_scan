# This file search for the Credit card number in files
import os
import time
from odf import text, teletype
from odf.opendocument import load
import re
import luhn_algo

# ------Global Area--------------
temp_files = ['txt_email_file.txt', 'txt_pass_file.txt', 'txt_card_file.txt', 'txt_passport_file.txt', 'txt_ssn_file.txt']
esc_char = [' ', '-']
for i in temp_files:
    f = open(i,'w')
    f.close

# ----------Functions------------
def find_emails(txt_data_lower, email_read_file, email_write_file):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    email_list = [s for s in re.findall(regex, txt_data_lower)]
    if len(email_list) > 0:
        write_file(email_list, email_read_file, email_write_file)
    return 1
def find_card_info(txt_data_lower,card_read_file,card_write_file):
    # lower_str: input string in lower case
    # cards_list = [s for s in re.findall(r"\d{16}", txt_data_lower)]
    # cards_list = [s for s in re.findall(r"[\d]{16}", txt_data_lower)]
    c_no = ''
    cards_list = []
    for char in txt_data_lower:
        if char.isdigit():
            c_no += char
            if len(c_no) == 16:
                if int(c_no) == 0:  # to remove 00...00 entries
                    c_no = ''
                    continue
                if luhn_algo.is_luhn_valid(c_no):
                    cards_list.append(c_no)
                c_no = ''
        elif char in esc_char:
            continue
        else:
            c_no = ''
            continue

    if len(cards_list) > 0:
        write_file(cards_list, card_read_file, card_write_file)
    return 1

def find_passport_info(txt_data_lower, pass_read_file, pass_write_file):
    regex = "[A-PR-WYa-pr-wy][1-9]\d\s?\d{4}[1-9]"
    passport_list = [s.upper() for s in re.findall(regex, txt_data_lower)]
    if len(passport_list) > 0:
        write_file(passport_list, pass_read_file, pass_write_file)

def find_ssn_info(txt_data_lower, ssn_read_file, ssn_write_file):
    regex = r'(\d{3}[- ]\d{2}[- ]\d{4})'
    ssn_list = [s.upper() for s in re.findall(regex, txt_data_lower)]
    if len(ssn_list) > 0:
        write_file(ssn_list, ssn_read_file, ssn_write_file)


def write_file(data_list, fl_name, wr_file):
    if fl_name in temp_files:  # to skip cards from our own list
        return 0
    data_file = open(wr_file, 'a')
    for i in data_list:
        data_file.write(i + '\n')
    data_file.close()
    return 1

# ---------------main function----------------------------------
if __name__ == "__main__":
    # for (root,dirs,files) in os.walk('/home/sachin', topdown=True):
    for (root, dirs, files) in os.walk('.', topdown=True):
        try:
            if len(files):
                for file in files:
                    if ('.txt' in file) | ('.csv' in file):
                        file_data = open(root+'/'+file,'r').read()
                        for txt_data in file_data.split('\n'):
                            txt_data_lower = txt_data.lower()
                            # ----for email information-------
                            txt_file_name = temp_files[0]
                            find_emails(txt_data_lower,file,txt_file_name)

                            # ----For Cards Information-------
                            txt_file_name = temp_files[2]
                            find_card_info(txt_data_lower,file,txt_file_name)

                            # ----For Passport Information-------
                            txt_file_name = temp_files[3]
                            find_passport_info(txt_data_lower, file, txt_file_name)

                            # -----For SSN Information--------------
                            txt_file_name = temp_files[4]
                            find_ssn_info(txt_data_lower, file, txt_file_name)

                    elif ('.odt' in file):
                        textdoc = load(root+'/'+file)
                        allparas = textdoc.getElementsByType(text.P)
                        for odt_par in allparas:
                            odt_data = teletype.extractText(odt_par)
                            odt_data_lower = odt_data.lower()

                            # ----for email information-------
                            txt_file_name = temp_files[0]
                            find_emails(odt_data_lower, file, txt_file_name)

                            # ----For Cards Information-------
                            txt_file_name = temp_files[2]
                            find_card_info(odt_data_lower, file, txt_file_name)

                            # ----For Passport Information-------
                            txt_file_name = temp_files[3]
                            find_passport_info(odt_data_lower, file, txt_file_name)

                            # -----For SSN Information--------------
                            txt_file_name = temp_files[4]
                            find_ssn_info(odt_data_lower, file, txt_file_name)

        except Exception as e:
            # print(e)
            # print(file)
            continue


# a_string = "Hi this is sachin +91-7503363236123456. I live in noida"
# result = [s for s in re.findall(r"\d{16}", a_string)]
# print(result)

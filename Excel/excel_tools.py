# -*- coding: utf-8 -*-

# read and write 2007 excel
import numbers

import openpyxl
import json
import os


# filePath="data/正确.xlsx"

def read_07_Excel_sheet(path,sheet_name='Sheet1'):
    wb = openpyxl.load_workbook(path)
    sheet = wb[sheet_name]
    return sheet

def print_entire_sheet(sheet):
    '''

    :param sheet: a sheet object
    :return:
    '''
    for row in sheet.rows:
        for cell in row:
            print(cell.value, "\t", end="")
        print()

'''
@:return a list of map {name:string,url:string,JSONdata:json} from Excel document
'''
def getAllNameJSONDataURL(path):
    data = []
    wb = openpyxl.load_workbook(path)
    sheet = wb['Sheet1']
    for row in sheet.rows:
        if (len(row)) >= 8:
            name = row[2].value
            url = row[7].value
            JSONdata = json.loads(row[8].value)
            data.append({"name": name, 'url': url, 'JSONdata': JSONdata})
    return data


def getNameURLList(path):
    '''

    :param path: excel document path
    :return: a list of map {name:string, url:string, JSONdata:json}
    '''
    data = []
    wb = openpyxl.load_workbook(path)
    sheet = wb['图片识别情况']
    for row in sheet.rows:
        if (len(row)) >= 3:
            name = row[2].value
            url = row[0].value
            JSONdata = ""
            data.append({"name": name, 'url': url, 'JSONdata': JSONdata})
    return data


def excel07_fill_in_blanks(path,row=None,col=None,range=[0,0]):
    wb = openpyxl.load_workbook(path)
    sheet = wb['Sheet1']
    previous_value=None
    if(col!=None):
        for cell in sheet[col][range[0]:range[1]]:
            if(cell.value!=None):
                print(cell.value)
                previous_value=cell.value
            else:
                print(previous_value)
    if(row!=None):
        for cell in sheet[row][range[0]:range[1]]:
            if(cell.value!=None):
                print(cell.value)
                previous_value=cell.value
            else:
                print(previous_value)

def get_selected_mentors(sheet,mentee_info_dict):
    mentor_mentee_dict_1st=dict()
    for row in sheet.rows:
        if row[2].value.lower()=="mentee":
            email = row[1].value.strip()
            first_will=int(row[4].value.split(" ")[0])
            second_will = int(row[5].value.split(" ")[0])
            if first_will not in mentor_mentee_dict_1st:
                mentor_mentee_dict_1st[first_will]=[email]
            else:
                mentor_mentee_dict_1st[first_will].append(email)
            # todo continue add to mentee info
            mentee_info_dict[email].append(row[6].value)
            mentee_info_dict[email].append(row[7].value)

    print("1st round mentor numbers:",len(mentor_mentee_dict_1st))
    for key in mentor_mentee_dict_1st.keys():
        print("{:3}".format(key),end=" ")
        # "{:3} mentees".format(len(mentor_mentee_dict_1st[key]))
        for email in mentor_mentee_dict_1st[key]:
            print(email,end=" ")
        print()
    return mentor_mentee_dict_1st

def get_mentee_info(sheet):
    mentee_info_dict=dict()
    for row in sheet.rows:
        if isinstance(row[0].value, int):
            index=int(row[0].value)
            name=row[1].value.strip()
            email=row[2].value.strip()
            print(index,name,email)
            mentee_info_dict[email]=[name]
    print(mentee_info_dict)
    return mentee_info_dict

def get_mentor_info(sheet):
    mentor_info_dict=dict()
    for row in sheet.rows:
        if isinstance(row[0].value, numbers.Rational):
            index=int(row[0].value)
            name=row[1].value.strip()
            email=row[2].value.strip()
            #print(index,name,email)
            mentor_info_dict[index]=name+" "+email
    print(mentor_info_dict)
    return mentor_info_dict

def change_email_info_name(sheet,mentee_info_dict,mentor_info_dict):
    for row in sheet.rows:
        for col in row:
            if not isinstance(col.value,int):
                if col.value in mentee_info_dict.keys():
                    print("{:30}".format(str(mentee_info_dict[col.value][0:3])+": "+col.value+","),end="")
            else:
                print("Mentor: {:50}".format(mentor_info_dict[col.value]),end="")
        print()




if __name__=="__main__":
    mentor_mentee_index_sheet_path = "/Users/yuyang/Downloads/Mentor & Mentee序号.xlsx"
    sheet_info = read_07_Excel_sheet(mentor_mentee_index_sheet_path, "Mentee")
    # print_entire_sheet(sheet_info)
    mentee_info_dict = get_mentee_info(sheet_info)

    print()
    path="/Users/yuyang/Downloads/Mentee选择Mentor意向和感谢信 - for all (Responses).xlsx"
    sheet=read_07_Excel_sheet(path,"Form Responses 1")
    mentor_mentee_dict_1st=get_selected_mentors(sheet,mentee_info_dict)

    sheet_info = read_07_Excel_sheet(mentor_mentee_index_sheet_path, "Mentor")
    mentor_info_dict = get_mentor_info(sheet_info)

    print()
    sheet = read_07_Excel_sheet(path, "Statistics")
    change_email_info_name(sheet,mentee_info_dict,mentor_info_dict)

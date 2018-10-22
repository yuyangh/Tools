# -*- coding: utf-8 -*-

# read and write 2007 excel
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

def get_selected_mentors(sheet):
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
        if isinstance(row[0].value, float):
            index=int(row[0].value)
            name=row[1].value.strip()
            email=row[2].value.strip()
            print(index,name,email)
            mentee_info_dict[email]=name
    # print(mentee_info_dict)
    return


if __name__=="__main__":
    path="/Users/yuyang/Downloads/Mentee选择Mentor意向和感谢信 - for all (Responses).xlsx"
    sheet=read_07_Excel_sheet(path,"Form Responses 1")
    mentor_mentee_dict_1st=get_selected_mentors(sheet)

    print()
    mentor_mentee_index_sheet_path="/Users/yuyang/Downloads/Mentor & Mentee序号.xlsx"
    sheet_info=read_07_Excel_sheet(mentor_mentee_index_sheet_path,"Mentee")
    get_mentee_info(sheet_info)

    # excel07_fill_in_blanks(path,col="F",range=[0,98])

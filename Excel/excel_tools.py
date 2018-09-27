# -*- coding: utf-8 -*-

# read and write 2007 excel
import openpyxl
import json
import os


# filePath="data/正确.xlsx"

def read07Excel(path):
    wb = openpyxl.load_workbook(path)
    sheet = wb['Sheet1']
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


'''
@:parameter path: excel document path 
@:return a list of map {name:string, url:string, JSONdata:json}'''
def getNameURLList(path):
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
                
if __name__=="__main__":
    path="/Users/yuyang/OneDrive/Research Symposium presentation schedule.xlsx"
    excel07_fill_in_blanks(path,col="F",range=[0,98])

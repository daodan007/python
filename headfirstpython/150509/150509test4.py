import pickle
import os
print(os.getcwd())

from test3_150509 import AthleteList

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:                #循环
        ath = get_coach_data(each_file)         #从文件中取出内容，给链接，返回List
        all_athletes[ath.name] = ath            #将内容放入字典
    try:
        with open('athletes.pickle', 'wb') as athf:    #打开pickle
            pickle.dump(all_athletes, athf)            #将文件写入pickle
    except IOError as ioerr:
        print('File error(put_and_store):'+ str(ioerr))
    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:    #打开pickle
            all_athletes = pickle.load(athf)           #取出pickle中数据
    except IOError as ioerr:
        print('File error(get_from_store):'+str(ioerr))
    return(all_athletes)

def get_coach_data(filename):            #给一个文件，返回一个AthleteList
    try:
        with open(filename) as f:                   #step1:打开文件
            data = f.readline()                     #step2:读出文件
        templ=data.strip().split(',')               #step3:分割文件
        return(AthleteList(templ.pop(0),templ.pop(0),templ))
    
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

def sanitize(time_string):
    if '_' in time_string:
        splitter = '_'
    elif ':' in time_string:
        splitter = ':'
    elif '-' in time_string:
        splitter = '-'
    else:
        return(time_string)

    (mins, sec) = time_string.split(splitter)
    return(mins+ ':' +sec)

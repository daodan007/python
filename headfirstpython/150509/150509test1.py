import os
os.chdir('python')

def sanitize(time_string):
    if '_' in time_string:
        splitter = '_'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, sec) = time_string.split(splitter)
    return(mins+ ':' +sec)

def get_coach_data(filename):
    try:
        with open(filename) as f:                   #step1:打开文件
            data = f.readline()                     #step2:读出文件
        templ=data.strip().split(',')               #step3:分割文件
        
        return({'name' : templ.pop(0),
                'dob' : templ.pop(0),
                'times' : str(sorted(set([sanitize(t) for t in templ]))[0:3])})
    
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

sarah = get_coach_data('sarah2.txt')
'''
sarah_data={}
sarah_data['name']=sarah.pop(0)
sarah_data['dob']=sarah.pop(0)
sarah_data['times']=sarah
print(sarah)
print(sarah_data['name']+"'s fastest times are: "+str(sorted(set([sanitize(t) for t in sarah_data['times']]))[0:3]))
'''
print(sarah['name']+"'s fastest times are:" +sarah['times'])

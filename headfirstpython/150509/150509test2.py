import os
os.chdir('python')

class Athlete:
    def __init__(self, a_name, a_dob=None, a_times=[]):
        self.name = a_name
        self.dob = a_dob
        self.times = a_times

    def top3(self):
        return(sorted(set([sanitize(t) for t in self.times]))[0:3])

    def add_time(self, time_value):
        self.times.append(time_value)

    def add_times(self, list_of_times):
        self.times.extend(list_of_times)

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

def get_coach_data(filename):
    try:
        with open(filename) as f:                   #step1:打开文件
            data = f.readline()                     #step2:读出文件
        templ=data.strip().split(',')               #step3:分割文件
        return(Athlete(templ.pop(0),templ.pop(0),templ))
    
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

sarah = get_coach_data('sarah2.txt')
sarah.add_time('1.2')
print(sarah.name+"'s fastest times are" + str(sarah.top3()))

from datetime import datetime,timedelta


'''


---------------
 -------------------------
     ---
             ---
                     -----
               --------
                   ---------

'''

def solution(lines):
    in_range_datetimes = list()
    max_throughput = 0
    timeout = 3
    current_line_index = 0
    moai = 0
    start = None
    while len(lines) > current_line_index:
        line = lines[current_line_index]
        end_date, end_time, working_sec = line.split(' ')
        end_datetime = datetime.strptime(end_date + end_time, '%Y-%m-%d%H:%M:%S.%f')
        sec = milli_sec = 0
        if working_sec.find('.') == -1:
            sec = int(working_sec.rstrip('s'))
        else:
            sec, milli_sec = map(int, working_sec.rstrip('s').split('.'))

        start_datetime = end_datetime - timedelta(seconds=sec, milliseconds=milli_sec-1)

        print(start_datetime, " ~ " , end_datetime, )
        print(end_datetime - start_datetime)
        if len(in_range_datetimes) == 0:
            in_range_datetimes.append([start_datetime, end_datetime])
            start = start_datetime


        # lineslines[current_line_index]
        while in_range_datetimes[moai][0]
        while in_range_datetimes[moai][0] > in_range_datetimes[moai][1
        '''
        while (in_range_datetimes[-1] - in_range_datetimes[0]) <= timedelta(seconds=1):
            in_range_datetimes.append(start_datetime)
            if max_throughput < len(in_range_datetimes):
                max_throughput = len(in_range_datetimes)
        else:
            in_range_datetimes.pop(0)

        '''
        current_line_index += 1

    print(in_range_datetimes)

    answer = 0
    return answer


data =  [
'2016-09-15 01:00:04.002 2.0s',
'2016-09-15 01:00:07.000 2s',
]


data = [
'2016-09-15 20:59:57.421 0.351s',
'2016-09-15 20:59:58.233 1.181s',
'2016-09-15 20:59:58.299 0.8s',
'2016-09-15 20:59:58.688 1.041s',
'2016-09-15 20:59:59.591 1.412s',
'2016-09-15 21:00:00.464 1.466s',
'2016-09-15 21:00:00.741 1.581s',
'2016-09-15 21:00:00.748 2.31s',
'2016-09-15 21:00:00.966 0.381s',
'2016-09-15 21:00:02.066 2.62s'
]





print(solution(data))

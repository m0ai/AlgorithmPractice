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


def process_datetime(line):
    end_date, end_time, working_sec = line.split(' ')
    end_datetime = datetime.strptime(end_date + end_time, '%Y-%m-%d%H:%M:%S.%f')
    sec = milli_sec = 0
    if working_sec.find('.') == -1:
        sec = int(working_sec.rstrip('s'))
    else:
        sec, milli_sec = map(int, working_sec.rstrip('s').split('.'))
    start_datetime = end_datetime - timedelta(seconds=sec, milliseconds=milli_sec-1)

    return start_datetime, end_datetime, working_sec

    #print(start_datetime, " ~ " , end_datetime, )
    #print(end_datetime - start_datetime)
def solution(lines):
    in_range_datetimes = list()
    max_throughput = 0
    timeout = 3
    current_line_index = 0
    moai = 0
    start = None

    current_line_index = len(lines)-1
    max_request_per_second = 0

    ends = list()
    ends_index = list()
    starts = list()
    starts_index = list()

    while 0 < current_line_index:
        if len(in_range_datetimes) > max_request_per_second:
            max_request_per_second = len(in_range_datetimes)

        print(current_line_index)
        line = lines[current_line_index]
        start_datetime, end_datetime, working_sec = process_datetime(line)

        if len(in_range_datetimes) == 0:
            ends.append([current_line_index, end_datetime])
            ends.sort(reverse=True, key=lambda x: x[1])

            starts.append([current_line_index,start_datetime])
            starts.sort(key=lambda x: x[1])

            in_range_datetimes.append( current_line_index )

            max_request_per_second = len(in_range_datetimes)

            current_line_index -= 1
            continue

        lastest_end = ends[0][1]
        nearly_start = starts[0][1]



        # if end - new_start > 1 sec
        if  (lastest_end - nearly_start) > timedelta(seconds=1):
            # Remove Lastest End in dict and starts
            i, end = ends.pop()
            in_range_datetimes.remove(i)

            # Added New start Datetime
            starts.append([current_line_index, start_datetime])
            starts.sort(key=lambda x: x[1])

            in_range_datetimes.append( current_line_index )
            current_line_index -= 1
            continue

        elif (lastest_end - nearly_start) < timedelta(seconds=1):
            # Added New start Datetime
            starts.append([current_line_index, start_datetime])
            starts.sort(key=lambda x: x[1])

            in_range_datetimes.append( current_line_index )
            current_line_index -= 1
            continue
        print("WTF")
        continue


    answer = 0

    for start, end in in_range_datetimes:
        print(start,end)


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

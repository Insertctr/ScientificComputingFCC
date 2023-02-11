#Pair programmed in real time with Sidharth Anand 
def add_time(start_time, duration, day=None):
    week = ['sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday']
    message = None
    result_hr = None
    result_mn = None
    result_day = None
    day_no = 0
    final_result = []


    # Start Time
    temp = tuple(start_time.split())
    start_time_list = [int(x) for x in temp[0].split(':')]
    start_time_list.append(temp[1])
    
    # converting time to 24 hour format
    if start_time_list[2] == 'PM' and start_time_list[0] != 12: 
        start_time_list[0] += 12

    elif start_time_list[2] == 'AM' and start_time_list[0] == 12:
        start_time_list[0] = 0


    # Duration 
    duration_list = [int(x) for x in duration.split(':')]
    no_of_days = duration_list[0]//24
    duration_list[0] %= 24


    # Time Calculation 
    result_mn, result_hr = (start_time_list[1] + duration_list[1])%60, (start_time_list[1] + duration_list[1])//60
    result_hr = (result_hr + start_time_list[0] + duration_list[0])%24
    
    am_pm = 'AM'
    if result_hr >= 12: 
        am_pm = 'PM'
        
    if result_hr > 12: 
        result_hr %= 12
    elif result_hr == 0: 
        result_hr = 12
        
    if (start_time_list[2] == 'PM' and am_pm == 'AM'): 
        no_of_days += 1


    # Storing the days message 
    if no_of_days == 1: 
        message = '(next day)'
    elif no_of_days > 1: 
        message = f'({no_of_days} days later)'


    # If day is given
    if day != None: 
        day = day.lower()
        for i in range(len(week)): 
            if week[i] == day: 
                day_no = i
                break

        day_no = (day_no + no_of_days)%7
        result_day = week[day_no].capitalize()

    
    # Final Output
    final_result.append(str(result_hr) + ':')
    final_result.append('0' + str(result_mn) if result_mn <= 9 else str(result_mn))
    final_result.append(' ' + am_pm)

    if day != None: 
        final_result.append(', ' + result_day)

    if no_of_days > 0: 
        final_result.append(' ' + message)

    return ''.join(final_result)
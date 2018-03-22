initial_hr = 6
initial_min = 52

easy_hr = 1
easy_min = 23

tempo_hr = 0
tempo_min = 20

easy_time_hr = 2 * easy_hr
easy_time_min = 2 * easy_min

tempo_time_hr = 3 * tempo_hr
tempo_time_min = 3 * tempo_min

total_hr = easy_time_hr + tempo_time_hr
total_min = easy_time_min + tempo_time_min

time_hr = initial_hr + total_hr
time_min = initial_min + total_min

if(time_min > 60):
    time_hr += time_min / 60
    time_min %= 60

print ("Breakfast time : %d:%d AM\n" %(time_hr, time_min))

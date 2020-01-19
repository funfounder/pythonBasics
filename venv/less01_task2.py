user_time_sec = int(input('Insert time in seconds: '))

minutes = int(user_time_sec / 60)
hours = int(minutes / 60)
print(f'The time is {hours:02}:{minutes%60:02}:{user_time_sec%60:02}')

# if user_time_sec >= 3600:
#     hours = user_time_sec // 3600
#     if hours < 10:
#         hours = f'0{hours}'
#     minutes = user_time_sec % 60
#     if minutes < 10:
#         minutes = f'0{minutes}'
#     seconds = user_time_sec % 60
#     if seconds < 10:
#         seconds = f'0{seconds}'
#     print(f'The time is {hours}:{minutes}:{seconds}.')
# elif user_time_sec >= 60 and user_time_sec < 3600:
#     minutes = user_time_sec // 60
#     if minutes < 10:
#         minutes = f'0{minutes}'
#     seconds = user_time_sec % 60
#     if seconds < 10:
#         seconds = f'0{seconds}'
#     print(f'The time is 00:{minutes}:{seconds}.')
# elif user_time_sec < 60:
#     if user_time_sec < 10:
#         user_time_sec = f'0{user_time_sec}'
#     print(f'The time is 00:00:{user_time_sec}.')
# else:
#     print('You type incorrect time.')

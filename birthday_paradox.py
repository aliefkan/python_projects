# import random
# import datetime
# import random
# def dates(start, end):
#     print("Please enter the years that we will take samples from.")
#     difference = (end - start)*365 + (end - start)/4
#     return difference
#
# start_year = int(input("Enter the starting year: "))
# end_year = int(input("Enter the ending year: "))
# start_date = str(start_year) + "0101"
# end_date = str(end_year) + "0101"
#
#
# def list_of_birthdays():
#     list_of_bd = []
#     num_of_bd = 0
#     while num_of_bd < 1000:
#         random_num = random.randrange(int(dates(start_year, end_year)))
#         random_date = int(start_date) + random_num
#         list_of_bd.append(random_date)
#         num_of_bd += 1
#         if num_of_bd == 1000:
#             break
#     return list_of_bd
#
# def converted_dates():
#     li_bd = list_of_birthdays()
#     converted_list = []
#     for date in li_bd:
#         converted_list.append(datetime.datetime.strptime(date, '%m%d'))
#     return converted_list
#
# def same_bd():
#     sample_list = converted_dates()

import random
import datetime

start_year = int(input("Enter the starting year: "))
end_year = int(input("Enter the ending year: "))
start_date = str(start_year) + "0101"
end_date = str(end_year) + "0101"
def date_generator(n, d):
    i = 0
    date_list = []
    while i < n:
        random_num = random.randrange(int(d))
        random_date = datetime.datetime.strptime(start_date, '%Y%m%d') + datetime.timedelta(days=random_num)
        modif_date = random_date.strftime('%m%d')
        date_list.append(modif_date)
        i+=1
        if i == n:
            break
    percentage = (len(set(date_list)) / len(date_list)) * 100
    return print(date_list, "\n",  set(date_list), "\n" , len(date_list), "\n", percentage, "%" )
def dates(start, end):
    print("Please enter the years that we will take samples from.")
    difference = (end - start)*365 + (end - start)/4
    return int(difference)

date_generator(70, dates(start_year,end_year))



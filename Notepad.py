# Bot консольный
weekday_list = ['Day_1', 'Day_2', 'Day_3', 'Day_4', 'Day_5', 'Day_6', 'Day_7']
weekdays = {1: 'Day_1.txt', 2: 'Day_2.txt', 3: 'Day_3.txt', 4: 'Day_4.txt', 5:
    'Day_5.txt', 6: 'Day_6.txt', 7: 'Day_7.txt'}
day = int(input('Введите день недели ( от 1 до 7): '))
schedule_change = int(input('Введите \n1 для чтения \n2 для записи \n3 для изменения \n '))

if schedule_change == 1:
    with open(weekdays[day], 'r', encoding='utf-8') as my_fix:
        my_fix.readlines()
elif schedule_change == 2:
 event = input('Впишите заметку на день: ')
 with open(weekdays[day], 'a', encoding='utf-8') as my_fix:
     my_fix.write(event)
elif schedule_change == 3:
    event = input('Впишите свои изменения: ')
    with open(weekdays[day], 'w', encoding='utf-8') as my_fix:
        my_fix.write(event)

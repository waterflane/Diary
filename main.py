import text
import datetime

def write():
    print('Напишите небольшой текст на 1 предложение:')
    now_text = input()
    f = open('diary/diary.txt', 'a', encoding='utf-8')
    f.write(f'{datetime.datetime.now()}--!--{now_text}\n')
    f.close()

def read():
    try:
        f = open('diary/diary.txt', 'r', encoding='utf-8')
    except FileNotFoundError:
        f_helper = open('diary/diary.txt', 'a', encoding='utf-8')
        print('Ничего оне найденно!')
        f_helper.close()
        print('Enter чтобы продолжить')
        now_text = input()
    else:
        len_F = sum(1 for _ in f)
        if len_F == 0: print('Ничего оне найденно!')
        else: print(f.readlines())
        f.close()
        print('Enter чтобы продолжить')
        now_text = input()

def alarm_st():
    print('Напишите напоминание')
    now_text = input()

    print('Напишите дату, когда вам напомнить об этом в формате: Y, M, D')
    now_text = input()
    list_date = list(map(int, now_text.split(', ')))
    date = datetime.date(list_date[0], list_date[1], list_date[2])

    f = open('diary/alarm_text.txt', 'a', encoding='utf-8')
    f.write(f'{date}---!---{now_text} \n')
    f.close()
    text.ALARM_NEW = True


def main():
    print(text.TEXT_COMMAND)
    # alarm.main()
    match input():
        case 'w': write()
        case 'r': read()
        case 'a': alarm_st()
        case 'q': exit()
    main()


if __name__ == "__main__": 
    main()

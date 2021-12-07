"""
Домашнее задание №2

Работа с файлами


1. Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
2. Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
3. Подсчитайте количество слов в тексте
4. Замените точки в тексте на восклицательные знаки
5. Сохраните результат в файл referat2.txt
"""
import shutil

def main():

    with open ('referat.txt', "r", encoding='utf-8') as f:
        shutil.copyfile("C:\\projects\\learn-homework-2\\referat.txt","C:\\projects\\learn-homework-2\\referat2.txt")

    with open ('referat2.txt', "r", encoding='utf-8') as s:
        content = s.read()

    with open ('referat2.txt', "w+", encoding='utf-8') as s:    

        str_content = str(content)
        words = str_content.split()
        str_content_2 = str_content.replace('.','!')
        s.write(str_content_2)
        print(str_content_2)
        print (f'\nКоличество символов в строке - {len(str_content)}')
        print(f'\nКоличество слов в тексте - {len(words)}')   

if __name__ == "__main__":
    main()

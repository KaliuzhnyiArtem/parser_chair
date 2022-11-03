Скрипт витягує данні з сторінки
https://home-club.com.ua/ua/sku-90507603?gclid=CjwKCAjwzY2bBhB6EiwAPpUpZhSieA2DRWXhLcbNCpIvJcC9dLHc534Djx5FKNpL9iXaLZlSQaNyLBoCEwYQAvD_BwE

- Артикуль
- Наявність для поставки
- Прогноз наявності в Польщі
- Наявність у Львові:


Для використання виконати наступні кроки
1. Відкрити термінал, зайти в папку в яку будете клонувати репозиторій

2. Клонувати репозиторій
Команда: git clone https://github.com/KaliuzhnyiArtem/parser_chair.git

3. Створити віртуальне середовище(якщо у вас вже встановлений python)
Команда: python3 -m venv venv

4. Активувати віртуальне середовище
Команда: source venv/bin/activate

5. Встановити всі необхідні залежності
Команда: pip install requirements.txt

6. В проєкті використовується chromedriver версії 106.0.5249
Перевірте свою версію Google Chrome.
Для цього виконайте наступні кроки:
        - Відкрийте браузер
        - в правому верхньому кутку натисніть 3 крапки
        - Справка
        - Про бразері Google Chrome

Якщо версія співпада переходьте до наступно пункту №7.

Якщо ні перейдіть по посиланню https://chromedriver.storage.googleapis.com/index.html
і скачайте версію chromedriver відповідно до верісї  вашого браузера

Помістіть розпакований файл у папку проєкта замінивши старий

7. Відкрити файл main.py.
В 6 рядку потрібно змінити данні на ваші
driver_service = Service(executable_path='Сюди впишіть ваш шлях до файла chromedriver')

8. Запустити програму
Команда: python3 main.py

9. Після виконання результат буде записаний у файл homeclub.txt



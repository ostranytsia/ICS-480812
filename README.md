<center><b>
Київський Національний Торговельно-Економічний Університет

Кафедра комп'ютерних наук та інформаційних систем
</center></b>

---

<center><h2><b>ЛАБОРАТОРНИЙ ПРАКТИКУМ</b></h2><br>

*з дисципліни __"Уведення в комп'ютерні науки"__*<br>
**Завдання №12**

Студента 1 курсу, 4 групи ФІТ<br>
**Остраниці Дмитра Миколайовича**</center>

---


<br>
<b>ПОСТАНОВКА ЗАДАЧІ</b><br>
Розробити програмне забеспечення (ПЗ), яке виріщує задачу розрахунку і аналізу руху основних засобів на основі вхідних даних з таблиць 1 і 2.
<br><br>

**Вимоги до ПЗ:**<br>
   1. Мова програмування - PYTHON
   2. Вхідні дані розміщені в локальних текстових файлах
   3. Результати представляються у вигляді:
       * Таблиці на екрані комп'ютера
       * Текстового файла на диску
       * Структорованого файла в форматі JSON
       * Exel таблиці
       * Графіка на екрані комп'ютера
   4. В процесі роботи програма повинна мати можливість виводити на екран вхідні дані у вигляді відповідних таблиць (див. табл. 1, 2) та надавати можливість відбору записів із довідника по критерію.
<br><br>

---
<br>

**Вхідні дані**
<br><br>

<p align="right">Таблиця 1</p>
<center><b>Рух основних засобів</b></center>

Підприємство | Код виду основних засобів | Залишок на 01.01.2018 | Надійшло у 2018 | Вибуток у 2018
:--- | :---: | :---: | :---: | :---:
Універсам 22 | 1 | 44 048,00 | 500,00 | 200,00
Дніпрянка | 1 | 22 456,00 | 365,00 | 123,00
Універсам 22 | 2 | 5 564,00 | 2 571,00 | 135,00
Дніпрянка | 2 | 10 087,00 | 15 972,00 | 58,00
Універсам 22 | 3 | 0,00 | 0,00 | 0,00
Дніпрянка | 3 | 206,00 | 34,00 | 50,00
Універсам 22 | 4 | 116,00 | 64,00 | 23,00
Дніпрянка | 4 | 34,00 | 23,00 | 25,00

<br><br>
<p align="right">Таблиця 2</p>
<b>Довідник видів основних засобів</b>

Код виду основних засобів | Вид основних засобів
:---: | ---
1 | Будівлі
2 | Машини та обладнення
3 | Транспортні засоби
4 | Інструмент та інвентар

<br><br>
---
<br><br>

**Вихідні дані**

<p align="right">Таблиця 3</p>
<b>АНАЛІЗ РУХУ ОСНОВНИХ ЗАСОБІВ</b>

Підприємство | Вид основних засобів | Залишок на 01.01.18 | Надійшло у 2018 | Вибуло у 2018 | Залишок на 01.01.19 | Зміни вартості за рік
--- | --- | ---: | ---: | ---: | ---: | ---:
Дніпрянка | Будівлі | 22456 | 365 | 123 | 22698 | 242
Дніпрянка | Машини та обладнення | 10087 | 15972 | 58 | 26001 | 15914
Дніпрянка | Транспортні засоби | 206 | 34 | 50 | 190 | -16
Дніпрянка | Інструмент та інвентар | 34 | 23 | 25 | 32 | -2
Універсам 22 | Будівлі | 44048 | 500 | 200 | 44348 | 300
Універсам 22 | Машини та обладнення | 5564 | 2571 | 135 | 8000 | 2436
Універсам 22 | Транспортні засоби | 12 | 33 | 3 | 42 | 30
Універсам 22 | Інструмент та інвентар | 116 | 64 | 23 | 157 | 41
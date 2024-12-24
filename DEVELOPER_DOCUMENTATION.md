# Документация разработчика

## Текст программы

### Наименование программы

**ColorConverterApp** — приложение для конвертации и визуализации цветов между цветовыми моделями CMYK, LAB и HSV на языке Python с использованием библиотеки Tkinter.

### Область применения

Программа предназначена для визуализации работы с цветовыми моделями и их взаимных преобразований. Она может быть использована в учебных целях, а также для выбора и анализа цветов в графических или печатных проектах.

### Назначение программы

- Конвертация цветов между следующими цветовыми моделями:
  - CMYK (Cyan, Magenta, Yellow, Black)
  - LAB (Lightness, A, B)
  - HSV (Hue, Saturation, Value)
- Выбор цвета с помощью цветового диалога.
- Отображение выбранного (или сконвертированного) цвета в виде цветового превью.
- Ввод и изменение значений цветов через ползунки или текстовые поля.

### Функциональные возможности

- Ввод значений цветов в одной из моделей (CMYK, LAB или HSV) с автоматической конвертацией в другие модели.
- Выбор цвета через встроенный диалог выбора цвета.
- Отображение текущего цвета в виде цветового превью.
- Взаимодействие с пользователем через графический интерфейс (GUI).

---

## Описание программы

### Структура программы

- **Главное окно приложения**:
  - Отображение текущего цвета в виде цветового блока.
  - Ввод значений цветов через ползунки и текстовые поля для каждой цветовой модели.
  - Кнопка "Choose color" для открытия диалога выбора цвета.
- **Основные функции**:
  - `cmyk_to_rgb(c, m, y, k)`: преобразование значений CMYK в RGB.
  - `rgb_to_cmyk(r, g, b)`: преобразование значений RGB в CMYK.
  - `update_preview(r, g, b)`: обновление цветового блока на основе значений RGB.
  - `update_colors_from_cmyk(c, m, y, k)`: обновление LAB и HSV на основе значений CMYK.
  - `update_from_cmyk`, `update_from_lab`, `update_from_hsv`: обработка изменений значений в каждой из моделей.
  - `choose_color`: выбор цвета с помощью встроенного диалога.
- **Цветовые модели и их преобразования**:
  - Используются библиотеки `colormath` для преобразования между моделями LAB, HSV и RGB.
  - Функции `convert_color` реализуют преобразования между цветовыми пространствами.

---

### Используемые библиотеки и модули

- **tkinter**: стандартная библиотека Python для создания GUI.
- **colormath**: библиотека для работы с цветовыми пространствами.
- **colorchooser**: встроенный диалог выбора цвета из библиотеки tkinter.

---

### Логические структуры данных

- **Переменные для каждой цветовой модели**:
  - CMYK: `cmyk_c`, `cmyk_m`, `cmyk_y`, `cmyk_k` — значения цветов CMYK.
  - LAB: `lab_l`, `lab_a`, `lab_b` — значения цветов LAB.
  - HSV: `hsv_h`, `hsv_s`, `hsv_v` — значения цветов HSV.
- **Флаги для предотвращения рекурсивного обновления**:
  - `updating_cmyk`, `updating_lab`, `updating_hsv` — используются для предотвращения бесконечных циклов при обновлении значений.

---

### Взаимодействие с пользователем

1. **Ввод значений цвета**:
   - Пользователь может вводить значения через ползунки или текстовые поля для каждой из моделей (CMYK, LAB или HSV).
   - При изменении значений происходит автоматическое обновление других цветовых моделей.
2. **Выбор цвета**:
   - Пользователь может выбрать цвет через диалоговое окно выбора цвета.
   - Выбранный цвет автоматически преобразуется во все цветовые модели и отображается в цветовом блоке.
3. **Цветовое превью**:
   - Текущий цвет отображается в виде блока, который обновляется при изменении значений.

---

## Инструкция по установке и запуску

### Требования к системе

- **Python** версии 3.6 и выше.
- Установленные библиотеки `tkinter` и `colormath`.

### Установка

1. **Убедитесь, что установлен Python**:
   ```
   python --version
   ```

2. **Установите библиотеку colormath**:
   ```
   pip install colormath
   ```

3. **Проверьте наличие tkinter**:
   - Для Ubuntu/Debian:
     ``
     sudo apt-get install python3-tk
     ```

### Запуск программы

1. Сохраните код программы в файл с расширением `.py`, например, `color_converter.py`.

2. Запустите программу:
  
   python color_converter.py
  

---

## Инструкция пользователя

1. **Ввод значений**:
   - Введите значения цвета в одном из полей (CMYK, LAB или HSV).
   - Используйте ползунки для изменения значений.
   - Остальные модели автоматически обновятся.

2. **Выбор цвета**:
   - Нажмите кнопку "Choose color", чтобы выбрать цвет через встроенный диалог.
   - Выбранный цвет автоматически отобразится в цветовом блоке.

3. **Отображение цвета**:
   - Цвет, соответствующий текущим значениям, отображается в блоке "Your color".

---

## Требования к техническим характеристикам

- **Процессор**: не менее 1 ГГц.
- **Оперативная память**: не менее 512 МБ.
- **Дисплей**: поддержка разрешения не менее 1024x768.

---

## Обработка ошибок

- **Некорректный ввод**:
  - Если пользователь вводит некорректные значения (например, значения вне диапазона), данные не будут обработаны.
- **Сообщения об ошибках**:
  - Ошибки отображаются в консоли (терминале), откуда был запущен скрипт.

---

## Дополнительные сведения

### Цветовые модели

1. **CMYK**:
   - Основана на синтезе субтрактивных цветов.
   - Используется для печати.

2. **LAB**:
   - Цветовая модель, основанная на восприятии человека.
   - Используется для точной цветокоррекции.

3. **HSV**:
   - Цветовая модель, близкая к восприятию цвета человеком.
   - Удобна для выбора цвета по тону, насыщенности и яркости.

### Преобразования

- Преобразования между цветовыми пространствами выполняются с использованием библиотеки `colormath`.
- Основные функции: `convert_color`, `cmyk_to_rgb`, `rgb_to_cmyk`.

---

## Сопровождение и развитие

- Код программы хорошо документирован и снабжен комментариями.
- Для добавления новых функций (например, других цветовых моделей) можно расширить существующие функции или добавить новые.

## Заключение

Программа **ColorConverterApp** предоставляет удобный инструмент для работы с цветовыми моделями, их преобразованиями и визуализацией. Она может быть использована как в учебных целях, так и в практических задачах, связанных с выбором и анализом цветов.
Чтобы создать .exe файл из Python-кода, используется библиотека pyinstaller. Вот пошаговая инструкция:
1. Установите библиотеку pyinstaller
Откройте терминал в PyCharm или командную строку и выполните:
Copy
pip install pyinstaller
2. Подготовьте ваш .py файл
Убедитесь, что ваш Python-скрипт работает корректно. Например, пусть у вас есть файл main.py, который вы хотите превратить в .exe.

3. Создайте .exe файл с помощью pyinstaller
В терминале PyCharm выполните следующую команду:
Copy
pyinstaller --onefile main.py
--onefile: объединяет все файлы в один .exe.
main.py: это ваш Python-скрипт.
После выполнения команды в папке проекта появятся новые директории, такие как build и dist.
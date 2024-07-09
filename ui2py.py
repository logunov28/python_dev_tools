import os

# Узнаём версию PyQt
pip_list = os.popen('pip list').read().split('\n')
qt_version = None
for i in range(len(pip_list)):
    if 'PyQt' in pip_list[i]:
        qt = pip_list[i][0:5]
        qt_version = qt[-1]
        break


if qt_version is None:
    print('Библиотека PyQt не установлена!')
    os.popen('pause')

# Конвертируем
else:
    print("Это конвертер для преобразования файла, созданного в Qt Designer, в файл с расширением py.")
    ui_file = input('Введите путь к исходному файлу:')
    py_file = input('Введите имя, под которым нужно сохранить файл (например, gui.py):')
    os.popen('pyuic' + qt_version + ' ' + ui_file+ ' -o ' + py_file)
    print('Готово! Результат лежит в одной папке с этим скриптом. Нажмите любую клавишу, чтобы выйти.')
    os.popen('pause')
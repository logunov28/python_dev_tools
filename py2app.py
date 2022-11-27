import os, subprocess, shutil
from time import sleep

# Проверяем, установлен ли pyinstaller
pip_list = os.popen('pip list').read().split('\n')
is_PI_installed = 0
for i in range(len(pip_list)):
    if 'pyinstaller' in pip_list[i]:
        is_PI_installed = 1

# Устанавливаем pyinstaller
if is_PI_installed == 0:
    subprocess.run('pip install pyinstaller')

py_file = input('Введите путь к исходному файлу:')
doc_path = py_file.split('\\')
py_file = doc_path[-1]
doc_path[-1] = 'dist"'


to_remove = doc_path.copy()
to_remove[-1] = 'build"'
to_remove = "\\".join(to_remove)

app_dir = doc_path.copy()
app_dir[-1] = '"'
app_dir = "\\".join(app_dir)

result = "\\".join(doc_path)

app_dir = app_dir.replace('"', '')
os.chdir(app_dir)

subprocess.run('pyi-makespec ' + py_file)
sleep(1)

py_file = py_file.replace('"', '')
if py_file.endswith('.py'):
    spec_file = py_file.replace('.py', '.spec')
elif py_file.endswith('.pyw'):
    spec_file = py_file.replace('.pyw', '.spec')

subprocess.run('pyinstaller ' + spec_file)
sleep(1)
to_remove = to_remove.replace('"', '')

shutil.rmtree(to_remove, ignore_errors=True)
spec_file = spec_file.replace('"', '')
os.remove(spec_file)

print('Программа собрана и лежит в папке: ' + result)
os.popen('@pause')

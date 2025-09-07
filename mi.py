import os
import sys
import subprocess

def main():
    # Путь к файлу mi_5.2.pyc
    pyc_file = "mi_5.2.pyc"
    
    # Проверяем существование файла
    if not os.path.exists(pyc_file):
        print(f"Ошибка: Файл {pyc_file} не найден!")
        input("Нажмите Enter для выхода...")
        sys.exit(1)
    
    try:
        # Запускаем файл .pyc с теми же аргументами командной строки
        # и заменяем текущий процесс
        os.execv(sys.executable, [sys.executable, pyc_file] + sys.argv[1:])
        
    except Exception as e:
        print(f"Ошибка при запуске файла: {e}")
        input("Нажмите Enter для выхода...")
        sys.exit(1)

if __name__ == "__main__":
    main()

path=('Path_to_file')

def total_salary(path) -> tuple:
    total_salary = 0
    num_developers = 0

    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                try:
                    # Розділяємо рядок на ім'я та заробітну плату
                    name, salary_str = line.split(',')
                    # Перетворюємо заробітну плату у дійсне число
                    salary = float(salary_str)
                    # Додаємо зарплату до загальної суми
                    total_salary += salary
                    # Рахуємо к-ть працівників
                    num_developers += 1
                except ValueError:
                    # Ігноруємо рядки, де немає зарплати або вона не є числом
                    pass
    #Опрацьовуємо можливі помилки читання файлу
    except FileNotFoundError:
        print(f"File '{path}' not found.")
        return None
    except Exception as e:
        print(f"Error occurred: {e}")
        return None

    # Обчислюємо середню заробітну плату
    average_salary = total_salary / num_developers

    return (total_salary, average_salary)

# Приклад використання
total, average = total_salary(path)

if total > 0:
    print(f"Загальна сума заробітної плати: {total:.2f}, Середня заробітна плата: {average:.2f}")
else:
    print(f"Загальна сума заробітної плати: {total:.2f} не може бути від'ємним значенням. Перевірте файл: \n{path}")
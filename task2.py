path = ('Path')

def get_cats_info(path) -> list[dict]:
    #Оголошую порожній словник
    cats_info = []
    try:
        with open (path, 'r', encoding='utf-8') as file:
            #Оголошою ключі що повинні бути у словниках
            keys = ['id','name','age']
            for line in file:
                try:
                    #Розділяю кожен рядок файлу на окремі значення
                    values = line.strip().split(',')
                    #Обєднюю ключі із значеннями та додаю до порожнього словнику 
                    cat_info=dict(zip(keys,values))
                    cats_info.append(cat_info)
                    #Обробляю можливі помилки читання рядків файлу
                except Exception as e:
                    print(f'Error occurred while processing line: {line}. Error: {e}')
    #Обробляю можливі помилки читання файлу                
    except FileNotFoundError:
        print(f'File: {path}, not found')
    except Exception as e:
        print(f'Error occured: {e}')
    return(cats_info)

print(get_cats_info(path))
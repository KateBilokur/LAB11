import csv
flag = False
try:
    # Відкриття файлу для читання
    with open("world_gdp.csv", "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Виведення заголовка для даних
        print("Country Name: GDP per capita (2019)")

        # Перевірка, чи є потрібні дані у файлі
        for row in reader:
            try:
                if row['Year'] == '2019':
                    print(f"{row['Country Name']}: {row['GDP per capita (current US$)']}")
            except KeyError:
                print("Помилка: відсутні потрібні поля у файлі.")
                break

    csvfile.close()

except FileNotFoundError:
    print("Файл 'world_gdp.csv' не знайдено!")


try:
    # Відкриття файлу для читання
    with open("world_gdp.csv", "r", encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        # Запит у користувача назви країни для пошуку
        search_country = input("\nВведіть назву країни для пошуку даних GDP per capita (2019): ")

        with open("search_results.csv", "w", newline='', encoding='utf-8') as csvfile2:
            writer = csv.writer(csvfile2)
            writer.writerow(["Country Name", "GDP per capita (2019)"])

            # Шукаємо країну у файлі та записуємо результат
            for row in reader:
                if row['Country Name'].lower() == search_country.lower() and row['Year'] == '2019':
                    writer.writerow([row['Country Name'], row['GDP per capita (current US$)']])
                    print(f"\nРезультат знайдено: {row['Country Name']} - {row['GDP per capita (current US$)']}")
                    flag = True

        csvfile2.close()

    # Якщо результат не знайдено
    if not flag:
        print(f"Даних для країни '{search_country}' за 2019 рік не знайдено.")

    csvfile.close()

except FileNotFoundError:
    print("Файл 'world_gdp.csv' не знайдено!")
except Exception as e:
    print(f"Виникла помилка: {e}")

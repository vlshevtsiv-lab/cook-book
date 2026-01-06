import os


FILE_NAME = "recipies.txt"
SEPARATOR = "---RECIPE_END---"

def load_recipes():
    """"Читає рецепти з файлу i повертає список словників (Dictionary).
    Чекліст: Використано роботу з файлами (читання), обробку помилок (try/except), різні типи даних (список, словник)."""
    recipes = []
    try:
        with open(FILE_NAME, 'r', encoding='utf-8') as file:
            content = file.read()
            raw_recipes = content.strip().split(SEPARATOR)

            for raw in raw_recipes:
                raw = raw.strip()
                if not raw:
                    continue

                parts = raw.split('\n\n')
                if len(parts) >= 3:
                    title = parts[0].replace("Ha3Ba: ", "").strip()
                    ingrediants = parts[1].replace("IHrpegieHTn: \n", "").strip()
                    instructions = parts[2].replace("IHcTpykuia:\n", "").strip()

                    recipes.append({
                        "title": title,
                        "Ingrediants": ingrediants,
                        "instructions": instructions
                    })

    except FileNotFoundError:
        print("Файл із рецептами не знайдено. Створено нову книгу рецептів.")
    except Exception as e:
        print(f"Виникла помилка при читанні файлу: {e}")

    return recipes


import requests

def get_superheroes():
    response = requests.get('https://akabab.github.io/superhero-api/api/all.json')
    return response.json()

def filter_superheroes(gender, has_job):
    superheroes = get_superheroes()
    filtered_superheroes = [hero for hero in superheroes if hero['appearance']['gender'] == gender and ('work' in hero and hero['work']['occupation'] != '' if has_job else 'work' not in hero or hero['work']['occupation'] == '')]
    return filtered_superheroes

def get_highest_superhero(gender, has_job):
    filtered_superheroes = filter_superheroes(gender, has_job)
    if not filtered_superheroes:
        return None
    highest_superhero = max(filtered_superheroes, key=lambda hero: hero['appearance']['height'] if 'height' in hero['appearance'] else 0)
    return highest_superhero

# пример использования
highest_superhero = get_highest_superhero('Male', True)
if highest_superhero:
    print(f"Самый высокий мужской супергерой, который имеет работу: {highest_superhero['name']} ({highest_superhero['appearance']['height']})")
else:
    print("Не найден супергерой, соответствующий заданным критериям")

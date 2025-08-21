from random import randint
import requests

class Pokemon:
    pokemons = {}
    # Инициализация объекта (конструктор)
    def __init__(self, pokemon_trainer):

        self.pokemon_trainer = pokemon_trainer   

        self.pokemon_number = randint(1,1000)
        self.img = self.get_img()
        self.name = self.get_name()
        self.weight = self.get_weight()
        self.height = self.get_height()
        self.bonus = self.get_bonus()
        self.xp = 0
        self.feed = 0 
        self.level = 1
        self.xp_to_level = 10

        Pokemon.pokemons[pokemon_trainer] = self

    # Метод для получения картинки покемона через API
    def get_img(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            pic = response.json()
            return (pic['sprites']['other']['official-artwork']['front_default'])
        else:
            return "Не удалось найти картинку :("
        
    # Метод для получения имени покемона через API
    def get_name(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['forms'][0]['name'])
        else:
            return "Не удалось узнать имя твоего глупого покемона:("

    def get_bonus(self):
        url = f'https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}'
        response = requests.get(url)
        if response.status_code == 200:
            if 900 < self.pokemon_number < 1001:
                rand_bonus = randint(1,100)
                return f"У вас редкий покемон выполучаете + {rand_bonus}"
            else:
                TEXT = "Вы остались без бонусов :("
                return TEXT
            
    def get_weight(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['weight'])
        else:
            return "У твоего покемона 0 кг... странно как-то получается"
        
    def get_height(self):
        url = f"https://pokeapi.co/api/v2/pokemon/{self.pokemon_number}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            return (data['height'])
        else:
            return "У твоего покемона 0 см... странно как-то получается"

    def feed_pokimon(self):
        rand_xp = randint(5, 20) 
        self.feed += 1
        self.xp += rand_xp

        text = f"{self.name} покормлен! +{rand_xp} XP"

        if self.xp >= self.xp_to_level:
            self.level_up()
            text += f"\n{self.name} поднялся до {self.level} уровня!"
        return text

    def level_up(self):
        self.level += 1
        self.xp = 0
        self.xp_to_level = int(self.xp_to_level * 1.5)

    def info(self):
        return f"""Имя: {self.name}\nВес: {self.weight}\nРост: {self.height}\nБонусы: {self.bonus}\nУровень: {self.level}\nОпыт: {self.xp}/{self.xp_to_level}\nКормлений: {self.feed}"""

    def show_img(self):
        return self.img

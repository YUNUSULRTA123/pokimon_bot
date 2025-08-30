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
        self.power = randint(1,50)
        self.hp = randint(1,100)
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

    def attack(self, enemy):
        if isinstance(enemy, Wizard): 
            шанс = randint(1,5)
            if шанс == 1:
                return "Покемон-волшебник применил щит в сражении"
        if enemy.hp > self.power:
            enemy.hp -= self.power
            return f"Сражение @{self.pokemon_trainer} с @{enemy.pokemon_trainer}"
        else:
            enemy.hp = 0
            return f"Победа @{self.pokemon_trainer} над @{enemy.pokemon_trainer}! "
    
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
        return f"Имя: {self.name}\nВес: {self.weight}\nРост: {self.height}\nБонусы: {self.bonus}\nУровень: {self.level}\nХП: {self.xp}/{self.xp_to_level}\nКормлений: {self.feed}\nHP: {self.hp}\nСила:{self.power}"

    def show_img(self):
        return self.img
    

class Wizard(Pokemon):
    def attack(self, enemy):
        return super().attack(enemy)

class Fighter(Pokemon):
    def attack(self, enemy):
        супер_сила = randint(5,15)
        self.power += супер_сила
        результат = super().attack(enemy)
        self.power -= супер_сила

        return результат + f"\nБоец применил супер-атаку силой:{супер_сила} "

if __name__ == '__main__':
    wizard = Wizard("username1")
    fighter = Fighter("username2")

    print(wizard.info())
    print()
    print(fighter.info())
    print()
    print(fighter.attack(wizard))

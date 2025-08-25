# 🐾 Pokemon Telegram Bot

## 📚 Описание

Это Telegram-бот на Python, позволяющий пользователям создавать, кормить и узнавать информацию о своих покемонах. Для каждого пользователя создаётся уникальный покемон, все данные берутся из [PokeAPI](https://pokeapi.co/api/v2/pokemon/). Бот написан на базе библиотеки [pyTelegramBotAPI](https://github.com/eternnoir/pyTelegramBotAPI).

---

## 🚀 Возможности

- 🟢 **/go** – создать покемона (один на пользователя)
- 🥣 **/feed** – покормить покемона (рандомно срабатывает)
- ℹ️ **/info** – узнать всё о своём покемоне
- 🆘 **/start** и **/help** – инструкция по командам

---

## 🛠️ Установка и запуск

1. **Установите зависимости:**
   ```bash
   pip install pyTelegramBotAPI requests
   ```
2. **Создайте файл `config.py`**  
   В корне проекта создайте файл `config.py` с содержимым:
   ```python
   token = "ВАШ_ТОКЕН_ТЕЛЕГРАМ_БОТА"
   ```
3. **Проверьте наличие файлов:**  
   - `logic.py` — с классом `Pokemon` (см. пример выше)
   - `config.py` — с вашим токеном

4. **Запустите бота:**
   ```bash
   python main.py
   ```

---

## 📂 Структура проекта

```
pokemon_bot/
├── logic.py        
├── main.py  
├── config.py       
└── README.md
```

---

## ⚙️ Особенности

- Один покемон — один пользователь
- Рандом на кормление и бонусы, редкие покемоны (№ 901–1000) приносят бонус
- Все данные о покемоне подтягиваются через PokeAPI

---

## 👤 Автор

[@YUNUSULRTA123](https://github.com/YUNUSULRTA123)

---

✨ Для любых вопросов используйте [PokeAPI](https://pokeapi.co/api/v2/pokemon/) или пишите мне!

## Вот скриншоты нашего бота
<img width="865" height="253" alt="{B802CEB5-D52B-4285-9664-F24B680AF2E3}" src="https://github.com/user-attachments/assets/36d95d1f-cdc5-4e33-9c6d-926e575e124e" />
<img width="859" height="629" alt="{6829D02B-F1D5-42A0-A3C2-88DB868B6240}" src="https://github.com/user-attachments/assets/bec22095-f7ca-4567-b0d6-d719a3160d08" />
<img width="859" height="102" alt="{B8B0DD6D-CA11-481B-A819-F8C91C299BAF}" src="https://github.com/user-attachments/assets/decd1198-3c76-45e7-ae4a-b85ae2ea96f6" />
<img width="853" height="133" alt="{0EC7CC12-3238-4F68-A75A-D75F01B0AA6F}" src="https://github.com/user-attachments/assets/8f6c4cab-0b85-4ee7-9166-b5150881a6ec" />
<img width="861" height="86" alt="{E556B36C-C26D-4DA6-A31E-5D27E320AE07}" src="https://github.com/user-attachments/assets/b5b0e4f8-78c5-4f95-9027-52770de30583" />
<img width="829" height="219" alt="{B836991D-420D-4AB6-8175-962098BCADC7}" src="https://github.com/user-attachments/assets/3cfd14d6-9f6b-49ea-b96c-3ccecdbbe30a" />
<img width="844" height="135" alt="{C1DABE37-95E8-439B-9680-ED45C358B803}" src="https://github.com/user-attachments/assets/bcfeea83-68cc-4b2c-9b49-f8ddc0a1e463" />
<img width="861" height="134" alt="{B0B08F06-C0B7-4AF5-9DD7-74990864DBD8}" src="https://github.com/user-attachments/assets/da8f2dd3-8da2-4f40-9af5-582e5488ac68" />

# QR-коды моего тг-бота
<img width="500" height="1000" alt="image" src="https://github.com/user-attachments/assets/0b320cf6-850a-45b5-9bf9-18847aab577b" />


> Спасибо за внимание 🙏

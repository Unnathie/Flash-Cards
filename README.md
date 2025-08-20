
# 🃏 Flash Card Project (French ↔ English)

Bonjour 👋 and welcome to your new vocabulary sparring partner!  
This app helps you sharpen your French–English skills one flashcard at a time.  

You get the French word first… wait a few seconds… and voilà — the English translation appears.  
Know it? ✅ Mark it off and it’s gone from your deck.  
Don’t know it? ❌ No worries, it’ll pop up again until you conquer it.  

---
## ✨ Working Display
![Working](https://github.com/user-attachments/assets/d24f747f-b2c1-4011-b42a-9ac6127f2aa1)



## ✨ Features
- 🎴 Flashcards that automatically flip from French → English after 4 seconds
- 🧠 Smart progress tracking with `to_learn.csv` (so your memory gets the workout, not you)
- 👆 Click ✔️ if you nailed it, or ✖️ if it needs more practice
- 💾 Progress is saved between sessions — the app remembers what you’ve mastered

---

## 📂 Project Structure
```

flash-card-project-start/
├── data/
│   ├── french-english.csv   # the starter deck
│   └── to_learn.csv         # your personalized "in-progress" deck
├── images/
│   ├── card_back.png
│   ├── card_front.png
│   ├── right.png
│   └── wrong.png
├── main.py                  # the flashcard arena
└── README.md

````

---

## 🚀 How to Run
1. Clone this repo:
   ```bash
   git clone https://github.com/Unnathie/Flash-Cards.git
   cd Flash-Cards

2. Launch the app:

   ```bash
   python main.py
   ```
Then grab a croissant 🥐 and start flipping cards.

---

## 🛠 Requirements

* Python 3.x
* [pandas](https://pandas.pydata.org/) for handling your decks
* Tkinter (comes pre-installed with Python on most systems)

---

## 📸 Screenshots

**Front (French):**  
![Flashcard Front](https://github.com/user-attachments/assets/7c824cd5-3e6a-4f26-a0e8-fd8e9538d2c7)

**Back (English):**  
![Flashcard Back](https://github.com/user-attachments/assets/02c0380d-2142-4fc5-9546-4207ce6ea789)

---

## 📌 Notes

* The file `data/to_learn.csv` is auto-generated as you study.
  Pro tip: add it to `.gitignore` so it doesn’t get tracked:

  ```
  data/to_learn.csv
  __pycache__/
  *.pyc
  ```

---

## 🎯 Future Ideas

* Multi-language decks 🌍
* Adjustable flip timers ⏱
* Scoreboards or streaks 🏆
* Sleeker UI themes 🎨

---

## 📜 License

This project is open-source under the [MIT License](LICENSE).
Flash responsibly. 😉

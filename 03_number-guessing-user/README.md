
# 🤖 Computer Guessing Game (Python)

This is a simple command-line based Python game in which **the computer tries to guess a number that the user is thinking of**, between 1 and a given upper bound. The user provides feedback whether the guess is too high, too low, or correct.

---

## 🎯 Features

- Computer guesses intelligently using narrowing range
- Interactive text-based game
- Fun and beginner-friendly Python project
- Great for understanding `if-else`, `while loops`, and `random` module

---

## 🛠 Tech Stack

- Python 3
- Command-line Interface (CLI)

---

## 🚀 How to Run

1. Make sure Python 3 is installed.
2. Save the code in a file called `user-guess.py`.
3. Open terminal or command prompt.
4. Run the script using:

```bash
python user-guess.py
```

5. The program will start guessing numbers between 1 and the number you provide (default is 10).
6. You respond with:
   - `H` or `h` → if guess is too high
   - `L` or `l` → if guess is too low
   - `C` or `c` → if guess is correct

---

## 📷 Example Gameplay

```
Is 5 too high (H), too low (L), or correct (C)? l
Is 8 too high (H), too low (L), or correct (C)? h
Is 6 too high (H), too low (L), or correct (C)? l
Is 7 too high (H), too low (L), or correct (C)? c
Congrats! The computer guessed your number, 7, correctly!
```


## 📌 Note

You can change the range by modifying the `computer_guess(x)` function call. For example:

```python
computer_guess(100)
```

Will let the computer guess numbers from 1 to 100.

---


---

## 👤 Author

- Developed by: **Shahid Ali**  
- Project: Python Projects for beginners #3

---


# 🧮 BMI Calculator (Streamlit App)

This is a simple and interactive **BMI Calculator Web App** built using **Streamlit** and **Python**. The app allows users to calculate their Body Mass Index (BMI) based on their height and weight.

---

## 🎯 Features

- Interactive sliders for height and weight input
- Real-time BMI calculation
- Categorized BMI result display
- Clean and user-friendly interface

---

## 🛠 Tech Stack

- Python 3
- [Streamlit](https://streamlit.io/)
- pandas (imported for future scalability)

---

## 🚀 How to Run

1. Make sure you have Python 3 installed.
2. Install Streamlit:

```bash
pip install streamlit
```

3. Save the code in a file named `bmi_calculator.py`.
4. Run the app with the following command:

```bash
streamlit run bmi_calculator.py
```

5. The browser will open automatically with the app.

---

## 💡 How It Works

- Input height (in cm) and weight (in kg) using sliders.
- The app calculates your BMI using the formula:

```python
BMI = weight / ((height / 100) ** 2)
```

- It also shows which BMI category you fall into.

---

## 📊 BMI Categories

- **Underweight:** BMI less than 18.5  
- **Normal weight:** BMI between 18.5 and 24.9  
- **Overweight:** BMI between 25 and 29.9  
- **Obesity:** BMI 30 or greater

---

## 👤 Author

- Developed by: **Shahid Ali**  
- Project: Python Practice Project #6 (Streamlit)

---

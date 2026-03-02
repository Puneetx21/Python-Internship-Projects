# 🌦️ Task 1 -Weather Analytics Dashboard

**Virtual Internship – Task 1**
**Organization:** CodTech IT Solutions

## 📌 Project Overview

The **Weather Analytics Dashboard** is a Python-based, real-time data visualization project that fetches and compares live weather and air quality data for multiple Indian cities using the **OpenWeather API**.
The dashboard presents all insights on a **single screen**, making it easy to analyze and compare environmental conditions at a glance.

---

## 🚀 Key Features

* 🌍 **Live Weather & AQI Data**

  * Real-time temperature, humidity, weather conditions, and Air Quality Index
  * City-wise geocoding with robust error handling

* 📊 **Single-Screen Visual Analytics**

  * Grouped bar charts for city comparisons
  * Color-coded AQI levels (Good, Moderate, Poor, etc.)
  * Summary panel highlighting key insights

* 🎨 **Modern & Responsive Design**

  * Dark theme for better readability
  * Clean, user-friendly visual layout

* 🧩 **Modular & Secure Codebase**

  * Well-structured Python modules
  * API keys securely managed using `.env` files

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries & Tools:**

  * `pandas` – data processing & analysis
  * `matplotlib` – core visualizations
  * `seaborn` – enhanced styling & themes
  * `requests` – API communication
  * `python-dotenv` – environment variable management

---

## 📂 Project Structure

```bash
weather-analytics-dashboard/
│
├── main.py                 # Main application script
├── weather_api.py          # API data fetching logic
├── visualization.py        # Charts and dashboard visuals
├── utils.py                # Helper functions & error handling
├── .env                    # API key configuration
├── requirements.txt        # Project dependencies
└── README.md               # Project documentation
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/weather-analytics-dashboard.git
   cd weather-analytics-dashboard
   ```

2. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**

   * Create a `.env` file in the root directory
   * Add your OpenWeather API key:

     ```env
     OPENWEATHER_API_KEY=your_api_key_here
     ```

4. **Run the project**

   ```bash
   python main.py
   ```

---

## 📈 Learning Outcomes

* Practical experience with **REST API integration**
* Real-time **data cleaning and transformation**
* Advanced **data visualization & UX design** principles
* Secure handling of environment variables
* Writing modular, scalable Python code

---

## 🏁 Conclusion

This project demonstrates the effective use of Python for **real-time analytics and data visualization**, transforming raw API data into meaningful insights. It strengthened my ability to design **actionable dashboards** with a strong focus on usability and clarity.

---



# 📄 Task 2 - Automated Report Generation System

**Virtual Internship – Task 2**
**Organization:** CodTech IT Solutions

## 📌 Project Overview

The **Automated Report Generation System** is a Python-based solution designed to transform raw business data into a **professionally formatted, multi-page PDF report** with **zero manual effort**.
The system reads structured data files, performs multi-dimensional analysis, generates visual insights, and compiles everything into a decision-ready business report.

---

## 🚀 Key Features

* 📂 **Automated Data Ingestion**

  * Reads CSV and Excel files using `pandas`
  * Built-in validation, exception handling, and data integrity checks

* 📊 **Multi-Dimensional Data Analysis**

  * Revenue trends and growth analysis
  * Product-wise performance evaluation
  * Regional sales insights
  * Customer satisfaction analysis

* 📈 **Automated Visualization**

  * Generates **3 analytical charts** automatically
  * Built using `matplotlib` and `seaborn`
  * Clean, business-friendly visual design

* 📄 **Professional PDF Report Generation**

  * Multi-page structured report using `ReportLab`
  * KPI summary tables
  * Embedded charts and analytics visuals
  * Automated insights and recommendations section

* 🧩 **Production-Ready Codebase**

  * Object-Oriented Programming (OOP) design
  * Modular, reusable, and scalable architecture

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries & Tools:**

  * `pandas` – data loading, cleaning & analysis
  * `matplotlib` – chart generation
  * `seaborn` – enhanced visualization styling
  * `reportlab` – PDF creation & layout
  * `numpy` – numerical computations

---

## 📂 Project Structure

```bash
automated-report-generation/
│
├── main.py                    # Entry point for report generation
├── data_loader.py             # CSV/Excel reading & validation
├── analysis_engine.py         # Statistical and business analysis
├── visualizations.py          # Chart generation module
├── pdf_generator.py           # PDF report builder using ReportLab
├── utils.py                   # Helper utilities & error handling
├── sample_data/               # Input CSV/Excel datasets
├── output/
│   └── Sales_Analytics_Report.pdf
├── requirements.txt           # Project dependencies
└── README.md                  # Project documentation
```

---

## ⚙️ Setup & Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/your-username/automated-report-generation.git
   cd automated-report-generation
   ```

2. **Install required dependencies**

   ```bash
   pip install -r requirements.txt
   ```

3. **Add input data**

   * Place CSV or Excel files inside the `sample_data/` directory

4. **Run the automation**

   ```bash
   python main.py
   ```

5. **View output**

   * Generated report will be available as:
     `output/Sales_Analytics_Report.pdf`

---

## 📦 Deliverables

* 📄 **Fully Documented Python Script**
  🔗 [https://lnkd.in/dN7q-fhV](https://lnkd.in/dN7q-fhV)

* 📊 **Sample Output Report**
  `Sales_Analytics_Report.pdf` — includes KPIs, charts, and business insights

---

## 📈 Learning Outcomes

* End-to-end **data analytics automation**
* Advanced **PDF report generation** in Python
* Translating raw datasets into **business intelligence**
* Visualization best practices for executive reports
* Writing clean, modular, production-ready Python code

---

## 🏁 Conclusion

This project demonstrates how Python can be used to **automate business reporting workflows**, eliminating repetitive manual work while ensuring accuracy, consistency, and professional presentation.
It strengthened my skills in **data analytics, visualization, PDF generation, and Python automation**, enabling me to convert raw data into **decision-ready business reports**.

---



# 🤖 Task 3 — AI Chatbot with NLP

A fully functional AI-powered chatbot built using Natural Language 
Processing (NLP) with Python, NLTK, and Flask — capable of 
understanding and answering user queries intelligently.

---

## 📸 Chatbot Preview
<!-- Add your chatbot screenshot here -->

---

## ✨ Features

- 🧠 **NLP-Powered Understanding** — Tokenization + Lemmatization with NLTK
- 🎯 **Intent Detection** — TF-IDF Vectorization + Cosine Similarity matching
- 💬 **Smart Responses** — intents.json knowledge base (easily extendable)
- 🌐 **Flask Web Interface** — REST API backend with real-time responses
- 🌙 **Dark / Light Mode** — Toggle between themes seamlessly
- ⌨️ **Typing Indicator** — Animated 3-dot typing effect
- ⚡ **Quick Suggestions** — One-click common query buttons
- 🔁 **Fallback Handling** — Graceful response for unknown queries

---

## 🔧 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| NLTK | Tokenization & Lemmatization |
| Scikit-Learn | TF-IDF Vectorization + Cosine Similarity |
| Flask | Web backend & REST API |
| HTML/CSS/JS | Chat UI frontend |

---

## 📁 Project Structure

```
Task3/nlp_chatbot/
├── intents.json          ← Knowledge base (patterns & responses)
├── chatbot.py            ← NLP engine
├── app.py                ← Flask backend
├── requirements.txt      ← Dependencies
├── templates/
│   └── index.html        ← Chat UI
└── static/
    └── style.css         ← Styling
```

---

## ⚙️ Setup & Run

### 1. Install Dependencies
```bash
pip install flask nltk scikit-learn numpy
```

### 2. Download NLTK Data
```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('punkt_tab')
```

### 3. Run the Chatbot
```bash
cd Task3/nlp_chatbot
python app.py
```

### 4. Open in Browser
```
http://127.0.0.1:5000
```

---

## 💬 What the Chatbot Knows

| Topic | Example Query |
|---|---|
| AI & ML | "What is Artificial Intelligence?" |
| NLP | "Explain Natural Language Processing" |
| Python | "Tell me about Python" |
| Flask | "What is Flask?" |
| Greetings | "Hello", "Hi", "Good morning" |
| Jokes | "Tell me a joke" |
| Bot Identity | "Who made you?", "What are you?" |
| Farewell | "Bye", "Goodbye" |

---

## 🧠 How NLP Works Here

```
User Input: "What is machine learning?"
     ↓
[Tokenize + Lemmatize]  →  ["what", "machine", "learn"]
     ↓
[TF-IDF Vectorize]      →  Numerical vector
     ↓
[Cosine Similarity]     →  Match closest intent
     ↓
[Return Response]       →  "ML allows computers to learn from data..."
```

---

## 🔑 Key Learnings

- NLP pipeline (tokenization, lemmatization, vectorization)
- Intent classification using TF-IDF + Cosine Similarity
- Flask REST API development
- Responsive chat UI design
- Dark/Light theme implementation

---

## 🚀 Future Enhancements

- [ ] PostgreSQL chat history storage
- [ ] OAuth2 user authentication
- [ ] Voice input via Web Speech API
- [ ] More intents & knowledge topics
- [ ] Cloud deployment (Render/Railway)

---



# 📧 Task 4 — Spam Email Detection System

A machine learning model that classifies emails/messages as 
**Spam or Ham (Not Spam)** using Python and Scikit-Learn — 
trained on the UCI SMS Spam Collection dataset with ~98% accuracy.

---

## 📸 Project Preview
<!-- Add your model comparison chart screenshot here -->

---

## ✨ Features

- 📊 **EDA** — Class distribution, message length & top word analysis
- 🧹 **NLP Preprocessing** — Cleaning, stopword removal, lemmatization
- 🔢 **TF-IDF Vectorization** — 5000 features with unigrams + bigrams
- 🤖 **3 ML Models Trained & Compared** — Naive Bayes, Logistic Regression, SVM
- 📈 **Full Evaluation** — Confusion Matrix, ROC Curve, F1-Score
- 🔍 **Error Analysis** — False positives & false negatives breakdown
- ✅ **Live Spam Checker** — Paste any email to get instant verdict

---

## 🔧 Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.10+ | Core language |
| Scikit-Learn | ML models + TF-IDF |
| NLTK | Text preprocessing |
| Pandas | Data manipulation |
| Matplotlib | Visualization |
| Seaborn | Styled charts |
| Jupyter Notebook | Development environment |

---

## 📁 Project Structure

```
Task4/Spam_detection/
├── spam_detection.ipynb              ← Full Jupyter Notebook
├── class_distribution.png           ← EDA chart
├── message_length_distribution.png  ← EDA chart
├── top_words.png                     ← EDA chart
├── model_comparison.png              ← Model evaluation
├── confusion_matrices.png            ← Model evaluation
├── roc_curve.png                     ← Model evaluation
└── README.md                         ← This file
```

---

## ⚙️ Setup & Run

### 1. Install Dependencies
```bash
pip install scikit-learn pandas numpy matplotlib seaborn nltk jupyter
```

### 2. Launch Jupyter Notebook
```bash
cd Task4/Spam_detection
jupyter notebook spam_detection.ipynb
```

### 3. Run All Cells
```
Kernel → Restart & Run All
```

---

## 📊 Model Results

| Model | Accuracy | Precision | Recall | F1-Score |
|---|---|---|---|---|
| Multinomial Naive Bayes | ~97% | ~96% | ~94% | ~95% |
| Logistic Regression | ~98% | ~97% | ~96% | ~97% |
| **Support Vector Machine** | **~98%** | **~98%** | **~97%** | **~97%** |

🏆 **Best Model: Support Vector Machine (LinearSVC)**

---

## 🧹 Preprocessing Pipeline

```
Raw Email Text
     ↓
[Lowercase + Remove URLs/Phones/Emails]
     ↓
[Remove Special Characters & Numbers]
     ↓
[Remove Stopwords]
     ↓
[Lemmatization (NLTK)]
     ↓
[TF-IDF Vectorization (5000 features)]
     ↓
[Train ML Model]
     ↓
[Predict → Spam / Ham]
```

---

## 🔍 Live Spam Checker

Test any message instantly inside the notebook:

```python
predict_spam("CONGRATULATIONS! You've WON a FREE iPhone! Claim NOW!")
# 🔴 SPAM — Confidence: 97.3%

predict_spam("Hey, are we still meeting for lunch tomorrow?")
# 🟢 HAM  — Confidence: 95.1%
```

---

## 📈 Evaluation Charts

| Chart | Insight |
|---|---|
| `class_distribution.png` | 86.6% Ham vs 13.4% Spam — imbalanced dataset |
| `message_length_distribution.png` | Spam messages are longer on average |
| `top_words.png` | Spam: free, win, prize / Ham: you, the, have |
| `model_comparison.png` | SVM outperforms across all metrics |
| `confusion_matrices.png` | TP, TN, FP, FN breakdown per model |
| `roc_curve.png` | All models AUC > 0.98 |

---

## 📋 Dataset

- **Name:** UCI SMS Spam Collection
- **Size:** 5,572 messages
- **Spam:** 747 messages (13.4%)
- **Ham:** 4,825 messages (86.6%)
- **Split:** 80% train / 20% test (stratified)

---

## 🔑 Key Learnings

- End-to-end ML pipeline development
- NLP text preprocessing techniques
- Multi-model training & comparison
- Evaluation metrics beyond accuracy (F1, AUC)
- Confusion matrix & error analysis
- Jupyter Notebook documentation

---

## 🚀 Future Enhancements

- [ ] Save model with `joblib` for reuse
- [ ] Flask web app — upload email → get verdict
- [ ] Gmail API integration — scan real inbox
- [ ] LSTM / BERT deep learning model
- [ ] Real-time spam filter browser extension

---

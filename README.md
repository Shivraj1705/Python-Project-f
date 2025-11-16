# Smart Personal Finance Manager with Expense Prediction

![Python](https://img.shields.io/badge/Python-3.9%2B-blue)
![Pandas](https://img.shields.io/badge/Pandas-2.0%2B-green)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28%2B-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

A **lightweight personal finance tracker** that:
- Tracks expenses by category
- Detects overspending
- Predicts next month's expenses
- Visualizes spending patterns
- Suggests saving tips

Built with **Pandas, Plotly, Statsmodels & Streamlit** — perfect for **portfolios, interviews, or personal use**.

---

## Features

| Feature | Description |
|--------|-------------|
| Add Expenses | Form to log date, category, amount |
| Budget Alerts | Warns at 80% of budget |
| Next Month Forecast | Uses **Exponential Smoothing** |
| Interactive Charts | Pie, trend, budget vs actual |
| Saving Tips | Smart suggestions |
| CSV Storage | No database needed |

---

## Quick Start

```bash
git clone https://github.com/yourusername/smart-finance-manager.git
cd smart-finance-manager
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py

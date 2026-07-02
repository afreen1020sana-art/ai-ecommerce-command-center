# 🚀 AI-Powered Supply Chain Command Center

An end-to-end analytics project that simulates an enterprise Supply Chain Command Center using Python, AI-generated alerts, and Power BI.

This project demonstrates how businesses can monitor KPIs, identify operational risks, and take data-driven decisions through an executive dashboard and intelligent alerting system.

---

# 📌 Project Overview

The project covers the complete analytics lifecycle:

- Synthetic data generation using Python
- Data modeling and transformation
- Supply chain KPI monitoring
- AI-driven business alerts and explanations
- Executive dashboard development in Power BI
- Interactive analytics and business insights

---

# 🎯 Business Problem

Supply chain teams often struggle with:

- Delivery delays
- High return rates
- Inventory shortages
- Lack of real-time visibility
- Slow decision-making

This project provides a centralized command center to monitor performance and proactively identify issues.

---

# 🛠️ Tech Stack

| Technology | Purpose |
|------------|----------|
| Python | Data Generation & AI Logic |
| Pandas | Data Processing |
| Faker | Synthetic Data Creation |
| Power BI | Dashboard & Visualization |
| Git & GitHub | Version Control |
| DAX | KPI Calculations |

---

# 📂 Project Structure

```text
ai-ecommerce-command-center/
│
├── data/
│   ├── customers.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── shipments.csv
│   ├── returns.csv
│   └── alerts.csv
│
├── ai/
│   ├── explain_alerts.py
│   └── ask_business_question.py
│
├── dashboard/
│   └── Supply_Chain_Command_Center.pbix
│
├── docs/
│   └── screenshots/
│       ├── dashboard.png
│       ├── ai_alert_explanation.png
│       └── project_architecture.png
│
├── requirements.txt
└── README.md
```

---

# 🏗️ Project Architecture

<img width="387" height="587" alt="image" src="https://github.com/user-attachments/assets/1f2947ea-aa41-41ab-89b8-4f456fba13eb" />

---

# 📊 Dashboard Preview

<img width="1397" height="732" alt="image" src="https://github.com/user-attachments/assets/f0c49268-e168-407a-b6dd-2e6743fe880f" />


---

# 🤖 AI Alert Explanation

<img width="930" height="705" alt="ai explanation " src="https://github.com/user-attachments/assets/8d365203-0f3c-45b1-95be-64a5d6ee7a6f" />


---

# 📈 Dashboard Features

## Executive KPIs

- Total Revenue
- Total Orders
- Total Customers
- Return %
- Delay %
- Low Stock Products

## Business Visualizations

- Revenue Trend
- Revenue by Category
- Top Products
- Return Analysis
- Delay Analysis
- Order Status Distribution
- Alert Feed

## Interactive Features

- Date Slicer
- Region Filter
- Category Filter
- Dynamic KPI Updates

---

# 🧠 AI Capabilities

The project includes an AI layer that:

✅ Detects delivery delays

✅ Identifies low inventory

✅ Flags high return rates

✅ Explains business impact

✅ Recommends corrective actions

### Example

```text
ALERT: Delivery Delays
SEVERITY: High
MESSAGE: Delay rate is 49.88%

Business Impact:
- Customer dissatisfaction
- Increased cancellations
- Revenue loss

Recommended Action:
- Review logistics operations
```

---

# 📁 Dataset Information

| Dataset | Description |
|----------|-------------|
| Customers | Customer master data |
| Products | Product catalog |
| Orders | Sales transactions |
| Shipments | Delivery information |
| Returns | Product returns |
| Alerts | AI-generated business alerts |

---

# 📐 Data Model

```text
Customer ───┐
            │
            ▼
          Orders ───► Shipments
            │
            ├──────► Returns
            │
            ▼
          Product

Date ───────► Orders

Alerts (Disconnected)
```

---

# 🚀 Getting Started

## Clone Repository

```bash
https://github.com/afreen1020sana-art/ai-ecommerce-command-center
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Generate Data

```bash
python data/generate_customers.py
python data/generate_products.py
python data/generate_orders.py
python data/generate_shipments.py
python data/generate_returns.py
python data/generate_alerts.py
```

## Run AI Alert Explanation

```bash
python ai/explain_alerts.py
```

---

# 📊 Power BI Dashboard

Open:

```text
https://app.powerbi.com/view?r=eyJrIjoiMDAzODhhZDgtY2E0Yy00Y2IwLThlNGEtN2Y4YzVjMTgxYTRlIiwidCI6ImM2ZTU0OWIzLTVmNDUtNDAzMi1hYWU5LWQ0MjQ0ZGM1YjJjNCJ9
```

Refresh the data and explore the dashboard.

---

# 💼 Business Value

This solution helps organizations:

- Monitor supply chain performance
- Detect operational issues proactively
- Improve customer satisfaction
- Reduce inventory shortages
- Enable faster decision-making

---

# 🎯 Key Learnings

- End-to-end analytics project development
- Data modeling in Power BI
- DAX measure creation
- Dashboard design principles
- Python automation
- AI-driven business insights

---

# 👨‍💻 Author

**Sana Afreen**

Power BI Developer | Data Analyst | Business Intelligence Engineer

📧 Email: afreen1020sana@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/sana3438/

🔗 GitHub: https://github.com/afreen1020sana-art

---

# ⭐ If you found this project useful, please give it a star!

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
ai-powered-supply-chain-command-center/
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

![Architecture](docs/screenshots/project_architecture.png)

---

# 📊 Dashboard Preview

![Dashboard](docs/screenshots/dashboard.png)

---

# 🤖 AI Alert Explanation

![AI Alert Explanation](docs/screenshots/ai_alert_explanation.png)

---

# 📈 Dashboard Features

### Executive KPIs
- Total Revenue
- Total Orders
- Total Customers
- Return %
- Delay %
- Low Stock Products

### Business Visualizations
- Revenue Trend
- Revenue by Category
- Top Products
- Return Analysis
- Delay Analysis
- Order Status Distribution
- Alert Feed

### Interactive Features
- Date Slicer
- Region Filter
- Category Filter
- Dynamic KPI Updates

---

# 🧠 AI Capabilities

The project includes an AI layer that:

Detects delivery delays
Identifies low inventory
Flags high return rates
Explains business impact
Recommends corrective actions

Example:
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
git clone https://github.com/YOUR_USERNAME/ai-powered-supply-chain-command-center.git
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

<img width="930" height="705" alt="image" src="https://github.com/user-attachments/assets/ef2a0fdd-a06d-4607-a194-0b2346025b38" />

# 📊 Power BI Dashboard

<img width="1392" height="727" alt="image" src="https://github.com/user-attachments/assets/7f5bfc83-9e5e-41fb-a989-4c754dc3c938" />

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

Sana Afreen

Power BI Developer | Data Analyst | Business Intelligence Engineer

📧 Email: afreen1020sana@gmail.com

🔗 LinkedIn: https://www.linkedin.com/in/sana3438/

🔗 GitHub: https://github.com/your-username

---

# ⭐ If you found this project useful, please give it a star!

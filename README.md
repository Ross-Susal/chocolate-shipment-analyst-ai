# Chocolate Shipment Analyst AI

## Short Description
An AI-powered chocolate shipment analytics application that combines Python data analysis, PostgreSQL, SQLAlchemy, and Gemini function calling to analyze shipment status, profitability, regional performance, and cancellations.

## Project Overview

This project analyzes 25,073 chocolate shipments and transforms shipment data into actionable business insights.

The project combines traditional data analytics with an AI-powered natural-language interface. Users can ask questions in natural language, and Gemini uses function calling to select the appropriate predefined analytical tool and retrieve information from the PostgreSQL database.

## Example Questions

- What is the status of shipment S00000004?
- Show me the total profit by region. Which region is highest?
- Show me 5 cancelled shipments.
- What is the total number of cancelled shipments?
- Show me the top 5 most profitable shipments.

## Key Features

### Data Cleaning

- Cleaned and prepared shipment data using Pandas.
- Converted date fields into appropriate datetime types.
- Removed unnecessary columns.
- Corrected and standardized financial fields.
- Created profit and profit-margin calculations.
- Validated cancellation and shipment-status information.

### Exploratory Data Analysis

Analyzed revenue, profit, profit margin, regional performance, product performance, salesperson performance, team performance, cancellation rates, monthly/yearly trends, and loss-making products.

### PostgreSQL Database

The cleaned shipment data is stored in PostgreSQL and accessed using SQLAlchemy ORM and psycopg2.

### Analytical Query Layer

Reusable query functions provide shipment status, top profitable shipments, profit by region, and cancelled shipment analysis.

### AI Function Calling

Gemini determines which predefined Python analytical tool should be called based on the user's natural-language question. The tool executes the appropriate database query and returns structured data to Gemini.

### Automated Testing

The project uses pytest to test the shipment query layer and Gemini tool functions. The current test suite has 10 passing tests.

## Architecture

User
  ↓
Gemini
  ↓ Function Calling
Python Tools
  ↓
SQLAlchemy Query Layer
  ↓
PostgreSQL
  ↓
Shipment Data
  ↓
Result returned to Gemini
  ↓
Natural-language response

## Project Structure

chocolate-shipment-analyst-ai/
│
├── charts/
│   ├── revenue_by_region.png
│   ├── monthly_revenue_trend.png
│   ├── profit_by_product.png
│   └── profit_margin_by_product.png
│
├── reports/
│   └── insights.md
│
├── src/
│   ├── analysis.py
│   ├── data_cleaning.py
│   ├── database.py
│   ├── gemini_client.py
│   ├── models.py
│   ├── shipment_queries.py
│   ├── sqlalchemy_db.py
│   ├── tools.py
│   ├── test_shipment_queries.py
│   └── test_tools.py
│
├── .gitignore
├── README.md
└── requirements.txt

Do NOT commit:
.env
.venv/
__pycache__/
.pytest_cache/
*.pyc
data/

## Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application and analysis logic |
| Pandas | Data cleaning and analysis |
| NumPy | Numerical calculations |
| Matplotlib | Data visualization |
| PostgreSQL | Relational database |
| SQLAlchemy | ORM and database interaction |
| psycopg2 | PostgreSQL connectivity |
| Google Gemini API (gemini-2.5-flash) | Natural-language AI and function calling |
| python-dotenv | Environment variable management |
| pytest | Automated testing |
| Git/GitHub | Version control |

## Dataset

The project analyzes 25,073 chocolate shipment records containing shipment, product, location, salesperson, financial, and status information.

The dataset was obtained from a publicly available YouTube tutorial where it was provided for practice purposes.

Original source:

https://www.youtube.com/watch?v=9sEJclxSxFQ

The raw and processed datasets are not included in this repository.

To reproduce the project, obtain the dataset from the original source and place it locally at:

data/sample-chocolate-shipments-data-all-Apr-2025.csv

The data-cleaning pipeline can then be used to generate the processed dataset locally.

## Business Analysis

### Overall Performance

- Total revenue: approximately $141.49 million
- Total shipments: 25,073
- Cancelled shipments: 1,215
- Cancellation rate: approximately 4.85%

### Regional Performance

APAC was the strongest-performing region by both revenue and absolute profit.
Approximate revenue:
- APAC: $100.33 million
- Americas: $30.93 million
- Europe: $10.23 million

### Product Performance

- Organic Choco Syrup generated the highest absolute profit.
- Peanut Butter Cubes had the highest profit margin.
- Raspberry Choco also had a high profit margin.
- 85% Dark Bars was significantly loss-making.
- Baker's Choco Chips and After Nines also generated losses.

### Cancellation Analysis

- Overall cancellation rate: approximately 4.85%.
- APAC had the highest regional cancellation rate.
- Caramel Stuffed Bars had the highest product-level cancellation rate.
- Peanut Butter Cubes had the lowest product-level cancellation rate.

### Salesperson Performance

Performance was evaluated using both absolute profit and profit margin, showing that high-volume performance and high efficiency are different dimensions.

### Time-Based Analysis

2025 contains only January through March data and should not be directly compared with the full-year 2023 and 2024 periods.

## Business Recommendations

- Investigate the cost structure and pricing of 85% Dark Bars.
- Investigate the causes of losses for Baker's Choco Chips and After Nines.
- Study high-margin products such as Peanut Butter Cubes and Raspberry Choco.
- Investigate the relatively high cancellation rate in APAC.
- Analyze monthly revenue patterns to improve inventory and sales planning, while accounting for the incomplete 2025 period.
- Evaluate salesperson performance using both absolute profit and profit margin.

## Visualizations
The project includes:
- Revenue by Region
- Monthly Revenue Trend
- Profit by Product
- Profit Margin by Product
The charts are stored in the charts/ directory.

## Gemini AI Tools

### get_shipment_status

Returns the status and basic information for a specific shipment.

### get_top_profitable_shipments_tool

Returns the highest-profit shipments based on a requested limit.

### get_profit_by_region_tool

Returns total profit grouped by region.

### get_cancelled_shipments_tool

Returns the total number of cancelled shipments and a limited list of cancelled shipment records.

## Database Design

SQLAlchemy maps the shipment data to PostgreSQL.
The database layer contains:
- SQLAlchemy models
- Database connection management
- Shipment query functions
- Reusable analytical queries
The separation between database access, query logic, tools, and the Gemini client makes the application easier to maintain and extend.

## Testing

The project uses pytest for automated testing.
The test suite covers:
- Valid shipment lookup
- Invalid shipment lookup
- Top profitable shipments
- Profit by region
- Cancelled shipments
- Gemini tool return types
- Success responses
- Expected result fields
- List-based results
- Result limits
Run:
pytest
Current result:
10 passed

## Installation

### Clone the repository

git clone https://github.com/Ross-Susal/chocolate-shipment-analyst-ai.git

### Navigate to the project

cd chocolate-shipment-analyst-ai

### Create a virtual environment

python -m venv .venv

### Activate it on Windows PowerShell

.venv\Scripts\Activate.ps1

### Install dependencies

pip install -r requirements.txt

## Environment Variables

Create a .env file in the project root:
GEMINI_API_KEY=your_gemini_api_key
DATABASE_URL=your_database_connection_string
Never commit .env to GitHub.

## PostgreSQL Setup

Create a PostgreSQL database and configure the database connection using the environment variables required by the project.
The application uses SQLAlchemy to communicate with PostgreSQL.
Database credentials must remain private and should never be committed to the repository.

## Running the Project

Activate the virtual environment:
.venv\Scripts\Activate.ps1
Run the Gemini application:
python src/gemini_client.py
The application prompts:
Ask about a shipment:
Example:
Show me the total profit by region. Which region is highest?

## Running Tests

pytest
Expected current result:
10 passed

## Security

API keys and database credentials are stored in environment variables.
The following should be excluded through .gitignore:
.env
.venv/
__pycache__/
.pytest_cache/
*.pyc
data/

## Project Goals

This project demonstrates practical skills in:
- Python
- Data cleaning
- Data analysis
- SQL
- PostgreSQL
- SQLAlchemy
- Database design
- API integration
- LLM function calling
- Automated testing
- Business analysis
- Git and GitHub
The project uses the `gemini-2.5-flash` model to combine traditional data analytics with an LLM interface to create a practical AI-powered business analytics application.

## Future Improvements

- Add more analytical tools for Gemini.
- Add shipment trend analysis through natural-language queries.
- Add product-level analytics tools.
- Add salesperson performance tools.
- Add automated database initialization.
- Add a web interface.
- Add dashboard functionality.
- Add broader test coverage.
- Add stronger API/database error handling.
- Add deployment support.

## Author

**Rahul Ross**

GitHub: https://github.com/Ross-Susal/chocolate-shipment-analyst-ai

## Final GitHub Checklist

Before pushing the final project:

- [ ] README.md updated
- [ ] requirements.txt updated
- [ ] .gitignore includes .env, .venv/, __pycache__/, .pytest_cache/, and *.pyc
- [ ] No API key is visible in any file
- [ ] No database password is visible in any file
- [ ] Tests pass: pytest → 10 passed
- [ ] Charts are present in charts/
- [ ] reports/insights.md is present
- [ ] Source files are present in src/
- [ ] Raw dataset is not included in the repository
- [ ] Processed dataset is not included in the repository
- [ ] Dataset source is documented in README.md
- [ ] Git status shows only intended changes
- [ ] Commit and push to GitHub

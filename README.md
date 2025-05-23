# The StudentSpot SummerInternship Projects - Python Automation, Chatbot, and Web Scraping.

Hi! I'm **Munnuri Vaishnavi**, and this repository showcases the three core tasks I completed during my internship at **The Student Spot**. These tasks helped me enhance my Python programming skills through real-world applications in chatbot design, Excel automation, and web scraping.

I also actively used **AI tools like ChatGPT** to guide my approach, solve errors, and improve the quality of my solutions throughout these projects.

## 1. Basic ChatBot Using Conditional Statements (with Streamlit UI)

This is a beginner-level chatbot built using Python if-elif-else statements, wrapped with an interactive web UI using *Streamlit*.

### Features:
- Simple decision-based logic
- Real-time input and response interface
- Clean and lightweight UI using Streamlit

### Learnings:
- Implementing conditional flows in Python
- Using Streamlit to create interactive user interfaces
- Structuring logic for text-based conversation

### Installation:
```bash
pip install streamlit

How to Run:
```bash
streamlit run basic_chatbot.py 

## 2. Automating Excel Reports using Pandas and OpenPyXL

### Description:
This project involved cleaning the Titanic dataset (train.csv) and generating an insightful, styled Excel report using *Pandas* and *OpenPyXL*. I created visual summaries like bar charts and pie charts based on the cleaned data.

### What I Learned:
- Data cleaning: handling null values, dropping irrelevant columns
- Type conversions and renaming columns in Pandas
- Excel automation: formatting cells, adjusting column widths
- Creating and embedding charts (bar, pie) in Excel sheets using OpenPyXL
- Efficient use of AI tools like ChatGPT for troubleshooting and chart creation logic

*Input:* train.csv  
*Output:* cleaned_titanic_report_with_charts.xlsx  
*File:* automatingtheexcelfile.py


## 3. Web Scraping using BeautifulSoup

### Description:
In this task, I used *BeautifulSoup* to scrape and extract data from a sample webpage. I focused on retrieving text content, links, and headings from HTML elements.

### What I Learned:
- Sending HTTP requests with the requests library
- Navigating HTML DOM with BeautifulSoup
- Extracting data using .find(), .find_all(), tag names, and CSS selectors
- Understanding the importance of clean, structured parsing for data analysis

*File:* webscraper_beautifulsoup.py
## Tools & Libraries Used

- Python 3
- Pandas
- OpenPyXL
- BeautifulSoup
- Requests
- *AI Assistance*: ChatGPT for guidance, debugging, and optimization

## How to Run

Install the required libraries using pip:

```bash
pip install pandas openpyxl beautifulsoup4 requests

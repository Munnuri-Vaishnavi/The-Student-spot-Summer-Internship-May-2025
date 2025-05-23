# Web Scraping with BeautifulSoup - Internship Project

This project demonstrates how to scrape structured information from a webpage using **Python**, the **BeautifulSoup** library, and additional built-in modules. It extracts useful content like titles, headings, paragraphs, tables, links, forms, images, and more from a real website.

## Table of Contents

- [About](#about)
- [Technologies Used](#technologies-used)
- [Features](#features)
- [How It Works](#how-it-works)
- [Setup & Installation](#setup--installation)
- [Usage](#usage)
- [Output Example](#output-example)
- [Credits](#credits)

---
## About

This script was developed as part of my internship at *The Student Spot, focused on learning web scraping techniques with BeautifulSoup. The script extracts data from the Wikipedia page on **Web Scraping* and performs structured extraction, visualization (opening images in browser), and formatted printing of the content.

---
## Technologies Used

- Python 3
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)
- Built-in:
  - webbrowser

---
## Features
- Extracts:
  - Page title
  - Meta description
  - First paragraph
  - Headings (H1, H2, H3)
  - List items
  - Working hyperlinks
  - First table rows (if any)
  - Forms and input fields
  - Opens the first 2 images in a browser

- Filters:
  - Skips empty, anchor (#) or invalid links
  - Handles relative URLs

---
## sample output
## How It Works

1. Sends a request to the target URL using requests.
2. Parses the HTML content using BeautifulSoup.
3. Searches for different HTML elements and extracts their content.
4. Opens image URLs in your default browser using the webbrowser module.

---
## Title: Web scraping - Wikipedia

Meta Description: Web scraping is data scraping used for extracting data from websites.

## First Paragraph:
Web scraping, web harvesting, or web data extraction is data scraping used for extracting data from websites.

Headings:
- Web scraping
- History
- Techniques
...

## Working Links:
Web scraping -> https://en.wikipedia.org/wiki/Web_scraping
...

Opening: https://upload.wikimedia.org/...image1.png 

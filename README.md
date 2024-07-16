# Hacker News Scraper

This project contains a Python script for scraping news articles from Hacker News and sending them via email. It automates the fetching of the latest news titles and links, and emails them. 

## Features

- Fetches latest titles and URLs from Hacker News.
- Emails the fetched news items to a specified email address.
- Runs scheduled tasks to automate the process daily (TODO)

## Prerequisites

Before running this script, you will need:

- Python 3.6+
- pip (Python package installer)

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/mrmrjing/python-web-scraper-ycombinator.git
cd python-web-scraper-ycombinator
``` 

## Configuration
1. Create a .env file in the root directory of the project 
2. Add the following environment variables to the `.env` file: 
```bash
EMAIL_USER=your-email@example.com
EMAIL_PASS=your-email-password
SMTP_SERVER=smtp.your-email-provider.com
SMTP_PORT=465
```
Replace the placeholder values with your actual email settings.

## Usage 
Run the script manually with: 
```bash
python news_scraper.py
``` 

To set up daily execution at a specific time, configure a cron job (Linux/macOS) or a scheduled task (Windows).
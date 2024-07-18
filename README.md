# Hacker News Scraper

This project contains a Python script for scraping news articles from Hacker News and sending them via email. It automates the fetching of the latest news titles and links, and emails them. 

## Features

- Fetches latest titles and URLs from Hacker News.
- Emails the fetched news items to a specified email address.
- Runs scheduled tasks to automate the process daily.

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
### Running the script manually 
Run the script manually with: 
```bash
python news_scraper.py
``` 

### Automating the script using a Cron Job  
The cron command-line utility is a job scheduler on Unix-like operating systems. Users who set up and maintain software environments use cron to schedule jobs, also known as cron jobs, to run periodically at fixed times, dates, or intervals. (https://en.wikipedia.org/wiki/Cron)

1. Open the terminal 
2. Type crontab -e to edit the cron jobs 
3. Add the following line to schedule the script: 
```bash
0 10 * * * /path/to/python3 /path/to/news_scraper.py
```
Replace /path/to/python3 with the path to the Python executable and /path/to/news_scraper.py with the path to the news_scraper.py script.
4. Save and exit the editor. The cron job is now set up and will run at 10am everyday. 

5. Confirm that the cron jobs have been added by listing them: 
```bash
crontab -l
```
 
This is the format of a Cron job entry: 
* * * * * command
- - - - -
| | | | |
| | | | +----- Day of the week (0 - 7) (Sunday=0 or 7)
| | | +------- Month (1 - 12)
| | +--------- Day of the month (1 - 31)
| +----------- Hour (0 - 23)
+------------- Minute (0 - 59)

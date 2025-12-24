# Austin Public Library Event Scraper

Python scripts to extract event information (name, date, time, location) from the Austin Public Library events page.

## Files

1. **library_event_scraper.py** - Basic version using requests + BeautifulSoup
2. **library_event_scraper_selenium.py** - Advanced version using Selenium (better for JavaScript-heavy sites)
3. **requirements.txt** - Python dependencies

## Installation

### Option 1: Basic Version (Faster, simpler)

```bash
pip install requests beautifulsoup4 lxml
python library_event_scraper.py
```

### Option 2: Selenium Version (More reliable for modern websites)

1. Install Python dependencies:
```bash
pip install selenium requests beautifulsoup4
```

2. Install Chrome/Chromium browser if not already installed

3. Install ChromeDriver:
   - **macOS:** `brew install chromedriver`
   - **Linux:** `sudo apt-get install chromium-chromedriver`
   - **Windows:** Download from https://chromedriver.chromium.org/

4. Run the scraper:
```bash
python library_event_scraper_selenium.py
```

## Usage

Simply run either script:

```bash
# Basic version
python library_event_scraper.py

# Selenium version (recommended)
python library_event_scraper_selenium.py
```

The script will:
1. Connect to https://library.austintexas.gov/events
2. Extract event name, date, time, and location
3. Print results to console

## Sample Output

```
================================================================================
AUSTIN PUBLIC LIBRARY EVENTS
================================================================================

Event #1
  Name:     Storytelling for Kids
  Date:     December 25, 2024
  Time:     10:00 AM - 11:00 AM
  Location: Central Library
--------------------------------------------------------------------------------
Event #2
  Name:     Book Club: Mystery Lovers
  Date:     December 26, 2024
  Time:     6:00 PM - 7:30 PM
  Location: Yarborough Branch
--------------------------------------------------------------------------------

Total events found: 2
```

## Troubleshooting

### Error: 403 Forbidden
The website may be blocking automated requests. Try:
1. Use the Selenium version (library_event_scraper_selenium.py)
2. Check if the website's terms of service allow scraping

### Error: No events found
The website structure may have changed. The scripts include debugging output to help identify the issue.

### ChromeDriver errors
Make sure:
- Chrome/Chromium is installed
- ChromeDriver version matches your Chrome version
- ChromeDriver is in your PATH

## Notes

- These scripts are designed for one-time manual execution
- The Austin Public Library website structure may change over time, requiring script updates
- Always respect the website's robots.txt and terms of service
- For frequent scraping, consider checking if the library provides an official API

## Customization

To modify what data is extracted, edit the event_data dictionary in either script:

```python
event_data = {
    'name': '',
    'date': '',
    'time': '',
    'location': ''
    # Add more fields as needed
}
```

Then add corresponding extraction logic for each new field.

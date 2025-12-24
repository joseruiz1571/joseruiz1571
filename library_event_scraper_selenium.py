#!/usr/bin/env python3
"""
Austin Public Library Event Scraper (Selenium Version)
Extracts event name, date, time, and location from library.austintexas.gov/events
Uses Selenium to handle JavaScript-rendered content and anti-bot measures
"""

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import time


def scrape_library_events_selenium(url):
    """
    Scrape events from Austin Public Library events page using Selenium.

    Args:
        url: The URL of the events page

    Returns:
        List of dictionaries containing event information
    """
    # Set up Chrome options for headless browsing
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36')

    driver = None
    events = []

    try:
        print(f"Initializing browser...")
        driver = webdriver.Chrome(options=chrome_options)

        print(f"Fetching events from {url}...")
        driver.get(url)

        # Wait for page to load - adjust timeout as needed
        wait = WebDriverWait(driver, 10)

        # Wait for events to load (trying multiple possible selectors)
        time.sleep(3)  # Give JavaScript time to render

        # Try to find event containers with various selectors
        event_selectors = [
            (By.CSS_SELECTOR, 'div.event-item'),
            (By.CSS_SELECTOR, 'article.event'),
            (By.CSS_SELECTOR, '.event-listing'),
            (By.CSS_SELECTOR, 'div[class*="event"]'),
            (By.CSS_SELECTOR, 'article'),
            (By.XPATH, '//div[contains(@class, "event")]'),
        ]

        event_elements = []
        for by, selector in event_selectors:
            try:
                event_elements = driver.find_elements(by, selector)
                if event_elements:
                    print(f"Found {len(event_elements)} elements using selector: {selector}")
                    break
            except NoSuchElementException:
                continue

        if not event_elements:
            print("\nNo event elements found. Attempting to analyze page structure...")
            print(f"Page title: {driver.title}")
            print("\nPage source preview (first 1000 chars):")
            print(driver.page_source[:1000])
            return events

        # Extract event details
        for i, event_elem in enumerate(event_elements):
            event_data = {
                'name': '',
                'date': '',
                'time': '',
                'location': ''
            }

            try:
                # Extract event name/title (try multiple selectors)
                title_selectors = [
                    (By.CSS_SELECTOR, 'h2'),
                    (By.CSS_SELECTOR, 'h3'),
                    (By.CSS_SELECTOR, '.event-title'),
                    (By.CSS_SELECTOR, '.title'),
                    (By.CSS_SELECTOR, 'a'),
                ]

                for by, selector in title_selectors:
                    try:
                        title_elem = event_elem.find_element(by, selector)
                        if title_elem and title_elem.text.strip():
                            event_data['name'] = title_elem.text.strip()
                            break
                    except NoSuchElementException:
                        continue

                # Extract date
                date_selectors = [
                    (By.CSS_SELECTOR, '.event-date'),
                    (By.CSS_SELECTOR, '.date'),
                    (By.CSS_SELECTOR, 'time'),
                    (By.XPATH, './/*[contains(@class, "date")]'),
                ]

                for by, selector in date_selectors:
                    try:
                        date_elem = event_elem.find_element(by, selector)
                        if date_elem and date_elem.text.strip():
                            event_data['date'] = date_elem.text.strip()
                            break
                    except NoSuchElementException:
                        continue

                # Extract time
                time_selectors = [
                    (By.CSS_SELECTOR, '.event-time'),
                    (By.CSS_SELECTOR, '.time'),
                    (By.XPATH, './/*[contains(@class, "time")]'),
                ]

                for by, selector in time_selectors:
                    try:
                        time_elem = event_elem.find_element(by, selector)
                        if time_elem and time_elem.text.strip():
                            event_data['time'] = time_elem.text.strip()
                            break
                    except NoSuchElementException:
                        continue

                # Extract location
                location_selectors = [
                    (By.CSS_SELECTOR, '.event-location'),
                    (By.CSS_SELECTOR, '.location'),
                    (By.CSS_SELECTOR, '.venue'),
                    (By.CSS_SELECTOR, '.branch'),
                    (By.XPATH, './/*[contains(@class, "location") or contains(@class, "venue") or contains(@class, "branch")]'),
                ]

                for by, selector in location_selectors:
                    try:
                        location_elem = event_elem.find_element(by, selector)
                        if location_elem and location_elem.text.strip():
                            event_data['location'] = location_elem.text.strip()
                            break
                    except NoSuchElementException:
                        continue

                # Only add if we found at least a name
                if event_data['name']:
                    events.append(event_data)

            except Exception as e:
                print(f"Error extracting event {i+1}: {e}")
                continue

        return events

    except TimeoutException:
        print("Timeout waiting for page to load")
        return events
    except Exception as e:
        print(f"Error: {e}")
        return events
    finally:
        if driver:
            driver.quit()


def print_events(events):
    """
    Print events in a formatted way.

    Args:
        events: List of event dictionaries
    """
    if not events:
        print("\nNo events found.")
        return

    print(f"\n{'='*80}")
    print(f"AUSTIN PUBLIC LIBRARY EVENTS")
    print(f"{'='*80}\n")

    for i, event in enumerate(events, 1):
        print(f"Event #{i}")
        print(f"  Name:     {event['name']}")
        print(f"  Date:     {event['date']}")
        print(f"  Time:     {event['time']}")
        print(f"  Location: {event['location']}")
        print(f"{'-'*80}")

    print(f"\nTotal events found: {len(events)}")


def main():
    """Main function to run the scraper."""
    url = "https://library.austintexas.gov/events"

    events = scrape_library_events_selenium(url)
    print_events(events)


if __name__ == "__main__":
    main()

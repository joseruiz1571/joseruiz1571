#!/usr/bin/env python3
"""
Austin Public Library Event Scraper
Extracts event name, date, time, and location from library.austintexas.gov/events
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime


def scrape_library_events(url):
    """
    Scrape events from Austin Public Library events page.

    Args:
        url: The URL of the events page

    Returns:
        List of dictionaries containing event information
    """
    # Set up headers to mimic a browser request
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Language': 'en-US,en;q=0.5',
        'Accept-Encoding': 'gzip, deflate, br',
        'Connection': 'keep-alive',
        'Upgrade-Insecure-Requests': '1'
    }

    try:
        # Fetch the webpage
        print(f"Fetching events from {url}...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()

        # Parse HTML
        soup = BeautifulSoup(response.content, 'html.parser')

        events = []

        # Try different common selectors for event listings
        # These are common patterns - may need adjustment based on actual page structure
        event_selectors = [
            {'container': 'div.event-item', 'title': '.event-title', 'date': '.event-date', 'time': '.event-time', 'location': '.event-location'},
            {'container': 'article.event', 'title': 'h2', 'date': '.date', 'time': '.time', 'location': '.location'},
            {'container': '.event-listing', 'title': 'h3', 'date': '.event-date', 'time': '.event-time', 'location': '.venue'},
            {'container': 'div[class*="event"]', 'title': 'h2, h3, .title', 'date': 'time, .date', 'time': '.time', 'location': '.location, .venue'},
        ]

        # Try to find events using different selectors
        event_elements = None
        for selector in event_selectors:
            event_elements = soup.select(selector['container'])
            if event_elements:
                print(f"Found {len(event_elements)} events using selector: {selector['container']}")
                break

        if not event_elements:
            # Fallback: try to find any event-related containers
            event_elements = soup.find_all(['article', 'div'], class_=lambda x: x and 'event' in x.lower())
            if event_elements:
                print(f"Found {len(event_elements)} events using fallback search")

        if not event_elements:
            print("\nNo events found. Page structure may have changed.")
            print("Showing page title and first 500 characters of content for debugging:")
            print(f"Title: {soup.title.string if soup.title else 'No title'}")
            print(f"Content preview: {soup.get_text()[:500]}...")
            return events

        # Extract event details
        for event_elem in event_elements:
            event_data = {
                'name': '',
                'date': '',
                'time': '',
                'location': ''
            }

            # Extract event name/title
            title_elem = event_elem.find(['h1', 'h2', 'h3', 'h4', 'a'], class_=lambda x: not x or 'title' in str(x).lower() or 'name' in str(x).lower())
            if not title_elem:
                title_elem = event_elem.find(['h1', 'h2', 'h3', 'h4'])
            if title_elem:
                event_data['name'] = title_elem.get_text(strip=True)

            # Extract date
            date_elem = event_elem.find(['time', 'span', 'div', 'p'], class_=lambda x: x and 'date' in str(x).lower())
            if not date_elem:
                date_elem = event_elem.find('time')
            if date_elem:
                event_data['date'] = date_elem.get_text(strip=True)

            # Extract time
            time_elem = event_elem.find(['span', 'div', 'p'], class_=lambda x: x and 'time' in str(x).lower())
            if time_elem:
                event_data['time'] = time_elem.get_text(strip=True)

            # Extract location
            location_elem = event_elem.find(['span', 'div', 'p', 'address'], class_=lambda x: x and ('location' in str(x).lower() or 'venue' in str(x).lower() or 'branch' in str(x).lower()))
            if location_elem:
                event_data['location'] = location_elem.get_text(strip=True)

            # Only add if we found at least a name
            if event_data['name']:
                events.append(event_data)

        return events

    except requests.exceptions.RequestException as e:
        print(f"Error fetching the webpage: {e}")
        return []
    except Exception as e:
        print(f"Error parsing events: {e}")
        return []


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

    events = scrape_library_events(url)
    print_events(events)


if __name__ == "__main__":
    main()

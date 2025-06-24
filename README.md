# SAT Seat Finder

> **Disclaimer**  
> This project is not affiliated with or endorsed by the College Board, which owns the SAT® trademark. It is also not affiliated with or endorsed by Pyto or the Pyto IDE. This tool is intended for educational and personal use only.

## Overview

**SAT_SeatFinder** is a lightweight Python script designed to help users quickly check for available SAT testing seats near a given location. It is optimized for use on mobile devices and supports home screen widgets through Python IDEs like **Pyto** on iOS.

## Features

- Simple configuration with minimal code edits  
- Mobile-friendly, ideal for on-the-go use  
- Optional widget support using **Pyto** for iOS  

## Requirements

- iOS device with the [**Pyto** IDE](https://pyto.app) installed  
- Internet access for API requests  

## Getting Started

1. **Open Pyto**  
   Launch the Pyto app.

1. **Create script**  

   Create a new blank script in Pyto and copy&paste [`satcenterfinder.py`](./satcenterfinder.py) to it. 

1. **Configure your inputs**  
   In the script, find the section marked `# Inputs` and update the following variables:
   ```python
   test_date = "YYYY-MM-DD"      # e.g., "2025-10-04"
   zipcode = "12345"             # your ZIP code
   state = "WA"                  # your state abbreviation
   country = "US"                # country code
   ```

1. **Run the script**  
   Tap the play button in Pyto to execute the script and view seat availability.

1. **Set up widget**  
   Go to home screen and add new Pyto widge with the script. The widget will be refreshed with available test centers every 30 minutes by default.

1. **(Optional) Change widget refresh time**   
   In the script, you may change the refresh time of the widget by changing the next reload time interval from 30 minutes to something else. 
   ```python
   wd.schedule_next_reload(timedelta(minutes=30))
   wd.show_widget(widget)
   ```
   (Note: Setting the time interval to a value too small may lead to the widget not updating properly.)
## Notes

- The script uses public test center availability data and may be subject to rate limits or access changes.
- Be sure to double-check availability and register on the official [College Board](https://satsuite.collegeboard.org/sat) site.

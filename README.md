# SAT Seat Finder

> **Disclaimer**  
> This project is not affiliated with or endorsed by the College Board, which owns the SAT® trademark. This tool is intended for educational and personal use only. It is also not affiliated with or endorsed by Pyto or the Pyto IDE. This tool is intended for educational and personal use only.

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

1. **Download the script**  
   Save the file [`satcenterfinder.py`](./satcenterfinder.py) to your mobile device.

2. **Open in Pyto**  
   Launch the Pyto app and open the script.

3. **Configure your inputs**  
   In the script, find the section marked `# Inputs` and update the following variables:
   ```python
   test_date = "YYYY-MM-DD"      # e.g., "2025-10-04"
   zipcode = "12345"             # your ZIP code
   state = "WA"                  # your state abbreviation
   country = "US"                # country code
   ```

4. **Run the script**  
   Tap the play button in Pyto to execute the script and view seat availability.

5. **(Optional) Set up a widget**  
   Pyto supports adding scripts as widgets to your iOS home screen. Use this feature to monitor seat availability without opening the app.

## Notes

- The script uses public test center availability data and may be subject to rate limits or access changes.
- Be sure to double-check availability and register on the official [College Board](https://satsuite.collegeboard.org/sat) site.

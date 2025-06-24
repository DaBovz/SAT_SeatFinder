# SAT Seat Finder

> **Disclaimer**  
> This project is not affiliated with or endorsed by the College Board, which owns the SAT® trademark. It is also not affiliated with or endorsed by Pyto or the Pyto IDE. This tool is intended for educational and personal use only.

## Overview

**SAT_SeatFinder** is a lightweight Python tool that helps you check for SAT testing seat availability near a given ZIP code and date. It supports both standard script execution and optional widget integration on iOS using **Pyto**.

---

## 🔹 Option 1: Standard Script (`satcenterfinder.py`)

This is the main version of the script. It runs directly in the Pyto console and is the most reliable way to use this tool.

### Features

- Simple configuration with minimal code edits  
- Prints results directly to the console  
- Reliable performance in the Pyto app  

### Requirements

- Program to run Python scripts
- Internet access for API requests  

### Getting Started

1. **Open Pyto**  
   Launch the Pyto app on your iOS device.

2. **Create a new script**  
   Copy and paste the contents of [`satcenterfinder.py`](./satcenterfinder.py) into a new script.

3. **Configure your inputs**  
   Find the section marked `# Inputs` and update the following variables:
   ```python
   test_date = "YYYY-MM-DD"      # e.g., "2025-10-04"
   zipcode = "12345"             # your ZIP code
   state = "WA"                  # your state abbreviation
   country = "US"                # country code
   
4. **Run the script**  
   Run the script in Pyto to see available centers printed in the console.

---

## 🔹 Option 2: Home Screen Widget (`satcenterfinderWIDGET.py`)

This version attempts to show results directly in a Pyto home screen widget.

> ⚠️ **Note:** The widget version is experimental and may not work correctly depending on your device or Pyto version. Use the main script above if the widget fails to update.

### Requirements

- iOS device with [**Pyto** IDE](https://pyto.app)  
- Internet access for API requests****

### Setup Instructions

1. **Open Pyto**

2. **Create a new script** and paste in [`satcenterfinderWIDGET.py`](./satcenterfinderWIDGET.py)

3. **Edit the same inputs** (`test_date`, `zipcode`, etc.)

4. **Add the Pyto widget** to your home screen and select this script

5. **(Optional) Adjust the widget's refresh interval**
   ```python
   wd.schedule_next_reload(timedelta(minutes=30))

> Avoid very short intervals to reduce update errors.

---

## Notes

- The script uses public test center availability data and may be subject to rate limits or access changes.
- Be sure to double-check availability and register on the official [College Board](https://satsuite.collegeboard.org/sat) site.

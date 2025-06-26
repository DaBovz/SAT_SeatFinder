# SAT Seat Finder

> **Disclaimer**  
> This project is not affiliated with or endorsed by the College Board, which owns the SAT® trademark. It is also not affiliated with or endorsed by Pyto or the Pyto IDE. This tool is intended for educational and personal use only.

## Overview

**SAT_SeatFinder** is a lightweight Python tool that helps you check for SAT testing seat availability near a given ZIP code and date. It supports both standard script execution and optional widget integration on iOS using **Pyto**.

---

## 🔹 Option 1: Standard Script (`satcenterfinder.py`)

This is the main version of the script and is compatible with any Python environment (desktop, terminal, mobile app, etc.).

### Features

- No dependencies beyond Python 3  
- Prints results directly to the terminal/console  

### Requirements

- Python 3.7+  
- Internet access for API requests  

### Getting Started

1. **Download the script**  
   Save [`satcenterfinder.py`](./satcenterfinder.py) to your local machine or device.

2. **Configure your inputs**  
   Open the script in any code editor and find the section marked `# Inputs`. Update the following:
   ```python
   test_date = "YYYY-MM-DD"      # e.g., "2025-10-04"
   zipcode = "12345"             # your ZIP code
   state = "WA"                  # your state abbreviation
   country = "US"                # usually "US"
   
4. **Run the script**  
   Run the script using the python environment

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

4. **Add the Pyto widget**

   Hold down on the home screen of your iOS device. Then click "edit" in the top left then click "Add Widget". Click on Pyto for the widget and then swipe right on the options until the option "Run script" is visible. Select the script with [`satcenterfinderWIDGET.py`](./satcenterfinderWIDGET.py) and place it where you want in your home screen.

6. **(Optional) Adjust the widget's refresh interval**
   ```python
   wd.schedule_next_reload(timedelta(minutes=30))

> Avoid very short intervals to reduce update errors.

---

## Notes

- The script uses public test center availability data and may be subject to rate limits or access changes.
- Be sure to double-check availability and register on the official [College Board](https://satsuite.collegeboard.org/sat) site.
- If you have any questions, run into issues, or have suggestions for improvements, feel free to email me at youngjinjack@gmail.com

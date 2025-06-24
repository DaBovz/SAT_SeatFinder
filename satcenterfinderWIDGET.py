import requests
from datetime import datetime, timedelta
import widgets as wd

BACKGROUND = wd.Color.rgb(255/255, 250/255, 227/255)
FOREGROUND = wd.Color.rgb(75/255, 72/255, 55/255)

def find_available_test_centers(date, zip_code, country, state):
    url = f"https://aru-test-center-search.collegeboard.org/prod/test-centers?date={date}&zip={zip_code}&country={country}"
    response = requests.get(url)

    if response.status_code == 200:
        test_centers = response.json()
        available_centers = [
            (center["name"], center["address1"], center["state"], center["distance"])
            for center in test_centers
            if center["seatAvailability"] and center["state"] == state
        ]
        available_centers.sort(key=lambda x: x[3])  # Sort by distance
        return available_centers
    else:
        print(f"Error: {response.status_code}")
        return []

# Inputs
date = "2025-08-23"
zip_code = "98006"
country = "US"
state = "WA"

# Widget setup
widget = wd.Widget()
layout_small = widget.small_layout
layout_medium = widget.medium_layout
layout_large = widget.large_layout
layout_extralarge = widget.extra_large_layout

# Print the title and current date time
now = datetime.now()
now_text = now.strftime("%H:%M")
title_text = wd.Text(
    text=f"Available centers for {date} SAT test as of {now_text}",
    font=wd.Font("AmericanTypewriter", 10),
    color=FOREGROUND
)

layout_small.add_row([title_text])
layout_medium.add_row([title_text])
layout_large.add_row([title_text])
layout_extralarge.add_row([title_text])

layout_small.add_vertical_divider()
layout_medium.add_vertical_divider()
layout_large.add_vertical_divider()
layout_extralarge.add_vertical_divider()

# Get available centers
available_centers = find_available_test_centers(date, zip_code, country, state)

if available_centers:
    for name, address, state, distance in available_centers:
        center_text_small = wd.Text(
            text=f"{name}, {distance} miles",
            font=wd.Font("AmericanTypewriter", 9),
            color=FOREGROUND
        )
        layout_small.add_row([center_text_small])

        center_text_medium = wd.Text(
            text=f"{name}, {distance} miles",
            font=wd.Font("AmericanTypewriter", 9),
            color=FOREGROUND
        )
        layout_medium.add_row([center_text_medium])

        center_text_large = wd.Text(
            text=f"{name}, {address}, {distance} miles",
            font=wd.Font("AmericanTypewriter", 9),
            color=FOREGROUND
        )
        layout_large.add_row([center_text_large])
        layout_extralarge.add_row([center_text_large])
else:
    error_text = wd.Text(
        text="No test centers with available seats found.",
        font=wd.Font("AmericanTypewriter", 18),
        color=FOREGROUND
    )
    layout_small.add_row([error_text])
    layout_medium.add_row([error_text])
    layout_large.add_row([error_text])
    layout_extralarge.add_row([error_text])

layout_small.set_background_color(BACKGROUND)
layout_medium.set_background_color(BACKGROUND)
layout_large.set_background_color(BACKGROUND)
layout_extralarge.set_background_color(BACKGROUND)

wd.schedule_next_reload(timedelta(minutes=30))
wd.show_widget(widget)

"""Default homescreen

This is the default homescreen for the Tilda Mk4.
It gets automatically installed when a badge is
newly activated or reset.
"""

___name___         = "Homescreen Lain"
___license___      = "MIT"
___categories___   = ["Homescreens"]
___dependencies___ = []
___launchable___   = True
___bootstrapped___ = True

import ugfx
from homescreen import *
import time
from machine import Pin

# tot height 320
status_height = 20
name_height = 60
# lain_img = ugfx.Image("shared/lain.gif")
lain_height = 200  # 180
lain_width = 194  # 175

# Maximum length of name before downscaling
max_name = 8

# Background stuff
init()
ugfx.clear(ugfx.BLACK)

# Colour stuff
style = ugfx.Style()
style.set_enabled([ugfx.html_color(0xe2a1b4),
                   ugfx.BLACK,
                   ugfx.BLACK,
                   ugfx.BLACK])
style.set_background(ugfx.BLACK)
ugfx.set_default_style(style)

# Draw for wearer to see
ugfx.orientation(270)
ugfx.set_default_font(ugfx.FONT_SMALL)
status = ugfx.Label(0, ugfx.height() - status_height,
                    ugfx.width(), status_height,
                    "", justification=ugfx.Label.CENTER)

# Draw for people to see
ugfx.orientation(90)
# Draw introduction
# ugfx.set_default_font(ugfx.FONT_TITLE)
# Process name
name_setting = name("Set your name in the settings app")
if len(name_setting) <= max_name:
    ugfx.set_default_font(ugfx.FONT_NAME)
else:
    ugfx.set_default_font(ugfx.FONT_MEDIUM_BOLD)
# Draw name
ugfx.Label(0, ugfx.height() - name_height - lain_height,
           ugfx.width(), name_height,
           name_setting, justification=ugfx.Label.CENTER)

# update loop
img = ugfx.Image("home_lain/res_lain.gif", False)
img.bg_color(ugfx.BLACK)
# ugfx.set_tear_line(lain_height)
# ugfx.enable_tear()
tear = Pin(11, Pin.IN)
while True:
    # i = i % 23
    text = "";
    value_wifi_strength = wifi_strength()
    value_battery = battery()
    if value_wifi_strength:
        text += "Wi-Fi: %s%%, " % int(value_wifi_strength)
    if value_battery:
        text += "Battery: %s%%" % int(value_battery)
    ugfx.orientation(270)
    status.text(text)
    # Logo stuff
    ugfx.orientation(90)
    img.display(
        (ugfx.width() - lain_width) // 2,
        ugfx.height() - lain_height)
    sleep_or_exit(img.next() / 100)
    # print(tear.value())
    # i += 1

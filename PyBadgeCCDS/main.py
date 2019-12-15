from adafruit_pybadger import PyBadger
display_name = "Your Name Here"
pybadger = PyBadger()

pybadger.show_badge(name_string=display_name, hello_scale=2, my_name_is_scale=2, name_scale=2)

while True:
    pybadger.auto_dim_display(delay=10) # Remove or comment out this line if you have the PyBadge LC
    try:
        if pybadger.button.a:
            pybadger.show_business_card(image_name="ccds_logo_160x160.bmp")
        elif pybadger.button.b:
            pybadger.show_qr_code(data="https://www.ccds.io/")
        elif pybadger.button.start:
            pybadger.show_badge(name_string=display_name, hello_scale=2, my_name_is_scale=2, name_scale=2)
    except Exception as ex:
        print(ex)
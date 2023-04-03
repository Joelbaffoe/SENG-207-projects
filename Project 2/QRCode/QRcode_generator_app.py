# Name : Joel Baffoe
# ID: 10627688 - Resit
# Department: FPEN

# Importing libraries
import PySimpleGUI as sg
import qrcode
import re

# Error Checking Function


def check_url(URL):
    URL = re.sub(r"\s+", "", URL, flags=re.UNICODE)
    regex = 'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+'
    if not re.match(regex, URL):
        URL = f'https://{URL}'
    return URL


    # Layout of App
layout = [
    [
        sg.Text("Enter URL Here: "),
        sg.Input(key='URL'),
    ],
    [
        sg.Button(button_text="Create", key="Create"),
        sg.Text(text='Kindly Enter the full URL(including the https:// or http:// )')
    ],
    [
        sg.Text(text="", key="Status")
    ],
    [
        sg.Text(text="", key="Content")
    ],
    [sg.Image(key='QRCODE')]
]

# Window
myApp = sg.Window(title='QR code Generator', layout=layout)

# Create an event loop
while True:
    event, values = myApp.read()
    print(event, values)
    myApp['URL'].update(move_cursor_to=5)
    if event == "Create":
        if not values['URL']:
            myApp['Status'].update(
                value='Enter Valid URL', text_color='red')
        else:
            URL = values['URL']
            URL = check_url(URL)
            img = qrcode.make(URL)
            img.save("qrCode.png")
            myApp['Status'].update(
                value='URL Created Successfully!', text_color='green', background_color='white')
            myApp['Content'].update(value=URL,
                                    background_color='black', text_color='white')
            myApp['QRCODE'].update(source='qrCode.png')
    # End program if user closes
    if event == sg.WIN_CLOSED:
        break


myApp.close()

# Name : Joel Baffoe
# ID: 10627688 - Resit
# Department: FPEN

# Importing libraries
import pyttsx3
import PySimpleGUI as sg

# Initializing  Text to Speech Engine
engine = pyttsx3.init()
voices = engine.getProperty('voices')
m_voice = voices[0]
f_voice = voices[1]

# Layout of App
layout = [
    [
        sg.Input(default_text="Enter text here", key='Text'),
        sg.Button(button_text="Speak", key="Speak")
    ],
    [
        sg.Text(text='Select Voice Type:'),
        sg.Radio(group_id='gender', text='Male', default=True, key='male'),
        sg.Radio(group_id='gender', text='Female', key="female")
    ]
]

# Window
myApp = sg.Window(title='Text To Speech App', layout=layout,)


# Create an event loop
while True:
    event, values = myApp.read()
    print(event, values)
    if event == "Speak":
        if values['male']:
            engine.setProperty('voice', m_voice.id)
        if values['female']:
            engine.setProperty('voice', f_voice.id)
        engine.say(values['Text'])
    engine.runAndWait()
    # End program if user closes
    if event == sg.WIN_CLOSED:
        break


myApp.close()

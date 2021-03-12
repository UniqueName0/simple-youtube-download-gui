import PySimpleGUI as sg
import pytube
from pytube import YouTube

sg.theme('DarkAmber')
layout = [  [sg.Text('Enter url of video'), sg.InputText()],
            [sg.Button('Ok'), sg.Button('Cancel')] ]

window = sg.Window('Window Title', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Cancel':
        break

    yt = YouTube(values[0]) 

    pytube.YouTube(values[0])
    stream = yt.streams.first()
    stream.download("./")

    window.close
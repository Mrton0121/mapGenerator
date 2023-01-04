import eel
from generator import GenerateMap

eel.init("web")

@eel.expose
def send_data():
    return "Ezt az adatot"

@eel.expose
def get_data(params):
    GenerateMap(params)
    print("Generating has been successful...")

eel.start("index.html")

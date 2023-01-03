import eel

eel.init("web")

@eel.expose
def send_data():
    return "Ezt az adatot"

@eel.expose
def get_data(msg):
    print(msg[0],"asd")

eel.start("index.html")

function setDefaultValues(){
    document.getElementById("m_width").value = 100;
    document.getElementById("m_height").value = 100;

}

async function getDataFromPython(){
    document.getElementById("title").innerText = await eel.send_data()();
}

function getData(){
    getDataFromPython();
}

async function sendDataToPython(msg){
    await eel.get_data(msg);
}

function sendData(){
    let m_width = document.getElementById("m_width").value;
    let m_height = document.getElementById("m_height").value;
    sendDataToPython([m_width,m_height]);
}
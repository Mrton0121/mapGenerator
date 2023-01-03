function setDefaultValues(){
    document.getElementById("m_width").value = 10;
    document.getElementById("m_height").value = 10;

}

async function getDataFromPython(){
    document.getElementById("title").innerText = await eel.send_data()();
}

function get_data(){
    getDataFromPython();
}

async function sendDataToPython(msg){
    await eel.get_data(msg);
}

function send_data(){
    let m_width = document.getElementById("m_width").value;
    let m_height = document.getElementById("m_height").value;
    sendDataToPython([m_width,m_height]);
}

function teszt(n){
    alert(n);
}
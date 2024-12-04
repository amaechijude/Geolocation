// Get full url
const urlForm = document.getElementById("urlForm");
urlForm.addEventListener("submit", async (event) => {
    event.preventDefault();
    const form = new FormData(urlForm);
 
    const response = await fetch(`/get_url`, {
        method: 'POST',
        body: form
    });
    const data = await response.json();
    console.log(data);
    urlForm.reset();
});




function GetDistance(sId, sURL) {
    const trow = document.getElementById(`distance_${sId}`);
    trow.textContent = sURL;
}

function CurrentLocation()
{
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosiion)
    } else {
        console.log("Odi egwu")
    }
}

function showPosiion(position) {
    console.log(position.coords.latitude);
}
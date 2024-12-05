// Get full url
async function Coordinate(paramID) {
    try {
        const response = await fetch(`/get_url/${paramID}`);
        const data = await response.json();
        console.log(data)

    } catch (error) {
        console.log("Server error");
    }
}



function GetDistance(sId, sURL) {
    const trow = document.getElementById(`distance_${sId}`);
    trow.textContent = sURL;
}

function CurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosiion)
    } else {
        console.log("Odi egwu")
    }
}

function showPosiion(position) {
    const latitude = position.coords.latitude;
    const longiude = position.coords.longiude;
}
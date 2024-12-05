// csrftoken
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
      const cookies = document.cookie.split(';');
      for (let i = 0; i < cookies.length; i++) {
        const cookie = cookies[i].trim();
        if (cookie.substring(0, name.length + 1) === (name + '=')) {
          cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
          break;
        }
      }
    }
    return cookieValue;
  }
  
  const csrftoken = getCookie('csrftoken');
  

let schId;
let schURL;
async function GetDistance(sId, sURL) {
    schId = sId;
    schURL = sURL;
    await CurrentLocation();
}

async function CurrentLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition)
    } else {
        console.log("Odi egwu")
    }
}

async function showPosition(position) {
    const userLatitude = position.coords.latitude;
    const userLongitude = position.coords.longitude;

    // fetch to the backend
    const response = await fetch(`/getDistance/${schId}`, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrftoken
        },
        body: JSON.stringify({
            "userLongitude": userLongitude,
            "userLatitude": userLatitude
        })
    });

    const data = await response.json();
    // console.log(data.distance);
    trow = document.getElementById(`distance_${schId}`);
    trow.innerHTML = `<strong>${data.distance} </strong> : kilometers`;
}

// fetch to backend with user location data
// async function sendUserLocationData(schoolID, userLongitude, userLatitude) {
//     const response = await fetch(`/getDistance/${schoolID}`, {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json',
//             'X-CSRFToken': csrftoken
//         },
//         body: JSON.stringify({
//             "userLongitude": userLongitude,
//             "userLatitude": userLatitude
//         })
//     });

//     const data = response.json();
//     console.log(data);
//     trow = document.getElementById(`distance_${schId}`);
//     trow.textContent = `${data['distance']} kilometers`;

// }

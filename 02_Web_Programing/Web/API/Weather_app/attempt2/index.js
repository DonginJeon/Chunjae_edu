async function getApi(city) {
    const API_KEY = '4ef3ba3aeb065135a2aa9243e787d81a'
    const API_URL = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${API_KEY}`
    const response = await fetch(API_URL);
    const json = await response.json();

    return json;
}

function setImage(main) {
    const image = document.querySelector(".weather-box img");
    switch (main) {
        case "Clear":
            image.src = "images/clear.png"
            break;
        case "Rain":
            image.src = "images/rain.png"
            break;
        case "Snow":
            image.src = "images/snow.png";
            break;
        case "Clouds":
            image.src = "images/cloud.png";
            break;
        case "Haze":
            image.src = "images/mist.png";
            break;
        default:
            image.src = "";
    }
}

const container = document.querySelector(".container");
const search = document.querySelector(".search-box button");
const weatherBox = document.querySelector(".weather-box");
const weatherDetails = document.querySelector(".weather-details");
const error404 = document.querySelector(".not-found");

search.addEventListener("click", async () => {
    const city = document.querySelector(".search-box input").value;
    // #. 변수명만 if문에다가 적을 경우
    // #. city !== null && city !== ""
    // #. !city > city === null || city === ""
    if (!city) {
        return;
    }

    const json = await getApi(city);
    // #. API 값이 404 Not Found 였을 때 유효한 주소가 아닐때
    if (json.cod === "404") {
        container.style.height = "400px";
        weatherBox.style.display = "none";
        weatherDetails.style.display = "none";
        error404.style.display = "block";
        error404.classList.add("fadeIn");
        return;
    }

    error404.style.display = "none";
    error404.classList.remove("fadeIn");

    const temperature = document.querySelector(".weather-box .temperature");
    const description = document.querySelector(".weather-box .description");
    const humidity = document.querySelector(".weather-details .humidity span");
    const wind = document.querySelector(".weather-details .wind span");

    setImage(json.weather[0].main);
    temperature.innerHTML = `${parseInt(json.main.temp)}<span>°C</span>`;
    description.innerHTML = `${json.weather[0].description}`;
    humidity.innerHTML = `${json.main.humidity}%`;
    wind.innerHTML = `${parseInt(json.wind.speed)}Km/h`;

    weatherBox.style.display = "";
    weatherDetails.style.display = "";
    weatherBox.classList.add("fadeIn");
    weatherDetails.classList.add("fadeIn");
    container.style.height = "590px";

});
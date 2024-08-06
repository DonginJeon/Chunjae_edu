async function getApi(city) {
    const API_KEY = 'eb0f5be5adcbec6668756c4c292d7079'
    const API_URL = `https://api.openweathermap.org/data/2.5/weather?q=${city}&units=metric&appid=${API_KEY}`
    const response = await fetch(API_URL);
    const json = await response.json();
    return json;
}

function setImage(main) {
    switch (json.weather[0].main) {
        case 'Clear':
            image.src = 'images/clear.png';
            break;

        case 'Rain':
            image.src = 'images/rain.png';
            break;

        case 'Snow':
            image.src = 'images/snow.png';
            break;

        case 'Clouds':
            image.src = 'images/cloud.png';
            break;

        case 'Haze':
            image.src = 'images/mist.png';
            break;
        default:
            image.src = '';
    }
}

const container = document.querySelector('.container');
const search = document.querySelector('.search-box button');
const weatherBox = document.querySelector('.weather-box');
const weatherDetails = document.querySelector('.weather-details');
const error404 = document.querySelector('.not-found');


// 이벤트 리스너를 달아준다
// 함수를 바깥에 선언해도 되고 직접 안에 이름없는 함수를 넣어도 된다

search.addEventListener("click", async () => {
    // 사용자의 입력값을 받는 태그들
    // value라는 속성을 가진다
    // value = 사용자의 입력값을 가져온다
    const city = document.querySelector(".search-box input").value;
    console.log(city);


    // 변수명만 if문에다가 적을 경우
    // city !== null && city !== ""
    //!city >city === null || city === ""
    if (!city)
        return;


    // error 핸들링 용도로 try ~ catch 문이 있다
    // try는 에러가 나는 문에서 사용하면 되고 catch는 실제 에러가 났을 때 처리를 해줍니다.
    const json = await getApi(city);
    // API 값이 404 not found 였을때(유효한 주소가 아닐때)
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

    const image = document.querySelector('.weather-box img');
    const temperature = document.querySelector('.weather-box .temperature');
    const description = document.querySelector('.weather-box .description');
    const humidity = document.querySelector('.weather-details .humidity span');
    const wind = document.querySelector('.weather-details .wind span');

    setImage(json.weather[0].main);
    temperature.innerHTML = `${parseInt(json.main.temp)}<span>°C</span>`;
    description.innerHTML = `${json.weather[0].description}`;
    humidity.innerHTML = `${json.main.humidity}%`;
    wind.innerHTML = `${parseInt(json.wind.speed)}Km/h`;

    weatherBox.style.display = '';
    weatherDetails.style.display = '';
    weatherBox.classList.add('fadeIn');
    weatherDetails.classList.add('fadeIn');
    container.style.height = '590px';



});




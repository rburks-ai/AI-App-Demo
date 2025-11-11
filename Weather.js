import { useState } from "react";

export default function WeatherApp() {
  const [city, setCity] = useState("");
  const [weather, setWeather] = useState(null);
  const [error, setError] = useState("");

  const getWeather = async () => {
    setError("");
    setWeather(null);
    try {
      // Step 1: Get city coordinates
      const geoRes = await fetch(
        `https://geocoding-api.open-meteo.com/v1/search?name=${city}`
      );
      const geoData = await geoRes.json();

      if (!geoData.results || geoData.results.length === 0) {
        setError("City not found.");
        return;
      }

      const { latitude, longitude, name, country } = geoData.results[0];

      // Step 2: Get weather data
      const weatherRes = await fetch(
        `https://api.open-meteo.com/v1/forecast?latitude=${latitude}&longitude=${longitude}&current_weather=true`
      );
      const weatherData = await weatherRes.json();

      setWeather({
        name,
        country,
        temperature: weatherData.current_weather.temperature,
        windspeed: weatherData.current_weather.windspeed,
        code: weatherData.current_weather.weathercode,
      });
    } catch (err) {
      setError("Error fetching weather data.");
    }
  };

  return (
    <div className="flex flex-col items-center justify-center min-h-screen bg-gradient-to-br from-sky-100 to-sky-300 p-6">
      <h1 className="text-3xl font-bold mb-4 text-sky-800">🌤️ Weather App</h1>

      <div className="flex gap-2 mb-4">
        <input
          type="text"
          placeholder="Enter city name..."
          value={city}
          onChange={(e) => setCity(e.target.value)}
          className="px-3 py-2 border border-sky-400 rounded-lg focus:outline-none focus:ring-2 focus:ring-sky-500"
        />
        <button
          onClick={getWeather}
          className="px-4 py-2 bg-sky-500 text-white rounded-lg hover:bg-sky-600 transition"
        >
          Get Weather
        </button>
      </div>

      {error && <p className="text-red-600">{error}</p>}

      {weather && (
        <div className="bg-white rounded-2xl shadow-md p-6 mt-4 text-center w-72">
          <h2 className="text-xl font-semibold mb-2">
            {weather.name}, {weather.country}
          </h2>
          <p className="text-4xl font-bold">{weather.temperature}°C</p>
          <p className="text-gray-600 mt-2">💨 {weather.windspeed} km/h wind</p>
          <p className="text-gray-700 mt-1">Code: {weather.code}</p>
        </div>
      )}

      <footer className="mt-10 text-gray-500 text-sm">
        Powered by{" "}
        <a
          href="https://open-meteo.com/"
          target="_blank"
          rel="noopener noreferrer"
          className="underline"
        >
          Open-Meteo API
        </a>
      </footer>
    </div>
  );
}

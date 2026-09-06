document.addEventListener("DOMContentLoaded", function () {

    console.log("JavaScript loaded!");

    const form = document.getElementById("predictionForm");

    form.addEventListener("submit", async function (event) {

        event.preventDefault();

        console.log("Predict button clicked!");

        const ocean = document.getElementById("ocean_proximity").value;

        const data = {
            longitude: Number(document.getElementById("longitude").value),
            latitude: Number(document.getElementById("latitude").value),
            housing_median_age: Number(document.getElementById("housing_median_age").value),
            total_rooms: Number(document.getElementById("total_rooms").value),
            total_bedrooms: Number(document.getElementById("total_bedrooms").value),
            population: Number(document.getElementById("population").value),
            households: Number(document.getElementById("households").value),
            median_income: Number(document.getElementById("median_income").value),

            ocean_proximity_INLAND: ocean === "INLAND" ? 1 : 0,
            ocean_proximity_ISLAND: ocean === "ISLAND" ? 1 : 0,
            ocean_proximity_NEAR_BAY: ocean === "NEAR BAY" ? 1 : 0,
            ocean_proximity_NEAR_OCEAN: ocean === "NEAR OCEAN" ? 1 : 0
        };

        console.log("Sending data:", data);

        try {

            const response = await fetch(
                "http://127.0.0.1:8000/predict",
                {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json"
                    },
                    body: JSON.stringify(data)
                }
            );

            console.log("Response status:", response.status);

            const result = await response.json();

            console.log("Result:", result);

            if (!response.ok) {
                throw new Error(result.detail || "Prediction failed");
            }

            document.getElementById("result").innerText =
                "Predicted House Price: $" +
                result.prediction.toFixed(2);

        } catch (error) {

            console.error("Error:", error);

            document.getElementById("result").innerText =
                "Error: " + error.message;
        }

    });

});
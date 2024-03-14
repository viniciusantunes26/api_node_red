document.addEventListener("DOMContentLoaded", function () {
    fetch("/api/dados/")
        .then(response => response.json())
        .then(data => displayData(data))
        .catch(error => console.error("Erro ao obter dados da API:", error));
});

function displayData(data) {
    const displayDiv = document.getElementById("data-display");
    data.forEach(item => {
        const dataItem = document.createElement("div");
        dataItem.classList.add("data-item");
        dataItem.innerHTML = `
            <label>Sensor:</label> <span>${item.Sensor}</span><br>
            <label>Botao:</label> <span>${item.Botao}</span><br>
            <label>LigaRobo:</label> <span>${item.LigaRobo}</span><br>
            <label>ResetContador:</label> <span>${item.ResetContador}</span><br>
            <label>ValorContagem:</label> <span>${item.ValorContagem}</span><br>
        `;
        displayDiv.appendChild(dataItem);
    });
}

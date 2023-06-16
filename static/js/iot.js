// Função para lidar com o botão "Checar Sensor"
document.getElementById("checar").addEventListener("click", function() {
    var sensorSelecionado = document.getElementById("sens").value;
    alert("O sensor selecionado é: " + sensorSelecionado);
  });
  
  // Função teste para lidar com o botão "Modificar Sensor"
  document.getElementById("modificar").addEventListener("click", function() {
    var novoNomeSensor = prompt("Digite o novo nome do sensor:");
    if (novoNomeSensor) {
      var sensorSelecionado = document.getElementById("sens").value;
      var option = document.querySelector("#sens option[value='" + sensorSelecionado + "']");
      option.innerHTML = novoNomeSensor;
    }
  });
  
  // Função teste para lidar com o botão "Ativar/Desativar Sensor"
  document.getElementById("ativar-desativar").addEventListener("click", function() {
    var sensorSelecionado = document.getElementById("sens").value;
    var option = document.querySelector("#sens option[value='" + sensorSelecionado + "']");
    if (option.disabled) {
      option.disabled = false;
      alert("O sensor " + sensorSelecionado + " foi ativado");
    } else {
      option.disabled = true;
      alert("O sensor " + sensorSelecionado + " foi desativado");
    }
  });

  document.getElementById("add-remove").addEventListener("click", function() {
    var action = prompt("Deseja adicionar ou remover um sensor? (a/r)");
    if (action === "a") {
      var novoSensor = prompt("Digite o nome do novo sensor:");
      if (novoSensor) {
        var option = document.createElement("option");
        option.value = document.getElementById("sens").options.length + 1;
        option.innerHTML = novoSensor;
        document.getElementById("sens").appendChild(option);
      }
    } else if (action === "r") {
      var sensorSelecionado = document.getElementById("sens").value;
      var option = document.querySelector("#sens option[value='" + sensorSelecionado + "']");
      option.remove();
    }
  });
  
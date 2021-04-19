var building = true;
var planting = false;

function modeToggle(){
  var plant-button = document.getElementById("planting-button");
  var build-button = document.getElementById("building-button");
  if(building){ //if building mode is enabled
    planting = true;
    building = false;
    plant-button.classList.add("enabled"); //trigger a change in the CSS by changing the classes around
    plant-button.classList.remove("disabled");
    build-button.classList.add("disabled");
    build-button.classList.remove("enabled");
  } else { //if planting mode is enabled
    planting = false;
    building = true;
    plant-button.classList.add("disabled"); //trigger a change in the CSS by changing the classes around
    plant-button.classList.remove("enabled");
    build-button.classList.add("enabled");
    build-button.classList.remove("disabled");
  }
}

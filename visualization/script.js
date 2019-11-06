function assignDensities(dens) {
  for (i = 0; i < dens.length; i++) {
    document.getElementById(i).innerHTML = dens[i].toString() + "%";
  }
}

function changeDensities(lane, time) {
  let val = document.getElementById(lane).innerHTML.split("%")[0];
  // val = newval
  document.getElementById(i).innerHTML = newVal.toString() + "%";
}

fetch("http://127.0.0.1:5000/getDensities")
  .then(res => {
    res.json();
  })
  .then(data => {
    console.log(data);
    assignDensities(data.dens);
  });

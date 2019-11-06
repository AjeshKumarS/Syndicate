let initialAssign = true;
let prevDens = [];

function initDensities(dens) {
  prevDens = dens;
  for (i = 0; i < dens.length; i++) {
    document.getElementById(i).innerHTML = Math.floor(dens[i]).toString() + "%";
  }
}

function fixedDensities(dens) {
  for (i = 0; i < dens.length; i++) {
    document.getElementById((i + 4).toString()).innerHTML =
      Math.floor(dens[i]).toString() + "%";
  }
}

// function assignDensities(dens) {
//   let update = setInterval(() => {
//     for (i = 0; i < dens.length; i++) {
//       // let val = document.getElementById(i).innerHTML.split("%")[0];
//       if (prevDens[i] <= dens[i]) clearInterval(update);
//       else prevDens[i]--;
//       document.getElementById(i).innerHTML =
//         Math.floor(prevDens[i]).toString() + "%";
//     }
//   }, 500);
// }

setInterval(() => {
  fetch("http://127.0.0.1:5000/getDensities")
    .then(res => {
      return res.json();
    })
    .then(data => {
      for (i = 0; i < data.dens.length; i++)
        data.dens[i] = Math.floor(data.dens[i]);
      console.log(data.dens);
      if (initialAssign) {
        initDensities(data.dens);
      } else assignDensities(data.dens);
    });
}, 500);

setInterval(() => {
  fetch("http://127.0.0.1:5000/getFixed")
    .then(res => {
      return res.json();
    })
    .then(data => {
      for (i = 0; i < data.dens.length; i++)
        data.dens[i] = Math.floor(data.dens[i]);
      console.log(data.dens);
      if (initialAssign) {
        fixedDensities(data.dens);
      } else assignDensities(data.dens);
    });
}, 500);

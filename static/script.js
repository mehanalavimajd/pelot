let inputs = document.querySelectorAll("input");
let dict = {
  meter: 190,
  district: "bagh-feyz",
  elevator: 0,
  space: 0,
  rooms: 0,
  floor: 0,
  parking: 0,
  buildYear: 1370,
};
function drop() {
  alert("لطفا همه داده‌ها را وارد کنید");
}
let button = document.querySelector("button");
let select = document.querySelector("select");

button.addEventListener("click", () => {
  let c = true;
  if (select.value == "sel") {
    drop();
    c = false;
  } else {
    dict.district = select.value;
    for (let i = 0; i < inputs.length; i++) {
      const e = inputs[i];
      if (e.value == "") {
        drop();
        c = false;
        break;
      }
      if (i == 0) {
        if (e.value < 10) {
          alert("مساحت منطقی نیست");
          c = false;
          break;
        }
        dict.meter = Number(e.value);
      }
      if (i == 1) {
        let d = e.value;
        if (e.value > 4) d = 4;
        dict.rooms = Number(d);
      }
      if (i == 2) dict.floor = Number(e.value);
      if (i == 3) {
        if (e.value < 1300 || e.value > 1404) {
          alert("سال منطقی نیست");
          c = false;
          break;
        }
        dict.buildYear = Number(e.value);
      }
      if (i == 4) dict.parking = e.checked ? 1 : 0;
      if (i == 5) dict.space = e.checked ? 1 : 0;
      if (i == 6) dict.elevator = e.checked ? 1 : 0;
    }
  }
  if (c) {
    fetch("/predict", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(dict),
    })
      .then((response) => response.json())
      .then((data) => {
        String.prototype.toPersianDigits = function () {
          var id = ["۰", "۱", "۲", "۳", "۴", "۵", "۶", "۷", "۸", "۹"];
          return this.replace(/[0-9]/g, function (w) {
            return id[+w];
          });
        };
        let prediction = String(data.prediction);
        let digit = document.querySelector(".price-digit");
        digit.innerHTML = prediction.toPersianDigits();
      });
  }
});

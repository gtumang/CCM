window.onload = function () {
  btn = document.getElementById('btn_teste');
  btn.addEventListener('click', teste);
  function teste() {
    var enable;
    if (localStorage.getItem('teste') == null) {
      enable = false;
    } else {
      let en = (localStorage.getItem('teste') === 'true');
      enable = !en;
    }
    localStorage.setItem('teste', enable);

    if (enable) {
      btn.style.color = "green";
    } else {
      btn.style.color = "red";
    }
  }
}
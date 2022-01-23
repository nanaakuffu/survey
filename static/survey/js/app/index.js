const emailSent = document.getElementById("eMails");
const emailResponded = document.getElementById("eMailRes");

const reLoad = () => {
  fetch("/home")
    .then((response) => response)
    .then(async (res) => {
      const data = await res.json();
      emailSent.textContent = data.sent;
      emailResponded.textContent = data.response;
    })
    .catch((err) => console.log(err));
};

setInterval(reLoad, 5000);

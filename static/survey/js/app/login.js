const loginForm = document.getElementById("login-form");

loginForm.addEventListener("submit", (e) => {
  e.preventDefault();

  const formData = new FormData(loginForm);

  console.log(...formData);

  fetch("/accounts/login/", {
    method: "POST",
    body: formData,
  })
    .then((response) => response)
    .then(async (responseData) => {
      const data = await responseData.json();
      console.log(data);
    })
    .catch((err) => console.log(err));

  alert("here");
});
// $("#login-form").on("submit", function (e) {
//   e.preventDefault();

//   alert("here");

//   $.ajax({
//     url: "{% url 'login' %}",
//     method: "POST",
//     data: $("#login-form").serialize(),
//     type: "json",
//     success: function (response) {
//       console.log(response);
//       // let jObj = JSON.parse(response);
//       // if (jObj.status == 200) {
//       //   window.location.href = "index.php";
//       // } else {
//       //   $("#logAlert").show();
//       //   $("#logAlert").html(jObj.message);
//       // }
//     },
//   });
// });

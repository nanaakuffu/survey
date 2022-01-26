const addRecipient = document.getElementById("addRecipient");
const saveRecipientDetails = document.getElementById("saveRecipient");
const recipientModal = new bootstrap.Modal(
  document.getElementById("recipientModal"),
  {}
);
const formElements = document.querySelectorAll(
  "#recipient-form input[type=text]"
);

const form = document.getElementById("recipient-form");

const recipientId = document.getElementById("id");

const clearFieldsAndShowModal = () => {
  for (const element of formElements) {
    document.getElementById(element.id).value = "";
  }

  recipientModal.show();
};

const showRecipientDetails = (recipientData) => {
  for (const element of formElements) {
    document.getElementById(element.id).value = recipientData[element.id];
  }

  recipientModal.show();
};

const viewRecipientData = (id) => {
  fetch(`/recipients/${id}/edit`)
    .then((response) => response)
    .then(async (res) => {
      const data = await res.json();

      showRecipientDetails(data.data);
    });
};

const sendSurveyEmail = (id) => {
  fetch(`/survey/send-survey`, {
    method: "POST",
    body: { id },
  });
};

addRecipient.addEventListener("click", (e) => {
  clearFieldsAndShowModal();
});

saveRecipientDetails.addEventListener("click", (e) => {
  e.preventDefault();
  const id = recipientId.value;
  const url = id > 0 ? `/recipients/${id}/update` : "/recipients";

  const formData = new FormData(form);

  fetch(url, {
    method: "POST",
    body: formData,
  })
    .then((response) => response)
    .then(async (res) => {
      const data = await res.json();

      if (data.status === 200) {
        recipientModal.hide();
        window.location.reload();
      }
    })
    .catch((err) => console.log(err));
});

Chart.defaults.global.defaultFontFamily =
  '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = "#292b2c";

const plotChart = (data, ctx) => {
  let dataLabels = [],
    dataValues = [];

  for (let i in data) {
    dataLabels.push(i);
    dataValues.push(data[i]);
  }

  let arrLegend = [
    "Compliant",
    "Partially Compliant",
    "Not Compliant",
    "Not Applicable",
  ];

  let chartData = {
    labels: arrLegend.slice(0, dataLabels.length),
    datasets: [
      {
        label: "Responses",
        backgroundColor: "rgba(2,117,216,1)",
        borderColor: "rgba(2,117,216,1)",
        barThickness: 5,
        data: dataValues,
      },
    ],
  };

  let chartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      yAxes: [{ ticks: { fontSize: 14 } }],
      xAxes: [{ ticks: { min: 0, fontSize: 14 } }],
    },
    legend: { display: false },
  };

  window.bar = new Chart(ctx, {
    type: "horizontalBar",
    data: chartData,
    options: chartOptions,
  });
};

Notiflix.Loading.Init({
  className: "notiflix-loading",
  zindex: 4000,
  backgroundColor: "rgba(0,0,0,0.8)",
  useGoogleFont: true,
  fontFamily: "Raleway",
  cssAnimation: true,
  cssAnimationDuration: 400,
  clickToClose: false,
  messageID: "NotiflixLoadingMessage",
  messageFontSize: "15px",
  messageMaxLength: 34,
  messageColor: "#dcdcdc",
});

function csrfSafeMethod(method) {
  // these HTTP methods do not require CSRF protection
  return /^(GET|HEAD|OPTIONS|TRACE)$/.test(method);
}

function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== "") {
    var cookies = document.cookie.split(";");
    for (var i = 0; i < cookies.length; i++) {
      var cookie = jQuery.trim(cookies[i]);
      // Does this cookie string begin with the name we want?
      if (cookie.substring(0, name.length + 1) === name + "=") {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

$(function () {
  var loadingDialog = Notiflix.Loading;
  var reportDialog = Notiflix.Report;

  // alert(sendMessage);
  $("#logAlert").hide();

  // Scroll to top button appear
  $(document).on("scroll", function () {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $(".scroll-to-top").fadeIn();
    } else {
      $(".scroll-to-top").fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on("click", "a.scroll-to-top", function (event) {
    var $anchor = $(this);
    $("html, body")
      .stop()
      .animate(
        {
          scrollTop: $($anchor.attr("href")).offset().top,
        },
        1000,
        "easeInOutExpo"
      );
    event.preventDefault();
  });

  $(document).on("click", ".deleteData", function () {
    // get the product id
    var valueID = $(this).attr("data-id");

    // bootbox for good looking 'confirm pop up'
    bootbox.confirm({
      message: "<h4>Are you sure you want to delete this data?</h4>",
      centerVertical: true,
      buttons: {
        confirm: {
          label: "Yes",
          className: "btn-danger",
        },
        cancel: {
          label: "No",
          className: "btn-primary",
        },
      },
      callback: function (result) {
        if (result) {
          // send delete request to api / remote server
          $.getJSON(
            "_data_processor.php",
            `flag=delete&key=${valueID}`,
            function (data) {
              let responseData = data.deleting;
              if (responseData == "user_details") {
                window.location.href = "display_users.php";
              } else {
                window.location.href = responseData + ".php";
              }
            }
          );
        }
      },
    });
  });

  $("#qEditModal").on("show.bs.modal", function (e) {
    let id = $(e.relatedTarget).data("id");

    $.getJSON("/questions/show", { questionID: id }, function (data) {
      $("#e_question_text").val(data.question_text);
      $("#e_recommendation").val(data.recommendation);
      $("#key").val(id);
    });
  });

  $("#aEditModal").on("show.bs.modal", function (e) {
    let id = $(e.relatedTarget).data("id");

    $.getJSON("/answers/show", { answerID: id }, function (data) {
      $("#e_answer").val(data.answer);
      $("#e_question").val(data.question);
      $("#e_choice").val(data.choice);
      if (data.needs_recommendation == 1) {
        $("#e_needs_recommendation").prop("checked", true);
      } else {
        $("#e_needs_recommendation").prop("checked", false);
      }
      $("#id").val(id);
    });
  });

  $("#EditModal").on("show.bs.modal", function (e) {
    let id = $(e.relatedTarget).data("id");

    $.getJSON("/recipients/show", { recID: id }, function (data) {
      $("#e_name").val(data.name);
      $("#e_email").val(data.email);
      $("#e_contact").val(data.contact_number);
      $("#e_institution").val(data.institution);
      $("#key").val(id);
    });
  });

  $("#surveyResponseForm").on("submit", function (e) {
    e.preventDefault();

    let formData = $("#surveyResponseForm").serialize();

    // alert(formData);

    if (formData.split("&").length == 27) {
      // Start the indicator
      loadingDialog.Circle();

      // Send the survey
      $.ajax({
        method: "POST",
        url: "/survey/process",
        data: formData,
        type: "json",
        success: function (responseData) {
          loadingDialog.Remove();

          if (responseData.status != 200) {
            reportDialog.Failure(
              "Survey Feedback",
              `${responseData.message}. Meaning: Your responses could not be sent. It may be due to bad internet connection or wrong email address. Please contact PharmAccess for help`,
              "Ok! Thanks."
            );
          } else {
            window.location.href = "/survey/sent";
          }
        },
      });
    }
  });

  $("#sendSurvey").on("click", function (e) {
    // alert($("#key").val());
    let sendID = $("#key").val();
    let sendeMail = $("#e_email").val();
    let errMess = "";

    let csrftoken = getCookie("csrftoken");

    // alert(sendeMail);

    $("#EditModal").modal("hide");

    loadingDialog.Circle();

    $.ajax({
      type: "POST",
      url: "/survey/send_survey",
      data: { sendID: sendID, sendeMail: sendeMail },
      dataType: "json",
      beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
          xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
      },
      success: function (data) {
        // alert(data.link)
        loadingDialog.Remove();

        switch (data.status) {
          case "success":
            reportDialog.Success(
              "Survey Feedback",
              "Survey sent successfully.",
              "Great"
            );
            break;

          case "double":
            reportDialog.Failure(
              "Survey Feedback",
              "This recipient has already been served a survey",
              "Ok! Got it"
            );
            break;

          default:
            for (var variable in data) {
              if (variable != "status") {
                errMess = errMess + data[variable];
              }
            }
            reportDialog.Failure(
              "Survey Feedback",
              `Sending mail failed. The following mail was not sent; ${errMess}. This is normally due to bad internet connection.`,
              "Ok! Got it"
            );
            break;
        }
      },
    });
  });

  $("#user_name").on("blur", function () {
    let username = $("#user_name").val();
    if (username != "") {
      $.getJSON(
        "_data_processor.php",
        "flag=getUser&key=" + username,
        function (data) {
          if (data.status == "taken") {
            $("#status").html(
              "<ul><li>Username already exists. Please create a new username!</li></ul>"
            );
            $("#_user_").attr("disabled", true);
          } else {
            $("#status").text("");
            $("#_user_").attr("disabled", false);
          }
        }
      );
    } else {
      $("#status").text("");
      $("#_user_").attr("disabled", false);
    }
  });

  $("#opass").on("blur", function () {
    let user_name = $("#uname").val();
    let password = $("#opass").val();

    if (user_name != "" && password != "") {
      $.post(
        "_data_processor.php",
        "flag=getPassword&key=" + user_name + "&password=" + password,
        function (data, status, xhr) {
          if (xhr.status === 200) {
            if (data.status == "unmatch") {
              $("#oldpass").html(
                "<ul><li>Incorrect old password! Please type the correct old password.</li></ul>"
              );
              $("#_user_").attr("disabled", true);
            } else {
              $("#oldpass").text("");
              $("#_user_").attr("disabled", false);
            }
          } else {
            alert(xhr.statusText);
          }
        },
        "json"
      );
    } else {
      $("#oldpass").text("");
      $("#_user_").attr("disabled", false);
    }
  });

  $("#question").editableSelect({
    filter: true,
    effects: "slide",
  });

  $("#e_question").editableSelect({
    filter: true,
    effects: "slide",
  });

  $("#choice").editableSelect({
    filter: true,
    effects: "slide",
  });

  $("#e_choice").editableSelect({
    filter: true,
    effects: "slide",
  });

  $("#eSelect").editableSelect({
    filter: true,
    effects: "slide",
  });

  $("input,select,textarea")
    .not("[type=submit]")
    .jqBootstrapValidation({
      preventSubmit: true,
      submitError: function ($form, _event, errors) {
        reportDialog.Failure(
          "Input Errors",
          "It appears you have not answered some question(s). Please go over the questions again!",
          "Ok! Got it."
        );
      },
      filter: function () {
        return $(this).is(":visible");
      },
    });

  $.getJSON("/survey/analytics/data", function (response) {
    const data = JSON.parse(response.data);
    $(".chart").each(function (index, element) {
      var ctx = element.getContext("2d");
      // The data serialize by django serialise comes in the format
      // Hence we access it this way
      plotChart(data[index].fields.responses, ctx);
    });
  });

  // reLoad();
});

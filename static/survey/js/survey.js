Chart.defaults.global.defaultFontFamily = '-apple-system,system-ui,BlinkMacSystemFont,"Segoe UI",Roboto,"Helvetica Neue",Arial,sans-serif';
Chart.defaults.global.defaultFontColor = '#292b2c';

function plotChart(data, ctx) {
  let dataLabels = [], dataValues = [];
  for (let i in data) {
    dataLabels.push(i);
    dataValues.push(data[i]);
  }

  let arrLegend = ['Compliant', 'Partially Compliant', 'Not Compliant', 'Not Applicable'];
  
  let chartData = {
    labels: arrLegend.slice(0, dataLabels.length),
    datasets: [{
      label: 'Responses',
      backgroundColor: "rgba(2,117,216,1)",
      borderColor: "rgba(2,117,216,1)",
      barThickness: 7,
      data: dataValues
    }]
  };

  let chartOptions = {
    scales: {
        yAxes: [{ ticks: { fontSize: 14,} }],
        xAxes: [{ ticks: { min: 0, fontSize: 14,}}]
      },
    legend: { display: false }
  };

  window.bar = new Chart(ctx, {
    type: 'horizontalBar',
    data: chartData,
    options: chartOptions
  });
}

Notiflix.Loading.Init({ 
  className: 'notiflix-loading', 
  zindex: 4000, 
  backgroundColor: 'rgba(0,0,0,0.8)', 
  useGoogleFont: true, 
  fontFamily: 'Raleway', 
  cssAnimation: true, 
  cssAnimationDuration: 400, 
  clickToClose: false, 
  messageID: 'NotiflixLoadingMessage', 
  messageFontSize: '15px', 
  messageMaxLength: 34, 
  messageColor: '#dcdcdc', 
}); 

function reLoad() {
  let reFresh = setTimeout(reLoad, 5000);
  $.getJSON("/home", "", function(data) {
    sent = (data.sent <= 1) ? " e-Mail sent!" : " e-Mails sent!";
    $('#eMails').text(data.sent + sent);

    let response = (data.response <= 1) ? " has responded" : " have responded";
    $("#eMailRes").text(data.response + response);
  });
}

$(function(){

  var loadingDialog = Notiflix.Loading;
  var reportDialog = Notiflix.Report;

  // alert(sendMessage);
  $('#logAlert').hide();

  // Scroll to top button appear
  $(document).on("scroll",function() {
    var scrollDistance = $(this).scrollTop();
    if (scrollDistance > 100) {
      $(".scroll-to-top").fadeIn();
    } else {
      $(".scroll-to-top").fadeOut();
    }
  });

  // Smooth scrolling using jQuery easing
  $(document).on("click", "a.scroll-to-top", function(event) {
    var $anchor = $(this);
    $("html, body").stop().animate({
      scrollTop: ($($anchor.attr("href")).offset().top)
    }, 1000, "easeInOutExpo");
    event.preventDefault();
  });

  $(document).on('click', '.deleteData', function () {
    // get the product id
    var valueID = $(this).attr('data-id');

    // bootbox for good looking 'confirm pop up'
    bootbox.confirm({

      message: "<h4>Are you sure you want to delete this data?</h4>",
      centerVertical: true,
      buttons: {
        confirm: {
          label: 'Yes',
          className: 'btn-danger'
        },
        cancel: {
          label: 'No',
          className: 'btn-primary'
        }
      },
      callback: function (result) {
        if (result == true) {
          // send delete request to api / remote server
          $.getJSON(
            "_data_processor.php",
            `flag=delete&key=${valueID}`,
            function (data) {
              let responseData = data.deleting;
              if (responseData == 'user_details') {
                window.location.href = "display_users.php";
              } else {
                window.location.href = responseData + ".php";
              }
            }
          );
        }
      }
    });
  });

  $("#qEditModal").on("show.bs.modal", function (e) {
    let id = $(e.relatedTarget).data("id");

    $.getJSON(
      "/questions/show",
      {questionID : id},
      function (data) {
        $("#e_question_text").val(data.question_text);
        $("#e_recommendation").val(data.recommendation);
        $("#key").val(id);
      }
    );
  });

  $("#aEditModal").on("show.bs.modal", function (e) {
    let id = $(e.relatedTarget).data("id");

    $.getJSON(
      "/answers/show",
      {answerID : id},
      function (data) {
        $("#e_answer").val(data.answer);
        $("#e_question").val(data.question);
        $("#e_choice").val(data.choice);
        if (data.needs_recommendation == 1) {
          $("#e_needs_recommendation").prop("checked", true);
        } else {
          $("#e_needs_recommendation").prop("checked", false);
        }
        $("#id").val(id);
      }
    );
  });

  $("#EditModal").on("show.bs.modal", function (e) {
    let id = $(e.relatedTarget).data("id");

    $.getJSON(
      "/recipients/show",
      {recID : id},
      function (data) {
        $("#e_name").val(data.name);
        $("#e_email").val(data.email);
        $("#e_contact").val(data.contact);
        $("#e_institution").val(data.institution);
        $("#key").val(id);
      }
    );
  });

  $("#surveyResponseForm").on("submit", function (e) {
    e.preventDefault();

    let formData = $("#surveyResponseForm").serialize();

    if (formData.split("&").length == 26) {
      // Start the indicator
      loadingDialog.Circle();

      // Send the survey
      $.ajax({
        method: "POST",
        url: "_process_survey.php",
        data: formData + "&sendResponse=Yes",
        type: "json",
        success: function(responseData) {
          let obj = JSON.parse(responseData);

          loadingDialog.Remove();

          if (obj.status != 200) {
            reportDialog.Failure('Survey Feedback', 
                                 `${obj.message}. Meaning: Your responses could not be sent. It may be due to bad internet connection or wrong email address. Please contact PharmAccess for help`, 
                                 'Ok! Thanks.')
          } else {
            window.location.href = "sent_page.php";
          }          
        }
      });
    }
  });

  $("#sendSurvey").on("click", function (e) {
    // alert($("#key").val());
    let sendID = $("#key").val();
    let sendeMail = $("#recipient_email_address").val();
    let errMess = "";

    $("#EditModal").modal("hide");

    loadingDialog.Circle();

    $.ajax({
      type: "POST",
      url: "_send_survey.php",
      data: "sendID="+ sendID + "&sendeMail="+ sendeMail + "&send_survey=send_survey",
      success: function (data) {
        var myobj = JSON.parse(data);

        loadingDialog.Remove();

        switch (myobj.status) {
          case "success":
            reportDialog.Success('Survey Feedback', 'Survey sent successfully.', 'Great');
            break;

          case "double":
            reportDialog.Failure('Survey Feedback',
              'This recipient has already been served a survey',
              'Ok! Got it'
            );
            break;
        
          default:
            for (var variable in myobj) {
              if (variable != "status") {
                errMess = errMess + myobj[variable];
              }
            }
            reportDialog.Failure('Survey Feedback',
              `Sending mail was unsuccessful. The following mail was not sent; ${errMess}. This is normally due to bad internet connection.`,
              'Ok! Got it'
            );
            break;
        }
      }
    });
  });

  $("#user_name").on("blur", function (){
    let username = $("#user_name").val();
    if (username != "") {
      $.getJSON(
        "_data_processor.php",
        "flag=getUser&key=" + username,
        function (data) {
          if (data.status == "taken") {
            $("#status").html("<ul><li>Username already exists. Please create a new username!</li></ul>");
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

  $("#opass").on("blur", function (){
    let user_name = $("#uname").val();
    let password = $("#opass").val();

    if (user_name != "" && password != "") {
      $.post(
        "_data_processor.php",
        "flag=getPassword&key=" + user_name + "&password=" + password,
        function (data, status, xhr) {
          if (xhr.status === 200) {
            if (data.status == "unmatch") {
              $("#oldpass").html("<ul><li>Incorrect old password! Please type the correct old password.</li></ul>");
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

  $("#loginForm").on("submit", function (e) {
    e.preventDefault();

    $.ajax({
      url: "_login.php",
      method: "POST",
      data: $("#loginForm").serialize(),
      type: "json",
      success: function (responseData) {
        let jObj = JSON.parse(responseData);
        if (jObj.status == "success") {
          window.location.href = 'index.php';
        } else {
          $('#logAlert').show();
          $("#logAlert").html(jObj.message);
        }
      }
    });
  });

  $("#question").editableSelect({
    filter: true,
    effects: "slide"
  });

  $("#e_question").editableSelect({
    filter: true,
    effects: "slide"
  });

  $("#choice").editableSelect({
    filter: true,
    effects: "slide"
  });

  $("#e_choice").editableSelect({
    filter: true,
    effects: "slide"
  });

  $('#dataTable').DataTable({
    'paging': true,
    'searching': true,
    'ordering': true,
    'info': true,
    'autoWidth': true
  });
  
  $('.dataTables_filter input[type="search"]').
    attr('placeholder','Search this table...').
    css({'width':'250px',
         'height':'40px',
         'padding':'6px 12px',
         'display':'inline-block',
         'font-size':'16px'
  });

  $("#eSelect").editableSelect({
    filter: true,
    effects: "slide"
  });

  $("input,select,textarea").not("[type=submit]").jqBootstrapValidation({
    preventSubmit: true,
    submitError: function($form, _event, errors) {
      reportDialog.Failure(
        'Input Errors',
        'It appears you have not answered some question(s). Please go over the questions again!',
        'Ok! Got it.'
      )
    },
    filter: function() {
        return $(this).is(":visible");
    }
  });

  $('.chart').each(function (index, element) {
    var ctx = element.getContext('2d');

    let qID = $(element).attr("id");

    $.getJSON(
      "_data_processor.php",
      "flag=getAnalytics&key=" + qID,
      function (data) {
        plotChart(data, ctx);
      }
    );
  });

  reLoad();
});
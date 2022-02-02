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
});

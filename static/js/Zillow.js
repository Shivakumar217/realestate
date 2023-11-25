// Validate zip code input
function validateInput() {
  var zipCode = $("#zipcode").val().trim();
  if (!zipCode) {
      alert("Please enter a zip code");
      return false;
  }
  return true;
}

// Make AJAX request
function fetchProperties() {
  if (!validateInput()) {
      return;
  }

  var zipCode = $("#zipcode").val().trim();

    $.ajax({
      url: "/property-listing/",
      type: "GET",
      data: {
        zipcode: zipCode,
        csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
      },
      success: function (response) {
          $("#propertyTable tbody").empty();

          // Iterate over properties and append to the table
          response.properties.forEach(function (property) {
              var $row = $("<tr>");
              $row.append($("<td>").text(property.address));
              $row.append($("<td>").text(property.zpid));

              // Add a Save button in a new column
              var $saveButton = $("<button>").text("Save").addClass("btn btn-primary save-button");
              $row.append($("<td>").append($saveButton));

              $("#propertyTable tbody").append($row);

              
          });
      },
      
      
  });
}

// Hook up event listener
$(document).ready(function () {
  $("#fetchProperties").click(fetchProperties);
});

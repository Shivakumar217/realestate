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
                if (property.is_saved) {
                    $saveButton.prop("disabled", true);
                }
                $row.append($("<td>").append($saveButton));
  
                $("#propertyTable tbody").append($row);
  
                // Add event listener for the Save button in the same loop
                $saveButton.on("click", function () {
                    var $saveRow = $(this).closest("tr");
                    var saveAddress = $saveRow.find("td:first-child").text();
                    var saveZpid = $saveRow.find("td:nth-child(2)").text();
  
                    // Perform the save operation by sending data to a Django view
                    $.ajax({
                        url: "/save-property/",  // Replace with your actual URL
                        type: "POST",  // Adjust the request method as needed
                        data: {
                            address: saveAddress,
                            zpid: saveZpid,
                            csrfmiddlewaretoken: $('input[name=csrfmiddlewaretoken]').val()
                            
                        },
                        success: function (saveResponse) {
                            if (saveResponse.status === 'success') {
                                alert("Property saved successfully!");
                                // Optionally, you can update the UI to indicate success
                                $saveRow.find(".save-button").text("Saved").prop("disabled", true);
                            } else if (saveResponse.status === 'error' && saveResponse.message === 'Property already saved.') {
                                alert("Property is already saved.");
                                // Disable the button if the property is already saved
                                $saveRow.find(".save-button").prop("disabled", true);
                            }
                        },
                        error: function (xhr, status, error) {
                            console.log("Error saving property:", error);
                        }
                    });
                });
            });
        },
        error: function (xhr, status, error) {
            console.log("Error fetching properties:", error);
        }
    });
  }
  
  // Hook up event listener
  $(document).ready(function () {
    $("#fetchProperties").click(fetchProperties);
  });
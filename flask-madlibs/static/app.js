// create story
input_keys = [];
input_story = [];
function newElement(inputFieldId) {
  let inputType = document.createElement("div");
  let inputValue = document.getElementById(inputFieldId).value;
  let inputItem = document.createTextNode(inputValue);
  // console.log("Input Value from", inputFieldId, ":", inputValue);
  inputType.appendChild(inputItem);
  if (inputValue === "") {
    alert("You must write something!");
  } else {
    document.getElementById("pharagrapth").appendChild(inputType);
  }
  document.getElementById("myLine").value = "";
  document.getElementById("myKey").value = "";

  // adding into array
  if (inputFieldId == "myKey") {
    input_keys.push(inputValue);
    input_story.push("{" + inputValue + "}");
  } else {
    input_story.push(inputValue);
  }
}

// when submit story button is pressed submit inputs
document
  .getElementById("submit_own_story")
  .addEventListener("click", function () {
    story_title = document.getElementById("story_title").value;
    if (story_title == "") {
      alert("You must have a title!");
    } else if (input_story.length == 0) {
      alert("You must add at least 1 line!");
    } else if (input_keys.length == 0) {
      alert("You must add at least 1 key!");
    } else {
      sendDataToPython(story_title);
      window.location.assign("/");
    }
  });

function sendDataToPython(story_title) {
  // URL of the Python server's endpoint
  const url = "/submit_own_story";

  // Data to be sent
  const data = {
    input_keys: input_keys,
    input_story: input_story,
    story_title: story_title,
  };

  // Use fetch API to send data
  fetch(url, {
    method: "POST", // or 'PUT'
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  })
    .then((response) => response.json())
    .then((data) => {
      console.log("Success:", data);
    })
    .catch((error) => {
      console.error("Error:", error);
    });
}

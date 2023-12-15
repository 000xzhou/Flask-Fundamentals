document
  .getElementById("story_form")
  .addEventListener("submit", function (event) {
    event.preventDefault();
    const form = this;
    let input1Value = form["place"].value;
    let input2Value = form["noun"].value;
    let input3Value = form["verb"].value;
    let input4Value = form["adjective"].value;
    let input5Value = form["plural_noun"].value;
    if (
      input1Value == "" ||
      input2Value == "" ||
      input3Value == "" ||
      input4Value == "" ||
      input5Value == ""
    ) {
      return console.error("Inputs cannot be empty");
    } else if (
      input1Value.length < 3 ||
      input2Value.length < 3 ||
      input3Value.length < 3 ||
      input4Value.length < 3 ||
      input5Value.length < 3
    ) {
      return console.error("Inputs need to be least 3 characters long");
    } else {
      return form.submit();
    }
  });

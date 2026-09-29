async function submitTask() {

    const task =
        document.getElementById("task").value;

    const text =
        document.getElementById("inputText").value;

    const result =
        document.getElementById("result");


    if (text.trim() === "") {

        result.innerText =
            "Please enter something first.";

        return;
    }


    result.innerText =
        "Generating response...";


    let url = "";
    let body = {};


    if (task === "qa") {

        url = "/qa";

        body = {
            text: text
        };

    }


    else if (task === "explain") {

        url = "/explain";

        body = {
            text: text
        };

    }


    else if (task === "quiz") {

        url = "/quiz";

        body = {
            topic: text,
            num_questions: 5
        };

    }


    else if (task === "summarize") {

        url = "/summarize";

        body = {
            text: text
        };

    }


    else if (task === "learn") {

        url = "/learn/recommendations";

        body = {
            text: text
        };

    }


    try {

        const response =
            await fetch(url, {

                method: "POST",

                headers: {
                    "Content-Type":
                        "application/json"
                },

                body: JSON.stringify(body)

            });


        const data =
            await response.json();


        if (data.answer) {

            result.innerText =
                data.answer;

        }

        else if (data.explanation) {

            result.innerText =
                data.explanation;

        }

        else if (data.summary) {

            result.innerText =
                data.summary;

        }

        else if (data.learning_path) {

            result.innerText =
                data.learning_path;

        }

        else if (data.questions) {

            result.innerText =
                JSON.stringify(
                    data.questions,
                    null,
                    2
                );

        }

        else {

            result.innerText =
                JSON.stringify(
                    data,
                    null,
                    2
                );

        }

    }

    catch (error) {

        result.innerText =
            "Error: " + error.message;

    }

}
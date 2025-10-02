// Fetch message from backend API
fetch("/api/message")
    .then(response => response.json())
    .then(data => {
        document.getElementById("msg").innerText = data.message;
    })
    .catch(err => {
        document.getElementById("msg").innerText = "Error loading message!";
    });

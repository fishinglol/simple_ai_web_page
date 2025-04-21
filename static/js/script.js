function submitMessage() {
    var input = document.getElementById('message-input').value;

    // Display user's message immediately (optional)
    var userDisplay = document.getElementById('user-message');
    userDisplay.textContent = input;

    // Call backend to get AI response
    fetch('/get_ai_response', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ message: input })
    })
    .then(response => response.json())
    .then(data => {
        var aiDisplay = document.getElementById('ai-response');
        aiDisplay.textContent = data.ai_response;
    })
    .catch(error => {
        console.error('Error:', error);
    });
}

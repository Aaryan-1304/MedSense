async function sendMessage() {
    const inputBox = document.getElementById('user-input');
    const message = inputBox.value;
    if (!message) return;

    // Display user message
    displayMessage(message, 'user');

    // Send message to backend
    const response = await fetch('/chat', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ content: message }),
    });

    const data = await response.json();

    // Display bot response
    displayMessage(data.response, 'bot');

    // Clear input
    inputBox.value = '';
}

function displayMessage(message, sender) {
    const chatBox = document.getElementById('chat-box');
    const messageDiv = document.createElement('div');
    messageDiv.className = `message ${sender}`;
    messageDiv.textContent = message;
    chatBox.appendChild(messageDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

const socket = io();

// Function to send a message
function sendMessage() {
    const message = document.getElementById('message-input').value;
    if (message) {
        socket.send({ text: message, sender: 'You' });
        document.getElementById('message-input').value = ''; // Clear the input field
    }
}

// Send message on button click
document.getElementById('send-button').onclick = sendMessage;

// Send message on pressing Enter key
document.getElementById('message-input').addEventListener('keydown', function(event) {
    if (event.key === 'Enter') {
        sendMessage();
    }
});
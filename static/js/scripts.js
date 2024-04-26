// document.getElementById('send-btn').onclick = function() {
//     const userInputField = document.getElementById('user-input');
//     const userInput = userInputField.value.trim();
//
//     if (userInput) {
//         // Display the user's message on the chat window
//         displayMessage(userInput, 'You: ');
//
//         // Clear the input field
//         userInputField.value = '';
//
//         // Here you would call your backend service to send the input to OpenAI or any chatbot logic
//         sendMessageToBackend(userInput);
//     }
// };
//
// function displayMessage(message, prefix) {
//     const chatWindow = document.getElementById('output');
//     const newMessageDiv = document.createElement('div');
//     newMessageDiv.textContent = prefix + message;
//     chatWindow.appendChild(newMessageDiv);
//
//     // Scroll to the bottom of the chat window
//     chatWindow.scrollTop = chatWindow.scrollHeight;
// }
//
// async function sendMessageToBackend(message) {
//     // This is where you implement the POST request to your server
//     // For now, a mock response is generated after a short delay
//     setTimeout(() => {
//         const botReply = "This is a mock reply.";
//         displayMessage(botReply, 'Bot: ');
//     }, 1200);
// }

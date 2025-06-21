const conversationDiv = document.getElementById("conversation");
const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;
const recognition = new SpeechRecognition();
recognition.lang = "en-US";
recognition.continuous = true;
recognition.interimResults = false;

let isActive = false;

// GPT memory
let chatMemory = [
  {
    role: "system",
    content: `You are JARVIS, a powerful and polite voice assistant who helps the user with any task like coding, writing, advice, or daily help. You respond intelligently, ask clarifying questions, and keep the conversation flowing.`,
  }
];

// Start recognition
recognition.start();

recognition.onresult = async (event) => {
  const text = event.results[event.resultIndex][0].transcript.trim().toLowerCase();
  console.log("👂 Heard:", text);
  addMessage("👂 Heard", text); // Optional display

  // Wake word
  if (!isActive && /(jarvis|jervis|service|nervous)/i.test(text)) {
    isActive = true;
    speakText("Hello, how can I help you?");
    addMessage("🧍 You", text);
    return;
  }

  // Sleep word
  if (isActive && /(goodnight buddy|go to sleep|stop talking)/i.test(text)) {
    speakText("Goodnight. Going to sleep now.");
    isActive = false;
    return;
  }

  // If active, send to GPT
  if (isActive) {
    addMessage("🧍 You", text);
    const reply = await getGPTReply(text);
    addMessage("🤖 JARVIS", reply);
    speakText(reply);
  }
};

recognition.onerror = (e) => {
  console.error("🎤 Speech error:", e.error);
};

recognition.onend = () => {
  recognition.start(); // Restart for continuous listening
};

// GPT request
async function getGPTReply(text) {
  chatMemory.push({ role: "user", content: text });

  try {
    const response = await fetch("https://openrouter.ai/api/v1/chat/completions", {
      method: "POST",
      headers: {
        "Authorization": "YOUR API KEY", 
        "Content-Type": "application/json",
        "HTTP-Referer": "https://github.com/darksoule26/Jarvis"
      },
      body: JSON.stringify({
        model: "openai/gpt-3.5-turbo", // You can use gpt-4o here too
        messages: chatMemory,
      }),
    });

    const data = await response.json();
    const reply = data.choices?.[0]?.message?.content?.trim() || "Sorry, I couldn't understand.";
    chatMemory.push({ role: "assistant", content: reply });
    return reply;
  } catch (err) {
    console.error("❌ GPT Error:", err);
    return "There was a problem talking to my brain. Please check the internet or API key.";
  }
}

// Add message to page
function addMessage(sender, text) {
  const msg = document.createElement("p");
  msg.innerHTML = `<strong>${sender}:</strong><br>${text.replace(/\n/g, "<br>")}`;
  conversationDiv.appendChild(msg);
  conversationDiv.scrollTop = conversationDiv.scrollHeight;
}

// Text-to-speech
function speakText(text) {
  const utter = new SpeechSynthesisUtterance(text);
  utter.lang = "en-US";
  speechSynthesis.speak(utter);
}


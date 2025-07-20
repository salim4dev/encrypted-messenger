document.getElementById('msgForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const sender = document.getElementById('sender').value;
    const receiver = document.getElementById('receiver').value;
    const message = document.getElementById('message').value;

    const res = await fetch('/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ sender, receiver, message })
    });

    const result = await res.json();
    alert(result.status === "success" ? "Message envoyé !" : "Erreur.");
});
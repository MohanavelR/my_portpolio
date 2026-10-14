const form = document.getElementById('contactForm'); // Updated to match your form ID
const submitBtn = form.querySelector('button[type="submit"]');
const status = document.getElementById("formStatus"); // Added status element

form.addEventListener('submit', async (e) => {
    e.preventDefault();

    // Collect form data into a JSON payload
    const payload = {
        access_key: "d1a9982f-f85f-467d-a1c2-67049150d57f",
        name: form.name.value,
        email: form.email.value,
        subject: form.subject.value,
        message: form.message.value
    };

    const originalText = submitBtn.textContent;
    submitBtn.textContent = "Sending...";
    submitBtn.disabled = true;
    
    if (status) {
        status.textContent = "Sending...";
        status.style.color = "orange";
    }

    try {
        const response = await fetch("https://api.web3forms.com/submit", {
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Accept": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (response.ok) {
            if (status) {
                status.style.color = "green";
                status.textContent = "Success! Your message has been sent.";
            } else {
                alert("Success! Your message has been sent.");
            }
            form.reset();
        } else {
            if (status) {
                status.style.color = "red";
                status.textContent = data.message || "Failed to send message.";
            } else {
                alert("Error: " + data.message);
            }
        }

    } catch (error) {
        if (status) {
            status.style.color = "red";
            status.textContent = "Something went wrong. Please try again.";
        } else {
            alert("Something went wrong. Please try code again.");
        }
        console.error("Contact form error:", error);
    } finally {
        submitBtn.textContent = originalText;
        submitBtn.disabled = false;
    }
});
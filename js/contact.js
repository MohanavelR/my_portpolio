document.getElementById("contactForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const form = this;
    const status = document.getElementById("formStatus");

    const payload = {
        name: form.name.value,
        email: form.email.value,
        message: form.message.value,
        subject:form.subject.value
    };
    console.log(payload)
    status.textContent = "Sending...";

    try {
        const response = await fetch("https://my-portpolio-ruby.vercel.app/api/send-mail", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(payload)
        });

        const data = await response.json();

        if (data.success) {
            status.style.color = "green";
            status.textContent = "Message sent successfully!";
            form.reset();
        } else {
            status.style.color = "red";
            status.textContent = data.message || "Failed to send message.";
        }

    } catch (error) {
        status.style.color = "red";
        status.textContent = "Server error. Please try again later.";
        console.error("Contact form error:", error);
    }
});

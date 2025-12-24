const express = require("express");
const nodemailer = require("nodemailer");
const cors = require("cors");
const dotenv = require("dotenv");
const sendEmail  = require("./api/sendmail");

dotenv.config();
const app = express();

// Allow all origins
app.use(
  cors({
    origin: "*",
  })
);

app.use(express.json());

app.post("/api/send-mail", sendEmail);

app.listen(5000, () => console.log("Server running on port 5000"));

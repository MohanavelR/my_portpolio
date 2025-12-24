const express =require("express");
const nodemailer= require("nodemailer")
const cors =require("cors")
const dotenv=require( "dotenv")

async function sendEmail(req, res) {
  const { name, email, message,subject } = req.body;

  if (!name || !email || !message|| !subject) {
    return res.status(400).json({ success: false, message: "All fields required" });
  }

  try {
    const transporter = nodemailer.createTransport({
      service: "gmail",
      auth: {
        user: process.env.MAIL_USER,
        pass: process.env.MAIL_PASS
      }
    });

    await transporter.sendMail({
      from: `"Portfolio Contact" <${process.env.MAIL_USER}>`,
      to: process.env.MAIL_USER,
      replyTo: email,
      subject: ` ${subject}`,
      html: `
        <h3>New Contact Message</h3>
        <p><strong>Name:</strong> ${name}</p>
        <p><strong>Email:</strong> ${email}</p>
        <p>${message}</p>
      `
    });

    res.json({ success: true, message: "Email sent successfully" });

  } catch (error) {
    console.error(error);
    res.status(500).json({ success: false, message: "Email failed" });
  }
}

module.exports= sendEmail
#!/usr/bin/env python

import os
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, CallbackContext, filters, ContextTypes,Application
import tensorflow as tf
# related to SSL verification (development only)
import requests

# Disable SSL certificate verification
# **Security Warning**
requests.packages.urllib3.disable_warnings()

# Function to handle the /evaluate command
async def evaluate_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Please upload a picture for evaluation.")

# Function to handle the image upload
async def handle_image(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Get the photo file
    photo = update.message.photo[-1].get_file()
    photo_path = f"images/test.jpg"
    #photo_path = f"images/{photo.file_unique_id}.jpg"
    photo.download(photo_path)

    # Load and evaluate the image using the TensorFlow model
    # Replace this with your TensorFlow model code
    evaluation_result, confidence = evaluate_image(photo_path)
    

    # Send the evaluation result and confidence level as a response
    response = f"Evaluation Result: {evaluation_result}\nConfidence: {confidence}"
    await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    # Delete the temporary image file
    os.remove(photo_path)

# Function to evaluate the image using a TensorFlow model
# Replace this with your own TensorFlow model code
def evaluate_image(image_path):
    # Load and preprocess the image
    image = tf.io.read_file(image_path)
    # Add your TensorFlow model code here to evaluate the image and get the results
    # Replace the placeholder code with your actual model evaluation code
    evaluation_result = "Some evaluation result"
    confidence = 0.85

    return evaluation_result, confidence

# Set up the Telegram bot
def main():
    # Telegram bot token
    token = "6276281454:AAGhhy4t-2oIBt1tNENMt7L7SCgCeqIEOfk"

    # Create the updater
    updater = Application.builder().token(token).build()

    # Get the application to register handlers
    #application = updater.application

    # Add handlers for the /evaluate command and image uploads
    updater.add_handler(CommandHandler("evaluate", evaluate_command))
    updater.add_handler(MessageHandler(filters.PHOTO, handle_image))
    #application.add_handler(CommandHandler("evaluate", evaluate_command))
    #application.add_handler(MessageHandler(filters.photo, handle_image))

    # Start the bot
    updater.run_polling()
    #application.run_polling()


if __name__ == '__main__':
    main()

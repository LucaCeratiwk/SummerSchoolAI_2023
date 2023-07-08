#!/usr/bin/env python

import os
import telegram
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import tensorflow as tf

#add
import sys
sys.path.append('../local/')
from config import TOKEN

from test_model import model_evaluate

# Function to handle the /evaluate command
def evaluate_command(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Please upload a picture for evaluation.")

# Function to handle the image upload
def handle_image(update, context):
    # Get the photo file
    photo = update.message.photo[-1].get_file()
    photo_path = f"\{photo.file_id}.jpg"
    photo.download(photo_path)

    # Load and evaluate the image using the TensorFlow model
    # Replace this with your TensorFlow model code
    evaluation_result, confidence = evaluate_image(photo_path)

    # Send the evaluation result and confidence level as a response
    response = f"Evaluation Result: {evaluation_result}\nConfidence: {confidence}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=response)

    # Delete the temporary image file
    os.remove(photo_path)

# Function to evaluate the image using a TensorFlow model
# Replace this with your own TensorFlow model code
def evaluate_image(image_path):
    # Load and preprocess the image
    #image = tf.io.read_file(image_path)
    # Add your TensorFlow model code here to evaluate the image and get the results
    # Replace the placeholder code with your actual model evaluation code
    evaluation_result, confidence = model_evaluate(image_path)

    return evaluation_result, confidence

# Set up the Telegram bot
def main():

    # Create the updater and dispatcher
    updater = Updater(TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Add handlers for the /evaluate command and image uploads
    dispatcher.add_handler(CommandHandler("evaluate", evaluate_command))
    dispatcher.add_handler(MessageHandler(Filters.photo, handle_image))

    # Start the bot
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
# cook-book

📘 Recipe Book (Python)
Description

This project is a simple Python recipe book application that reads recipes from a text file and stores them in a structured format. Each recipe is loaded from a file and converted into a dictionary containing the recipe title, ingredients, and cooking instructions. The project demonstrates basic file handling, string processing, and error handling in Python.

Features

Load recipes from a text file

Store recipes as dictionaries inside a list

Handle missing files safely using try/except

Parse and organize text data into structured form

Beginner-friendly and easy to extend

File Structure

recipies.txt — text file containing saved recipes

main.py (or similar) — Python script that loads and processes recipes

How It Works

Recipes in the text file are separated using a special marker:
---RECIPE_END---

Each recipe contains:

Title

Ingredients

Instructions

How to Run

Make sure you have Python 3 installed.

Place the recipies.txt file in the same directory as the Python script.

Run the program using the command:

python main.py


The program will load all recipes from the file and store them in memory.

Example Recipe Format
Ha3Ba: Pancakes

IHrpegieHTn:
Flour, Eggs, Milk, Sugar

IHcTpykuia:
Mix ingredients and cook on a pan.
---RECIPE_END---

Learning Goals

This project helps practice:

File reading in Python

Working with lists and dictionaries

String manipulation

Error handling

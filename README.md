# AutoIDBook

## About
This is a set of Python scripts that utilize Latex to generate species identification books (PDF files) based on tables that hold image file names and information about each species, such as their names and ecological information.

This has been used to create a PDF version of the [Reef Fish Trainer](https://uni-tuebingen.de/de/251585) developed by Nico Michiels at the University of Tübingen.

## Requirements to use the scripts
- Latex and `xelatex`
- Python3
- appropriately formatted table
- images that **exactly** match the file names in the table

## Running the scripts
There is one pyhton script (`automatic_layout.py`) that holds all major functions needed to write Latex code into text files. The other file (`create_red_sea_book.py`) is used to call these functions and this is where the file names have to be specifies.

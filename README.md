# AutoIDBook

## About
This is a set of Python scripts that utilize Latex to generate species identification books (PDF files) based on tables that hold image file names and information about each species, such as their names and ecological information.

This has been developed to create a PDF version of the [Reef Fish Trainer](https://uni-tuebingen.de/de/251585) developed by Nico Michiels at the University of Tübingen, which is available as an [ANKI](https://apps.ankiweb.net/) deck.

The code is made freely available here, despite in part being very specific to the table and the files (not hosted here), because we think this could inspire others to adjust the code to their needs or to simply inspect it when preparing for a similar project.
 

## Basic principle
A Latex interpreter (`xelatex`) is used to transform a plain text Latex file into a PDF document. The Latex document is created by populating a 'backbone' version with additional content via a Python script. The 'backbone' version contains marks that define where the additonal content gets inserted. The additional content comprises headings (incl. the spacing around them) and tables with three columns that will appear as rows in a grid-like layout. The tables consist of a row that houses the images (in our case all images have the same dimensions), a row that (wheb a condition is met) refers to a photographer, and three rows that contain the names and ecological information of/about the depicted species. Page breaks are inserted manually, in order to prevent headings to not appear at the bottom of the page (Latex could do that automatically but this interferes with the regularity of the grid layout (tables are floating objects in Latex). Invisible sections are used to separate the headings into two parts (the Latin name of the systematic group and their vernacular names).


## Prerequesites
The code assumes a UNIX like operating system (Linux, MacOS, etc.), but can be easily adjusted to work on Windows.
- A text editor or IDE (Integrated Development Environment) with Python and Latex syntax highlighting (e.g. [Visual Studio Code](https://code.visualstudio.com/) or [RStudio](https://posit.co/download/rstudio-desktop/)) should be installed 
- Python3 needs to be installed, either system-wide or in a virtual environment (e.g. 'pyenv' or 'conda'). To install Python, use the package manager of your operating system or install a third party one (e.g. install [homebrew](https://brew.sh/) on MacOS)
- The pandas Python package needs to be installed
- A Latex distribution needs to be installed. On Ubuntu or Debian install `texlive-latex-extra`(comprises much more than needed here). On MacOS install [MacTex](https://www.tug.org/mactex/)
- The tabular data should be appropriately formatted (entries as rows, first row are the column names) and saved in text format (`.csv` or `.txt`) with commas as separators
- The images need to have file names that **exactly** match the ones in the table


## Running the scripts
There is one Python script (`automatic_layout.py`) that holds all major functions needed to write Latex code into text files. The other file (`create_red_sea_book.py`) is used to call these functions, and this is where the file names have to be specified. In order to generate a new PDF, adjust the file names in the file-specific script and execute the script, either from within an IDE or from the terminal or from the file manager. Make sure that your previously generated versions have a file name that is not used by the script, otherwise the execution of the script will overwrite your previous version!


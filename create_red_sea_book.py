'''
This script is used to compile the fish identification book for the Red Sea.
It uses functions from another script that control the general page layout.
This script is limited to the more specific tasks such as referring to 
Latex file names, column names etc. For this to work, this script needs to be
in the same directory as the script that holds the herein imported functions.
'''

from importlib import reload
import automatic_layout
reload(automatic_layout) 
# reload(automatic_layout) forces to reload the actual functions,
# opening a new Python REPL, as necessary with just the import command

### Writing the title page and specifying all Latex environment variables,
# to-be-used packages and custom commands to the final Latex file
automatic_layout.write_pre_automation_part("red_sea_book_backbone.tex", "red_sea_book_automated.tex", r"%%% automated entries start %%%")

### Loading data from the table csv file
df = automatic_layout.load_table("RedSea 2023-07-24 Anki Deck 17 - Production.csv", "Sorting FOR BOOKLET")

### Inserting additonal column to table, determining the position of the section headings
df = automatic_layout.first_in_section_column(df)

### Safety switch, used for testing
# df = df.iloc[0:200,].reset_index(drop=True)

### Append all entries to the Latex file
automatic_layout.make_all_entries("red_sea_book_automated.tex", df)

### Writing what comes after the automated entries to the final Latex file.
automatic_layout.write_post_automation_part("red_sea_book_backbone.tex", "red_sea_book_automated.tex", r"%%% automated entries end %%%")


### Compiling the PDF
# xelatex is used because it can use system fonts.
# automatic_layout.compile_pdf("red_sea_book_automated.tex")
automatic_layout.compile_pdf_xelatex("red_sea_book_automated.tex")






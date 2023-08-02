'''
This script is used to compile the fish identification book for the Red Sea.
It uses functions from another script that control the general page layout.
This script is limited to the more specific tasks such as referring to Latex file names, column names etc.
For this to work, this script needs to be in the same directory as the script that holds the herein imported functions.
'''
from importlib import reload
import automatic_layout
reload(automatic_layout)

automatic_layout.write_pre_automation_part("red_sea_book_backbone.tex", "red_sea_book_automated.tex", r"%%% automated entries start %%%")


df = automatic_layout.load_table("RedSea 2023-07-24 Anki Deck 17 - Production.csv", "Sorting FOR BOOKLET")
df = automatic_layout.first_in_section_column(df)

# Safety switch
# df = df.iloc[0:200,].reset_index(drop=True)

# automatic_layout.three_entries("red_sea_book_automated.tex", 0, df)
# automatic_layout.section_heading("red_sea_book_automated.tex", 0, df)
# automatic_layout.one_entry("red_sea_book_automated.tex", 6, df)
# automatic_layout.two_entries("red_sea_book_automated.tex", 45, df)
# automatic_layout.three_entries("red_sea_book_automated.tex", 12, df)

automatic_layout.make_all_entries("red_sea_book_automated.tex", df)

automatic_layout.write_post_automation_part("red_sea_book_backbone.tex", "red_sea_book_automated.tex", r"%%% automated entries end %%%")

# automatic_layout.compile_pdf("red_sea_book_automated.tex")

automatic_layout.compile_pdf_xelatex("red_sea_book_automated.tex")






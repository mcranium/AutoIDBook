'''
This script holds the relevant functions to create the *page layout* for the fish identification book for the Red Sea as well as for other future books.
The functions from this script are to be executed in another script, for which they need to be imported.
For this to work, both (or all) scripts need to stay in the same directory.
'''

import pandas as pd
import os


def load_table(filepath, sortcolumn):
    '''
    Loeads and sorts the data from the table.
    '''
    df = pd.read_table(filepath, sep=",", index_col=0)
    df = df.sort_values(by=sortcolumn).reset_index()
    return df


def filewriter(filename, list_of_lines):
    """
    Appends a list of strings as lines to a textfile.
    """
    with open(filename, "a") as textfile:
        for i in range(len(list_of_lines)):
            textfile.write(list_of_lines[i])


def linewriter(filename, string):
    """
    Appends a string as a new row to a textfile.
    """
    with open(filename, "a") as textfile:
        textfile.write(string + "\n")

# linewriter("red_sea_book_automated.tex", r"% something at the very last line")


def markfinder(filename, mark):
    """
    Returns the position of the line in a text file that contains a defined string (mark).
    """
    textfile = open(filename)
    list_of_lines = textfile.readlines()
        
    occurrences = list()
    for i in range(len(list_of_lines)):
        occurrences.append(mark in list_of_lines[i])
    return [i for i in range(len(occurrences)) if occurrences[i] == True]



def write_pre_automation_part(backbone_file_name, output_file_name, automation_start_mark):
    '''
    Takes the first set of lines from a text file up to a specied marker (will not be included) and writes them into another text file.
    '''
    backbone = open(backbone_file_name)
    backbone = backbone.readlines()
    pre_automation_end = markfinder(backbone_file_name, automation_start_mark)
    pre_automation_part = backbone[0:pre_automation_end[0]]

    try:
        os.remove(output_file_name)
    except:
        pass

    filewriter(output_file_name, pre_automation_part)



def write_post_automation_part(backbone_file_name, output_file_name, automation_end_mark):
    '''
    Takes the last set of lines from a text file, from a specied marker (will not be included) to to the end and writes them into another text file.
    '''
    backbone = open(backbone_file_name)
    backbone = backbone.readlines()
    post_automation_start = markfinder(backbone_file_name, automation_end_mark)
    post_automation_part = backbone[post_automation_start[0]+1:]

    filewriter(output_file_name, post_automation_part)




def compile_pdf(texfile_name):
    '''
    Takes a textfile (assumes Latex formatting) and uses pdflatex to compile a PDF with the same filename base.
    Compiles twice to achieve a correct table of contents.
    '''
    os.system(f"pdflatex {texfile_name}")
    os.system(f"pdflatex {texfile_name}")
    os.system(f"pdflatex {texfile_name}")

def compile_pdf_xelatex(texfile_name):
    '''
    Takes a textfile (assumes Latex formatting) and uses pdflatex to compile a PDF with the same filename base.
    Compiles twice to achieve a correct table of contents.
    '''
    os.system(f"xelatex {texfile_name}")
    os.system(f"xelatex {texfile_name}")




def read_textfile(filename):
    '''
    Reads a textfile and returns a list of strings where each item is a line of the textfile.
    '''
    textfile = open(filename)
    text = textfile.readlines()
    return text



def replacer(listoflines, dictionary):
    '''
    Takes a list of strings (extracted from a text file) and replaces parts of the strings with the aid of a dictionary.
    '''
    # loop through the lines
    for i in range(len(listoflines)):
        # loop through the dictionary
        for key, value in dictionary.items():
            textfile[i] = textfile[i].replace(key, value)

    return listoflines


def photographer_credit(i, df):
    photographer = df["Photographer in full"][i]
    credit = r"\tiny{\phantom{Ig}} \hfill \textcopyright \ " + photographer[4:]
    nocredit = r"\tiny{\phantom{Ig}}"
    if df["Photographer"][i] != "NMic":
        return(credit)
    else:
        return(nocredit)


def actual_length(i, df):
    length_info = df["Length (cm) for adults only"][i]
    try:
        length_string = length_info[2:][:2] + r" cm, "
    except:
        length_string = r""
    return length_string


def behaviour(i, df):
    behav_info = df["Behaviour translated"][i]
    if isinstance(behav_info, str) == True:
        behav_str = behav_info
    else:
        behav_str = r""
    return behav_str


def abundance(i, df):
    if df["% Category"][i] in ["Abundance-A-(>95%)", "Abundance-B-(90-95%)"]:
        icon = r"\abundanceAB"
    elif df["% Category"][i] == "Abundance-C-(75-89%)":
        icon = r"\abundanceC"
    elif df["% Category"][i] == "Abundance-D-(50-74%)":
        icon = r"\abundanceD"
    elif df["% Category"][i] == "Abundance-E-(25-49%)":
        icon = r"\abundanceE"  
    else:
        icon = r"\abundanceFH"
    return icon

def identification_cf(i, df):
    if df["ok/cf"][i] == 'cf':
        ident_str = " (?)"
    else:
        ident_str = ""
    return ident_str




def three_entries(target, i, df):
    # " + df[""][i] + r"
    content = [
        # r"\vspace{-0.5cm}",
        r"\begin{center}",
        r"\def\arraystretch{0.2} % vertical padding inside the table",
        r"\setlength{\tabcolsep}{0.5mm} % horizontal padding inside the table",
        r"\begin{tabular}{p{0.33\textwidth} p{0.33\textwidth} p{0.33\textwidth}}",
        r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i] + r"}",
        r"&",
        r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i+1] + r"}",
        r"&",
        r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i+2] + r"}",
        r"\\",
        photographer_credit(i, df),
        r"&",
        photographer_credit(i+1, df),
        r"&",
        photographer_credit(i+2, df),
        r"\\[-0.5ex]",
        r"\normalsize{\textbf{\textit{" + df["Genus Species"][i] + r"}" + identification_cf(i, df) + r"}\phantom{Ig}}",
        r"&",
        r"\normalsize{\textbf{\textit{" + df["Genus Species"][i+1] + r"}" + identification_cf(i+1, df) + r"}\phantom{Ig}}",
        r"&",
        r"\normalsize{\textbf{\textit{" + df["Genus Species"][i+2] + r"}" + identification_cf(i+2, df) + r"}\phantom{Ig}}",
        r"\\",
        r"\small{" + df["Species English"][i] + r"\phantom{Ig}}",
        r"&",
        r"\small{" + df["Species English"][i+1] + r"\phantom{Ig}}",
        r"&",
        r"\small{" + df["Species English"][i+2] + r"\phantom{Ig}}",
        r"\\",
        r"\footnotesize{" + df["Stage translated"][i] + r", " + actual_length(i, df) + df["Colour form translated"][i][2:] + behaviour(i, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i, df) + r"}}",
        r"&",
        r"\footnotesize{" + df["Stage translated"][i+1] + r", " + actual_length(i+1, df) + df["Colour form translated"][i+1][2:] + behaviour(i+1, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i+1, df) + r"}}",
        r"&",
        r"\footnotesize{" + df["Stage translated"][i+2] + r", " + actual_length(i+2, df) + df["Colour form translated"][i+2][2:] + behaviour(i+2, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i+2, df) + r"}}",
        r"\\",
        r"\end{tabular}",
        r"\end{center}"
    ]
    for j in range(len(content)):
        linewriter(target, content[j])


def two_entries(target, i, df):
    # " + df[""][i] + r"
    content = [
        # r"\vspace{-0.5cm}",
        r"\begin{center}",
        r"\def\arraystretch{0.2} % vertical padding inside the table",
        r"\setlength{\tabcolsep}{0.5mm} % horizontal padding inside the table",
        r"\begin{tabular}{p{0.33\textwidth} p{0.33\textwidth} p{0.33\textwidth}}",
        r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i] + r"}",
        r"&",
        r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i+1] + r"}",
        r"&",
        # r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i+2] + r"}",
        r"\\",
        photographer_credit(i, df),
        r"&",
        photographer_credit(i+1, df),
        r"&",
        # photographer_credit(i+2, df),
        r"\\[-0.5ex]",
        r"\normalsize{\textbf{\textit{" + df["Genus Species"][i] + r"}" + identification_cf(i, df) + r"}\phantom{Ig}}",
        r"&",
        r"\normalsize{\textbf{\textit{" + df["Genus Species"][i+1] + r"}" + identification_cf(i+1, df) + r"}\phantom{Ig}}",
        r"&",
        # r"\normalsize{\textbf{\textit{" + df["Genus Species"][i+2] + r"}" + identification_cf(i+2, df) + r"}\phantom{Ig}}",
        r"\\",
        r"\small{" + df["Species English"][i] + r"\phantom{Ig}}",
        r"&",
        r"\small{" + df["Species English"][i+1] + r"\phantom{Ig}}",
        r"&",
        # r"\small{" + df["Species English"][i+2] + r"\phantom{Ig}}",
        r"\\",
        r"\footnotesize{" + df["Stage translated"][i] + r", " + actual_length(i, df) + df["Colour form translated"][i][2:] + behaviour(i, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i, df) + r"}}",
        r"&",
        r"\footnotesize{" + df["Stage translated"][i+1] + r", " + actual_length(i+1, df) + df["Colour form translated"][i+1][2:] + behaviour(i+1, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i+1, df) + r"}}",
        r"&",
        # r"\footnotesize{" + df["Stage translated"][i+2] + r", " + actual_length(i+2, df) + df["Colour form translated"][i+2][2:] + behaviour(i+2, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i+2, df) + r"}}",
        r"\\",
        r"\end{tabular}",
        r"\end{center}"
    ]
    for j in range(len(content)):
        linewriter(target, content[j])


def one_entry(target, i, df):
    # " + df[""][i] + r"
    content = [
        # r"\vspace{-0.5cm}",
        r"\begin{center}",
        r"\def\arraystretch{0.2} % vertical padding inside the table",
        r"\setlength{\tabcolsep}{0.5mm} % horizontal padding inside the table",
        r"\begin{tabular}{p{0.33\textwidth} p{0.33\textwidth} p{0.33\textwidth}}",
        r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i] + r"}",
        r"&",
        # r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i+1] + r"}",
        r"&",
        # r"\includegraphics[width=0.33\textwidth, keepaspectratio]{" + df["Picture-name"][i+2] + r"}",
        r"\\",
        photographer_credit(i, df),
        r"&",
        # photographer_credit(i+1, df),
        r"&",
        # photographer_credit(i+2, df),
        r"\\[-0.5ex]",
        r"\normalsize{\textbf{\textit{" + df["Genus Species"][i] + r"}" + identification_cf(i, df) + r"}\phantom{Ig}}",
        r"&",
        # r"\normalsize{\textbf{\textit{" + df["Genus Species"][i+1] + r"}" + identification_cf(i+1, df) + r"}\phantom{Ig}}",
        r"&",
        # r"\normalsize{\textbf{\textit{" + df["Genus Species"][i+2] + r"}" + identification_cf(i+2, df) + r"}\phantom{Ig}}",
        r"\\",
        r"\small{" + df["Species English"][i] + r"\phantom{Ig}}",
        r"&",
        # r"\small{" + df["Species English"][i+1] + r"\phantom{Ig}}",
        r"&",
        # r"\small{" + df["Species English"][i+2] + r"\phantom{Ig}}",
        r"\\",
        r"\footnotesize{" + df["Stage translated"][i] + r", " + actual_length(i, df) + df["Colour form translated"][i][2:] + behaviour(i, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i, df) + r"}}",
        r"&",
        # r"\footnotesize{" + df["Stage translated"][i+1] + r", " + actual_length(i+1, df) + df["Colour form translated"][i+1][2:] + behaviour(i+1, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i+1, df) + r"}}",
        r"&",
        # r"\footnotesize{" + df["Stage translated"][i+2] + r", " + actual_length(i+2, df) + df["Colour form translated"][i+2][2:] + behaviour(i+2, df) + r"\phantom{Ig} \hfill \scriptsize{" + abundance(i+2, df) + r"}}",
        r"\\",
        r"\end{tabular}",
        r"\end{center}"
    ]
    for j in range(len(content)):
        linewriter(target, content[j])

def section_heading(target, i, df):
    content = [
        r"\invisiblesection{" + df["Booklet Section Header"][i] + r"}",
        r"\vspace*{3.25cm}", ### This is one of the most important adjustment sites!
        r"\LARGE{\textbf{" + df["Booklet Section Header"][i].split("-")[0][:-1] + r"}}",
        r"\vspace*{0.3cm} \\",
        r"\large{\textbf{" + df["Booklet Section Header"][i].split("-")[1][1:] + r"}}",
        r"\vspace*{0.5cm}"
    ]
    for j in range(len(content)):
        linewriter(target, content[j])
    


def first_in_section_column(df):
    df["first_in_section"] = 0
    for i in range(0,df.shape[0]):
        section_name = df["Booklet Section Header"][i]
        if i == df[df["Booklet Section Header"] == section_name].index[0]:
            df.loc[i,"first_in_section"] = 1
        else:
            pass
    return df





def make_all_entries(target, df):

    i = 0
    pagerow = 0

    while i <= df.shape[0]-1: # was only < not <=
        print("currently at i == " + str(i))
        ## Page breaks
        if pagerow > 4:
            linewriter(target, r"\newpage")
            pagerow = 0
        else:
            pass

        ### Headings
        if df["first_in_section"][i] == 1:
            ### Check if it is not the last row on the page
            if pagerow < 4:
                ### The heading would *not* land on the last page row 
                section_heading(target, i, df)
                pagerow += 1
                
            else:
                ### The heading *would* land on the last page row 
                # but this will be prevented by a page break
                linewriter(target, r"\newpage")
                pagerow = 0
                section_heading(target, i, df)
                pagerow += 1
        else:
            ### No heading needed
            pass

        ### Entries
        ### One, two or three entries per row on page


        ### One entry per page row
        try:
            ### Try statement to avoid index errors when at the last rows
            if df["first_in_section"][i+1] == 1:
                one_entry(target, i, df)
                pagerow += 1
                i += 1
                print("put 1 item")
                continue
            else:
                pass
        except:
            print("could not put 1 item")
            pass

        if i == df.shape[0]-1:
            one_entry(target, i, df)
            pagerow += 1
            print("ended after putting 2 items")
            break
        else:
            pass


        ### Two entries per page row

        try:
            if df["first_in_section"][i+2] == 1:
                two_entries(target, i, df)
                pagerow += 1
                i += 2
                print("put 2 items")
                continue
            
            else:
                pass
        except:
            print("could not put 2 items")
            pass

        if i+1 == df.shape[0]-1:
            two_entries(target, i, df)
            pagerow += 1
            print("ended after putting 2 items")
            break
        

        ### Three entries per page row
        else:
            try:
                three_entries(target, i, df)
                pagerow += 1
                i += 3 # could end the while loop
                print("put 3 items")
            except:
                print("could not put 3 items")
        
        















# def looping(df, target):
#     for i in range(len(df)):
#         # print(df.loc[i, "Alphabetical systematic/phenotypic Sorting"], df.loc[i, "Genus"])
#         # linewriter(filename, string)(df.loc[i, "Alphabetical systematic/phenotypic Sorting"] + df.loc[i, "Genus"])
#         linewriter(target, "% many more lines")

# # looping(df, "red_sea_book_automated.tex")






# if __name__ == "__main__":
#     # For testing purposes
#     df = load_table("RedSea 2023-07-12 Anki Deck 13 with template updated.txt", "Alphabetical systematic/phenotypic Sorting")
#     markfinder("red_sea_book_backbone.tex", r"%%% automated entries start %%%")
#     markfinder("red_sea_book_backbone.tex", r"%%% automated entries end %%%")
#     write_pre_automation_part("red_sea_book_backbone.tex", "red_sea_book_automated.tex", r"%%% automated entries start %%%")
#     write_post_automation_part("red_sea_book_backbone.tex", "red_sea_book_automated.tex", r"%%% automated entries end %%%")
#     # compile_pdf("red_sea_book_automated.tex")
    

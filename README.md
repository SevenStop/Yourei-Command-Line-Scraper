Command line program to scrape data from Yourei.jp.


Format: python Main.py [function] [expression] [number of pages to index]

Examples: 

python Main.py disp x 0 (the x and 0 are placeholders)

python Main.py collect 四面楚歌 2

python Main.py output 四面楚歌 2


functions:
disp (zero arguments but they must be filled) - display full passages with the setences

collect (2 arguments, the expression and number of pages to index) - collects data into a data structure and displays the indicated pages of data

output (2 arguments, the expression and number of pages to index) - collects data into a data structure, displays the indicated pages of data, and outputs it to a txt file

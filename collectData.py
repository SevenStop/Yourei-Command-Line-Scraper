
import requests
import math
import re
from bs4 import BeautifulSoup
#import BeautifulSoup
from urllib.parse import quote
#import quote

def data(term, num):
    #num is the number of pages after the first page to index. -1 means do all pages
    #dictionary for words. Index indicates order in search engine
    allSent = {}
    #key for the count of the sentence on the list. Starts at 1
    key = 1

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.79 Safari/537.36'
    }

    #url of yourei
    youreiURL = 'https://yourei.jp/'

    #preparing term
    prepterm = quote(term)
    query = youreiURL + prepterm
    print("Searching: ", query)
    print()
    response = requests.get(query, headers=headers)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the HTML content using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all sentences on the page

        number = soup.select_one('#sentence-frequency-line')
        numbertext = number.get_text(strip=True)
        print(numbertext)
        #clean up the string to use for calculations
        clean = numbertext.replace(",","")
        numbers = re.findall(r'\d+', clean)
        final = [int(number) for number in numbers]
        total = final[0]

        #print the first page
        sentences = soup.select('.sentence')

        blank = 0
        if sentences:
            # Print each sentence
            for sentence in sentences:
                txt = sentence.get_text()
                current = "".join(re.findall(r'([^。！？?!]*{}[^。！？?!]*(?:[。！？?!]))'.format(term), txt))
                current = current.strip()
                if current == "":
                    blank += 1
                else:
                    print(current)
                    print("--------------------")
                    allSent[key] = current
                    key+=1
        else:
            print("No sentences found for the given term.")

        indexed = key - blank
        output = str(indexed) + " SENTENCES INDEXED (" + str(blank) + " blank)"
        print(output)

        #now calculate number of pages of info
        pages = math.ceil(total / 30)
        print(pages, "pages of sentences")
        #run loop until all pages are iterated through
        if num != 0:
            if num == -1:
                print("Indexing all pages")
            elif num > 0:
                pages = num
            currentPage = 2
            startval = 1
            ogquery = query + "?start="
            blank = 0
            while currentPage <= pages:
               #update start value
                startval += 30
                query = ogquery + str(startval)
                #scrape new webpage
                response = requests.get(query, headers=headers)
                print("Searching: ", query)
                soup = BeautifulSoup(response.text, 'html.parser')

                sentences = soup.select('.sentence')


                if sentences:
                    # Index each sentence
                    for sentence in sentences:
                        txt = sentence.get_text()
                        current = "".join(re.findall(r'([^。！？?!]*{}[^。！？?!]*(?:[。！？?!]))'.format(term), txt))
                        current = current.strip()
                        if current == "":
                            blank += 1
                        else:
                            print(current)
                            print("--------------------")
                            allSent[key] = current
                            key += 1
                else:
                    print("No sentences found for the given term.")

                print("Page", currentPage, "completed.")
                currentPage +=1

                indexed = key - blank
                output = str(indexed) + " SENTENCES INDEXED (" + str(blank) + " blank)"
                print(output)

    else:
        print("Failed to retrieve webpage. Status code:", response.status_code)

    return allSent
#Final Project! 

# Part 1: Using Webscraping to scrape the text with <p> tags and then creating a file and writing the text from the webscrap into that file.
from bs4 import BeautifulSoup
import requests
import os
import re 
import pandas as pd
import matplotlib.pyplot as plt


wiki_url = "https://en.wikipedia.org/wiki/Taylor_Swift"
wiki_page = requests.get(wiki_url)

wiki_soup = BeautifulSoup(wiki_page.content, "html.parser")

wiki_content = wiki_soup.find_all("p") #incoperating the <p> tag
all_text = '\n'.join([para.get_text() for para in wiki_content])

print(all_text)

full_file_path = os.path.join(os.getcwd(), all_text)
with open ('new_file.txt', "w") as file:
    file.write(all_text) #creates a seperate .txt file after fetching all the text with <p> attributes


# Part 2: Using Regular Expressions to find consistent patterns within the text and counting the 
    # amount of times that pattern appears in the wikipedia and creating a dictionary. 

with open("new_file.txt") as file_connection:
    wiki_text= file_connection.read()

taylor_pattern = re.compile(r"Taylor") #Using regular_expression to find 'Taylor', not sure if I used it correctly. 
type(taylor_pattern)    
taylor_pattern_results = len(re.findall(taylor_pattern, wiki_text))
print(f"number of matches of 'Taylor': {taylor_pattern_results}")



taylor_sequence = [wiki_text[i:9] for i in range(3,8)] #Using regular expression to find the sequences of 'Taylor'
print(taylor_sequence)
type(taylor_sequence)

#using the sequences of 'Taylor' to find the amount of times each sequence appears in the text
with open("new_file.txt") as file_connection:
    new_file_text = file_connection.read()
    substring_counts = {}
    for seq in taylor_sequence:
        count = new_file_text.count(seq)
        substring_counts[seq] = count
    for seq, count in substring_counts.items():
        print(f"Substrings '{seq}' appears {count} times in new_file.txt")
type (substring_counts)

#using that data and make a dictionary

substring_counts = {
    'aylor': 15,
    'ylor': 15,
    'lor': 15,
    'or': 168,  
    'r' :734,
}
type(substring_counts)
#I bring Pandas into this by converting the substring_counts to a DataFrame then coverting it to a CSV file, 
# fufills requirement 8_1 and 8_2, and I think 8_4 is already completed since I technically created this data from
# the wikipage
taylor_data = pd.DataFrame(list(substring_counts.items()), columns=['Sequence', 'Count'])
print (taylor_data)

csv_file_path = 'taylor_sequence_data.csv'
taylor_data.to_csv(csv_file_path, index=False)  

data_frame = pd.read_csv(csv_file_path)

print(data_frame)

#Fufilling 8_3 requirement, using pandas to get a subset of a data frame using a boolean

subset_data = data_frame[data_frame['Count']>100]
print(subset_data)

#I'm finally using matplotlib to make charts for my data. I did recieve inspiration from
#"https://matplotlib.org/ - Plotting categorical variables" to write out the code. I adapted my code to matplotlibs
# code. Maybe a commit here?
names = list(substring_counts.keys())
values = list(substring_counts.values())

fig, axs = plt.subplots(1, 3, figsize=(12, 6), sharey=True)
axs[0].bar(names, values, color='red')
axs[0].set_title('Bar Plot')

axs[1].scatter(names, values, color='green')
axs[1].set_title('Scatter Plot')

axs[2].plot(names, values, color='purple')
axs[2].set_title('Line Plot')

plt.tight_layout()
plt.show()

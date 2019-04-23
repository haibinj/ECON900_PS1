# ECON900_PS1
this file use python to collect the information about board games from the "boardgamegeek.com".

1. scraping
The file named "game_request.py" is used to request html files from the website.
To run the code, you need selenium and web driver. In this code, chromedrive is used. You need to change the address to the file you save your web driver in the "brower".
You also need to set the directory to save the html files in the "completName" part.
To give some time for the javascript to be completely loaded, I set time waiting to 6 second. Longer waiting time can avoid incompleted files. 

2. parsing
The file named "game_parse.py" is used to parse the html files.
BeautifulSoup is used to parse the file.
Users need to change set the directory to save the parsed data. 
The parsed data is saved in csv file.

3. board game data
The file named "boardgame_data.csv" is the data parsed from the parsing file.
I cleaned the data by delete the va

4. Analysing the board game
The file named "machine.py" is used to analyze the board game data.


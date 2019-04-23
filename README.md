# ECON900_PS1
This file uses python to collect the information about board games from the "boardgamegeek.com" .

1. scraping
The file named "game_request.py" is used to request HTML files from the website.
To run the code, you need selenium and web driver. In this code, "chrome driver" is used. The "chrome driver" can be found in the folder named "driver". You need to change the address to the file you save your web driver in the code followed by "brower".
You also need to set the directory to save the HTML files in the "completName" part.
To give some time for the javascript to be loaded entirely, I set time waiting to 6 seconds. Longer waiting time can avoid incomplete files. 

2. parsing
The file named "game_parse.py" is used to parse the HTML files.
BeautifulSoup is used to parse the file.
Users need to change set the directory to save the parsed data. 
The parsed data is saved in "csv" file.

3. board game data
Some of the variable in the "csv" data contains some format that can not be run directly. I change the format in data process software.  I use Numbers on Mac machine.
I cleaned the data by deleting the variables that are not used in the machine learning part.
The file named "boardgame_data.csv" is the data parsed from the parsing file.


4. Analyzing the board game
The file named "machine.py" is used to analyze the board game data.
It looks at the relationship between the price of the game and the users rating of the game. 
It uses the "GaussianMixture" to separate the games into three clusters. The graph "Gaussian_cluster" shows the result.
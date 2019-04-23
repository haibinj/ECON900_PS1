# ECON900_PS1
This file uses python to collect the information about board games from the "boardgamegeek.com" .

System requirement: python3, BeautifulSoup, Pandas, selenium, Webdriver, sklearn. 

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
I ran the code on April 14, 2019. There was 1064 pages at that time. 

3. board game data
Some of the variable in the "csv" data contains some format that can not be run directly. I change the format in data process software. 
I cleaned the data by deleting the variables that are not used in the machine learning part.
The file named "boardgame_data.csv" is the data parsed from the parsing file.
Since most of the games that do not have ranking number do not have list price neither, so I chop the data from the point that do not have a ranking number.
The final data are in the ?csv? file named ?games_chop?.

4. Analyzing the board game
The file named "machine.py" is used to analyze the board game data.

It looks at the relationship between the price of the game and the users rating of the game. 
It uses the "GaussianMixture" to separate the games into three clusters. 
components = 2, silhouette_score =  0.39952376133117234 , Gaussian_cluster_graph_2 shows the plotting result.
components = 3, silhouette_score =  0.44701307212489155 , Gaussian_cluster_graph_3 shows the plotting result.
components = 4, silhouette_score =  0.5083493836471616 ,   Gaussian_cluster_graph_4 shows the plotting result.
components = 5, silhouette_score =  0.36574401476811047 , Gaussian_cluster_graph_5 shows the plotting result.
components = 6, silhouette_score =  0.2884292281841645 ,   Gaussian_cluster_graph_6 shows the plotting result.

I also tried higher number of clusters, but the silhouette scores are lower.  It seem the games can be clustered into three or four groups.
The price and the rating seems positively associated.

You can change the number in the ?components? for different cases.

If we take the cluster with component = 4. The game are separated into four groups. 
The group with blue dots form a group that have relatively low price and relatively low rating.
The group with yellow dots form a group that list relatively high price and receive relatively high rating.
And the group with green dots form a group that receives very high rating but still charges a relatively low price. 
The pattern of the group with purple dot is not quite clear.

If the rating reflect the real customer satisfaction, and if the customer satisfaction is related to the effort of game design, then the yellow group has the good return for the game designers.  For it charge good price for their good quality. The green group can be under priced, for it generate high customer satisfaction but charges a low price.
More information about the game will be needed to test the hypothesis.


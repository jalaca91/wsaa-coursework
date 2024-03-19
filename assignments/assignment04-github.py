# Author: Jaime Lara Carrillo
# Write a program in python that will read a file from a repository
# The program should then replace all the instances of the text "Andrew" with "Jaime"
# The program should then commit those changes and push the file back to the repository

import requests 
from github import Github
from config import config as cfg 

# APIKey from config.py
apikey = cfg["githubkey"]  
g = Github(apikey)

# Get clone url
repo = g.get_repo("jalaca91/WSAA-coursework")

# Get downloadurl
fileInfo = repo.get_contents("assignments/text_assignment04.txt")
urlOfFile = fileInfo.download_url

# Making a http request from the downloadurl 
response = requests.get(urlOfFile)
contentOfFile = response.text

# Replacing instances of "Andrew" with "Jaime"
newContents = contentOfFile.replace("Andrew", "Jaime")
print(newContents)
      
# Updating the file and pushing back to repository
gitHubResponse=repo.update_file(fileInfo.path,"updatedtest_text_assignment04.txt",newContents,fileInfo.sha)
print(gitHubResponse)



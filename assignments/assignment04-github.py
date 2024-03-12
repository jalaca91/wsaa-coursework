# Author: Jaime Lara Carrillo
# Write a program in python that will read a file from a repository
# The program should then replace all the instances of the text "Andrew" with "Jaime"
# The program should then commit those changes and push the file back to the repository

import requests 
from github import Github
from config import config as cfg 


###Step 1
Install pipenv
`pip install pipenv`
###Step 2
Install dependencies from project folder
`pipenv install`
###Step 3
Create JSON file with key value pair for your MindSphere Login
`{
  "user_name": <USERNAME>,
  "password": <PASSWORD>
}`
###Step 4
In the getMindSphereToken.py, edit the credential_file in to your path using the Path library. Please only use forward slash `/` for file name
`Path(folderpath/filename.json)`
###Step 5
Replace the Token App name with the name you called your tokenapp
Run `python3 getMindSphereToken.py`

####Optional Step:
Chromedriver may become outdated. Please updated when the drivers become obsolete!

##If you like my work please buy me a cup of coffee
##Etherium Wallet: 0x0ac7e3f5060700cf30da11a9f1a503dd8c471840
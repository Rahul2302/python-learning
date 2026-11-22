to work on jupyter notebook as virtual environment on your windows machine:
apt install python3-pip
source .venv/bin/activate
python -m pip install notebook
jupyter notebook --allow-root
copy the localhost to browser and do the labs


how to add the vscode codes to GitHub
 create new repo into GitHub on your account with + option into you GitHub account
install the git into windows machine with below commd:
winget install --id Git.Git -e --source winget
git init
git add .
git config --global user.name "Rahul Kumar"
git config --global user.email "your-email@example.com"
git commit -m "LearningPython" 
git remote add origin https://github.com/Rahul2302/python-learning.git
git branch -M main
git push -u origin main
it will ask for authentication then refresh the repo into GitHub all files are there.

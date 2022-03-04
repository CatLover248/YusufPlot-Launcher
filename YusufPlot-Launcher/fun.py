import subprocess

def clone_repo(repo):
    try:
        subprocess.run("git clone " + str(repo), shell=True)
    except:
        print("Failed to clone repo, make sure that you have git installed.")

def run():
    print("Comming soon...")
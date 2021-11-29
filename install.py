import os

"""
    python3
    exec(open('install.py').read())
"""

print("""
Qual é o seu sistema operacional:
Para selecionar Windows - (W)
Para selecionar Linux - (L)
""")

SO = input("\nWindows(W)").upper()

os.system("git clone git@github.com:LucasSantus/c-remedios.git")
os.system("cd c-remedios")

if(SO == "W" or SO == "WINDOWS"):
    os.system("python -m venv env")
    os.system("env\Scripts\activate")
    os.system("python -m pip install --upgrade pip")
    os.system("pip install -r requirements.txt")
    
elif(SO == "L" or SO == "LINUX"):
    os.system("python3 -m venv env")
    os.system("source env/bin/activate")
    os.system("python -m pip install --upgrade pip")
    os.system("pip install -r requirements.txt")

else:
    print("ERRO!!")
    exit()

os.system("python manage.py makemigrations home")
os.system("python manage.py makemigrations usuarios")
os.system("python manage.py makemigrations receitas")
os.system("python manage.py migrate")
os.system("python manage.py runserver")
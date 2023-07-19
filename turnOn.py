import subprocess, datetime, platform

# https://pt.stackoverflow.com/questions/402231/como-executar-programa-em-python-ao-iniciar-linux-mint#:~:text=ExecStart%3D%2Fusr%2Fbin%2Fpython%20%2Fhome%2Fmeuscript.py%20%3E%20%2Fhome%2Fmeuscript.log%202%3E%261%20OBS%3A%20pode%20salvar,sudo%20systemctl%20daemon-reload%20%26%26%20sudo%20systemctl%20enable%20meuscript.service

subprocess.call(args=["git push "], shell=True)

process = subprocess.call(args=["git status"], shell=True)

print(platform.node())

if str(platform.node()).__contains__("not"):

    inputLog = "\n   Notebook Ligado: " + str(datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S'))

if str(platform.node()).__contains__("pc"):

    inputLog = "\n PC Ligado: " + str(datetime.datetime.today().strftime('%Y/%m/%d %H:%M:%S'))


with open("log.txt", "a") as file:
    file.write(inputLog)

subprocess.call(args=["git add ."], shell=True)

subprocess.call(args=["git commit -m log"], shell=True)

subprocess.call(args=["git push origin main"], shell=True)

# print("data: ", datetime.datetime.now())

# process = subprocess.call(args=["git help"], shell=True)
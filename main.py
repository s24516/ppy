import smtplib
from email.mime.text import MIMEText
list  =[]

filepath = "./students.txt"

def sendEmail(subject,body,sender,recipients,password):
    msg = MIMEText(body)
    msg['Subject']=subject
    msg['From'] = sender
    msg['To'] = ',' .join (recipients)
    smtp_server = smtplib.SMTP_SSL('smtp.gmail.com',465)
    smtp_server.login(sender,password)
    smtp_server.sendmail(sender,recipients,msg.as_string())
    smtp_server.quit()


def fileLoader():
    wynik = "";
    for i in list:
        wynik += i["imie"]+ " " + i["nazwisko"] +" "+i["email"] + " " + str(i["punkty"]) + " " + str(i["ocena"]) + " " + i["status"] + "\n"
    with open(filepath, "w") as file_object:
        file_object.write(wynik)


def grade(punkty):
    ocena = 0
    if punkty <= 50:
        ocena = 2
    if punkty > 50 and punkty <= 60:
        ocena = 3
    if punkty > 60 and punkty <= 70:
        ocena = 3.5
    if punkty > 70 and punkty <= 80:
        ocena = 4
    if punkty > 80 and punkty <= 90:
        ocena = 4.5
    if punkty > 90 and punkty <= 100:
        ocena = 5
    return ocena


with open(filepath) as file_object:
    for i in file_object:
        linia = i.rstrip().split(" ")
        students = {}
        students["imie"] = linia[0]
        students["nazwisko"] = linia[1]
        students["email"] = linia[2]
        students["punkty"] = linia[3]
        if (len(linia) == 4):
            students["ocena"] = grade(int(linia[3]))
            students["status"] = ""
        if (len(linia) == 5):
            if (linia[4] == "GRADED" or linia[4] == "MAILED"):
                students["ocena"] = grade(int(linia[3]))
                students["status"] = linia[4]
            if linia[4] == "2" or linia[4] == "3" or linia[4] == "3.5" or linia[4] == "4" or linia[4] == "4.5" or linia[4] == "5":
                students["ocena"] = linia[4]
                students["status"] = ""
        if (len(linia) == 6):
            students["ocena"] = linia[4]
            students["status"] = linia[5]
        list.append(students)

wybor = ""
while True:
    index = 0
    for i in list:
        print(str(index)+ ". " +str(i))
        index+=1
        print("---------------------------")
        print("1. Dodaj nowego studenta")
        print("2. Usun studenta")
        print("3. Wyslij maile")
        print("4.Ocen uczniów automatycznie")
        print("5. Wyjdz")
        wybor = input("Podaj wybor: ")
        match wybor:
            case "1":
                isUnique = True

                students = {}
                students["imie"] = input("Podaj imie: ")
                students["nazwisko"] = input("Podaj nazwisko: ")
                email = input("Podaj email: ")
                for x in list:
                    if x["email"] == email:
                        isUnique = False
                while isUnique == False:
                    isUnique = True
                    print("Podano zajety email!")
                    email = input("Podaj email: ")
                    for x in list:
                        if x["email"] == email:
                            isUnique = False
                students["email"] = email
                students["punkty"] = input("Podaj punkty: ")
                students["ocena"] = grade(int(students["punkty"]))
                students["status"] = ""
                list.append(students)
                fileLoader()
            case "2":
                index = input("Podaj index rekordu do usuniecia: ")
                if int(index) <= len(list) - 1 and int(index) >= 0:
                    list.pop(int(index))
                fileLoader()
            case "3":
                for element in list:
                    if element["status"] != "MAILED":
                        subject = "Ocena z PPY"
                        body = "Ocena z PPY wynosi: " + element["ocena"]
                        sender = ""
                        recipients = element["email"]
                        password = ""
                        sendEmail(subject, body, sender, recipients, password)
                fileLoader()
            case"4":
                for x in list:
                    if x["status"] != "GRADED" or x["status"] != "MAILED":
                        x["ocena"] = grade(int(x["punkty"]))
                        x["status"] = "GRADED"
                fileLoader()
            case "5":
                fileLoader()
                break










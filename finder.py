# import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.select import By
from selenium import webdriver
import multiprocessing
import multiprocessing.connection
import winsound
import time
import sys
import random
from datetime import datetime


def next_month(browser):
    # Mouve to the next month
    cmp = 0
    while cmp < 3:
        try:
            time.sleep(2)
            next_month = browser.find_element_by_class_name("fc-corner-right")
            next_month.click()
            time.sleep(2)
            break

        except:
            print("ALERT!!! \tLe mois suivant est introuvable ... veuillez patienter !")
            browser.refresh()
            cmp += 1
            pass


def prev_month(browser):
    # Mouve to the previous month
    while True:
        try:
            prev_month = browser.find_element_by_class_name("fc-corner-left")
            prev_month.click()
            break
        except:
            print(
                "ALERT!!! \tLe mois precedant est introuvable ... veuillez patienter !"
            )
            browser.refresh()
            pass
    time.sleep(4)


def select_city(browser, nb):
    # Changing antenna
    # 1 : Alger
    # 2 : Oran
    # 3 : Annaba
    # 4 : Constantine
    # 5 : Tlemmcen
    cmp = 0
    while cmp < 4:
        try:
            select_element = browser.find_element(By.ID, "city_filter")
            select_object = Select(select_element)
            select_object.select_by_value(nb)
            break
        except:
            print("ALERT!!! \tCité introuvable")
            time.sleep(1)
            browser.refresh()
            cmp += 1
            pass


def login(browser, user, mdp):
    # Get Login Page
    while True:
        try:
            do = 1

            browser.get("https://website.com/login")
            while (
                browser.current_url == "https://website.com/login" or do == 1
            ):
                if do == 0:
                    browser.refresh()
                do = 0
                try:
                    print("trying to login ......")
                    time.sleep(2)
                    email_field = browser.find_element_by_name("email")
                    password_field = browser.find_element_by_name("password")
                    submit_button = browser.find_element_by_id("login")
                    # check = browser.find_element(By.XPATH,"//div[contains(@class,'checkbox')")
                    # Login Process
                    email_field.send_keys(user)
                    password_field.send_keys(mdp)
                    # check.click()
                    submit_button.click()
                    time.sleep(4)
                except:
                    print("ALERT!!! \tLe site est fermé !")
                    browser.refresh()
                    time.sleep(2)
            print("successfuly Logged")
            break
        except:
            pass


# Get rdv URL
def get_rdv(browser):
    while True:
        try:
            time.sleep(1)
            browser.get("https://website.com/")
            time.sleep(1)
            break
        except:
            print("erreur lors de l'inscription")
            time.sleep(1)
            pass


# Get INS URL
def get_inscription(browser):
    while True:
        try:
            time.sleep(1)
            browser.get("https://website.com/")
            time.sleep(1)
            break
        except:
            print("erreur lors de l'inscription")
            time.sleep(1)
            pass


# Get Home URL
def get_home(browser):
    while True:
        try:
            time.sleep(1)
            browser.get("https://website.com/")
            time.sleep(3)
            break
        except:
            print("erreur Home")
            time.sleep(1)
            pass


def Go(
    username, password, antenne, search_type, period
):  # section: class ='error-page'

    # create webdriver object
    trouv = 0
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.maximize_window()
    login(browser, username, password)
    get_inscription(browser)

    # # Search For Available Rooms
    # bin = -1
    # while trouv == 0:
    #     try:

    #         for a in antenne:
    #             if browser.current_url == "https://portail.if-algerie.com/exams":
    #                 time.sleep(5)
    #             browser.refresh()
    #             time.sleep(1)
    #             if a != "0":
    #                 select_antenna(browser, a)
    #             for i in range(int(period)):
    #                 try:
    #                     # browser.execute_script("document.body.style.zoom='100%'")
    #                     bin = (bin + 1) % 2
    #                     # if period == 2 and bin == 1: next_month(browser);print('Passage au mois suivant')
    #                     if i != 0:
    #                         next_month(browser)
    #                         print("Passage au mois suivant")
    #                     browser.execute_script("window.scrollTo(0, 70)")
    #                     if (
    #                         browser.current_url == "https://portail.if-algerie.com/home"
    #                     ) or (browser.current_url == "https://portail.if-algerie.com"):
    #                         print("Re-Directing ...")
    #                         get_inscription(browser)

    #                         # if period == 2 and bin % 2 == 1: next_month(browser);print('Passage au mois suivant')
    #                         # next_month(browser)

    #                     if (
    #                         browser.current_url
    #                         == "https://portail.if-algerie.com/login"
    #                     ):
    #                         print("Re-Logging ...")
    #                         login(browser, username, password)
    #                         get_inscription(browser)

    #                         # if period == 2 and bin % 2 == 1: next_month(browser);print('Passage au mois suivant')
    #                         # next_month(browser)

    #                     href = browser.find_elements(
    #                         By.XPATH,
    #                         "//a[contains(@class,'bg-info') or @class = 'fc-day-grid-event fc-h-event fc-event fc-start fc-end']",
    #                     )  # elements
    #                     # href.reverse()
    #                     rdvs = len(href)
    #                     print(str(rdvs) + " RDV TROUVES")
    #                     if rdvs > 0:
    #                         winsound.PlaySound(
    #                             "C:/Users/Lenovo/Desktop/Beep.wav",
    #                             winsound.SND_ASYNC | winsound.SND_FILENAME,
    #                         )
    #                     random.shuffle(href)
    #                 except:
    #                     pass

    #                 for i, a in enumerate(href):
    #                     print(f"\n RDV n° {i+1} :\n")
    #                     print("\tPhase de recherche :")

    #                     # print("Element is visible? " + str(a.is_displayed()))

    #                     if a.is_displayed() == False:
    #                         # browser.execute_script("window.scrollTo(0, 160)")
    #                         index = (
    #                             len(
    #                                 list(
    #                                     a.find_elements(
    #                                         By.XPATH,
    #                                         "./../preceding-sibling::td[contains(@class,'fc-event-container')]",
    #                                     )
    #                                 )
    #                             )
    #                             + 1
    #                         )
    #                         y = (
    #                             len(
    #                                 a.find_elements(
    #                                     By.XPATH, "./../../preceding-sibling::tr"
    #                                 )
    #                             )
    #                             + 1
    #                         )
    #                         print("\tindex = ", index, ", y = ", y)
    #                         # print('... recherche du parent ...')
    #                         # parent = a.find_element(By.XPATH,f"./../../..//a[contains(@class,'fc-more') and position()={index}")
    #                         parent = a.find_element(
    #                             By.XPATH,
    #                             f"./../../..//td[.//a[@class='fc-more' ] and @class='fc-more-cell' ][{index}]//a[@class='fc-more']",
    #                         )
    #                         parent.click()
    #                         # time.sleep(1)
    #                         # print('... parent trouvé ...')

    #                         a = browser.find_element(
    #                             By.XPATH,
    #                             f"//div[contains(@class,'fc-popover')]//a[contains(@class,'fc-h-event') ][{y}]",
    #                         )
    #                         # a = browser.find_element(By.XPATH,f"//div[contains(@class,'fc-popover')]//a[contains(@class , 'fc-day-grid-event fc-h-event fc-event fc-start fc-end') ][{y}]")
    #                         print(
    #                             "\t( Element rdv is visible? "
    #                             + str(a.is_displayed())
    #                             + " )"
    #                         )

    #                         tcf_type = a.find_element(
    #                             By.XPATH, ".//span[contains(@class,'fc-title')]"
    #                         )
    #                         # print(tcf_type.text)
    #                     else:
    #                         tcf_type = a.find_element(
    #                             By.XPATH, ".//span[contains(@class,'fc-title')]"
    #                         )  # a

    #                     # Appointment booking process
    #                     if tcf_type.text == search_type:
    #                         if tcf_type.text == "TCF DAP":
    #                             print("\t\tTCF DAP Apointment Found")

    #                         if tcf_type.text == "TCF Canada":
    #                             print("\t\tTCF Canada Apointment Found")

    #                         if tcf_type.text == "TCF SO":
    #                             print("\t\tTCF SO Apointment Found")
    #                         # Open Modal

    #                         try:
    #                             print("\t\tEntrain d'ouvrir la carte ... ")
    #                             a.click()
    #                             print("\t\tDone !")
    #                         except:
    #                             print("\t\tLa carte ne s'est pas ouvrte !")
    #                             pass

    #                         # Finalisation
    #                         time.sleep(5)
    #                         print("\n\tPhase de finalisation")
    #                         try:
    #                             # exams_modal = browser.find_element_by_id('exams-modal')
    #                             payment_day = browser.find_element_by_id("paymentDay")
    #                             submit_exam_button = browser.find_element_by_id(
    #                                 "submitExam"
    #                             )
    #                             submit_exam_button = browser.find_element_by_id(
    #                                 "submitExam"
    #                             )
    #                             payment_day.click()
    #                             print("\t\tOuverture du calendrier ...")
    #                             time.sleep(1)
    #                             day = browser.find_element(
    #                                 By.XPATH, "//td[contains(@class,'day active')]"
    #                             )

    #                             print(
    #                                 "\t( Day is visible? "
    #                                 + str(day.is_displayed())
    #                                 + " )"
    #                             )
    #                             day.click()
    #                             time.sleep(1)
    #                             browser.switch_to.window(browser.current_window_handle)
    #                             print("\t\tClick sur le jour trouvé ...")
    #                             submit_exam_button.click()
    #                             print("\t\tReservation effectuée via le calendrier !")
    #                             winsound.PlaySound(
    #                                 "C:/Users/Lenovo/Desktop/Sport.wav",
    #                                 winsound.SND_ASYNC | winsound.SND_FILENAME,
    #                             )
    #                             affich = 0
    #                             t1 = time.time()
    #                             t2 = time.time()
    #                             while (affich == 0) and (
    #                                 t2 - t1 < 10
    #                             ):  # ne sors de la boucle que si le delais depasse 1min30 ou l'alerte verte s'affiche
    #                                 try:
    #                                     alert = browser.find_element(
    #                                         By.XPATH,
    #                                         "//div[contains(@class,'bottom-right')]",
    #                                     )
    #                                     print(
    #                                         f"l'alerte est visible {alert.is_displayed()}"
    #                                     )
    #                                     if alert.displayed() == True:
    #                                         affich = 1
    #                                     else:
    #                                         t2 = time.time()
    #                                 except:
    #                                     print(
    #                                         "ALERT!!!\t La  reservation n'est pas encore validé !"
    #                                     )
    #                                     t2 = time.time()

    #                             if affich == 1:
    #                                 journal(username)
    #                                 # time.sleep(30)
    #                                 # get_home(browser)
    #                                 # change_pass(browser)
    #                                 winsound.PlaySound(
    #                                     "C:/Users/Lenovo/Desktop/door.wav",
    #                                     winsound.SND_ASYNC | winsound.SND_FILENAME,
    #                                 )
    #                                 print(
    #                                     "\t\tLa réservation a été effectuée avec succes !! CONGRATULATION !"
    #                                 )
    #                                 trouv = 1
    #                                 sys.exit(0)
    #                             if (
    #                                 (
    #                                     browser.current_url
    #                                     != "https://portail.if-algerie.com/exams"
    #                                 )
    #                                 and (
    #                                     browser.current_url
    #                                     != "https://portail.if-algerie.com"
    #                                 )
    #                                 and (
    #                                     browser.current_url
    #                                     != "https://portail.if-algerie.com/login"
    #                                 )
    #                             ):
    #                                 journal(username)
    #                                 winsound.PlaySound(
    #                                     "C:/Users/Lenovo/Desktop/door.wav",
    #                                     winsound.SND_ASYNC | winsound.SND_FILENAME,
    #                                 )
    #                                 trouv = 1
    #                                 sys.exit(0)

    #                         except:
    #                             print("\t\tErreur lors de l'inscription")

    #                         print("\tPhase de fermeture :")
    #                         try:
    #                             close_card(browser)
    #                         except:
    #                             print("\t\tErreur lors de la fermeture de la carte")
    #                             pass

    #                 href = []

    #     except:
    #         continue

    time.sleep(120)
    get_home(browser)
    change_pass(browser)


def verif(username, password, antenne, search_type):
    # create webdriver object
    trouv = 0
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.maximize_window()
    login(browser, username, password)
    get_rdv(browser)

    # Search For Available Appointment
    while trouv == 0:
        try:

            for a in antenne:
                try:
                    time.sleep(2)
                    browser.refresh()
                    time.sleep(1)

                    browser.execute_script("window.scrollTo(0, 70)")
                    if (
                        browser.current_url == "https://portail.if-algerie.com/home"
                    ) or (browser.current_url == "https://portail.if-algerie.com"):
                        print("Re-Directing ...")
                        get_rdv(browser)

                    if browser.current_url == "https://portail.if-algerie.com/login":
                        print("Re-Logging ...")
                        login(browser, username, password)
                        get_rdv(browser)

                    if (
                        browser.current_url
                        == "https://portail.if-algerie.com/exams/reserved"
                    ):
                        winsound.PlaySound(
                            "C:/Users/Lenovo/Desktop/Sport.wav",
                            winsound.SND_ASYNC | winsound.SND_FILENAME,
                        )
                        try:
                            a = browser.find_element(
                                By.XPATH,
                                f"//a[@class = 'm-t-30 text-center btn btn-warning']",
                            )
                            a.click()
                        except:
                            time.sleep(3)

                except:
                    pass
        except:
            continue


def verif2(username, password, antenne, search_type):
    # create webdriver object
    trouv = 0
    # browser = webdriver.Firefox()
    browser = webdriver.Chrome()
    browser.maximize_window()
    login(browser, username, password)
    get_rdv(browser)

    # Search For Available Appointment
    while trouv == 0:
        try:

            for a in antenne:
                try:
                    time.sleep(2)
                    browser.refresh()
                    time.sleep(1)

                    browser.execute_script("window.scrollTo(0, 70)")
                    if (
                        browser.current_url == "https://portail.if-algerie.com/home"
                    ) or (browser.current_url == "https://portail.if-algerie.com"):
                        print("Re-Directing ...")
                        get_rdv(browser)

                    if browser.current_url == "https://portail.if-algerie.com/login":
                        print("Re-Logging ...")
                        login(browser, username, password)
                        get_rdv(browser)

                    if (
                        browser.current_url
                        == "https://portail.if-algerie.com/exams/reserved"
                    ):
                        winsound.PlaySound(
                            "C:/Users/Lenovo/Desktop/Sport.wav",
                            winsound.SND_ASYNC | winsound.SND_FILENAME,
                        )
                        try:
                            a = browser.find_element(
                                By.XPATH,
                                f"//a[@class = 'm-t-30 btn text-center btn-inverse']",
                            )
                            a.click()
                        except:
                            time.sleep(3)

                except:
                    pass
        except:
            continue


def brute_change_pass(username, password, antenne, search_type):
    browser = webdriver.Chrome()
    browser.maximize_window()
    login(browser, username, password)

    while True:
        try:
            time.sleep(3)
            if browser.current_url == "https://portail.if-algerie.com/login":
                print("Re-Logging ...")
                login(browser, username, password)
                get_inscription(browser)
                next_month(browser)
            change_pass(browser)
            break
        except:
            browser.refresh()
    sys.exit(0)


def close_card(browser):
    cmp = 0
    while cmp < 3:
        try:
            but = browser.find_element(By.XPATH, "//button[@class='close']")
            but.click()
            print("\t\tCarte fermé avec succes!")
            break
        except:
            cmp += 1
            pass


def check_email(browser, expected_email):
    cmp = 0
    while cmp < 10:
        try:
            info = browser.find_element_by_id("profileLink")
            info.click()
            time.sleep(1)
            browser.execute_script("window.scrollTo(0, 800)")
            email = browser.find_element(
                By.XPATH,
                "//input[@class='form-control form-control-line' and @type = 'email']",
            )
            print(email.get_attribute("value"))
            if email.get_attribute("value") != expected_email:
                email.clear()
                email.send_keys(expected_email)
            sub = browser.find_element(By.XPATH, "//button[@id='update']")
            sub.click()
            time.sleep(1)
            break
        except:
            cmp += 1
            pass


def change_pass(browser):
    cmp = 0
    while cmp < 10:
        try:
            info = browser.find_element_by_id("profileLink")
            info.click()
            time.sleep(1)
            browser.execute_script("window.scrollTo(0, 800)")
            pwd = browser.find_element_by_id("password")
            pwdcmf = browser.find_element_by_id("cfmPassword")
            pwd.clear()
            pwd.send_keys("p@55w0Rd1963")
            pwdcmf.clear()
            pwdcmf.send_keys("p@55w0Rd1963")
            sub = browser.find_element(By.XPATH, "//button[@id='update']")
            sub.click()
            time.sleep(7)
            break
        except:
            cmp += 1
            pass


def journal(user):
    with open("C:/Users/Lenovo/Desktop/journal.txt", "a+") as f:
        f.write(f" _Reservation effectué pour : {user}, à {datetime.now()}\n")
        f.close()


def manager(list, max, type):
    processes = []

    # for client in clients:
    for i in range(max):

        if type == 0:
            p = multiprocessing.Process(
                target=Go,
                args=[
                    list[i]["username"],
                    list[i]["password"],
                    list[i]["antenne"],
                    list[i]["search_type"],
                    list[i]["period"],
                ],
            )
        if type == 1:
            p = multiprocessing.Process(
                target=brute_change_pass,
                args=[
                    list[i]["username"],
                    list[i]["password"],
                    list[i]["antenne"],
                    list[i]["search_type"],
                ],
            )
        if type == 2:
            p = multiprocessing.Process(
                target=verif,
                args=[
                    list[i]["username"],
                    list[i]["password"],
                    list[i]["antenne"],
                    list[i]["search_type"],
                ],
            )
        if type == 3:
            p = multiprocessing.Process(
                target=verif2,
                args=[
                    list[i]["username"],
                    list[i]["password"],
                    list[i]["antenne"],
                    list[i]["search_type"],
                ],
            )
        p.start()
        processes.append(p)
        time.sleep(5)

    i += 1

    # for p in processes:
    while i < len(list):
        # p.join()
        multiprocessing.connection.wait(p.sentinel for p in processes)
        for p in processes:
            if not p.is_alive():
                processes.remove(p)
        # processes.remove(p)
        if type == 0:
            p = multiprocessing.Process(
                target=Go,
                args=[
                    list[i]["username"],
                    list[i]["password"],
                    list[i]["antenne"],
                    list[i]["search_type"],
                    list[i]["period"],
                ],
            )
        if type == 1:
            p = multiprocessing.Process(
                target=brute_change_pass,
                args=[
                    list[i]["username"],
                    list[i]["password"],
                    list[i]["antenne"],
                    list[i]["search_type"],
                ],
            )
        if type == 2:
            p = multiprocessing.Process(
                target=verif,
                args=[
                    list[i]["username"],
                    list[i]["password"],
                    list[i]["antenne"],
                    list[i]["search_type"],
                ],
            )
        if type == 3:
            p = multiprocessing.Process(
                target=verif2,
                args=[
                    list[i]["username"],
                    list[i]["password"],
                    list[i]["antenne"],
                    list[i]["search_type"],
                ],
            )
        print(len(processes))
        p.start()
        processes.append(p)
        i += 1

    for p in processes:
        print(p.is_alive())

    # for p in processes:
    #     p.join()


if __name__ == "__main__":

    clients = [
        {  # 4000
            "username": "meriemkhaalef@gmail.com",
            "password": "7el9ouma",

        },
    ]

    # alger = multiprocessing.Process(target = manager, args=[clients,3,0])
    # alger.start()

    # # reserv.join()
    # alger.join()

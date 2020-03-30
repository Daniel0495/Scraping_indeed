from selenium import webdriver
import selenium.common.exceptions
import time, json
from functions import fun_titulo, company, ciudad, descripcion, rating, fun_paga, resumen
import re


def empleos():
    data = dict()
    data['Alemania'] = list()

    url = 'https://de.indeed.com/Jobs?q=%22intelligente+Mobilit%C3%A4t%22+OR+%22intelligente+Stadt%22+OR+%22smart+city%22+OR+%22smart+mobility%22+OR+%22smart+cities%22+OR+%22intelligent+transport%22&l='
    driver = webdriver.Chrome(executable_path='C:/Users/Asus/PycharmProjects/Indeed/chromedriver.exe')
    driver.get(url)
    driver.maximize_window()

    inicial_todos = driver.find_elements_by_xpath('//div[@class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')
    time.sleep(5)
    for inicial in inicial_todos:
        inicial.find_element_by_class_name('title').click()
        time.sleep(2)
        recuadro = driver.find_element_by_xpath('//div[@id="vjs-container"]')
        time.sleep(3)

        try:
            if len((recuadro.find_element_by_id('vjs-jobtitle')).text) == 0:
                continue
            else:
                print((recuadro.find_element_by_id('vjs-jobtitle')).text)
        except selenium.common.exceptions.NoSuchElementException:
            continue
            #time.sleep(4)
            #print((recuadro.find_element_by_id('vjs-jobtitle')).text)
        time.sleep(2)


        data['Alemania'].append({'País': 'Alemania',
                            'Búsqueda': '"intelligente Mobilität" OR "intelligente Stadt" OR "smart city" OR "smart mobility" OR "smart cities" OR "intelligent transport"',
                            'Titulo': fun_titulo(recuadro),
                            'Empresa': company(inicial),
                            'Resumen': descripcion(inicial),
                            'Rating empresa': rating(inicial),
                            'Ubicación': ciudad(inicial),
                            'Descripción detallada': resumen(recuadro),
                            'Salario': fun_paga(inicial)})
        time.sleep(3)
    driver.close()





    for number in range(31):
        start = (number + 1)*10
        url = 'https://de.indeed.com/Jobs?q=%22intelligente+Mobilit%C3%A4t%22+OR+%22intelligente+Stadt%22+OR+%22smart+city%22+OR+%22smart+mobility%22+OR+%22smart+cities%22+OR+%22intelligent+transport%22&l=' + '&start=' + str(start)
        driver = webdriver.Chrome(executable_path='C:/Users/Asus/PycharmProjects/Indeed/chromedriver.exe')
        driver.get(url)
        driver.maximize_window()

        inicial_todos = driver.find_elements_by_xpath('//div[@class="jobsearch-SerpJobCard unifiedRow row result clickcard"]')
        time.sleep(5)
        for inicial in inicial_todos:
            inicial.find_element_by_class_name('title').click()
            time.sleep(2)
            #print((((inicial.find_element_by_class_name('sjcl')).find_element_by_class_name('location accessible-contrast-color-location xh-highlight'))).text)
            #q = inicial.find_element_by_class_name('sjcl')
            #print([q.text])#.find_element_by_class_name('location accessible-contrast-color-location'))
            recuadro = driver.find_element_by_xpath('//div[@id="vjs-container"]')
            time.sleep(2)
            #print((recuadro.find_element_by_id('vjs-jobtitle')).text)
            try:
                if len((recuadro.find_element_by_id('vjs-jobtitle')).text) == 0:
                    continue
                else:
                    print((recuadro.find_element_by_id('vjs-jobtitle')).text)
            except selenium.common.exceptions.NoSuchElementException:
                continue
                #time.sleep(4)
                #print((recuadro.find_element_by_id('vjs-jobtitle')).text)
            #print([(recuadro.find_element_by_id('vjs-content')).text])
            except:
                continue
            time.sleep(2)


            data['Alemania'].append({'País' : 'Alemania',
                                'Búsqueda' : '"intelligente Mobilität" OR "intelligente Stadt" OR "smart city" OR "smart mobility" OR "smart cities" OR "intelligent transport"',
                                'Titulo': fun_titulo(recuadro),
                                'Empresa': company(inicial),
                                'Resumen': descripcion(inicial),
                                'Rating empresa' : rating(inicial),
                                'Ubicación' : ciudad(inicial),
                                'Descripción detallada' : resumen(recuadro),
                                'Salario' : fun_paga(inicial)})

        time.sleep(5)
        driver.close()

    with open('data_indeed_Alemania.json', 'a') as file:
        json.dump(data, file, indent=4)

empleos()


from django.shortcuts import render,HttpResponse
import requests
from bs4 import BeautifulSoup
# Create your views here.

def scraped(request):
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    html_text = session.get('https://www.careerguide.com/').text
    print(html_text)


def scraped1(request):
    cont = request.GET.get('cont')
    print(cont)
    #cont = cont.replace(" ", "+")
    USER_AGENT = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36"
    LANGUAGE = "en-US,en;q=0.5"
    session = requests.Session()
    session.headers['User-Agent'] = USER_AGENT
    session.headers['Accept-Language'] = LANGUAGE
    session.headers['Content-Language'] = LANGUAGE
    #html_content = session.get(f'https://www.google.com/search?q=+{cont}').text
    html_content = session.get('https://www.google.com/search').text
    print(html_content)
    #return html_content

def home(request):
    content = scraped(request)
    soup = BeautifulSoup(content, 'lxml')
    content1 = scraped1(request)
    soup1 = BeautifulSoup(content1, 'lxml')
    result = None
    res = None
    if 'cont' in request.GET:
        res = dict()
        res['region'] = soup1.find('div',class_="yuRUbf").h3.text
        res['info'] = soup1.find('div',class_="yuRUbf").a['href']
        print("\nData Appeared in the Website : ")
        print(res)
        return render(request, 'core/home.html', {'result': res})

    if request.method == "POST":
        vira = request.POST['num']
        vv=int(vira)
        main_page = soup.find('div', class_="row text-center")
        tests = main_page.find_all('div', class_='col-md-3')
        links=list()
        nm=list()
        result=dict()
        for test in tests:
            name = test.h5.text
            info = test.a['href']
            links.append(info)
            nm.append(name)
        result['no']=vv
        result['crs_name']=nm[(int(vira)+1)]
        result['info']=links[(int(vira)+1)]
        print("\nData Appeared in the Website by clicking "+str(vv)+" Number is: ")
        print(nm[vv+1])
        print(links[vv+1])
        return render(request,'core/home.html',{'result': result})
    else:
        return render(request,'core/home.html')

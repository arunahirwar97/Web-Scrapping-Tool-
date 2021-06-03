from django.shortcuts import render
import requests
import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
# Create your views here.
def index(request):
    if request.method == 'POST':
    
        search = request.POST.get('url', None) 
        print(search)
        request_url = urllib.request.urlopen(search)

        data = request_url.read()
        data = [data]
        return render(request,'index.html' , {'number':data})
    else:
        return render(request,'index.html')
    return render(request,'index.html')
    
# def index(request):
#     return render(request,'index.html')

def all_a_url(request):
    if request.method == 'POST':
        a_tag = request.POST.get('url', None)
        html_page = urllib.request.urlopen(a_tag)
        soup = BeautifulSoup(html_page, "html.parser")
        a_link = []
        for link in soup.findAll('a'):
            a_links = link.get('href')
            a_link.append(a_links)
        return render(request,'all_url_links.html',{'a_links':a_link})
    else:
        return render(request,'all_url_links.html')
    return render(request,'all_url_links.html')

def all_img_links(request):
    if request.method == 'POST':
        a_tag = request.POST.get('url', None)
        html_page = urllib.request.urlopen(a_tag)
        soup = BeautifulSoup(html_page)
        images_links = []
        for img in soup.findAll('img'):
            images_links.append(img.get('src'))

        return render(request,'all_img_links.html',{'images_links':images_links})
    else:
        return render(request,'all_img_links.html')
    return render(request,'all_img_links.html')

    # return render(request,'all_img_links.html')

def get_table_data(request):
    if request.method == 'POST':
        table_url = request.POST.get('url', None)
        r = requests.get(table_url)
        table = pd.read_html(r.text) # this parses all the tables in webpages to a list
        tables = table[0]
        return render(request,'get_table_data.html',{'tables':tables})
    else:
        return render(request,'get_table_data.html')
    return render(request,'get_table_data.html')

    # return render(request,'get_table_data.html')

def get_heading_data(request):
    if request.method == 'POST':
        heading_tag = request.POST.get('url', None)
        # request = requests.get(heading_tag)
        html_page = urllib.request.urlopen(heading_tag)
        Soup = BeautifulSoup(html_page)
        # creating a list of all common heading tags
        heading_tags = ["h1", "h2", "h3","h4"]
        head1 = []
        for tags in Soup.find_all(heading_tags):
            hh = tags.name + ' -> ' + tags.text.strip()
            head1.append(hh)
            print(hh)
        print(head1)
        return render(request,'get_heading_data.html',{'heading':head1})
    else:
        return render(request,'get_heading_data.html')
    return render(request,'get_heading_data.html')
    # return render(request,'get_heading_data.html')

def get_paragraph_data(request):
    if request.method == 'POST':
        paragraph_tag = request.POST.get('url', None)
        html_page = urllib.request.urlopen(paragraph_tag)
        # request = requests.get(paragraph_tag)
        Soup = BeautifulSoup(html_page)
        # creating a list of all common heading tags
        heading_tags = ["p", "span"]
        para = []
        for tags in Soup.find_all(heading_tags):
            pp = tags.name + ' -> ' + tags.text.strip()
            para.append(pp)
        print(para)
        return render(request,'get_paragraph_data.html',{'paragraph':para})
    else:
        return render(request,'get_paragraph_data.html')
    return render(request,'get_paragraph_data.html')
    # return render(request,'get_paragraph_data.html')
def get_list_data(request):
    if request.method == 'POST':
        list_tag = request.POST.get('url', None)
        html_page = urllib.request.urlopen(list_tag)
        # request = requests.get(list_tag)
        Soup = BeautifulSoup(html_page)
        # creating a list of all common heading tags
        heading_tags = ["li",'ul','ol']
        list = []
        for tags in Soup.find_all(heading_tags):
            listtt = tags.name + ' -> ' + tags.text.strip()
            list.append(listtt)

        return render(request,'get_list_data.html',{'lists':list})
    else:
        return render(request,'get_list_data.html')
    return render(request,'get_list_data.html')

def website_download(request):
    return render(request,'website_download.html')


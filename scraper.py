#imports 
import requests
from bs4 import BeautifulSoup
import requests
import urllib
from requests_html import HTMLSession
import streamlit as st

@st.cache
class s:
    """The responsibility of this Class is to take queries or URL inputs and return scraped text."""
    def get_source(self, url):
        """The 'get_source()' method starts an HTML session, then attempts to access HTML source code and returns a response."""
        try:
            session = HTMLSession()
            response = session.get(url)
            return response
        except requests.exceptions.RequestException as e:
            print(e)
    def scrape_google(self, query):
        """The 'scrape_google()' method returns a list of URLs."""
        google_domains = ('https://www.google.', 
                            'https://google.', 
                            'https://webcache.googleusercontent.', 
                            'http://webcache.googleusercontent.', 
                            'https://policies.google.',
                            'https://support.google.',
                            'https://maps.google.')
        
        query = urllib.parse.quote_plus(query)
        response = self.get_source("https://www.google.com/search?q=" + query)
        links = list(response.html.absolute_links)
        for url in links[:]:
            if url.startswith(google_domains):
                links.remove(url)
        return links
    def makeQuery(self, query, urlCount):
        """The 'make_query()' method appends 'p'-tagged HTML content to a string."""
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        urls = self.scrape_google(query)
        txt = ""
        for url in urls[:urlCount]:
            request = urllib.request.Request(url, None, headers) 
            response = urllib.request.urlopen(request)
            parsed = BeautifulSoup(response, 'html.parser')
            for string in parsed.find_all('p'):
                txt += string.get_text() 
        return txt
    def makeUrlQuery(self, url):
        """The 'makeUrlQuery()' method appends 'p'-taged HTML content to a string."""
        headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
        request = urllib.request.Request(url, None, headers) 
        response = urllib.request.urlopen(request)
        parsed = BeautifulSoup(response, 'html.parser')
        txt = ""
        for string in parsed.find_all('p'):
            txt += string.get_text()
        return txt


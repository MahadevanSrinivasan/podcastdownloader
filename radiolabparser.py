from BeautifulSoup import BeautifulSoup
import urllib2
import re

class radiolabparser():
    
    def __init__(self):
      self.url = 'http://www.radiolab.org/story/elements/'
      self.downloadAndParseHtml()
      self.parseTitle()
      self.parseDownloadUrl()

    def parseTitle(self):
      self.activeSlider = self.parsed_html.body.find('div', attrs={'class':'grid_8 main episode'})
      self.episodeTitle = re.sub(r'[^\w]+', '', self.activeSlider.find('h2', attrs={'class':'title'}).text)

    def parseDownloadUrl(self):
      self.downloadUrl = self.activeSlider.find('div', attrs={'class': 'player_element'})['data-download']

    def downloadAndParseHtml(self):
      hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
      req = urllib2.Request(self.url, headers=hdr)
      f = urllib2.urlopen(req)
      html = f.read()
      self.parsed_html = BeautifulSoup(html)
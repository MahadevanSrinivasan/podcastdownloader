import time
import urllib2

class downloader:
  def __init__(self, downloadUrl, episodeTitle, podcastName='podcast'):
    self.downloadUrl = downloadUrl
    if episodeTitle:
      self.episodeTitle = episodeTitle
    else:
      self.episodeTitle = podcastName + time.strftime("%d_%m_%Y_%I_%M_%S")
    self.startDownload()
    
  def startDownload(self):
    podcast = urllib2.urlopen(self.downloadUrl)
    output = open(self.episodeTitle + '.mp3', 'wb')
    output.write(podcast.read())
    output.close()

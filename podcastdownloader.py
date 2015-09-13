#!/usr/bin/python
import sys
from downloader import downloader
from podcastparser import podcastparser

def main(podcastname):
  p = podcastparser.factory(podcastname)
  print p.episodeTitle, p.downloadUrl
  if p.downloadUrl:
    d = downloader(p.downloadUrl, p.episodeTitle, podcastname)

if __name__ == "__main__":
  if(len(sys.argv) < 2):
    print "Mind telling me which podcast you want?"
    print "For 'This American Life' pass 'tal'"
    print "For 'Planet Money' pass 'money'"
    print "For 'RadioLab' pass 'radiolab'"
  else:
    main(sys.argv[1])
    
    

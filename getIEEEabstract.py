#!/usr/bin/env python
import urllib2, re, time, random, traceback, urllib
from os import listdir, rename, path
from os.path import isfile, join

# get title for IEEE paper
def getIEEEAbs(fname,workingdir):
    number = fname.split('.')[0]
    pattern="[0-9^]"
    patmatch = re.search(pattern,number)
    if patmatch: 
      print "Pattern matched!"
      number2= int(number)
      # open and read from those url
      url = 'http://ieeexplore.ieee.org/xpl/downloadCitations?recordIds='
      url += str(number2)
      url += "&citations-format=citation-abstract&download-format=download-ascii"
      opener = urllib2.build_opener()
      opener.addheaders = [('User-agent', 'Mozilla/5.0')]
      absPage = opener.open(url).read()
      return absPage
    else:
      return None
  
  
def batchabs(workingdir,summary):
    i=0
    files = [ fInput for fInput in listdir(workingdir) if isfile(join(workingdir,fInput)) ]
    for f in files:
          print "Reading File "+ f
          text = getIEEEAbs(f,workingdir)
          if (text is None):
            dummy=0
          else:
            i=i+1
            paperno= "Paper "+str(i)+ "<br>"
            summary.write(paperno)
            summary.write(str(text))
            time.sleep(random.randrange(5))
            print "Paper " + str(i) + " has been added"

if __name__ == '__main__':
    print 'Getting abstracts of files'
    workingdir = path.abspath('.')
    workingdir =workingdir + '/'
    print "I am working in " + workingdir
    summary = open("summary.html","a");
    batchabs(workingdir, summary)
    summary.close()
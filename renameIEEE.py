#!/usr/bin/env python
import urllib2, re, time, random, traceback
from os import listdir, rename, path
from os.path import isfile, join
IEEE = 1
# get title for IEEE paper
def getIEEETitle(fname):
    number = int(fname.split('.')[0])    
    targeturl = 'http://ieeexplore.ieee.org/xpl/freeabs_all.jsp?arnumber='+str(number)
    # open and read from those url
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]
    ieeePage = opener.open(targeturl).read()
    ieeePageSplit = ieeePage.replace('<','>').split('>')
    title = None
    # find a tag that start with 'meta name="citation_title" content="'
    for i in ieeePageSplit:
        if i.startswith('meta name="citation_title" content="'):
            # get the paper title
            title = i.split('"')[3]
            break
    return title.strip()[:150]
def batchRename(workingdir, site):
    files = [ fInput for fInput in listdir(workingdir) if isfile(join(workingdir,fInput)) ]
    reIlegalChar = re.compile(r'([<>:"/\\|?*])')
    for f in files:
        try:
            if site == IEEE:
                title = getIEEETitle(f)
            else:
                title = None
            if title:
                fnew = reIlegalChar.sub(r' ', title) + '.pdf'
                print '{} --> {}'.format(f, fnew)
                rename((workingdir + f), (workingdir + fnew))
                print 'Success'
            else:
                print '{}\nFailed'.format(f)
        except:
            print '{}\nERROR'.format(f)
            traceback.print_exc()
        time.sleep(random.randrange(5))

if __name__ == '__main__':
    print 'Writing filenames'
    workingdir = path.abspath('.')
    workingdir =workingdir + '/'
    print "I am working in " + workingdir
    batchRename(workingdir, IEEE)
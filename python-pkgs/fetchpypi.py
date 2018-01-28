#! /usr/bin/env nix-shell
#! nix-shell -i python -p python python2Packages.lxml python2Packages.requests

import requests, lxml, os
from lxml import html
#from threading import Thread
from multiprocessing import Process

url_pattern='http://pypi.python.org/pypi/%s/json'

def fetch_pkg_names():
  url='https://pypi.python.org/simple/'
  resp = requests.get(url)
  tree = lxml.html.fromstring(resp.content)
  names = tree.xpath('//a/text()')
  return names

def fetch_pkg(name,dst):
  url = url_pattern % name
  data=requests.get(url).content
  with open(dst, 'w') as f:
    f.write(data)

def fetch_pkgs(num,total_th,names):
  idx=num
  n=len(names)
  while idx<n:
    name=names[idx]
    print ("%s/%s %s" % (idx,n,name))
    dst='pkgs/%s' % name
    idx+=total_th
    if os.path.exists(dst):
      continue
    fetch_pkg(name,dst)

def manager(nmax=30):
  names = fetch_pkg_names()
  try:
    os.makedirs('pkgs')
  except:
    pass
  threads=[]
  for  i in range(nmax):
    #th=Thread(target=fetch_pkgs, args=(i,nmax,names))
    th=Process(target=fetch_pkgs, args=(i,nmax,names))
    th.start()
    threads.append(th)
  for th in threads:
    th.join()


def main():
  manager(3)

if __name__ == "__main__":
  main()
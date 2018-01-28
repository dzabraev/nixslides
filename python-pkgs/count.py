#!/usr/bin/env python

import os,json
from collections import defaultdict

def main():
  stat=defaultdict(int)
  py2=0
  py3=0
  py2_ver=set(['2.7'])
  py3_ver=set(['3.7','3.6','3.5','3.4'])
  prefix="Programming Language :: Python :: "
  d='pkgs'
  for filename in os.listdir(d):
    fname = os.path.join(d,filename)
    with open(fname) as f:
      data=f.read()
      if not data:
        continue
      try:
        info = json.loads(data)
      except:
        print ('Bad json: %s' % fname)
      if "info" not in info:
        continue
      else:
        if "classifiers" not in info['info']:
          continue
        else:
          classifiers = info['info']['classifiers']
          versions=[]
          for cl in classifiers:
            if cl.startswith(prefix):
              ver = cl[len(prefix):].strip()
              versions.append(ver)
          for ver in versions:
              stat[ver]+=1
          verset = set(versions)
          py2 += int(bool(verset & py2_ver))
          py3 += int(bool(verset & py3_ver))

  #for key, val in stat.iteritems():
  #  print key, val

  print('py2=%s' % py2)
  print('py3=%s' % py3)

if __name__=="__main__":
  main()
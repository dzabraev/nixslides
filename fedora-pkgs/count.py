#! /usr/bin/env nix-shell
#! nix-shell -i python -p python python2Packages.lxml

import lxml.etree as et

#fname='780b91b0ef99cf032d5e73b2fa21c7f76f94fb98bc0a31d20bbdb9413c3f1c03-primary.xml'
fname='48986ce4583cd09825c6d437150314446f0f49fa1a1bd62dcfa1085295030fe9-primary.xml'
with open(fname) as f:
  tree=et.fromstring(f.read())

names = set(tree.xpath("//*[name()='package']/*[name()='name']/text()"))
prefix_len = lambda prefix,names : len(filter(lambda x:x.startswith(prefix),names))

print ("total=%s" % len(names))
print ("py2=%s" % prefix_len('python2-',names))
print ("py=%s" % prefix_len('python-',names))
print ("py3=%s" % prefix_len('python3-',names))

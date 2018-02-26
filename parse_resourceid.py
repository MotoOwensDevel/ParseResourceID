import xml.etree.ElementTree as ET
import os, fnmatch
def findReplace(find, replace):
    for path, dirs, files in os.walk(os.path.abspath("APK")):
        for filename in fnmatch.filter(files, "*.smali"):
            filepath = os.path.join(path, filename)
            with open(filepath) as f:
                s = f.read()
            s = s.replace(find, replace)
            with open(filepath, "w") as f:
                f.write(s)

e = ET.parse('public.xml').getroot()
arraycnt=0
boolcnt=0
integercnt=0
stringcnt=0
for public in e.iter('public'):
    if public.get('type') == 'array':
        if arraycnt==0:
            arraya = public.get('name')
        arraycnt+=1
    if public.get('type') == 'bool':
        if boolcnt==0:
            boola = public.get('name')
        boolcnt+=1
    if public.get('type') == 'integer':
        if integercnt==0:
            integera = public.get('name')
        integercnt+=1
    if public.get('type') == 'string':
        if stringcnt==0:
            stringa = public.get('name')
        stringcnt+=1

print(arraya,boola,integera,stringa)

f = ET.parse('public_resources.xml').getroot()
for pubres in f.iter('public'):
    if pubres.get('name') == arraya:
        arrayid = int(pubres.get('id'),16)
        break;
for pubres in f.iter('public'):
    if pubres.get('name') == boola:
        boolid = int(pubres.get('id'),16)
        break;
for pubres in f.iter('public'):
    if pubres.get('name') == integera:
        integerid = int(pubres.get('id'),16)
        break;
for pubres in f.iter('public'):
    if pubres.get('name') == stringa:
        stringid = int(pubres.get('id'),16)
        break;

for x in e.iter('public'):
    if x.get('type') == 'array':
        print(str(hex(int(x.get('id'),16))),str(hex(arrayid)))
        findReplace(str(hex(int(x.get('id'),16))),str(hex(arrayid)))
        arrayid+=1
    if x.get('type') == 'bool':
        print(str(hex(int(x.get('id'),16))),str(hex(boolid)))
        findReplace(str(hex(int(x.get('id'),16))),str(hex(boolid)))
        boolid+=1
    if x.get('type') == 'integer':
        print(str(hex(int(x.get('id'),16))),str(hex(integerid)))
        findReplace(str(hex(int(x.get('id'),16))),str(hex(integerid)))
        integerid+=1
    if x.get('type') == 'string':
        print(str(hex(int(x.get('id'),16))),str(hex(stringid)))
        findReplace(str(hex(int(x.get('id'),16))),str(hex(stringid)))
        stringid+=1

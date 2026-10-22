f=open('ademofile2.txt','w')
content=['apple\n','banana\n','grapes\n','ornage\n','mango\n']
f.writelines(content)
f.close()
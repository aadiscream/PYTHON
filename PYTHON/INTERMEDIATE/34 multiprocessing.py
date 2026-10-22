import multiprocessing
import requests
def download(url, name):
    response = requests.get(url)
    open(f"D:\\PROGRAMMING\\PYTHON\\png\\{name}.jpg","wb").write(response.content)
    
url = "https://picsum.photos/200/300"
process=[]
for i in range(11,16):
    # download(url,i)
    p=multiprocessing.Process(target=download, args=[url,i])
    p.start()
    process.append(p)
for i in process:
    p.join()
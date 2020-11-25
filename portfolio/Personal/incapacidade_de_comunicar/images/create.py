import os

total=0
for filename in os.listdir('./'):
    print(filename)
    if filename.split(".")[1] == "jpg":
        total+=1

f1 = open("list.txt","w")
i=0

for filename in os.listdir('./'):
    print(filename)
    if filename.split(".")[1] == "jpg":
        i+=1
        f1.write('<div class="mySlides fade" style="display: none;">  <div class="numbertext">'+str(i)+' / '+str(total)+'</div>  <img src="images/'+str(filename)+'" style="width:100%"></div>\n')
        
f1.close()
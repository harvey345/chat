chat=[]
# filename=input("請輸入變更檔名(需副檔名)：")
# with open(filename,'w',encoding='utf-8')as f:
#     f.write("")
def read_file(readfile,chat):
    with open(readfile,'r',encoding='utf-8-sig') as f:
        for line in f:
            chat.append(line.strip())

def change_file(chat):
    new=[]
    person=None
    for i in chat:
        if i=='Allen':
            person=i
            continue
        elif i=='Tom':
            person=i
            continue
        if person:
            new.append(person+':'+i+'\n')
    return new 

def write_file(writefile,newword):
    with open (writefile,'w',encoding='utf-8-sig')as f:
        for i in newword:
            f.write(str(i))
# print(chat)
# print(new)

def main():
    read_file('input.txt',chat)
    newword=change_file(chat)
    write_file('results.txt',newword)

main()
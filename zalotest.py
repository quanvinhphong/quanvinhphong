import donvihanhchinh
from gtts import gTTS
import playsound
import os
#import wikipedia
import donvihanhchinh
import vietnamese
import wikipediaapi

wiki_wiki = wikipediaapi.Wikipedia('vi')

def print_sections(diaphuong):
    page_py = wiki_wiki.page(diaphuong)
    if page_py.exists() == True:
        for s in page_py.sections:
            if s.title=='Hành chính':
                print(s.text)
    else:
        print("Không tìm thấy nội dung trên Wikipedia")







# *: History - Python was conceived in the late 1980s,
# *: Features and philosophy - Python is a multi-paradigm programming l
# *: Syntax and semantics - Python is meant to be an easily readable
# **: Indentation - Python uses whitespace indentation, rath
# **: Statements and control flow - Python's statements include (among other
# **: Expressions - Some Python expressions are similar to l

def tonghoptukhoa(diaphuong,keywords):
    for tinh in donvihanhchinh.vietnam:
        for huyen in tinh[1:]:
            for xa in huyen[1:]:
                if diaphuong == tinh or diaphuong == donvihanhchinh.vietnam or diaphuong == huyen or diaphuong == xa:
                    if type(xa)==str:
                        print(keywords+" "+(" - ".join((xa,huyen[0],tinh[0]))))
                    else:
                        for thon in xa[1:]:
                            print(keywords+" "+(" - ".join((thon,xa[0],huyen[0],tinh[0]))))
def danhsachquanhuyen(tinhthanh):
    quanhuyen = (", ".join(tinhthanh[i][0] for i in range(1, len(tinhthanh[1:]))))
    return quanhuyen

def danhsachphuongxa(huyen):
    phuongxa = (", ".join(xa for xa in huyen[1:]))
    return phuongxa

def capxa(tinh):
    print(f'{tinh[0]} co bao nhieu huyen, thi xa, thanh pho?')
    print(f'{tinh[0]} duoc chia thanh {len(tinh[1:])} don vi hanh chinh cap huyen, bao gom:{danhsachquanhuyen(tinh)}')
    for huyen in tinh[1:]:
        print(f'{huyen[0]} co bao nhieu xa, thi tran?')
        print(f'{huyen[0]} thuoc {tinh[0]}, duoc chia thanh {len(huyen[1:])} don vi hanh chinh cap xa, bao gom: {danhsachphuongxa(huyen)}')

def speak(text):
    print(text)
    output = gTTS(text, lang="vi", slow=False)
    output.save("output.mp3")
    playsound.playsound('output.mp3', True)
    os.remove("output.mp3")
"""
def tell_me_about(text):
    contents = wikipedia.page(text).content.split('\n')
    noidung=[]
    for content in contents:
        if "don vi hanh chinh cap huyen" in vietnamese.no_accent_vietnamese(content).lower():
            noidung.append(content)
        else:
            continue
    print(noidung[0])
"""


if __name__ == '__main__':
    #print(capxa(donvihanhchinh.tinhsoctrang))
    #print(danhsachphuongxa(donvihanhchinh.tinhsoctrang[3]))
    #print(danhsachquanhuyen(donvihanhchinh.tinhsoctrang))
    #speak(donvihanhchinh.tinhsoctrang[0])
    """
    for tinh in donvihanhchinh.vietnam:
        print(tinh[0])
        tell_me_about(tinh[0])
    """
    x="Thủ Đức"
    #print(wiki_wiki.page(x).exists())
    #print_sections(x)
    #print(page_py.summary)


    """
    import requests

    # the required first parameter of the 'get' method is the 'url':
    x = requests.get('https://dalat.lamdong.vn')

    # print the response text (the content of the requested file):
    print(x.text)
    """
    list1=[]
    list2=[]
    mylist=[]
    for a in range(1,26):
        for b in range(1, 26):
            for c in range(1, 26):
                for d in range(1, 26):
                    for e in range(1, 26):
                        if (a != b != c != d != e):
                            if (a+b+c+d+e)==65:
                                list1.append([a,b,c,d,e])

    for a in list1:
        for b in list1:
            for c in list1:
                for d in list1:
                    for e in list1:
                        if (a[0] + b[0] + c[0] + d[0] + e[0]) == 65 and (a[1] + b[1] + c[1] + d[1] + e[1]) == 65 and (a[2] + b[2] + c[2] + d[2] + e[2]) == 65 and (a[3] + b[3] + c[3] + d[3] + e[3]) == 65 and (a[4] + b[4] + c[4] + d[4] + e[4]) == 65 and (a[0] + b[1] + c[2] + d[3] + e[4]) == 65 and (a[4] + b[3] + c[2] + d[1] + e[0]) == 65:
                            if a[0] not in (b and c and d and e) and b[0] not in (a and c and d and e) and c[0] not in (a and b and d and e) and d[0] not in (a and b and c and e):
                                print([a,b,c,d,e])


    


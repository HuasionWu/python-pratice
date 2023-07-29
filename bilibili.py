import requests

headers = {
    # 假装自己是浏览器
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/73.0.3683.75 Chrome/73.0.3683.75 Safari/537.36',
    # 把你刚刚拿到的Cookie塞进来
    'Cookie': 'l=v; buvid3=CE10C7E8-707C-43E6-B9F9-46C40A3A48B134778infoc; LIVE_BUVID=AUTO2316200373281935; CURRENT_BLACKGAP=0; buvid_fp_plain=undefined; DedeUserID=10238107; DedeUserID__ckMd5=1565449f42db3a26; kfcSource=link; deviceFingerprint=90d36c5659dce5812078166b762b034e; msource=pc_web; blackside_state=0; i-wanna-go-back=-1; is-2022-channel=1;',
}

session = requests.Session()
response = session.get('https://bibi.com', headers=headers)

print(response.text)
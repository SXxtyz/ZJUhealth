# coding=utf-8

import smtplib
from copy import deepcopy
from email.mime.text import MIMEText
from clock import ERROR_STATE, clock, SUCCESS
import json
import os
import time


def sendmail(state, sender, receiver, host, port, pwd, err_msg):
    if state != SUCCESS:
        body = f"<h4>打卡失败, {ERROR_STATE[state]}</h4>"
        msg = MIMEText(body, 'html')
        msg['subject'] = "打卡失败提醒\n\n" + err_msg
    else:
        body = "<h4>打卡成功</h4>"
        msg = MIMEText(body, 'html')
        msg['subject'] = "打卡成功提醒"
    msg['from'] = sender
    msg['to'] = receiver
    s = smtplib.SMTP_SSL(host, port)
    s.login(sender, pwd)
    s.sendmail(sender, receiver, msg.as_string())


def run():
    file_path = os.path.abspath(__file__)
    file_path = os.path.dirname(file_path) + '/config.json'
    config = json.load(open(file_path, 'r', encoding='utf-8'))
    log_path = os.path.dirname(file_path) + '/log.log'
    mode = 'a'
    with open(log_path, 'r', encoding='utf-8') as fp:
        if len(fp.readlines()) >= 2000:
            mode = 'w'
    with open(log_path, mode, encoding='utf-8') as fp:
        for usr, cfg in config.items():
            alive = cfg.get('alive')
            if not alive:
                continue
            url = cfg.get('uri')
            user_cfg = deepcopy(cfg)
            return_state, err_msg = clock(url, user_cfg)
            now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
            msg = err_msg or 'sucess'
            log = usr + "\t" + now + "\t" + msg + "\n"
            fp.write(log)
            send_mail = cfg.get('send_mail')
            if send_mail:
                sender = cfg.get('sender')
                receiver = cfg.get('receiver')
                host = cfg.get('host')
                port = cfg.get('port')
                pwd = cfg.get('mail_pwd')
                sendmail(return_state, sender, receiver, host, port, pwd, err_msg)


if __name__ == '__main__':
    run()

# -*-coding=utf-8-*-
# @Author Nicholas
# @Function 提交URL 可以选择 提交url时间 提交url的数量 提交url的格式 不一样的Token 提交失败的要输出日志
# @Function 检测网站是否添加到百度里面
import subprocess
import logging
import datetime
from random import sample
import time
import os
# 参数定义
# ————————————
post_url_path = 'url/token.txt'                 # 推送哪些url
# ————————————
# ————————————
logger = logging.getLogger(__name__)            # 日志配置
logger.setLevel(logging.INFO)
handler = logging.FileHandler('log/my_log.log', encoding='utf-8')
handler.setLevel(logging.INFO)
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
ch.setFormatter(formatter)
logger.addHandler(handler)
logger.addFilter(ch)

# ————————————


# 生成额定数量需要推送的url
def rand_char():
    char = 'qwertyuiopasdfghjklzxcvbnm1234567890'
    return ''.join(sample(char, 5))


def create_post_url():
    head = open('url/head.txt', 'r')
    for line in head:
        urls = open(post_url_path, "r")
        for temp in urls:
            url = temp.split(' ')[0].replace('www', line.strip())
            print(url)
            post_token = temp.split(' ')[1]
            num = 0
            now_time = datetime.datetime.now().strftime('%Y%m%d')  # 现在
            post_url = open('url/cache/' + post_url_path[4:], 'w+')
            while num < 1000:
                index = open('url/index.txt', "r+")
                for index_path in index:
                    value = rand_char()
                    target_url = 'http://' + url.strip('\n') + '/' + index_path.strip('\n') + \
                                 now_time + value + '.html\n'
                    post_url.write(target_url)
                    num += 1
                    if num == 1000:
                        index.close()
                        break
                index.close()
            post_all_url(post_token)
            time.sleep(2)
        urls.close()


# # 推送url到神马
def post_all_url(token):
    temp = 1
    while True:
        path = 'url/cache/' + post_url_path[4:]
        urls = open(path, 'r')
        url = urls.readline().split('/')[2]
        post = 'curl "http://data.zhanzhang.sm.cn/push?site=' + url + \
               '&user_name=914081010@qq.com&resource_name=mip_add&token=' + token.strip() + '" --data-binary @' + path
        output = subprocess.Popen(post, shell=True, stdout=subprocess.PIPE)
        out, err = output.communicate()
        try:
            if out.splitlines()[2] == b'  200':
                print('提交成功 post = ' + url)
                logger.info('提交成功 post = ' + url)
                break
            elif temp == 3:
                print('提交失败 post = ' + url)
                logger.error('提交失败 post = ' + url)
                break
            else:
                temp += 1
                for line in out.splitlines():
                    print(line)
                print('提交失败重试！')
                logger.debug('提交失败重试！')
                time.sleep(5)
        except IndexError as e:
            logger.debug(e)
            time.sleep(3)


def main():
    if os.path.exists('url/cache/') is not True:
        os.mkdir('url/cache')
    while True:
        today = datetime.datetime.now().strftime('%Y%m%d')
        create_post_url()
        print('to do %s' % today)
        while True:
            time.sleep(1)
            print('1 sec')
            tomorrow = datetime.datetime.now().strftime('%Y%m%d')
            if today != tomorrow:
                break


if __name__ == '__main__':
    main()



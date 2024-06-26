# encoding:utf-8
from common.douyu_request import dyreq
from common.logger import logger
import requests
from common.get_secrets import get_secrets


Is_login = 0
login_url = "/wgapi/livenc/liveweb/follow/list"


def is_login():
    """
    :return:返回登陆结果,用于主程序判断
    """
    global Is_login
    login = dyreq.request("get", login_url).json()
    if login['error'] == 0:
        Is_login = 1
        logger.debug("Cookie有效,登陆成功")
    else:
        logger.warning("登陆失败,请检查Cookie有效性")
        # check if get_secrets('BARKURL') starts with http
        barkurl = get_secrets('BARKURL')
        if barkurl.startswith('http'):
            requests.get(barkurl + "/斗鱼+Cookie+失效/登陆失败,请检查Cookie有效性")
        logger.warning("Notification Sent")

    return Is_login


if __name__ == '__main__':
    is_login()

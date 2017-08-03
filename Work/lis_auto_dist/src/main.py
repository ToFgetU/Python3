#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: PanFei Liu

import zipfile
import os, time
from conf import settings
from src import release_by_lis as rel

home_path = '/home/weblogic/lis_auto_dist/app'
app_path = '/app/lis'
def start(home_path):
    """input your fileanme by zip"""
    n_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
    filename = input("请输入要上传的文件名: ").strip()
    settings.logger.debug("输入的文件名：%s" % filename)
    file_path = os.path.join(home_path, filename)
    bak_path = os.path.join(home_path, filename + str(n_time))
    print(filename)
    if os.path.exists(file_path):
        file_zip = zipfile.ZipFile(file_path, 'r')
        for file in file_zip.namelist():
            file_zip.extract(file, home_path)
        file_zip.close()
        os.popen("mv %s %s" % (file_path, bak_path))
    else:
        settings.logger.error("输入的文件不存在")
        settings.logger.error("退出程序")
        exit("退出程序")

def file_list_to_upload(home_path, transport, ssh):
    """if dir is not exties, create the dir and upload the files, else only upload the files"""
    if os.path.exists("%s/ui" % home_path):
        file_list = os.walk("%s/ui" % home_path)
        for path, dir, filelist in file_list:
            for dirname in dir:
                s_dir = os.path.join(path, dirname)
                print(s_dir)
                t_dir = '/'.join(s_dir.split('/')[6:])
                dest_dir = os.path.join(app_path, t_dir)
                print(dest_dir)
                if os.path.exists(dest_dir):
                    pass
                else:
                    cmd = "mkdir -pv %s" % dest_dir
                    rel.exec(cmd)
            for file in filelist:
                s_file = os.path.join(path, file)
                print(s_file)
                t_file = '/'.join(s_file.split('/')[6:])
                dest_file = os.path.join(app_path, t_file)
                print(dest_file)
                rel.upload(transport, s_file, dest_file)
                # settings.logger.debug(os.path.join(path, file))

def run():
    settings.logger.debug("统一部署脚本启动".center(100, "#"))
    start(home_path)
    for hostname in settings.HOST:
        print(hostname)
        try:
            ssh = rel.ssh_conn(hostname)
            transport = rel.sftp_conn(hostname)
            file_list_to_upload(home_path, transport, ssh)
            transport.close()
        except Exception as e:
            settings.logger.error("%s 服务器连接失败：%s".center(60, '=') % (hostname, e))
    os.system("rm -rf %s/ui" % home_path)
    print("ui文件夹已删除")
    settings.logger.debug("统一部署脚本结束".center(100, "#"))



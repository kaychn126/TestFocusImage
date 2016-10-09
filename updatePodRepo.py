#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' Update pod repo and generate .framework use cocoapod-packager '

import os,sys,re,shutil

#获取脚本所在文件夹
def cur_file_dir():
    path = sys.path[0]
    if os.path.isdir(path):
        return path
    elif os.path.isfile(path):
        return os.path.dirname(path)

#替换行
def replace_text(src, des, file):
    with open(file, 'r') as f:
        with open(file+'.new', 'w') as g:
            for line in f.readlines():
                if src not in line:
                    g.write(line)
                else:
                    g.write(des)
        g.close()
    f.close()
    shutil.move(file+'.new', file)

#从文件file中获取包含string字符的行
def get_line(string, file):
    with open(file, 'r') as f:
        for line in f.readlines():
            if string in line:
                return line

#版本号加1,入参为包含版本号的一行字符串
def add_version_number(versionLine):
    verlist = versionLine[versionLine.index('"')+1:-2].split('.')
    addedverint = int(verlist[len(verlist)-1]) + 1
    verlist[len(verlist)-1] = str(addedverint)
    return '.'.join(verlist)

#检查是否有framework文件夹
def check_framework_dir():
    for lists in os.listdir(cur_file_dir()):
        path = os.path.join(cur_file_dir(), lists)
        if os.path.isdir(path):
            sublist = os.listdir(path)
            if "ios" in sublist:
                if "build" in sublist:
                    return path
    return ""

#删除framework文件夹和spec文件
def delete_framework_files():
    framework_dir = check_framework_dir()
    if len(framework_dir) > 0:
        shutil.rmtree(framework_dir)
    framework_spec_file = get_spec_file(cur_file_dir(), "-framework.podspec")
    if len(framework_spec_file) > 0:
        os.remove(framework_spec_file)

#文件名中包含特定字符的文件
def get_spec_file(dir, spec):
    filelist = []
    for lists in os.listdir(dir):
        path = os.path.join(dir, lists)
        if os.path.isfile(path):
            if(os.path.basename(path).find(spec)>=0):
                filelist.append(path)
    return filelist

#获取pod名字
def get_pod_name():
    filelist = get_spec_file(cur_file_dir(), ".podspec")
    for filename in filelist:
        if "-framework" not in filename:
            return os.path.basename(os.path.splitext(filename)[0])
    return ""

#更新git添加tag
def git_update_with_tag(tag):
    os.system('git add *')
    os.system('git commit -m "pod update"')
    os.system('git pull')
    os.system('git push origin master')
    os.system('git tag ' + tag)
    res = os.system('git push origin --tags')
    print('git_update_with_tag 返回值' + res)
    return res

def pod_update(podname):
    repo_push = 'pod repo push EZBSpecs ' + podname + '.podspec ' + '--sources=https://github.com/CocoaPods/Specs.git,https://git.coding.net/cker/EZBSpecs.git --allow-warnings --verbose'
    res = os.system(repo_push)
    print('pod_update 返回值' + res)
    return res

#打包framework
def pod_package(file):
    commond = "pod package " + file
    res = os.system(commond)
    print('pod_package 返回值' + res)
    return res


def main():
    #删除framework文件
    delete_framework_files()
    #获取pod_name
    pod_name = get_pod_name()
    #.podspec文件名
    pod_spec_file_name = pod_name + ".podspec"
    #版本号加1
    new_version_number = add_version_number(get_line("s.version", pod_spec_file_name))
    new_version_number_line = '  s.version      =  "' + new_version_number + '"\n'
    replace_text(get_line("s.version", pod_spec_file_name), new_version_number_line, pod_spec_file_name)

    #提交git,打tag
    git_update_with_tag(new_version_number)

    #更新pod
    pod_update(pod_name)

    # pod_framework_name = pod_name + "-framework"
    # pod_framework_spec_file_name = pod_framework_name + ".podspec"

    # pod_package("EZBSGFocusImage.podspec")
    # framework_dir = check_framework_dir()
    # if len(framework_dir) > 0:
    #     os.rename(framework_dir, "EZBSGFocusImage-framework")
    #
    # framework_spec_file = get_spec_file(cur_file_dir()+"/EZBSGFocusImage-framework", ".podspec")
    # framework_spec_file_new = os.path.splitext(framework_spec_file)[0] + "-framework.podspec"
    # os.rename(framework_spec_file, framework_spec_file_new)
    # shutil.move(framework_spec_file_new, cur_file_dir())


main()

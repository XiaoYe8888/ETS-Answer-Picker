#By:XiaoYe
#2026_2_4
#ETS-Auto-Analyze
#eaa
import re
def eaa(content):
    if "collector.read" in content:
        return
    th_list=[]
    aw_list=[]
    zsaw=''
    a = 0
    b = 0
    flag=0
    while a < len(content):
        c1 = content[a:a+7] if a + 7 <= len(content) else ''  # 避免索引越界
        th=''
        ######选择题######
        if c1 == 'xt_nr":':
            th = content[a + 8:a + 10]  # 取出题号
            th=th.replace('.','')
            a += 10
            while a<len(content):  # 这个循环是取出答案
                c1 = str(content[a:a + 8])
                if c1 == 'answer":':
                    a += 9
                    aw = content[a:a + 1]
                    th_list.append(th)
                    aw_list.append(aw)
                    break
                a += 1
        ######选择题结束######

        ######其他题型######
        elif c1 == '"std":[':
            a += 8
            # 循环处理 std 数组内的对象：
            # - role 题型:一个 std 数组只有第一个 value 是答案,题号来自 ask,处理一个即止
            # - fill 题型:每个 std 对象带 "th" 字段(题号),一个对象一道题,需全部处理
            # - 转述:std 内无 ask/th,提取文本后触发 zsaw 分支
            while True:
                if flag == 1:
                    break
                # 在 std 数组内定位下一个 "value":(兼容 value 前有 xth 等字段),遇到 "ref" 说明已离开 std 数组
                while a + 7 <= len(content):
                    if content[a:a+7] == '"value"':
                        break
                    if content[a:a+5] == '"ref"':
                        break
                    a += 1
                if a + 7 > len(content) or content[a:a+7] != '"value"':
                    break  # 已离开 std 数组
                a += 9
                b = 0
                aw = ''
                th = ''
                th_from_th = False
                # 提取答案内容(直到遇到引号),提取后去掉末尾句号
                while a+b<len(content):
                    if flag==1:
                        break
                    if content[a + b] != '"' or content[a+b-1]=="\\":
                        aw+=content[a + b]
                        b+=1
                    else:
                        # 找到后寻找题号
                        found_th = False
                        # 先向后搜索 ask/th；若中途遇到下一个题目的 "std":[，
                        # 说明当前题目的 ask 在 std 之前，回退一位并停止向后搜索
                        while a+b<len(content):
                            if str(content[a+b:a+b+5]) == 'ask":':
                                # 题号 = ask 值中的第一个数字(兼容"请你准备第一个问题。</br>1. ..."等格式)
                                th = ''
                                pos2 = a + b + 6
                                while pos2 < len(content) and not content[pos2].isdigit():
                                    pos2 += 1
                                while pos2 < len(content) and content[pos2].isdigit():
                                    th += content[pos2]
                                    pos2 += 1
                                found_th = True
                                break
                            elif str(content[a+b:a+b+4]) == 'th":':
                                th = str(content[a+b+5:a+b+7])
                                th_from_th = True
                                found_th = True
                                break
                            elif str(content[a+b:a+b+7]) == '"std":[':
                                # 越过当前题目边界：ask 在 std 之前
                                b -= 1  # 回退一位，避免跳过下一个题目的 "std":[
                                break
                            elif str(content[a+b:a+b+5]) == '"xh":' or str(content[a+b:a+b+6]) == '"xth":':
                                # 已进入下一个题目对象(ask 在 std 之前的结构)：停止向后，向前找当前题目自己的 ask
                                break
                            b += 1
                        if not found_th:
                            # 向后没找到(越过题目边界或已到字符串末尾)：
                            # 本题目 ask 在 std 之前，向前找最近的 ask(属于当前题目)
                            pos = a - 1
                            while pos > 0:
                                if str(content[pos:pos+5]) == 'ask":':
                                    # 题号 = ask 值中的第一个数字(兼容"请你准备第一个问题。</br>1. ..."等格式)
                                    th = ''
                                    pos2 = pos + 6
                                    while pos2 < len(content) and not content[pos2].isdigit():
                                        pos2 += 1
                                    while pos2 < len(content) and content[pos2].isdigit():
                                        th += content[pos2]
                                        pos2 += 1
                                    found_th = True
                                    break
                                pos -= 1
                        if not found_th:
                            zsaw+=re.sub(r'<[^>]*>', '', aw)
                            flag=1
                        if found_th:
                            th_list.append(th)
                            aw_list.append(re.sub(r'<[^>]*>', '', aw).rstrip('.'))
                            a += b  # 移动主指针
                        break  # 无论是否找到都退出内层循环
                if not th_from_th:
                    break  # role 题型:只取 std 数组第一个 value 作为答案
        ######其他题型结束######
        a += 1
    if zsaw!='':
        return zsaw
    else:
        return th_list,aw_list
if __name__ == '__main__':
    while True:
      test=input("输入content2.json:")
      print(eaa(test))
#E听说答案提取器
#ETS-Answer-Picker
#By:xiaoye
#最后修改:2026_2_2

import flet as ft
import zipfile
import os
import shutil
import eaa

#TODO:修改窗口标题
def main(page):
    #窗口居中
    page.window.left = (page.window.width-600)/2
    page.window.top = (page.window.height-450)/2
    #窗口大小
    page.window.width = 600
    page.window.height = 450
    page.theme = ft.Theme(font_family="Microsoft YaHei")#微软雅黑字体


    ######文件选择######
    async def pickfile():#选择文件函数
        global filepath
        file = await ft.FilePicker().pick_files(#文件选择器，把结果赋给file
            allowed_extensions=["zip"],#限制类型
            allow_multiple=False)#限制单个
        if file:#已选择
            filepath=file[0].path#修改变量的值为文件位置
            path_text.value="已选择:"+file[0].path#改文字内容
    ######文件选择######

    ######答案提取######
    def pick():
        if path_text.value=="未选择压缩包":#如果没选择压缩包
            return#返回

        dir=os.path.dirname(filepath)+r"\temp"
        os.makedirs(dir,exist_ok=True)#创建缓存目录
        with zipfile.ZipFile(filepath, 'r') as zf:#打开文件
            zf.extractall(dir)#解压

        dirs=os.listdir(dir)#所有文件夹的列表
        result={}#结果字典
        zsaw=""#转述答案

        for i in range(len(dirs)):#遍历 所有题目文件夹
            files=os.listdir(dir+r"\\"+dirs[i])#题目里的文件列表
            if "content2.json" in files:#判断是否有content2
                content2=open(dir+r"\\"+dirs[i]+r"\\"+"content2.json","r",encoding="utf-8")#打开content2.json
                answer=eaa.eaa(content2.read())#提取答案

                if isinstance(answer,tuple):#答案是元组
                    th=answer[0]#题号列表为元组的第1项
                    aw=answer[1]#答案列表
                    for i in range(len(th)):
                        result[th[i]]=aw[i]#把题号和答案添加到结果字典
                if isinstance(answer,str):#答案是字符串(只有听后转述的返回值是字符串)
                    zsaw=answer#转述答案
                content2.close()#关闭文件

        result=dict(sorted(result.items(),key=lambda x: int(x[0])))#结果字典 排序
        count=1
        answer_text.value = ""#先清空答案显示区

        for i in result.keys():#遍历结果的键(题号)
            if count%2==0:#为偶数
                answer_text.value+=i+'.'+result[i]
                answer_text.value+="\n"#换行
            else:
                answer_text.value+=i+'.'+result[i]+'  '
            count+=1

        answer_text.value=answer_text.value.replace("\\","")#去掉反斜杠
        zsaw=zsaw.replace(". ",".\n")#转述答案换行
        answer_text.value+='\n'+"听后转述:\n"+zsaw
        shutil.rmtree(dir)#删除这个缓存目录和所有缓存文件
    ######答案提取######

    def html():
        if copy_box.value:#已勾选
            answer_text.value=answer_text.value.replace("\n","<br>\n")#换行前加<br>
            answer_text.value = "<p>\n" + answer_text.value + "\n</p>"#开头结尾<p>标签
        else:#取消勾选
            answer_text.value = answer_text.value.replace("<br>\n", "\n")#去掉<br>
            answer_text.value = answer_text.value.replace("<p>\n", "")#去掉开头的<p>
            answer_text.value = answer_text.value.replace("\n</p>", "")#去掉结尾的</p>


    async def copy():
        await ft.Clipboard().set(answer_text.value)#设置剪切板内容

    def about():
        answer_text.value=("一个使用python flet开发的E听说答案提取软件\n"
                           "本软件完全开源免费，有且仅有以下两个渠道可以下载源码和软件\n"
                           "Github:https://github.com/XiaoYe8888/ETS-Answer-Picker\n"
                           "Gitee:https://gitee.com/XiaoYe_furry/ETS-Answer-Picker\n"
                           "License:CC BY-NC-SA 4.0\n"
                           "协议:知识共享 署名-非商业性使用-相同方式共享 4.0\n"
                           "使用教程请查看仓库里的readme\n"
                           "By:XiaoYe\nE-mail:yiewei123@163.com\nVersion:1.0")

    page.add(#添加控件到页面

        ft.Row(#第一行 三个按钮
            controls=[
                ft.Button("选择压缩包",
                    icon=ft.Icons.UPLOAD_FILE,#上传文件的图标
                    scale=1.2,#大小
                    on_click=pickfile),#点击后调用pickfile
                ft.Button("提取",scale=1.2,on_click=pick),
                ft.Button("关于",scale=1.2,on_click=about)],
            spacing=70,#间距70px
            alignment=ft.MainAxisAlignment.CENTER),#居中

        ft.Row(
            ft.Container(
                path_text:=ft.Text("未选择压缩包"),
                margin=ft.Margin.only(left=15))),#左侧15px间距

        ft.Column(ft.Divider()),#分割线

        ft.Row(
            controls=[
                ft.Container(
                    ft.ListView([#带滚动条的容器
                        answer_text:=ft.Text(
                            "(≧∇≦)ﾉ",
                            selectable=True)],#可选
                        auto_scroll=False),#关闭自动滚动
                    width=430,
                    height=290,
                    border=ft.Border.all(1, ft.Colors.GREY),#边框和颜色
                    padding=5),
                ft.Column(
                    controls=[
                        copy_box:=ft.Checkbox(label="HTML格式",on_change=html),#复选框
                        ft.Button("复制",icon=ft.Icons.COPY,on_click=copy)#复制按钮
                    ],
                    alignment=ft.MainAxisAlignment.START,#排到顶部
                    height=290#高度
                )
            ]
        )
    )
ft.run(main)#运行
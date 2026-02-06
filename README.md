# E听说答案提取器

---

一个基于 python flet 开发的 E听说 答案提取工具
**简洁、轻量、易用、美观**

![License](https://img.shields.io/badge/License-CC%20BY--NC--SA%204.0-767676.svg?logo=creativecommons) ![Python](https://img.shields.io/badge/Python-3.8+-3776ab.svg?logo=python) ![Flet](https://img.shields.io/badge/Flet-0.80+-ff005f.svg?logo=https%3A%2F%2Fflet.dev%2Fimg%2Flogo.svg)

**如果本工具对你有帮助，可以给我点一个⭐Star吗，非常感谢🙏**

## ✨ 作者

By:**小叶**

![抖音](https://img.shields.io/badge/抖音-小叶搞摄影-000000.svg?logo=tiktok&link=https://www.douyin.com/user/MS4wLjABAAAAIKRSE3HR19AJYvgZ4eCHPO3clYY9HYE-5apqa5n-A8ggoSeLgQ9QNntD0PRSFp_g)
![Bilibili](https://img.shields.io/badge/Bilibili-小叶搞摄影-00a1d6.svg?logo=bilibili&link=https://space.bilibili.com/2050229996)

## 📋使用教程

1. 打开手机端的E听说中学，点击“我的”，点击“清除缓存”

2. 点击进入你需要提取答案的听说作业，等待下载完成

3. 在你经常使用的文件管理工具(推荐使用`MT管理器`)
   打开`Android/data/com.ets100.secondary/files/Download/ETS_SECONDARY/resource/`

4. 把该路径下除`common`以外的所有文件夹全部压缩为zip，并发送到电脑

5. 打开`E听说答案提取器`，点击“选择压缩包”，选择刚刚那个压缩包，点击提取即可

## 🎯 支持题型

目前支持以下4类题型：

- 听后选择
- 听后回答
- 听后记录
- 听后转述

不支持的题型你可以按下面的方法提交给我，我会抽时间更新

## 🐞提交建议和反馈

### 问题/建议提交

如果遇到 Bug、需要新增题型，或有功能优化建议，可通过以下方式反馈： 

1. GitHub/Gitee 提交 Issues（优先推荐）
2. 邮箱联系：yiewei123@163.com

### 反馈要求

- 提交暂不支持的题型：请附带作业文件的 ZIP 压缩包 + 题型描述；
- 提交Bug/建议：请详细描述问题现象、复现步骤（Bug）或具体优化思路（建议）。

## 🛠️依赖

| 依赖库     | 版本要求   | 说明       |
| ------- | ------ | -------- |
| flet    | ≥ 0.80 | 界面开发核心框架 |
| zipfile | 内置     | ZIP 文件解压 |
| os      | 内置     | 文件操作     |
| shutil  | 内置     | 文件删除     |

## 📦源代码打包

在打包源代码前你需要先安装`flet-cli`和`PyInsTaller`

```bash
pip install flet-cli
pip install pyinstaller
```

进入项目的 src 目录；
打开 PowerShell/CMD，执行打包命令：

```bash
flet pack main.py -i ./assets/icon.ico
```

打包完成后，可在 dist 目录下找到 main.exe，可直接移动到任意目录使用。

不推荐使用`flet build windows`打包
因为它依赖 Flutter 和 Microsoft Visual Studio，打包耗时久、失败率高，需配置镜像 / 代理

## 📄 许可证

本项目采用 CC BY-NC-SA 4.0 许可协议。
这意味着您可以自由分享和改编本作品，但必须：

- 保留原作者署名
- 不得用于商业用途
- 基于本作品的衍生作品需采用相同许可协议

# SA-1B-Downloader
简体中文 | [English](./README_EN.md)

此脚本可以从opendatalab.com方便地下载SA-1B数据集。

优势：
- 连续下载无人自动化
- 方便多人分工，合作下载

## 环境配置
`pip install requests wget`

## 下载
- 将`sa_download.py`放在你想存放数据集文件的存放目录中，注意保证有足够的磁盘空间
- 在浏览器中打开[OpenDataLab网站](https://opendatalab.com/SA-1B/download)，并注册登录。
- 按F12打开开发者面板，点进“网络”（Network），在网页底部随意进行一次页面跳转查看请求头，复制其中的`cookie`项和`user-agent`项到代码文件对应行。可以参照下图操作。
- 依照分工，确定自己所需要下载的页数（默认每页10行，与网页显示相同），并在代码中填入`START_PAGE_NO`和`END_PAGE_NO`。页数起始索引为1，下载时包含起止页。
- 在存放目录中运行`python sa_download.py`。

![2](https://user-images.githubusercontent.com/34768678/234220708-cadba2f4-bcbd-4bf9-a3f0-5dc7ee2208fe.png)


## 成功运行示例

![1](https://user-images.githubusercontent.com/34768678/234219130-d68ef830-ee07-4a3d-8a5a-909a30efd0d3.png)

## 致谢

感谢OpenDataLab公开的数据集，以及ChatGPT在脚本方面提供的帮助。

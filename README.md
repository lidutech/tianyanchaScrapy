# tianyanchaScrapy

#### 项目介绍
天眼查( https://www.tianyancha.com/ ) 公司信息采集

#### 界面预览  
![tyc_list](https://github.com/TonyK-T/github_images/blob/master/tycAndQcc/tyc_list.png)
![tyc_info_title](https://github.com/TonyK-T/github_images/blob/master/tycAndQcc/tyc_info_title.png)
![tyc_info_detail](https://github.com/TonyK-T/github_images/blob/master/tycAndQcc/tyc_info_detail.png)

#### 执行过程
![tyc_run](https://github.com/TonyK-T/github_images/blob/master/tycAndQcc/tyc_run.png)

#### 执行结果
![tyc_data](https://github.com/TonyK-T/github_images/blob/master/tycAndQcc/tyc_data.png)

#### 软件架构
软件架构说明  
1、Scrapy + Scrapy-redis 分布式爬取  
2、bloomfilter 过滤、redis sadd去重  
3、数据入mysql(sqlalchemy) ，数据入mongodb(motor异步)  
4、User-Agent代理，IP代理，cookies登录态  
5、scrapyd-client打包  
6、gerapy 爬虫管理平台   

#### 安装教程
安装Python库    
安装redis    
安装mysql，mongodb    
搭建gerapy环境 - 略    

#### 懒人专享 一键docker
安装使用说明后续补上    

#### 使用说明
1、纯脚本运行：Python run.py    
2、gerapy 爬虫管理平台： 部署、启动停止删除爬虫 -略    

#### gerapy管理平台
![tyc_gerapy_1](https://github.com/TonyK-T/github_images/blob/master/tycAndQcc/tyc_gerapy_1.png)
![tyc_gerapy_2](https://github.com/TonyK-T/github_images/blob/master/tycAndQcc/tyc_gerapy_2.png)

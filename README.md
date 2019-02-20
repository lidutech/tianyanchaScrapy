# tianyanchaScrapy

#### 项目介绍
天眼查 公司信息采集

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
搭建gerapy环境

#### 使用说明
1、纯脚本运行：Python run.py
2、gerapy 爬虫管理平台： 部署、启动停止删除爬虫 -略


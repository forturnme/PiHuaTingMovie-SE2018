# 关于项目--皮划艇电影
![皮划艇电影](footage.png)
此项目为2018秋软件工程17组的课程项目。项目实现了一个简单的电影票房数据可视化系统，基于[Flask](http://flask.pocoo.org)、[jQuery](https://jquery.com)、[Materialize-UI](http://www.materializecss.cn/about.html)和[MySQL](https://www.mysql.com)构建，同时使用到了以下Python库：[PyMySQL](https://pypi.org/project/PyMySQL/)、[SQLAlchemy](https://www.sqlalchemy.org)、[Scrapy](https://scrapy.org/)、[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)、[Pandas](http://pandas.pydata.org)，以及以下Javascript库：[WordExport](https://github.com/Kent-Su/jquerty-wordExport)。项目演示时所用的数据来自[电影票房](http://58921.com)和[猫眼专业版](https://piaofang.maoyan.com/dashboard)。请遵循以上各自的使用条款，勿将此项目作为商业用途。

# 此发布版本的改进
相对于此前在课上演示的版本，此发布版本有以下改进：
* 改进了生成报表界面`生成报表`和`强制刷新`两个按钮的观感：
	* 现在它们是真正的按钮了，且带有点击效果
* 在送出的请求里加上了`Keep-Alive`，同时改进了服务器端访问数据库的方式：
	* 现在响应速度更快且更稳定
* 进一步改进了自适应显示机制，改善了页面在窄屏幕（主要是手机等移动设备）上的使用体验：

![窄页面排版示意](footage-mobile.png)

爬虫部分相对于此部分被检查时有了如下改进：
* 增加一个爬取猫眼专业版每日票房的爬虫

# 运行环境需求
对OS没有硬性要求。
### 1. 服务器端：
Python 3.7以及以下Python库：Flask、PyMySQL、SQLAlchemy、Pandas；
任意一个稳定的Web服务器（如Nginx或Apache）。

### 2. 爬虫：
需要记住登录Cookie，不一定需要运行于服务器端。
Python 3.7以及以下库：Scrapy、SQLAlchemy、PyMySQL、Pandas、BeautifulSoup。

### 3. 网页端：
支持除IE外的任何主流浏览器。


# 各部分功能简介
### 1. 爬虫
该套爬虫提供的特性：
* 可以在系统在线时更新数据
* 可以增量更新（电影元信息爬虫）

爬虫执行时的需求：
* （对于58921）需要登录了账号的有效Cookie：对此我们提供了转化工具

### 2. 查询服务器
* 基于`Flask`编写
* 使用`SQLAlchemy`连接数据库
* 使用`Pandas`做中间运算处理
* 解析请求并访问数据库

### 3. 登录/注册服务
* 基于`Socket`编写
* 服务器存储明文用户名和MD5密码
* 登录时密码的传递采用“加盐”方法
* 只有登录后才能访问“生成报表”功能

### 4. 网页端
* 基于`Materialize-UI`和`JQuery`
* 单页式应用（SPA）
* 根据页面宽度改变布局（见前面图片）
* 使用`ECharts`图表，每个图表支持单独的“另存为图片”功能

### 5. 生成报表
* 使用`WordExport`
* 生成为Word
* 唯一需登录的功能，登陆后径直去向此功能
* “所见即所得”

![Word报表](footage-report.png)

# 部署到您的服务器
### 1. Web端
待补充，大致就是把整个网页目录放进您的Web服务器（`Nginx`或者`Apache`等）的页面根目录下覆盖即可，首页设为`index.html`

### 2. 服务器
准备脚本中，待补充
脚本需要替换现有的服务器地址，数据库名，用户，密码等

### 3. 爬虫
准备脚本中，待补充
脚本需要替换现有数据库地址，用户，密码，库名等
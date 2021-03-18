# django_datafactory数据工厂django项目

* ` _init__.py`:项目的初始化文件 有了这个文件 标志当前文件夹是一个包,可以被引用
* `settings.py`:所有的django的配置信息都在这里面,包括数据库的配置,静态文件的配置,还有django依赖的第三方扩展包
* `urls.py`:路由分发器，配置每个页面的路径
* `wsgi.py`:是一个服务器的启动文件,项目上线需要用到他
* `manage.py`:他是整个Django项目的启动文件
* `models.py`:写和数据库项目的内容
* `view.py` 接受请求，进行处理，与M和T 进行交互，返回答应  定义处理函数（即视图函数）
* `admin.py` 网站的后代管理相关的文件



#### 启动项目：

1. 拉取代码

2.下载需要的项目运行必须的包
  打开requirements.txt 文件，检查包是否存在
  如果已经有了跳过该步骤
  下载包--terminal执行命令：pip install -r requirements.txt
  

3. 修改配置(修改后一定不要提交修改后的文件)：
    
    3.1修改**django_datafactory/settings.py**文件的**DATABASES**服务器地址：
    
        取消注释'HOST': '120.0.0.0'
    
        注释'HOST': "10.0.0.0"
    
    3.2修改**views.py** 文件create_data方法的返回路径: 
        
        跳转本地服务地址：HOST = get_host_ip()
        
        跳转远程服务器地址：SERVER_HOST = "120.0.0.0"

4. 启动本地服务：终端terminal 输入命令：

    默认本地启动：python manage.py runserver 
    
    服务器启动： python manage.py  runserver  0:8000（可以使用局域网+端口号访问）
 


5. 浏览器访问：

   工具页：127.0.0.1:8088

   创建工具页：127.0.0.1:8088/admin  


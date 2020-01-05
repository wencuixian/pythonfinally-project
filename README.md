# python期末考试项目
***

### 项目名称：世界少儿抚养比与GDP的关系
### 项目成员：17级黄舒婷             18级闻翠娴
### 项目需求：实现交互功能和部署pythonanywhere

******

### [github链接](https://github.com/wencuixian/python_finallyproject)
### [pythonanywhere链接](http://wcx1999.pythonanywhere.com/) 

******

### 三个文档的描述

##### Web App动作描述：

* "/": 响应GET请求，返回 flask.csv 文件内容数据并在界面展示

* "/hurun": 响应POST请求，首先读取 GDP.csv 文件内容数据并将GDP.csv内容数据以 Map 类型将世界各国GDP数据作为结果返回界面；
	                        以及读取 select_nation.csv 文件内容数据并将数据 根据响应列转化为饼状图、折线图、水平柱状图 返回界面；
	                        
##### python档描述：

* 通过flask "/"路由，指定GET请求方法，读取flask.csv 文件数据内容 并以result.html文件作为模板以响应返回。

* 通过 "/hurun"路由，指定POST请求方式， 调用函数将结果返回前段界面。

* 选取pandas模块，利用df1 = pd.read_csv("", encoding='')读取flask.csv

* line_markpoint: 传入 select_nation.csv 数据对象，生成折线图，sn列内容作为x轴数据，money列和dependency列数据作为y轴数据.

* 使用了循环和判断，用于自动生成表格和翻页按钮。

##### HTML档描述(为了防止标签变现，所以删掉了<>

* html的select标签的onchange实现了页面刷新。

* button标签的onclick实现翻页功能。

* 用了div class="box"   /div将数据放在盒子里，并且用了style.box { justify-content:center; display:flex; flex-wrap:wrap;  };   /style实现了n行3列布局。

* 用.dataframe{width:100%;}实现表格全局布满。

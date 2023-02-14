# 1.HTML入门

## 1.1 flask雏形

```python
##flask雏形网站

from flask import Flask

app = Flask(__name__)

@app.route("/show/info")
def index():
    return "hello"

if __name__=='__main__':
    app.run()


```

## 1.2 flask还可以允许附带文件

```python
from flask import Flask,render_template

app = Flask(__name__)
##app = Flask(__name__,template_folder=xxx)更改目录

@app.route("/show/info")
def index():

    return render_template("index.html")##附带文件

if __name__=='__main__':
    app.run()


```

## 1.3 div和span

```html
<div>
    内容
</div>##div独占一行
<span> 内容</span>  ##span根据内容决定占行
```

## 1.4 超链接

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>我的网站</title>
</head>
<body>

    <div style="text-align: center">百度一下你就知道
        <a href="https://www.baidu.com">点击链接</a>
    </div>

    <div style="text-align: center">搜狗一下
        <a href="/get/news">点击</a>
    </div>
</body>
</html>
```



```python
from flask import Flask,render_template

app = Flask(__name__)

@app.route("/show/info")
def index():
    return render_template("index.html")

@app.route("/get/news")
def get_news():
    return render_template("get_news.html")


if __name__=='__main__':
    app.run()

```

## 1.5 图片

```html
<img src="图片地址"style="height:100px;width:100px;"/>
```



## 1.6 小结

### 1.6.1 学习的标签

```html
<h1></h1>
<div></div>
<span></span>
<a></a>
<img/>
```

### 1.6.2  划分

```html
行内标签：<h1></h1>
        <div></div>
		<a>不能设置高度和边距，默认无效

块级标签：<span></span>
        <a></a>
		<img/>
```



### 1.6.3 嵌套

```html
<div>
    <span>xxx</span>
    <img />
    <a></a>
</div>
```



## 1.7 列表标签

```html
<ul>
	<li>中国联通</li>
    <li>中国电信</li>
    <li>中国移动</li>
</u1>
```



## 1.8 表格

```html
<table>
    <thead>
    <tr>  <th>id</th> <th> name</th> <th>age</th>	 </tr>
    </thead>
    <tbody>
    	<tr>	<td>101</td><td>alex</td><td>18</td>	</tr>
    	<tr>	<td>102</td><td>bilibili</td><td>19</td>	</tr>
        <tr>	<td>103</td><td>cheems</td><td>20</td>	</tr>
        <tr>	<td>104</td><td>doge</td><td>21</td>	</tr>
        <tr>	<td>105</td><td>edge</td><td>22</td>	</tr>
    </tbody>
</table>
```



## 1.9 input

```html
<input type="text">  普通输入框
<input type="password"> 密码框
<input type="file">	选择文件框
<input type="buttom">单纯就是一个按钮
<input type="submit">和form连用，提交数据

```

## 1.10 下拉框

```html
    <select>
        <option>tokyo</option>
        <option>kyoto</option>
        <option>nakayya</option>
        <option>sapporo</option>
    </select>

    <select multiple>
        <option>tokyo</option>
        <option>kyoto</option>
        <option>nakayya</option>
        <option>sapporo</option>
    </select>
```

# 2.CSS入门

## 2.1.书写方式

### 2.1.1  直接写在标签里

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .c1{
            color: brown;
        }
    </style>
</head>
<body>
<h1 class="c1">欢迎</h1>
</body>
</html>
```

### 2.1.2 写在文件里

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="common.css"/>
</head>
<body>
<h1 class="c1">欢迎</h1>
</body>
</html>

```



```css
.c1{
    height: 100px;
    text-align: center;
}
.c2{
    color: brown;
}
```

## 2.2.选择器

### 2.2.1  类选择器(最多)

```html
<style>
    .c1{
        color: darkred;
    }
<div class="c1">中国</div>
```

### 2.2.2  id选择器

```html
#c2{
    color: deeppink;
}
<div id="c2">江西</div>
```

### 2.2.3  li选择器

```html
li{
    color: aqua;
}
```

### 2.2.4  后代选择器

```html
 .yy li{
            color: blueviolet;
        }
 .yy > a{
            color: lawngreen;
        }
```

```html
<div class="yy">
    <a>百度</a>
    <div>
        <a>谷歌</a>
    </div>
    <ul>
        <li>搜狗</li>
    </ul>
</div>
```

### 2.2.5  CSS覆盖问题

默认用多个，上面的如果和下面的不重名，他们就会一起应用，如果重名，则下面的会把上面的覆盖掉。

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <styLe>
        .c1{
            color: darkred;
            border: 1px solid red;
        }
        .c2{
            font-size: 20px;
            color: green;
        }
    </styLe>
</head>
<body>
    <div class="c1 c2">中国联通</div>
</body>
</html>
```

## 2.3 样式

### 2.3.1  高度和宽度

```html
.c1{
    height: 300px;
    width: 500px;
}
```

注意事项：

1.宽度支持百分比

2.行内标签默认无效(span)

3.块级标签默认有效(霸道，即使右边部分留白，也不给别人占用)

### 2.3.2   块级和行内标签

1. 块级标签
2. 行内标签
3. CSS样式：标签-> display : inline-block

注意：块级标签和行内标签不是绝对的，只是默认如此，可以进行更改

```html
<div style="display: inline">中国联通</div>
<span style="display: block">中国移动</span>
```

### 2.3.3  字体颜色和大小

```html
  <style>
        .c1{
            color: red;
            font-size: 50px;
            font-weight: 500;
            font-family: 隶书;
        }
    </style>
</head>
```

### 2.3.4  文字对齐方式

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
  <style>
    .c1{
      height: 59px;
      width: 300px;
      border: 1px solid red;

        text-align: center;/*水平方向居中*/
        line-height: 59px;/*垂直方向居中（只能有一行文本）*/
    }
  </style>
</head>
<body>
<div class="c1">中国联通</div>
</body>
</html>
```

### 2.3.5  浮动

```html
<div>
  <span>左边</span>
  <span style="float: right">右边</span>
</div>
```

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .item{
            float: left;
            width: 200px;
            height: 170px;
            border: 1px solid red;
        }
    </style>
</head>
<body>
    <div style="background-color: dodgerblue">
        <div class="item"></div>
        <div class="item"></div>
        <div class="item"></div>
        <div class="item"></div>
        <div class="item"></div>
        <div class="item"></div>
        <div style="clear: both"></div>
    </div>
<div>hola</div>
</body>
</html>
注意：如果一个div中用到了浮动（float），必须要在最下面加一个<div style="clear: both"></div>，否则会没办法把父类撑起来
```

### 2.3.6   内边距

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .outer {
            border: 1px solid red;
            height: 400px;
            width: 200px;
            padding-top: 20px; /* 内边距 顶部空出20px*/
            padding-left: 20px; /*左*/
            padding-right: 20px; /*右*/
            padding-bottom: 20px; /*底部*/
            padding:20px/*简写，表示上下左右全部空出20px*/
            padding: 20px 20px 20px 20px/*上右下左*/
        }
    </style>
</head>
<body>
<div class="outer">
    <div style="background-color: dodgerblue">中国联通</div>
    <div>中国移动</div>
</div>
</body>
</html>
```

### 2.3.7  外边距

```html
  margin-top: 20px;
  margin-right: 20px;
  margin-left: 20px;
  margin-bottom: 20px;
  margin: 20px;
```

### 2.3.8  左右对齐

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        body{
            margin: 0;
        }
        .c1{
            width: 900px;
            height: 1000px;
            background-color: dodgerblue;
            margin: 0 auto ;
        }
    </style>
</head>
<body>
        <div class="c1"></div>
</body>
</html>
```

### 2.3.9  小米商城案例

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <link rel="icon" href="https://cdn.cnbj1.fds.api.mi-img.com/mi.com-assets/shop/img/logo-mi2.png">
    <title>小米商城 - Xiaomi 12、Redmi K50、MIX FOLD，小米电视官方网站</title>
    <style>
        body {
            margin: 0;
        }

        .header {
            background-color: #333;
            height: 40px;
        }

        .container {
            width: 1226px;
            margin-left: auto;
            margin-right: auto;
        }

        .header .menu {

            float: left;
            color: white;
            line-height: 40px;
        }
        .header .menu a{
            color: #b0b0b0;

            display: inline-block;
            font-family: "Microsoft YaHei UI";
            font-size: 12px;
            margin-right: 16px;
        }

        .header .accent {
            float: right;
            color: white;
            line-height: 40px;
        }
        .header .accent a{
            color: #b0b0b0;

            display: inline-block;
            font-family: "Helvetica Neue";
            font-size: 12px;
            margin-right: 16px;
        }
    </style>
</head>
<body>
<div class="header">
    <div class="container">
        <div class="menu">
            <a>小米官网</a>
            <a>小米商城</a>
            <a>MIUI</a>
            <a>loT</a>
            <a>云服务</a>
            <a>天星教科</a>
            <a>有品</a>
            <a>小爱开放平台</a>
            <a>企业团购</a>
            <a>资质证照</a>
            <a>协议规划</a>
            <a>下载app</a>
            <a>Select Location</a>
        </div>
        <div class="accent">
            <a>登录</a>
            <a>注册</a>
            <a>消息通知</a>
        </div>
        <div style="clear: both"></div>
    </div>
</div>
</body>
</html>
```

### 2.3.10  小结

```html
.opacity()设置透明度0-1
```

# 3.Bootstrap

## 3.1 案例

### 3.1.1  登录

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>登录</title>
    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <style>
        .account {
            width: 400px;
            height: 300px;
            border: 1.2px solid black;
            border-radius: 6px;
            margin: 145px auto auto;
            padding: 20px 40px;
            box-shadow: 4px 4px 16px #aaa;
        }

        .account h1 {
            text-align: center;
            margin-top: -1px;
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
        }

        .input-group{

        }


    </style>
</head>
<body>
<div class="account">
    <h1>
        用户登录
    </h1>
    <div class="form-group">
        <label for="exampleInputEmail">用户名</label>
        <input type="email"class="form-control"id="exampleInputEmail"placeholder="请输入用户名">
    </div>
    <div class="form-group">
        <label for="exampleInputPassword1">密码</label>
        <input type="password"class="form-control"id="exampleInputPassword1"placeholder="请输入密码">
    </div>
    <button type="submit"class="btn btn-primary">登录</button>



</div>
</body>
</html>
```

### 3.1.2  表格

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <link rel="stylesheet" href="/static/plugins/bootstrap-3.4.1/css/bootstrap.css">
    <style>
        .navbar {
            border-radius: 0;
        }

        .btn-primary {
            margin: 10px 30px;

        }
    </style>
</head>
<body>
<nav class="navbar navbar-default">
    <div class="container">
        <!-- Brand and toggle get grouped for better mobile display -->
        <div class="navbar-header">
            <button type="button" class="navbar-toggle collapsed" data-toggle="collapse"
                    data-target="#bs-example-navbar-collapse-1" aria-expanded="false">
                <span class="sr-only">Toggle navigation</span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
                <span class="icon-bar"></span>
            </button>
            <a class="navbar-brand" href="#">中国联通</a>
        </div>

        <!-- Collect the nav links, forms, and other content for toggling -->
        <div class="collapse navbar-collapse" id="bs-example-navbar-collapse-1">
            <form class="navbar-form navbar-left">
                <div class="form-group">
                    <input type="text" class="form-control">
                </div>
                <button type="submit" class="btn btn-default">搜索</button>
            </form>
            <ul class="nav navbar-nav navbar-right">
                <li><a href="#">登录</a></li>
                <li><a href="#">注册</a></li>
            </ul>
        </div><!-- /.navbar-collapse -->
    </div><!-- /.container-fluid -->
</nav>
<div class="container">
    <button type="button" class="btn btn-primary">新建</button>
</div>
<div class="container"style="margin-top: 20px">
    <div class="bs-example" data-example-id="bordered-table ">
    <table class="table table-bordered  table table-hover">
        <thead>
        <tr>
            <th>#</th>
            <th>First Name</th>
            <th>Last Name</th>
            <th>Username</th>
        </tr>
        </thead>
        <tbody>
        <tr>
            <th scope="row">1</th>
            <td>Mark</td>
            <td>Otto</td>
            <td>@mdo</td>
        </tr>
        <tr>
            <th scope="row">2</th>
            <td>Jacob</td>
            <td>Thornton</td>
            <td>@fat</td>
        </tr>
        <tr>
            <th scope="row">3</th>
            <td>Larry</td>
            <td>the Bird</td>
            <td>@twitter</td>
        </tr>
        </tbody>
    </table>
</div>
</div>



</body>
</html>
```

# 4.javaScript

## 4.1 初识JavaScript

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
    <style>
        .menus {
            border: 1px solid black;
            width: 500px;
            height: 400px;
        }

        .headers {
            background-color: #8c8c8c;
            padding: 50px 50px;
        }
    </style>
</head>
<body>

<div class="menus">
    <div class="headers"onclick="func()">标题</div>
    <div class="item">正文</div>
</div>

<script type="text/javascript">
     function func(){
         confirm("是否要继续")
     }

</script>
</body>
</html>
```

## 4.2字符串类型

```javascript
//声明 var name = "cheems"
var name = String("cheems")

var v1 =name.length; //求字符串长度
var name =name[0]
var v3 = name.trim();//去除空白
var v4 = name.substring(0,2）//前取后不取 ：ch

```

###  案例1. 跑马灯

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<span id="txt">欢迎xxx领导莅临本公司视察工作</span>


<script type="text/javascript">
    function show() {
        //1.去HTML标签中找到某个标签并获取他的内容（DOM）
        var tag = document.getElementById("txt");
        var dataString = tag.innerText;

        // 2.动态起来，把文本中的第一个字符串放到最后一位
        var firstChar = dataString[0];
        var otherString = dataString.substring(1, dataString.length);
        var newText = otherString + firstChar;


        //3.在HTML中更新内容
        tag.innerText = newText
    }

    //JavaScript中的内置函数，每500ms执行一次
    setInterval(show, 500)

</script>
</body>
</html>
```

## 4.3 数组类型

### 4.3.1  跑马灯

```javascript
//定义
var v1 = [11,22,33,44];
var v2 = Array([11,22,33,44]);

//操作
var v1 = [11,22,33,44];
v1[1]
v1[0] = "cheems";

v1.push("联通");//尾部追加[11，22，33，44，"联通"]
v1.unshift("联通")//尾部追加["联通"，11，22，33，44]
v1.splice(索引，0，元素)//指定追加
v1.splice(1，0，"中国")// [11,"中国",22,33,44];


v1.pop//尾部删除
v1.shift//头部删除

v1.splice(元素位置,1)//指定位置删除
v1.splice(1,1)//删除索引位置为1的元素[11,33,44]


```

### 4.3.2  动态生成数据

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<ul id="city">
    <!--<Li>北京</L1> -->
</ul>
<script type="text/javascript">

    // 发送网络请求，获取数据
    var cityList = ["北京", "上海", "深圳"];
    for (var idx in cityList) {
        var text = cityList[idx];
        //创建<Li></Li>
        var tag = document.createElement("Li");
        //在Li标签中写入内容
        tag.innerText = text;
        //添加到1d=city那个标签的里面，DOM
        var parentTag = document.getElementById("city");
        parentTag.appendChild(tag);
    }
</script>

</body>
</html>
```

## 4.4 对象（字典）

```
info = {
"name":"doge",
"age":18
}

info={
name:doge,
age:18
}
```

```javascript
info.age
info.name = "cheems"

info["name"]
info["age"]="cheems"  //读取数据
delete info["age"]
```

### 1.案例 动态生成表格

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>

<table style="border: 2px solid black">
    <thead>
    <tr>
        <th>id</th>
        <th>name</th>
        <th>age</th>
    </tr>
    </thead>
    <tbody id="body">

    </tbody>
</table>


<script type="text/javascript">
    var dataList = [
        {id: 1, name: "cheems", age: 18},
        {id: 2, name: "cheems", age: 18},
        {id: 3, name: "cheems", age: 18},
        {id: 4, name: "cheems", age: 18},
        {id: 5, name: "cheems", age: 18},
        {id: 6, name: "cheems", age: 18},
    ];
    for (var idx in dataList) {
        var info = dataList[idx];

        var tr = document.createElement("tr");
        for (var key in info) {
            var text = info[key];
            var td = document.createElement("td");
            td.innerText = text;
            tr.appendChild(td);
        }
        var bodyTag = document.getElementById("body");
        bodyTag.appendChild(tr);
    }


</script>
</body>
</html>
```

## 4.5 条件语句

```javascript
if(条件){

}else if{

}
```

## 4.6 函数

```javascript
funnction 函数名字(){
	函数内容
}
function func(){
    ......
}

func()
```

## 4.7 DOM语句

### 4.7.1 DOM语句

```javascript
//根据id获取标签
var tag = document.getElementById("xx");

//获取标签中的文本
tag.innerText

//修改标签中的文本
tag.innerText = "hhhhh";
```

```javascript
//创建标签<div>hello</div>
var tag = document.createElement("div");
//标签写内容
tag.innerText = "hhhh";
```

```html
<ul id="city">
    
</ul>

<script type="text/javascript">
	var tag = document.getElementById("city");
    var newTag = document.createElement("li");
    			//在li标签中添加内容
    newTag.innerText= "北京";
    
tag.appendChild(newTag); 

</script>

```

### 4.7.2 点击按钮将用户输入的内容添加到表格中

```javascript
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Title</title>
</head>
<body>
<input type="text"placeholder="请输入内容"id="txtUser"/>
<input type="button"value="点击添加"onclick="addcityInfo()">
<ul id="city">

</ul>
    <script type="text/javascript">
        function addcityInfo() {
        //1.找到输入标签
        var txtTag = document.getElementById("txtUser");
        // 2.获取input框中用户输入的内容
        var newString = txtTag.value;
        // 3.创建标签 <Li></Li> 中间的文本信息就是用户输入的内容
        var newTag = document. createElement ("Li");
        newTag. innerText = newString;
        // 4.标签添加到ul中
        var parentTag = document.getElementById("city");
        parentTag.appendChild(newTag);
        // 5.将input框内容清空
        txtTag.value ="";
         }
</script>
</body>
</html>
```

# 5. jQuery

## 5.1 直接寻找

### 5.1.1  id选择器

```html
<h1 id="txt">中国联通</h1>
<h1>中国联通</h1>
<h1>中国联通</h1>
```

```javascript
$("#txt")

```

### 5.1.2  样式选择器

```html
<h1 class="c1">中国联通</h1>

$(".c1")
```

### 5.1.3  标签选择器

```html
<h1 class="c1">中国联通</h1>

$("h1")
```

### 5.1.4  层级选择器

```html
<h1 calss="c1">中国联通</h1>
<h1 class="c1">
    <div class="c2">
        <span></span>
        <a></a>
    </div>
</h1>
<h1 class="c2">中国联通</h1>

$(".c1 .c2 a")
```

### 5.1.5  多选择器

```html
<h1 calss="c1">中国联通</h1>
<h1 class="c1">
    <div class="c3">
        <span></span>
        <a></a>
    </div>
</h1>
<h1 class="c2">中国联通</h1>
<ul>
    <li>xxx</li>
    <li>xxx</li>
</ul>

$("#c3,#c2,li")
```

### 5.1.6  属性选择器

```html
<input type="text" name="n1"/>
<input type="text" name="n1"/>
<input type="text" name="n1"/>

$("input[name='n1']")
```

## 5.2 间接寻找

### 5.2.1  找兄弟

```html
<div>
     <div>北京</div>
     <div class="c1">上海</div>
     <div>广州</div>
     <div>深圳</div>
</div>
    


$(#c1)  //上海
$(#c1).prev()//找到上一个兄弟：北京
$(#c1).next()//找到下一个兄弟：广州
$(#c1).next().next()找到下下个兄弟：深圳
$(#c1).sinlings()  //找到同级的所有兄弟

```

### 5.2.2  找父子

```html
<div>
    <div>
        <div>北京</div>
        <div id="c1">
            <div class="p1">青浦区</div>
            <div class="p2">黄埔区</div>
            <div class="p3">宝山区</div>
        </div>
        <div>深圳</div>
        <div>广州</div>
    </div>
        <div>陕西</div>
        <div>山西</div>
        <div>河南</div>
        <div>河北</div>
</div>

$("#c1").parent() //父亲
$("#c1").parent().parent()//还可以继续往上找


$("#c1").children()//找所有的儿子
$("#c1").children(".p2")  //找儿子中class等于p2的那个

$("#c1").find()//找所有的子孙
$("#c1").find(".p1") //找所有的子孙中class等于p2的那个
```

## 5.3操作样式

### 5.3.1  操作样式

```javascript
.addClass()
.removeClass()
.hasClass()
```

### 5.3.2  值的操作



# 6.MySQL

## 6.1 连接MySQL

```mysql
import pymysql

connection = pymysql.connect(host='localhost', port=3306, user='root', password='031120',database='qq')
cursor = connection.cursor()
#
# cursor.execute("create database qq") #创建数据库

# cursor.execute("show databases;")  #打印所有的数据库
# records = cursor.fetchall()
# for i in records:
#     print(i)


cursor.close()
connection.commit()#如果有需要动到资料的指令则需添加这个，例如：增、删、改、查
connection.close()
```

# 7.django

## 7.1  创建项目

### 7.1.1 终端创建项目

```python
1. 打开终端

2.进入某个目录（项目放在那里）
D:\PyCharm Project

3.执行命令创建项目
"C:\Users\33897\AppData\Local\Programs\Python\Python39\Scripts\django-admin.exe" startproject 项目名称

如果已经加入了环境变量，则可以直接
django-admin startproject 项目名称
```

### 7.1.2 pycharm创建都将哦项目

```python
直接新建django项目即可
```

### 7.1.3 django文件说明

```python
说明：
命令行中创建的项目是标准的

在pycharm中创建的django项目，在标准的基础上默认给我们加了点东西。
	1.创建了一个templates目录【删除】
    2.在settting.py中'DIRS'中内容删除【删除】
```

```python
默认文件介绍

mysite
	manage.py【项目的管理，启动项目、创建app、数据管理】
    mysite
    	__init__.py
        asgi.py		【接收网络请求，不用动（异步）】
        settings.py	 【项目配置文件】【数据库、注册app.....】【常操作 】
        urls.py		【url和python函数的对应关系】【常常操作】
        wsgi.py		【接收网络请求，不用动（同步）】
```

![image-20230121170622877](C:\Users\33897\AppData\Roaming\Typora\typora-user-images\image-20230121170622877.png)

## 7.2 快速上手

### 7.2.1 注册app

#### 1. 创建app（命令行模式）

```python
创建app
python manage.py startapp app01
```

#### 2. 创建app  tool-Run manage.py Task

输入startapp app名字 

![屏幕截图_20230125_174006](C:\Users\33897\Pictures\Screenshots\屏幕截图_20230125_174006.png)



#### 3.  注册app  在settings.py中 

![image-20230121171308210](C:\Users\33897\AppData\Roaming\Typora\typora-user-images\image-20230121171308210.png)

### 7.2.2  编写url和视图函数对应关系【urls.py中编写】

![屏幕截图 2023-01-21 172053](C:\Users\33897\Pictures\Screenshots\屏幕截图 2023-01-21 172053.png)

### 7.2.3 编写视图函数【views.py】

### 7.2.4  启动django

```python
1.命令行启动
python manage.py runserver

2.pycharm启动

```

### 7.2.5  问题（403 forbidden）

![image-20230124130905499](C:\Users\33897\AppData\Roaming\Typora\typora-user-images\image-20230124130905499.png)

```python
csef-token验证
解决办法：在表单中写上：{% csrf_token %}
<form>
    {% csrf_token %}
    <input type="text"name="user"placeholder="用户名">
    <input type="password"name="pwd"placeholder="密码">
    <input type="submit"value="提交">
</form>
```

## 7.3 django连接数据库

### 7.3.1 连接数据库

```python
1.先下载一个插件 pip install mysqlclient

2.在stetting。py中更换成这个
DATABASES = {
    'default':{
        "ENGINE":'django.db.backends.mysql',
        'NAME':'qq',
        'USER':'root',
        'PASSWORD':'031120',
        'HOST':'localhost',
        'PORT':'3306'
    }
}
```

### 7.3.2 创建表格

#### 1.创建表格

```python
1. 在models.py中操作
from django.db import models

# Create your models here.
class Userinfo(models.Model):                     #表示在mysql中创建一个名为Userindo的表格
    name = models.CharField(max_length=32)        #表示 名字为name 格式为varchar(32)的字段
    password = models.CharField(max_length=64)
    age = models.IntegerField()					  #表示：名字为age 格式为int的字段

# create table app01_userinfo(
#     name varchar(32),
#     password varchar(64),
#     age int
# )
```

```python
2. 在命令行执行下列操作
python manage.py makemigrations  
python manage.py migrate   
```

![image-20230124190254011](C:\Users\33897\AppData\Roaming\Typora\typora-user-images\image-20230124190254011.png)

#### 2.增删改更

```python
#1.添加数据的方法
Userinfo.objects.create(name='mubai',password='002200',age=21)

# #2.删除数据
Userinfo.objects.filter(name='mubai').delete()

# #3.筛选数据
Userinfo.objects.all() #所有数据 取到的数据【行（对象）、行、行】Queryset类型

# #4.更新数据
Userinfo.objects.filter(name='muzi').update(password='002200')

#自增id
id = models.BigAutoField(validators='ID',primary_keys=True)
models.AutoField  #int类型自增
BigAutoField	#big int类型自增
```

## 7.4 django模板

### 7.4.1 模板的定义与继承

#### 1. 定义模板 xxx.html

```html
<h1>顶部</h1>
    <div>
        {% block content %}{% endblock%}
    </div>
<h1>底部</h1>
```

#### 2. 继承母版

```html
{% extends xxx.html %}
{% block content %}
    <h1>首页</h1>
{% endblock %}
```

## 7.5 ModelForm模块

### 7.5.1  ModelForm的使用

```python
from django import forms

class UserModelForm(forms.ModelForm):
    name = forms.CharField(min_length=1, label="用户名")

    class Meta:
        model = models.Userinfo
        fields = ["name", "password", "age", "accent", "create_time", "gender", "depart"]

        # widgets = {
        #     "name" : forms.TimeInput(attrs={"class":"form-control"}),
        #     "password" : forms.PasswordInput(attrs={"class":"form-control"})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs = {"class": "form-control", "placeholder": field.label}


def user_modelform_add(request):
    if request.method == 'GET':
        form = UserModelForm()
        return render(request, 'user_modelform.html', {"form": form})

    form = UserModelForm(data=request.POST)

    if form.is_valid():
        form.save()
        return redirect("/user/list/")
    return render(request, 'user_modelform.html', {'form': form})


def user_edit(request, nid):
    row_object = models.Userinfo.objects.filter(id=nid).first()
    if request.method == 'GET':
        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {"form": form})

    form = UserModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/user/list/')
    return render(request, 'user_edit.html', {'form': form})


def user_del(request, nid):
    models.Userinfo.objects.filter(id=nid).delete()
    return redirect('/user/list/')

```

### 7.5.2 用户输入数据校验

#### 1.第一种方法（字段+正则）

```python
from django.core.validators import RegexValidator


class PrettyModelform(forms.ModelForm):
    mobile = forms.CharField(
        label="电话号码",
        validators=[RegexValidator(r'^1[3-9]\d{9}$','手机号格式错误')] #r'^166[0-9]','号段必须以166开头')
    )
```

#### 2. 第二种方法（钩子校验）

```python
from django.core.exceptions import ValidationError  
  def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        
        if len(txt_mobile) != 11:
            raise ValidationError("格式错误")
        return txt_mobile
```

### 7.5.3  手机号搜索

#### 1.方法

#####   方法1

```
    q1 = models.Prettynum.objects.filter(mobile="16666666666", id=6)
    print(q1)   
```

#####   方法2

```
    data_dict = {"mobile": "16666666666", "id": 6}
    q2 = models.Prettynum.objects.filter(**data_dict)
    print(q2)
```

#### 2.筛选方法

```python
models.Prettynum.objects.filter(id=12)  # 等于12
models.Prettynum.objects.filter(id__gt=12)  # 大于12
models.Prettynum.objects.filter(id__gte=12)  # 大于等于12
models.Prettynum.objects.filter(id__lt=12)  # 小于12
models.Prettynum.objects.filter(id__lte=12)  # 小于等于12

```

```python
models.Prettynum.objects.filter(mobile__startswith=166)    # 以166开头
models.Prettynum.objects.filter(mobile__endswith=166)	   # 以166结尾
models.Prettynum.objects.filter(mobile__contains=166)	   # 内容包括166
```

## 8. 中间件

### 8.1 体验中间件

#### 8.1.1 新建中间件

```python
1.创建一个文件夹存放中间件
2. 编写一个类
3.在setting MIDDLEWARE 中声明中间件的路径
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'applogin.middleware.auth.M1',
    'applogin.middleware.auth.M2',
]
```



```python
from django.middleware.common import CommonMiddleware


class M1(CommonMiddleware):
    """中间件1"""
    # 如果没有返回值（返回None），继续往后走
    # 如果有返回值 HttpResponse 、render 、redirect，则不向后执行

    def process_request(self, request):
        print("M1.entering")

    def process_response(self, request, response):
        print("M1.went")
        return response


class M2(CommonMiddleware):
    """中间件2"""

    def process_request(self, request):
        print("M2.entering")

    def process_response(self, request, response):
        print("M2.went")
        return response
```

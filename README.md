[toc]
## 一 设计思路
## 二 实现步骤
### 1 数据准备与爬虫设计
#### 1.1. 框架介绍
本项目使用了scrapy进行爬取。
需要安装`lxml`，`twisted`和`pywin32`，配置成功后，最后安装scrapy。
官方中文文档：`https://scrapy-chs.readthedocs.io/zh_C`

#### 1.2. 问题爬取
##### 初始设置
前往stackoverflow首页，按时间顺序排列整个网页。并设置一页显示50个问题，其网址如下：
`https://stackoverflow.com/questions?page=page}&sort=newest&pagesize=50`

按照要求，爬取90000页即可获取全部两年来的问题数据，这里使用`format`格式对网址标准格式进行遍历。
##### 爬取数据
设置`item.py`以规定爬取数据包含的内容。
为创建问题数据库，设置搜索结果中问题的排列顺序，以及将来与问题答案进行链接，这里为每一条问题爬取的属性如下：

| 属性变量名 |含义  |
| --- | --- |
| answersNumber | 问题回答数 |
| views | 浏览数 |
| votes | 问题投票数 |
| questions |问题内容  |
| links | 问题详情页面的链接（为后续爬取答案准备） |
|tags  | 问题标签 |
| questionTime |问题提出时间  |

为从网页中获取各不同属性的内容，我们使用xpath方法，在开发者模式下获取网页xml代码，从xml格式中提取数据。举例来说，如：

```python
sel = response.xpath('//*[@id="questions"]/div[{index}]'.format(index=index))
item['questions'] = sel.xpath('div[2]/h3/a/text()').extract()
item['views'] = sel.xpath('.//div[contains(@class,"views")]/text()').extract()[0][6:-7]
```

##### 代码运行
命令行运行
```
scrapy crawl stackoverflow > 1.csv 
```
即可运行。我们设置存储格式为`.csv`。

#### 1.3. 答案爬取

##### 初始设置
使用在第一部分爬取的数据，读取csv文件中的问题links部分。将link设置为爬取页面的网址。
举例来说，格式如下：
```
https://stackoverflow.com/questions/46535327/i-cant-parsing-with-json-by-swift4
```

为减少刷新次数，我们跳过问题答案数为0的条目，不进行爬取。


##### 爬取数据
遍历问题详情页面的每条答案，数据格式如下。

| 属性变量名 | 含义 |
| --- | --- |
| links | 问题详情页链接 |
| questionID | 问题的ID（唯一） |
| answerID | 答案的ID（唯一） |
| answerIndex | 问题的第几条答案 |
| contents | 答案内容 |
| answerTime | 回答时间 |
| votes | 答案获得投票数 |
##### 代码运行
同1所述。
##### 结果展示
共爬取问题4488582条，其中回答数不为0的问题3368851条。

![image](https://github.com/lumiran/crawlStackOF/blob/master/images/1.png)



#### 1.4. 其他技巧
爬虫刷新过快，会出现[403]号报错。这是由于网站的反爬虫策略所造成的，为避免爬虫被ban，我们的方法在以下列出。
##### 设置User Agent
在scrapy框架下，`./middleware/useragent.py`中，我们创建随机UserAgent类，在候选的UserAgent中每次随机挑选一个使用。本项目中设置了16个候选UserAgent。
##### 设置延迟
在`./setting.py`中，我们设置`DOWNLOAD_DELAY = 1`。即每次爬取后等待0.5至1.5秒，再爬取下一页。







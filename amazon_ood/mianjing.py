import _thread
# OOD
# 停车场
#
# 系统
# 音乐库
#
# design Amazon locker, design search API, design recommend system


# design：vending machine，中间要求实现找钱的一个函数（类似 coin change）
# 第四轮 白人大叔 20分钟bq，系统设计（我以为之前那个是系统设计，结果只是个oodesign），设计一个亚麻工人（1M员工）打卡系统，系统数据来自4个数据库（前2个来自自己系统，后两个不是自己control）。这轮感觉答得也不好，因为和练习看的都不太一样，最后基本上是大叔领着我走。


# bg：
# Why Amazon?
# What is your most challenging project?
# What is the challenging part?
# system design: Dropbox

# 第二轮：manager
# 一顿bg
# 有木有帮助client解决大问题
# 重大问题如何决策
# 和同事conflict 但是最后按照你的想法implement
# 和同事conflict 但是最后按照你同事想法implement
# 自己想出来的project 但是你的project help了很多人

# 第三轮：Manager轮， 20分钟BQ, 一轮设计：设计 sandwich shop with robots. 我根本不知道他在说什么。就当OOD设计了 - 他就一直记笔记，本来类图都设计好了。以为他要问 details 设计。结果他要我往更high level设计。
# 急忙补了 high level architecture 的设计图。然后问了怎么处理 robots, 怎么分配任务，怎么优化。答得马马虎虎，好像并没有为难我。

# Coding
# a
# game
# with monster and weapon classes
# Design elastic search engine data feeding system for prime video

# Design elastic search engine data feeding system for prime video

# 你的成功是什么
# 你deadline前info不够如何做决定 + 设计一个系统 接收无数个strs return unique longest string
#
# 你的缺点是什么 + 给你一个list输入 <name, building from, building to> 现在想要找到所有pair他们可以swap building .     比如 <a, 1, 2> <b, 2, 1>, <c, 1, 3> -> 输出<a,b > 因为他们能互换
# 亚洲年轻瘦弱男 alexa windows app马内机 还是逃脱不了的灵魂审问： 你跟你老板的争执 + 一道 一堆<id, attributes> 给一个<id, attributes> 找到top 5 相似的<id, attrs>。



# 1.
# LRU
# Cache
# followup： 给element加上TTL，需要做什么改动

# _thread.start_new_thread(deleteNode , (ttl , self , node))


# 2.
# Netflix
# OOD
# 3.
# LC
# 武斯伞
# 4.
# 小岛
# followup： 1 - 8
# 个方向都算land。
# 2 - matrix
# 内存放不下怎么处理。
# 总共四轮 两轮code 两轮设计 面的是西雅图 Alexa组的 SDEII
#
# 1. 亚洲小姐姐Manger + 美国小哥SDEIII. 1point3acres
# BQ 30Min + 一个Set查重 （基本就是问怎么记录浏览过的record set + iteration搞定 ） 聊得挺开心
#
# 2. 苏格兰哥SDEIII
# BQ 20Min + 设计一个交通管理系统 （类似停车场或者机场那种） 小哥照了不少照片 每次俺问个问题他都寻思半天。。
#
# 3. HM
# BQ 30Min + 设计亚麻产品推荐 （直接开了个亚麻首页说给我设计介个推荐系统） 聊得很high 当时感觉就是妥了。。。
#
# 4. 拉丁小哥SDEII
# BQ 30Min + 利口 伞 稍微变化点儿 小哥挺紧张 跟我面他一样
#
#
# aws 下面的一个组，面得sde21，烙印manager，自我介绍都不需要直接甩来bq，而且还是很恶心的bq，比如然后和manager的争吵，和同事的争吵，做了什么事帮组了小组的非technical方面的表现，和customer和business怎么撕逼的，怎么帮助新组员，做了什么difficult decision结果如何，有没有没做完过任务。本来就烦bq然后也没认真准备答得不好
# 2，烙印，bq+design a parking lot
# 3,中国小哥带吃饭
# 4，老美，bq+实现math.pow(a,b)
# 5,南美大叔，设计一个scheduler，需求比较模糊，要求这个scheduler 可以接受一堆task，每个task有timestamp，然后scheduler有个最大的capacity代表最多能schedule这么多个task。然后就要我自由发挥
# 6,bar raiser老美，问了45分钟bq之后给了个 copy list with random pointer
#
#
#
# 问简历，目前工作，有什么困难和挑战，有没有设计的经验。然后问，给一个 array of string，是 user 的 log，每一个 string 是 id，time，求出连续三天都 出现 的 user。
#
# 上门
# 1. BQ。给一个 video dataset，graph 表示，相连的就是相似的 video。每个 video 也有 rating。求给一个 video id，找出相似的 video 里面最高 rating 的 k 个 。
#
# 2. Hiring M。BQ。
#
# 3. BQ，Number of Island。
#
# 4. OOD。需要设计一个 delivery system，如果有单子，就要找一个 carrier。carrier 是可以 register 这个系统，这样就是有单子的时候就是候选。主要是设计怎么传参数，每个 class 都负责什么功能。我没有经验，就很佛系的靠感觉说了说。
#
# 5. OOD。飞机场设计。差不多也是那些东西。
#
# 6. HM。BQ。问了之前项目，有什么贡献。由于我本身没什么贡献，所以就没聊很久。然后问一个设计 customer who bought this also bought 的系统。我理解成 ML 设计了，就说了很多 DNN，feature，embedding 之类的。面试官只是在问这个我要怎么deploy，我内心表示这是什么问题，外面表示我想想，然后把时间拖过去了。

# 设计[hide=188]亚麻包裹追踪系统

# OOD 设计 log 访问
# 系统设计加实现。warehouse 问题
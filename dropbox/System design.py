#message queue
# 3. design a job processing system/queue
# 结果让设计一个message
# queue.queue里面每个节点需要哪些内容？
#  timestamp , data/payload (**kargs  dict()) , topic/event , offset?
# https://thehoard.blog/how-kafkas-storage-internals-work-3a29b02e026
# When Kafka writes to a partition, it writes to a segment — the active segment. If the segment’s size limit is reached, a new segment is opened and that becomes the new active segment.
#
# Segments are named by their base offset. The base offset of a segment is an offset greater than offsets in previous segments and less than or equal to offsets in that segment.
# On disk, a partition is a directory and each segment is an index file and a log file.
#
# $ tree kafka | head -n 6
# kafka
# ├── events-1
# │ ├── 00000000003064504069.index
# │ ├── 00000000003064504069.log
# │ ├── 00000000003065011416.index
# │ ├── 00000000003065011416.log
# Segment logs are where messages are stored
# Each message is its value, offset, timestamp, key, message size, compression codec, checksum, and version of the message format.
#
# The data format on disk is exactly the same as what the broker receives from the producer over the network and sends to its consumers. This allows Kafka to efficiently transfer data with zero copy.
#
# $ bin/kafka-run-class.sh kafka.tools.DumpLogSegments --deep-iteration --print-data-log --files /data/kafka/events-1/00000000003065011416.log | head -n 4
# Dumping /data/kafka/appusers-1/00000000003065011416.log
# Starting offset: 3065011416
# offset: 3065011416 position: 0 isvalid: true payloadsize: 2820 magic: 1 compresscodec: NoCompressionCodec crc: 811055132 payload: {"name": "Travis", msg: "Hey, what's up?"}
# offset: 3065011417 position: 1779 isvalid: true payloadsize: 2244 magic: 1 compresscodec: NoCompressionCodec crc: 151590202 payload: {"name": "Wale", msg: "Starving."}






# 如果message queue这个service
# down了怎么办？consumer花太多时间working on one task怎么办？consumer掉线了怎么办？
# there is a heartbeat topic. consumer send heartbeat to this topic. if there is a timeout. we assume this comsumer is down. revert offset to the last commited offset of this cusummer and trigger the rebalance mechanizm . so unfinished tasks will be processed by remaining comsumers


#
#
# 2： Coding. 多线程题目。 具体忘记了， 实现一个方法， def(Task task, long dealy)  task 是个interface， 有个action()方法。 用户端用调用def方法， 然后task将会在延迟后执行。里面涉及到lock, condition, notify,wait之类，小伙伴要是去面Dropbox就多看看多线程相关吧。
# 3：Design: 不是典型的Design设计，面试官出了他之前工作类似的一个项目。 设计一个电话簿， 假设我的team是application端， 他的team是DB端, 怎么交互，设计API，各种细节。
# 设计手机上的电话簿，主要靠API设计，和相关DB操作，比如如何显示电话，如何存入，怎么分页，异常怎么办
#
#









# 就聊了一个自己最proud的project，from start to end, 然后被问到做project有没有遇到难相处的人，自己怎么处理的，然后如何推进被block的project，如何give
# critical
# feedback，其他的有点记不住了
#
#





# https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=442936&extra=page%3D1%26filter%3Dsortid%26sortid%3D311%26searchoption%5B3089%5D%5Bvalue%5D%5B3%5D%3D3%26searchoption%5B3089%5D%5Btype%5D%3Dcheckbox%26searchoption%5B3046%5D%5Bvalue%5D%3D25%26searchoption%5B3046%5D%5Btype%5D%3Dradio%26sortid%3D311%26orderby%3Ddateline
# 4）这一轮是设计 log monitor，面试官规定了log 的format，
# ｛action: "view"，
#    page:   "www.dropbox.com",
#    location: "GB",
#    time stamp: xxxx｝
#   {action: "download",
#    file: "hello.txt",
#    time stamp: xxxx}
# 在log里面，一定会有action和time stamp，然后其他的不分根据action是什么来决定，你会怎么设计interface来 create log, 需要哪些function，之后就是讨论moniter service和web server这两个不分怎么交互，怎么存log，会有什么bottleneck ，怎么样improve，怎么样scale，然后又问了如果让设计个metrics来监测你的monitor service的健康状况，你会收集哪些数据。大概就是这些。
#
#
# 楼主给你加米，请问设计 log monitor，需要 back-of-the-envelope calculation，计算需要多少存储，多少 web service吗?
# moniter service和web server交互中 moniter 主要是作什么，能具体说一下吗？非常感谢，祝顺利！
# 他没有让我具体计算需要多少存储，多少server，只是后面scale up的时候大概说了说可以怎么sharding这些的。
# moniter service和web server交互，moniter主要是怎么接收拿过来的log data，拿过来之后需要做一些怎样的aggregation，然后更新moniter数据

# 1.avg response time (API response time , service response time), (fail , blocked , average response time) slow respose webservice  detect slow responce webservice
# 2.hit count for each web service.  detect which web service has been called alot, is there DDOS attach? should we add rate limite , should we add more nodes to handle this web service
# 3.bandwidth used for each webservice
# 4.status of each request , fail rate , effectivenesss of cache policy
# •	Server response time.
# •	Number of server requests and the details of each request.
# •	The top slowest requests in terms of average response time.
# •	The details of any failed requests.
# •	The number of sessions initiated by different browsers and user agents.
# •	The most frequently viewed pages (primarily useful for web applications rather than web APIs).
# •	The different user roles accessing the web API.
# above are monitoring system health, we can also log customer behavior
# how long a user stay in a page, which page user clicked , what customer buy, what customer searched. basicly we can put all things we are intersted in to a log tpoic


# 此轮要design的是丢盒子内部使用的logging
# system。此轮觉得interviewer问题描述的不是很清楚，因为楼主自己是做storage的，说完系统需求之后，楼主开始从log的结构开始设计。可是interviewer并不在意这些细节，也不在意log如何被读出来，interviewer要求楼主把这个系统的high
# level
# diagram画出来，然后问楼主 某个component坏了的话需要怎么做


#
# 非常感谢楼主的回答。能再问一个吗？
# “怎么设计interface来 create log, 需要哪些function”，能简单举个例子吗？
# 比如说 interface: createLog(Timestamp t, JSON data), 还是需要更具体的参数。
# 哪些function: 比如 preprocessData(), aggregationData(), saveLog() 之类的吧。



# 1. 系统设计，一个比较老资格三哥，问了我设计dropbox 的sync pipeline，多个client和一个server怎么样sync。
# 从最简单的案例开始（没有conflict），如何添加文件，修改文件，api 该如何定义，push 到server 端后，server 端怎么存，存什么，
# 数据结构长什么样，其他客户端怎么样pull。我总体就是按照git的思路来答的，总体来说三哥全程都笑呵呵的，所以不知道三哥是满意还是不满意


# ummm.... 这一轮真的是各种behavior questions..... 从describe两个project开始（一个从collaboration角度，一个从personal contribution角度）。大家要准备好各种story啊啊啊。


# 第三轮 thumbnail 系统设计
# 这轮答得有点崩，刚开始没反应过来这个是system design，回答的特别被动，基本是被面试官领着走的。其实就是让你设计一个简单的系统，
# 通过使用message queue， producer/consumer的pattern来完成一个 请求处理图片 -> 处理给定图片的小系统。
#
# 问了些producer这边的REST怎么设计？简单的POST, {domainName}/queue/{imageId}
# status code应该用什么？400,403,404 客户端错误/ 200 请求成功 / 500 服务器错误
# queue里面的message应该包含什么信息？imageId/loc, jobId/offset, metadata, timestamp , action
# 如果message没有放到queue里怎么办 ？async (no ack) ,ack leader , ack all ,retry 3 time then abandon and log. From 1point 3acres bbs
# consumer如果处理不了message怎么办？ based on error type put it to another topic
# 如果超时怎么办？ kill thread, put to anoher topic
# 怎么监控consumer的状态？  || have a heartbeat topic, send status info to this topic
# consumer会遇见什么问题？ message 不valid没法parse, 处理的时候image可能已经不存在了 || workload to high can not process and timeout.
# consumer挂了，没处理完成的图片怎么办？producer放message到queue的时候要log这个Event, 如果挂了对比producer/consumer的log找没处理的图片 || if timeout we set offset to where the the cosumer last picked up.
# queue挂了怎么办？ HA，做replication, producer log message
# 多台机器的consumer要考虑什么？
# design a service for processing thumbnail message from consumer to producer。 感觉跟thumbnail 什么关系没有，就是怎么处理message 没有重复怎么retry之类的
#补充一下，他刚开始的描述 queue, producer, consumer我第一反应是单机的多线程p/c问题，其实这个queue, p, c是分布在三台不同的机器上的。。。扯了半天才发现是这样
# 面试官的问题问的非常模糊，好久没面这种design了，自己把自己绕里面了，感觉说了很多东西他都不太满意的感觉，想了想主要原因是他一直在drive这个设计，如果自己设计的时候就把这些问题抛出来解决的话可能会好一些




# 第二题：一个迷之笑容的亚裔小哥，出了一道面经没有的题，心慌慌，完全没有打上来，五十分钟什么代码都没写，疯狂讨论（主要是我一个人在讲），最后也没给出比较好的解法，唉，感觉要挂，我每说一种解法，小哥就狂笑，脸都憋红了，很迷。题目大概是这样的：现在我们有一些代码出bug了，大概每个bug就是函数a调用函数b, 函数b又调用函数a，然后函数a报错，等等。现在出的bug有很多很多条，问你通过定义一种similarity来将这些bug归类，这样我们就可以将每类bug交给一个程序员去修复。
# 举个例子：
# bug1 : a->b->a->b->a...->b,b error.
# bug2：a->a->a->a...->a,a error.
# bug3：b->a->b->a...->a,a error
# ...
# 让你找出规律，定义similarity，然后group一下。。。
#
# 天哪！！！我完全没明白他要问什么好嘛？这是在干什么？？？
# 不用说了，楼主长跪不起。。。
# 我先说了个直接判断最后一个调用的函数，是a就归到一组，是b就归到另一组，小哥给出一些反例，然后我又给出一个构造树的方法（这里画不出来，就不画了），大概就是把这些路径表示成一个完整的树，然后找公共父节点，哪几个的公共父节点比较低，就把他们归到一组，因为从root出发，这些路径比较晚才开始分叉，而不同group的路径可能从很早就开始分叉了，就类似这样定义了similarity。。。小哥想了一下说了nice，然而他觉得我说的好诡异但他又说不出来什么，只能狂笑，脸都憋红了，弄得我好尴尬。。。反正到最后实在没时间小哥说得了，你就把你说的这个代码写了吧，我就把这个直接交给community评价（哭脸）。。。好难过
# 最后也没时间问他问题了，就问了一下“could you tell me what do you really expect from the question?”他就说了一个构造图的方法，还有一个他不太喜欢的brutal force找chain的方法，然而我没听懂，也没心情听了，因为下一个面试官已经在外面等了

# 收到offer了，回馈地里。重新解释一下第二题，面试官反复强调这个题比较开放，所以没有什么正确答案可言。题目重新解释一下，给出很多函数之间互相调用的路径，
# 如a call b call a call c和a call b call a call b等等很多路径，自己定义哪些路径相似，把相似的分成一类。
# 我提的方法就不说了，面试官提到的两种一种是暴力搜索最小循环节，具体怎么做我就不知道了，另一种是每条路径都建图，比如说上面两个例子，
# 第一个例子建成的图就是a和b互相指向，然后a指向c，第二个例子就是a和b互相指向，二者生成的图不同，所以认为二者不相似。
# 假设现在有一个路径是b call a call b call a，那么生成的图也是a和b互相指向，这个图和第二个相同，所以认为这两个路径相似。
# 这是个人理解，由于最后剩的时间不够太着急面试官讲的太快，我也没心思听了，所以对上面解法的准确度不负责。  其实电面也是新题，有人想听再说。



# 差不多是这么个意思......电面是，假设NASA想和dropbox合作储存太空影像照片，但是照片太大，每一张有一个G，所以将每张照片切分成1000*1000张小图片来储存，要求你设计数据结构储存。
# follow up，假设我们要反复访问小图片碎片，设计数据结构，并提供函数返回least recently used的小图片碎片，尽可能降低时间复杂度


# 第二轮：photo id, top K, 提供iterator，先用了heap，然后用hashmap+double linkedlist优化到O(1)，follow up: top K经常被call怎么优化
# 4. 亚裔美国小哥哥+国人shadow，刚吃过午饭有些困，加上demo听得太认真，有点精力不足。top k photo view，pq+hashmap，很多follow up包括time complexity和一些别的，中间有些波折，不过还好最后都解决了

# 3. System design。Design logging system。双人。
#     此轮要design的是丢盒子内部使用的logging system。此轮觉得interviewer问题描述的不是很清楚，因为楼主自己是做storage的，说完系统需求之后，楼主开始从log的结构开始设计。可是interviewer并不在意这些细节，也不在意log如何被读出来，interviewer要求楼主把这个系统的high level diagram画出来，然后问楼主某个component坏了的话需要怎么做


# 5. All around。双人。
# ummm.... 这一轮真的是各种behavior questions..... 从describe两个project开始（一个从collaboration角度，一个从personal contribution角度）。大家要准备好各种story啊啊啊。


# 三种分别是，
#
# 1. queue 加 counter，queue里面没有数，就counter++ 分配； queue里面有数，就从queue里面分配；deallocate的时候，就扔queue里就行了。需要一个hashset，去重。
#
# 2. 开一个bit array，每一位表示有没有被分配
#
# 3. 开一个线段树，也还是用bit array 表示， 只有叶子节点表示当前id有没有被分配，其他的中间节点表示他下面的叶子节点还有没有id可以分配。


#   2： Coding. 多线程题目。 具体忘记了， 实现一个方法， def(Task task, long dealy)  task 是个interface， 有个action()方法。 用户端用调用def方法， 然后task将会在延迟后执行。里面涉及到lock, condition, notify,wait之类，小伙伴要是去面Dropbox就多看看多线程相关吧。
# 3：Design: 不是典型的Design设计，面试官出了他之前工作类似的一个项目。 设计一个电话簿， 假设我的team是application端， 他的team是DB端, 怎么交互，设计API，各种细节。
# 4：BackGround and Cluture: 聊之前做过的项目，什么impact, 怎么和team还有其他team沟通，出现问题怎么办，为什么想要厉害， 为什么选他们面试，怎么领导team，对team的最大贡献。都是些老生常谈。



# 我们和NASA合作啦，现在有一个类似谷歌地球的东西，要存储地图瓦块图像，每个瓦块图像1mb大小，大概有10000个瓦块图像
# 你要实现一个类，类里面的方法可以修改图片数据，要可以返回图片数据，还要可以接收储存数据。
# receiveImage()
# changeImage(int id)
# returnImage(int id)
# 我想不出来用什么数据结构，他说就当每个图片是一个文件，进行文件操作。
# follow up是会出现什么边界条件？1.这个文件还没receive到却要求改查 2. 改查的文件不存在 处理方法 throw out exception/handle exception
#就是个hash map  key 是图片的id value 是图片在硬盘上的地址
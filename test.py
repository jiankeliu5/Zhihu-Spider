#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Required
- requests
Info
- author : "moran"
- email  : "moranzcw@gmail.com"
- github : "moranzcw@gmail.com"
- date   : "2017.7.24"
"""

# from threading import Thread
# from queue import Queue
import json
# my_queue = Queue()
#
#
# class MyThread1(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#
#     def run(self):
#         # put_data = "you producer data"
#         # my_queue.put(put_data)
#         pass
#
#
# class MyThread2(Thread):
#     def __init__(self):
#         Thread.__init__(self)
#
#     def run(self):
#         get_data = my_queue.get()
#         print(get_data)
#         pass


# if __name__ == '__main__':
#     thread1 = MyThread1()
#     thread2 = MyThread2()
#     thread1.start()
#     thread2.start()
#     thread1.join()
#     thread2.join()

# jsss = """{"asd":"testtest\\"test\\"test"}"""
jsss = """{"loading":{"global":{"count":0},"local":{"token/":false,"currentUser/get/":false,"env/getExperiments/":false,"config/getAppConfig/":false,"people/get/":false,"people/getFollowings/moranzcw":false}},"entities":{"users":{"bbc12345001":{"uid":873234127464337400,"followNotificationsCount":0,"adType":"normal","showSinaWeibo":false,"editorInfo":[],"isBindPhone":false,"accountStatus":[],"isForceRenamed":false,"id":"66d32bab5b5b3007e7e6526b76456c96","messagesCount":0,"headline":"医生","visitsCount":4,"isAdvertiser":false,"isBindSina":false,"favoritedCount":0,"isOrg":false,"followerCount":0,"employments":[],"articlesCount":0,"type":"people","email":"bb****@yahoo.com","caEnabled":false,"avatarUrlTemplate":"https://pic1.zhimg.com/da8e974dc_{size}.jpg","draftCount":0,"lastCommentPermission":"all","description":"","avatarUrl":"https://pic1.zhimg.com/da8e974dc_is.jpg","isActive":1500975347,"answerCount":0,"userType":"people","coverUrl":"","defaultNotificationsCount":0,"educations":[],"urlToken":"bbc12345001","canEditTopic":false,"name":"bbc12345001","locations":[],"badge":[],"availableMessageTypes":["common"],"url":"http://www.zhihu.com/api/v4/people/66d32bab5b5b3007e7e6526b76456c96","renamedFullname":"","voteThankNotificationsCount":0,"thankedCount":0,"gender":-1,"favoriteCount":0},"moranzcw":{"isFollowed":false,"educations":[{"school":{"url":"http://www.zhihu.com/api/v4/topics/19921029","avatarUrl":"https://pic1.zhimg.com/0aabb8324_is.jpg","name":"西北大学（中国）","introduction":"西北大学（Northwest University），简称“西大”，始建于1902年，由清末光绪皇帝御笔朱批设立，坐落于世界历史名城古都西安，是国家教育部与陕西省人民政府共建的综合性全国重点大学，“211工程”、“中西部高校基础能力建设工程大学，是中国西北地区历史最为悠久的高等学府。","type":"topic","excerpt":"西北大学（Northwest University），简称“西大”，始建于1902年，由清末光绪皇帝御笔朱批设立，坐落于世界历史名城古都西安，是国家教育部与陕西省人民政府共建的综合性全国重点大学，“211工程”、“中西部高校基础能力建设工程大学，是中国西北地区历史最为悠久的高等学府。","id":"19921029"},"major":{"url":"http://www.zhihu.com/api/v4/topics/19557552","avatarUrl":"https://pic2.zhimg.com/4670f7361_is.jpg","name":"软件工程","introduction":"软件工程 (Software Engineering) 是一门研究和应用如何以系统性的、规范化的、可定量的过程化方法去开发和维护软件，以及如何把经过时间考验而证明正确的管理技术和当前能够得到的最好的技术方法结合起来的学科。","type":"topic","excerpt":"软件工程 (Software Engineering) 是一门研究和应用如何以系统性的、规范化的、可定量的过程化方法去开发和维护软件，以及如何把经过时间考验而证明正确的管理技术和当前能够得到的最好的技术方法结合起来的学科。","id":"19557552"}},{"school":{"url":"http://www.zhihu.com/api/v4/topics/","avatarUrl":"https://pic1.zhimg.com/e82bab09c_is.jpg","name":"澧县一中","introduction":"","type":"topic","excerpt":"","id":""},"major":{"url":"http://www.zhihu.com/api/v4/topics/19588985","avatarUrl":"https://pic2.zhimg.com/89641a955_is.jpg","name":"学生","introduction":"学生，未来的希望。","type":"topic","excerpt":"学生，未来的希望。","id":"19588985"}}],"followingCount":199,"voteFromCount":0,"userType":"people","showSinaWeibo":false,"pinsCount":0,"isFollowing":false,"markedAnswersText":"知乎周刊、知乎圆桌和编辑推荐","isPrivacyProtected":false,"accountStatus":[],"isForceRenamed":false,"id":"ee99737ba14d20fcc7a131b5065c44fa","favoriteCount":1,"voteupCount":7808,"commercialQuestionCount":0,"isBlocking":false,"followingColumnsCount":32,"headline":"破事儿水","urlToken":"moranzcw","participatedLiveCount":8,"followingFavlistsCount":15,"isAdvertiser":false,"isBindSina":false,"favoritedCount":3381,"isOrg":false,"followerCount":1011,"employments":[{"company":{"url":"http://www.zhihu.com/api/v4/topics/","avatarUrl":"https://pic1.zhimg.com/e82bab09c_is.jpg","name":"自己玩儿","introduction":"","type":"topic","excerpt":"","id":""}},{"job":{"url":"http://www.zhihu.com/api/v4/topics/19550901","avatarUrl":"https://pic1.zhimg.com/v2-8e66233f5558e741bad3a8c50b9566c8_is.jpg","name":"前端开发","introduction":"web 前端开发","type":"topic","excerpt":"web 前端开发","id":"19550901"},"company":{"url":"http://www.zhihu.com/api/v4/topics/19551460","avatarUrl":"https://pic3.zhimg.com/e75e39ed2_is.jpg","name":"百度","introduction":"中国互联网公司之一，占有中国搜索引擎市场五成以上的份额。旗下有贴吧、知道、百科、文库等产品。&lt;br&gt;详细资料：&lt;a href=\\"http://zh.wikipedia.org/wiki/%E7%99%BE%E5%BA%A6\\" data-editable=\\"true\\" data-title=\\"百度\\" class=\\"&gt;百度&lt;/a&gt;&lt;br&gt;本话题适用于百度公司及其产品的讨论。","type":"topic","excerpt":"中国互联网公司之一，占有中国搜索引擎市场五成以上的份额。旗下有贴吧、知道、百科、文库等产品。 详细资料：百度 本话题适用于百度公司及其产品的讨论。","id":"19551460"}},{"job":{"url":"http://www.zhihu.com/api/v4/topics/19554575","avatarUrl":"https://pic3.zhimg.com/239ea3782_is.jpg","name":"服务器","introduction":"Server","type":"topic","excerpt":"Server","id":"19554575"},"company":{"url":"http://www.zhihu.com/api/v4/topics/19550757","avatarUrl":"https://pic3.zhimg.com/127ee131a4487388e104da2bba7a4df6_is.jpg","name":"腾讯","introduction":"中国最大的互联网综合服务提供公司，主营以腾讯网、QQ、微信、腾讯微博、《英雄联盟》等为代表的互联网产品与网络游戏。主要依靠在线游戏、移动及电信增值服务、网络广告和电子商务交易创收。目前，QQ月活跃用户数7.8亿，移动及电信增值服务付费用户数超过3000万，腾讯微博注册用户数4.6亿。&lt;br&gt;&lt;br&gt;2011年1月，腾讯推出手机应用「微信」进军移动互联网，并于2012年9月获得2亿用户，2013年1月15号用户数突破3亿。作为中国服务用户最多的互联网企业，实力强大的腾讯因对中小创业公司造成的竞争压力而常受诟病。&lt;br&gt;&lt;br&gt;2004年6月，公司以「0700」为代码正式登陆香港股市。","type":"topic","excerpt":"中国最大的互联网综合服务提供公司，主营以腾讯网、QQ、微信、腾讯微博、《英雄联盟》等为代表的互联网产品与网络游戏。主要依靠在线游戏、移动及电信增值服务、网络广告和电子商务交易创收。目前，QQ月活跃用户数7.8亿，移动及电信增值服务付费用户数超过3000万，腾讯微博注册用户数4.6亿。 2011年1月，腾讯推出手机应用「微信」进军移动互联网，并于2012年9月获得2亿用户，2013年1月15号用户数突破3亿。作为中国服务用户最多的…","id":"19550757"}}],"type":"people","avatarHue":"","avatarUrlTemplate":"https://pic2.zhimg.com/v2-73c9e54ae16c5d076ae8c898e7391199_{size}.jpg","followingTopicCount":63,"description":"没什么可以介绍的","business":{"url":"http://www.zhihu.com/api/v4/topics/19619368","avatarUrl":"https://pic1.zhimg.com/e82bab09c_is.jpg","name":"计算机软件","introduction":"徼","type":"topic","excerpt":"徼","id":"19619368"},"avatarUrl":"https://pic2.zhimg.com/v2-73c9e54ae16c5d076ae8c898e7391199_is.jpg","columnsCount":2,"hostedLiveCount":0,"isActive":1,"thankToCount":0,"mutualFolloweesCount":0,"markedAnswersCount":2,"coverUrl":"https://pic1.zhimg.com/v2-043e20d3fef8c39e1b80ca77fdb47498_b.jpg","thankFromCount":0,"voteToCount":0,"isBlocked":false,"answerCount":103,"allowMessage":true,"articlesCount":8,"name":"默然","questionCount":8,"locations":[{"url":"http://www.zhihu.com/api/v4/topics/19557394","avatarUrl":"https://pic4.zhimg.com/b3a13ec73_is.jpg","name":"广东省","introduction":"广东简称粤，是中华人民共和国南端沿海的一个省份，省会广州。广东省位于南岭以南，南中国海之滨，与香港、澳门、广西、湖南、江西和福建接壤，与海南隔琼州海峡相望。2015年GDP总量72812.55亿元，已连续27年为国内第一，是中国经济发展的“火车头”","type":"topic","excerpt":"广东简称粤，是中华人民共和国南端沿海的一个省份，省会广州。广东省位于南岭以南，南中国海之滨，与香港、澳门、广西、湖南、江西和福建接壤，与海南隔琼州海峡相望。2015年GDP总量72812.55亿元，已连续27年为国内第一，是中国经济发展的“火车头”","id":"19557394"},{"url":"http://www.zhihu.com/api/v4/topics/19550818","avatarUrl":"https://pic2.zhimg.com/aea66d640b12450a861282066d78bb2d_is.jpg","name":"上海","introduction":"上海，又称「上海滩」。中国第一大城市，四大直辖市之一，中国国家中心城市，中国的经济、科技、工业、金融、贸易、会展和航运中心。上海位于中国大陆海岸线中部长江口，拥有中国最大外贸港口和最大工业基地。隔海与日本九州岛相望，南濒杭州湾，西部与江苏、浙江两省相接。上海港货物吞吐量居世界第一。上海是一座新兴的旅游城市，有深厚近代城市文化底蕴和众多历史古迹，举办过世博会。江南的传统与移民带入的文化融合，逐渐形成了特有的海派文化。上海早已成为国际大都市，并致力于在2020年建设成为国际金融和航运中心。","type":"topic","excerpt":"上海，又称「上海滩」。中国第一大城市，四大直辖市之一，中国国家中心城市，中国的经济、科技、工业、金融、贸易、会展和航运中心。上海位于中国大陆海岸线中部长江口，拥有中国最大外贸港口和最大工业基地。隔海与日本九州岛相望，南濒杭州湾，西部与江苏、浙江两省相接。上海港货物吞吐量居世界第一。上海是一座新兴的旅游城市，有深厚近代城市文化底蕴和众多历史古迹，举办过世博会。江南的传统与移民带入的文化融合，逐渐形…","id":"19550818"},{"url":"http://www.zhihu.com/api/v4/topics/19564453","avatarUrl":"https://pic4.zhimg.com/f852cfdc7_is.jpg","name":"湖南","introduction":"湖南省，简称「湘」。为中国国家一级行政区；境内广植芙蓉（木芙蓉），古诗有「秋风万里芙蓉国」之句，故有「芙蓉国」之誉。湖南的省会长沙市。","type":"topic","excerpt":"湖南省，简称「湘」。为中国国家一级行政区；境内广植芙蓉（木芙蓉），古诗有「秋风万里芙蓉国」之句，故有「芙蓉国」之誉。湖南的省会长沙市。","id":"19564453"}],"badge":[],"url":"http://www.zhihu.com/api/v4/people/ee99737ba14d20fcc7a131b5065c44fa","messageThreadToken":"2484564100","logsCount":124,"followingQuestionCount":221,"thankedCount":1342,"gender":1},"liaoxuefeng":{"isFollowed":false,"avatarUrlTemplate":"https://pic1.zhimg.com/17237388534b0df48ec200192bb45cc4_{size}.jpg","userType":"people","answerCount":236,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/c32ad3f421f57eaa80782e51ec6a5bde","type":"people","urlToken":"liaoxuefeng","id":"c32ad3f421f57eaa80782e51ec6a5bde","articlesCount":16,"name":"廖雪峰","headline":"业余马拉松选手 &lt;a href=\\"https://link.zhihu.com/?target=http%3A//www.liaoxuefeng.com\\" class=\\" external\\" target=\\"_blank\\" rel=\\"nofollow noreferrer\\"&gt;&lt;span class=\\"invisible\\"&gt;http://www.&lt;/span&gt;&lt;span class=\\"visible\\"&gt;liaoxuefeng.com&lt;/span&gt;&lt;span class=\\"invisible\\"&gt;&lt;/span&gt;&lt;i class=\\"icon-external\\"&gt;&lt;/i&gt;&lt;/a&gt;","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic1.zhimg.com/17237388534b0df48ec200192bb45cc4_is.jpg","isOrg":false,"followerCount":37009,"badge":[]},"sama-elly":{"isFollowed":false,"avatarUrlTemplate":"https://pic2.zhimg.com/v2-2b440dad2c8e7955c068f910a0a78bbd_{size}.jpg","userType":"people","answerCount":11,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/c3465f2bffb0998551b9c20139eed694","type":"people","urlToken":"sama-elly","id":"c3465f2bffb0998551b9c20139eed694","articlesCount":2,"name":"MollyChang","headline":"冷门旅行爱好者/木材加工学生/葡萄酒与烈酒研习生","gender":0,"isAdvertiser":false,"avatarUrl":"https://pic2.zhimg.com/v2-2b440dad2c8e7955c068f910a0a78bbd_is.jpg","isOrg":false,"followerCount":30077,"badge":[]},"langlang0614":{"isFollowed":false,"avatarUrlTemplate":"https://pic1.zhimg.com/v2-81eb926b6ca2decac7ba1852faab3518_{size}.jpg","userType":"people","answerCount":4,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/aee1bb69845226f779ecd351a83eeb02","type":"people","urlToken":"langlang0614","id":"aee1bb69845226f779ecd351a83eeb02","articlesCount":0,"name":"郎朗","headline":"国际著名钢琴家/音乐教育者","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic1.zhimg.com/v2-81eb926b6ca2decac7ba1852faab3518_is.jpg","isOrg":false,"followerCount":50173,"badge":[{"type":"identity","description":"国际著名钢琴家"}]},"li-lao-shu":{"isFollowed":false,"avatarUrlTemplate":"https://pic2.zhimg.com/ecbabb5e5_{size}.jpg","userType":"people","answerCount":132,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/b1bb94da71d973cd44a13b38546d6fd6","type":"people","urlToken":"li-lao-shu","id":"b1bb94da71d973cd44a13b38546d6fd6","articlesCount":199,"name":"李老鼠","headline":"FXXK MY CAR节目主持人  |  old school","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic2.zhimg.com/ecbabb5e5_is.jpg","isOrg":false,"followerCount":246873,"badge":[{"topics":[{"url":"http://www.zhihu.com/api/v4/topics/19570257","avatarUrl":"https://pic1.zhimg.com/3655d622dfc9c0d02fa43213bd43f360_is.jpg","name":"二手车","introduction":"","type":"topic","excerpt":"","id":"19570257"},{"url":"http://www.zhihu.com/api/v4/topics/19551915","avatarUrl":"https://pic4.zhimg.com/e803f3e7a832b035f9bd2dff87033133_is.jpg","name":"汽车","introduction":"汽车，本来是指汽油车，在中国泛指四轮内燃机车，包括汽油车，柴油车，电动车，混动车。汽车由德国人发明，德语词为Automobil，这个词由两部分构成，分别是Auto和Mobil，意为自动运行车，或称为自动车。","type":"topic","excerpt":"汽车，本来是指汽油车，在中国泛指四轮内燃机车，包括汽油车，柴油车，电动车，混动车。汽车由德国人发明，德语词为Automobil，这个词由两部分构成，分别是Auto和Mobil，意为自动运行车，或称为自动车。","id":"19551915"}],"type":"best_answerer","description":"优秀回答者"}]},"zhanghui33":{"isFollowed":false,"avatarUrlTemplate":"https://pic1.zhimg.com/v2-5dbfdbd17c41fd25abcd659849409b64_{size}.jpg","userType":"people","answerCount":6826,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/18e124fe75e59d743ef8e6b578079536","type":"people","urlToken":"zhanghui33","id":"18e124fe75e59d743ef8e6b578079536","articlesCount":54,"name":"肛里拉出个电锯","headline":"贱骚的蔡英文～","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic1.zhimg.com/v2-5dbfdbd17c41fd25abcd659849409b64_is.jpg","isOrg":false,"followerCount":35191,"badge":[]},"tong-da-wei-92":{"isFollowed":false,"avatarUrlTemplate":"https://pic3.zhimg.com/692addb083936cdce679e3d910339572_{size}.jpg","userType":"people","answerCount":3,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/d165a15d55a226dc33002aa19b299631","type":"people","urlToken":"tong-da-wei-92","id":"d165a15d55a226dc33002aa19b299631","articlesCount":0,"name":"佟大为","headline":"","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic3.zhimg.com/692addb083936cdce679e3d910339572_is.jpg","isOrg":false,"followerCount":50429,"badge":[{"type":"identity","description":"演员，代表作品《奋斗》《中国合伙人》等"}]},"leon-huo-70":{"isFollowed":false,"avatarUrlTemplate":"https://pic1.zhimg.com/56d2ee7dd6b59d62b6aff9a492967e10_{size}.jpg","userType":"people","answerCount":28,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/419e1fcccada395aeff55040b130d569","type":"people","urlToken":"leon-huo-70","id":"419e1fcccada395aeff55040b130d569","articlesCount":8,"name":"Leon Huo","headline":"在美留学生","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic1.zhimg.com/56d2ee7dd6b59d62b6aff9a492967e10_is.jpg","isOrg":false,"followerCount":14264,"badge":[]},"huang-yikai":{"isFollowed":false,"avatarUrlTemplate":"https://pic4.zhimg.com/d49520ddf_{size}.jpg","userType":"people","answerCount":140,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/7cc6fd849698a70bbe086baa6d8356bd","type":"people","urlToken":"huang-yikai","id":"7cc6fd849698a70bbe086baa6d8356bd","articlesCount":15,"name":"黄一凯","headline":"00后首席富士脑残粉","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic4.zhimg.com/d49520ddf_is.jpg","isOrg":false,"followerCount":23690,"badge":[{"topics":[{"url":"http://www.zhihu.com/api/v4/topics/19551388","avatarUrl":"https://pic3.zhimg.com/d0786c77632f8287d03205491d731792_is.png","name":"摄影","introduction":"英文摄影 Photography 一词是源于希腊语 φω phos（光线）和 γραφι graphis（绘画、绘图）或γραφη graphê，两字一起的意思是“以光线绘图”。是指使用某种专门设备进行影像记录的过程，一般我们使用机械照相机或者数码照相机进行摄影。有时摄影也会被称为照相，也就是通过物体所反射的光线使感光介质曝光的过程。","type":"topic","excerpt":"英文摄影 Photography 一词是源于希腊语 φω phos（光线）和 γραφι graphis（绘画、绘图）或γραφη graphê，两字一起的意思是“以光线绘图”。是指使用某种专门设备进行影像记录的过程，一般我们使用机械照相机或者数码照相机进行摄影。有时摄影也会被称为照相，也就是通过物体所反射的光线使感光介质曝光的过程。","id":"19551388"}],"type":"best_answerer","description":"优秀回答者"}]},"timothy-wang-17":{"isFollowed":false,"avatarUrlTemplate":"https://pic3.zhimg.com/v2-f20236cd16626d98d25eb001f4419ed6_{size}.jpg","userType":"people","answerCount":256,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/d05de6224118819ddd29f0447da00c07","type":"people","urlToken":"timothy-wang-17","id":"d05de6224118819ddd29f0447da00c07","articlesCount":78,"name":"Timothy Wang","headline":"一念之间，万水千山。","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic3.zhimg.com/v2-f20236cd16626d98d25eb001f4419ed6_is.jpg","isOrg":false,"followerCount":51583,"badge":[{"topics":[{"url":"http://www.zhihu.com/api/v4/topics/19551388","avatarUrl":"https://pic3.zhimg.com/d0786c77632f8287d03205491d731792_is.png","name":"摄影","introduction":"英文摄影 Photography 一词是源于希腊语 φω phos（光线）和 γραφι graphis（绘画、绘图）或γραφη graphê，两字一起的意思是“以光线绘图”。是指使用某种专门设备进行影像记录的过程，一般我们使用机械照相机或者数码照相机进行摄影。有时摄影也会被称为照相，也就是通过物体所反射的光线使感光介质曝光的过程。","type":"topic","excerpt":"英文摄影 Photography 一词是源于希腊语 φω phos（光线）和 γραφι graphis（绘画、绘图）或γραφη graphê，两字一起的意思是“以光线绘图”。是指使用某种专门设备进行影像记录的过程，一般我们使用机械照相机或者数码照相机进行摄影。有时摄影也会被称为照相，也就是通过物体所反射的光线使感光介质曝光的过程。","id":"19551388"}],"type":"best_answerer","description":"优秀回答者"}]},"jessie-7-27":{"isFollowed":false,"avatarUrlTemplate":"https://pic1.zhimg.com/v2-0327a8e3da78df26f7b2edef4b876b54_{size}.jpg","userType":"people","answerCount":2,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/fc5191a5c5ffe74c677508aac8b06217","type":"people","urlToken":"jessie-7-27","id":"fc5191a5c5ffe74c677508aac8b06217","articlesCount":0,"name":"Infanta","headline":"立志成为一枚人类灵魂工程师。","gender":0,"isAdvertiser":false,"avatarUrl":"https://pic1.zhimg.com/v2-0327a8e3da78df26f7b2edef4b876b54_is.jpg","isOrg":false,"followerCount":1,"badge":[]},"chen-yi-61-1":{"isFollowed":false,"avatarUrlTemplate":"https://pic3.zhimg.com/v2-0fedf3683a61b256ef80a5157e69d41a_{size}.jpg","userType":"people","answerCount":4,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/ef06bedeb2a93e8100ec288299e139f1","type":"people","urlToken":"chen-yi-61-1","id":"ef06bedeb2a93e8100ec288299e139f1","articlesCount":0,"name":"陈易","headline":"口味独特，笑点新奇。","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic3.zhimg.com/v2-0fedf3683a61b256ef80a5157e69d41a_is.jpg","isOrg":false,"followerCount":4,"badge":[]},"lin-yu-qiang-33":{"isFollowed":false,"avatarUrlTemplate":"https://pic4.zhimg.com/49badce3a80582430e8b8777f53f0fc3_{size}.jpg","userType":"people","answerCount":30,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/f6347a9bce62487af69d35796689eae4","type":"people","urlToken":"lin-yu-qiang-33","id":"f6347a9bce62487af69d35796689eae4","articlesCount":1,"name":"林峰","headline":"Stay hungry, stay foolish.","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic4.zhimg.com/49badce3a80582430e8b8777f53f0fc3_is.jpg","isOrg":false,"followerCount":172,"badge":[]},"wu-di-wallenberg":{"isFollowed":false,"avatarUrlTemplate":"https://pic1.zhimg.com/v2-af82e9b38491191fed9ef5860308a3f8_{size}.jpg","userType":"people","answerCount":15,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/60d4642f2c8c0c244cf29926bc9197c3","type":"people","urlToken":"wu-di-wallenberg","id":"60d4642f2c8c0c244cf29926bc9197c3","articlesCount":0,"name":"吴迪-Wallenberg","headline":"工科狗，航模狗，跳进CFD大坑的人，奈何想成为文人","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic1.zhimg.com/v2-af82e9b38491191fed9ef5860308a3f8_is.jpg","isOrg":false,"followerCount":143,"badge":[]},"hao-hao-32-13":{"isFollowed":false,"avatarUrlTemplate":"https://pic2.zhimg.com/v2-086f570e98a4dc626006e4cd64aaa265_{size}.jpg","userType":"people","answerCount":943,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/4dbf93964732f2a9e053c3530c2600b5","type":"people","urlToken":"hao-hao-32-13","id":"4dbf93964732f2a9e053c3530c2600b5","articlesCount":10,"name":"徐枭涵","headline":"君不见，班定远，绝域轻骑催战云。","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic2.zhimg.com/v2-086f570e98a4dc626006e4cd64aaa265_is.jpg","isOrg":false,"followerCount":13668,"badge":[]},"yan-yuan-guo-xiao-dong":{"isFollowed":false,"avatarUrlTemplate":"https://pic3.zhimg.com/v2-1746a1ac688cba4287beb88d59f83b8a_{size}.jpg","userType":"people","answerCount":1,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/2099a6523da23e492197991edb7747c4","type":"people","urlToken":"yan-yuan-guo-xiao-dong","id":"2099a6523da23e492197991edb7747c4","articlesCount":0,"name":"演员郭晓东","headline":"电影作品:《暖》《推拿》《河上的爱情》《少年》","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic3.zhimg.com/v2-1746a1ac688cba4287beb88d59f83b8a_is.jpg","isOrg":false,"followerCount":20840,"badge":[]},"li-zi-qing-68-6":{"isFollowed":false,"avatarUrlTemplate":"https://pic2.zhimg.com/c7d53b471237006a318de480af7fd44d_{size}.jpg","userType":"people","answerCount":9,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/9ffd5c016aabeafd1030e63fe410beb8","type":"people","urlToken":"li-zi-qing-68-6","id":"9ffd5c016aabeafd1030e63fe410beb8","articlesCount":0,"name":"豆浆油条","headline":"微博：Cammmilla","gender":0,"isAdvertiser":false,"avatarUrl":"https://pic2.zhimg.com/c7d53b471237006a318de480af7fd44d_is.jpg","isOrg":false,"followerCount":3308,"badge":[]},"wang-xuan-yi-8":{"isFollowed":false,"avatarUrlTemplate":"https://pic2.zhimg.com/v2-898390b43e79f04fc297618b3c98a33d_{size}.jpg","userType":"people","answerCount":32,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/4253447dde7c702d08e6daa724f25062","type":"people","urlToken":"wang-xuan-yi-8","id":"4253447dde7c702d08e6daa724f25062","articlesCount":0,"name":"王选易","headline":"剩余价值","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic2.zhimg.com/v2-898390b43e79f04fc297618b3c98a33d_is.jpg","isOrg":false,"followerCount":2330,"badge":[]},"chenqiangpan":{"isFollowed":false,"avatarUrlTemplate":"https://pic4.zhimg.com/v2-9c51282790de15506c4e469734d6fe7b_{size}.jpg","userType":"people","answerCount":81,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/bf866279f5ca9b430487a6b51cd129cb","type":"people","urlToken":"chenqiangpan","id":"bf866279f5ca9b430487a6b51cd129cb","articlesCount":23,"name":"陈灼","headline":"游戏设计师","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic4.zhimg.com/v2-9c51282790de15506c4e469734d6fe7b_is.jpg","isOrg":false,"followerCount":3422,"badge":[]},"liang-jia-yang":{"isFollowed":false,"avatarUrlTemplate":"https://pic3.zhimg.com/e2523763ff0a845e3cb358fdf3dcbeaa_{size}.jpg","userType":"people","answerCount":55,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/878dd89ec98c6e18328ff9cc611026ae","type":"people","urlToken":"liang-jia-yang","id":"878dd89ec98c6e18328ff9cc611026ae","articlesCount":0,"name":"梁嘉洋","headline":"敏而不疑，缜而不繁；娇而不横，求而不奢；诤而有益，谋而有断；处危有度，历难有瞻。","gender":0,"isAdvertiser":false,"avatarUrl":"https://pic3.zhimg.com/e2523763ff0a845e3cb358fdf3dcbeaa_is.jpg","isOrg":false,"followerCount":19290,"badge":[]},"xiao-gong-ju-de-xiao-wang-zhi":{"isFollowed":false,"avatarUrlTemplate":"https://pic4.zhimg.com/3ed81028c7b8c3a90c95df4a424981b7_{size}.jpg","userType":"people","answerCount":19,"isFollowing":false,"url":"http://www.zhihu.com/api/v4/people/d24f8d67368b9042612c9db314ade14c","type":"people","urlToken":"xiao-gong-ju-de-xiao-wang-zhi","id":"d24f8d67368b9042612c9db314ade14c","articlesCount":0,"name":"古道孤月骨故人","headline":"前浙江人民，现为在河南的江西人民。","gender":1,"isAdvertiser":false,"avatarUrl":"https://pic4.zhimg.com/3ed81028c7b8c3a90c95df4a424981b7_is.jpg","isOrg":false,"followerCount":5,"badge":[]}},"questions":{},"answers":{},"articles":{},"columns":{},"topics":{},"roundtables":{},"favlists":{},"comments":{},"notifications":{},"ebooks":{},"activities":{},"feeds":{},"pins":{},"promotions":{}},"currentUser":"bbc12345001","token":{"xsrf":"56a3f9f05e903545080dbfc0128fa840","carCompose":"QUpCQzljOVpIZ3dYQUFBQVlRSlZUZWdwbjFtVlY0UmtwRU8xRXphZndFWGd0SEU3YVNoMC13PT0=|1501011176|d0f66f2e64fec03d749131edbb174a328a9ebacb","xUDID":""},"account":{"locakTicketStatus":false,"challenge":[],"errorStatus":false,"message":"","isFetching":false},"notification":{},"cookie":"","people":{"isFetching":false,"activitiesByUser":{},"answersByUser":{},"answersSortByVotesByUser":{},"answersMarkedByUser":{},"votedAnswersByUser":{},"thankedAnswersByUser":{},"voteAnswersByUser":{},"thankAnswersByUser":{},"topicAnswersByUser":{},"articlesByUser":{},"articlesSortByVotesByUser":{},"pinsByUser":{},"questionsByUser":{},"commercialQuestionsByUser":{},"favlistsByUser":{},"followingByUser":{"moranzcw":{"isDrained":false,"isFetching":false,"ids":["liaoxuefeng","sama-elly","langlang0614","li-lao-shu","zhanghui33","tong-da-wei-92","leon-huo-70","huang-yikai","timothy-wang-17","jessie-7-27","chen-yi-61-1","lin-yu-qiang-33","wu-di-wallenberg","hao-hao-32-13","yan-yuan-guo-xiao-dong","li-zi-qing-68-6","wang-xuan-yi-8","chenqiangpan","liang-jia-yang","xiao-gong-ju-de-xiao-wang-zhi",null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null,null],"totals":199}},"followersByUser":{},"mutualsByUser":{},"followingColumnsByUser":{},"followingQuestionsByUser":{},"followingFavlistsByUser":{},"followingTopicsByUser":{},"publicationsByUser":{},"columnsByUser":{},"allFavlistsByUser":{},"brands":null},"env":{"experiment":{"ge3":"ge3_9","ge2":"ge2_1","recomLiveAc":"live_ac_d4","nwebStickySidebar":"sticky","homeNweb":"default","favAct":"default","default":"None","newMore":"new","iOSNewestVersion":"3.55.0","qrcodeLogin":"pwd","recomTopicAc":"topic_ac_with_reason","homeUi2":"default","wechatShareModal":"wechat_share_modal_show","qaStickySidebar":"sticky_sidebar","mobileQaPageProxyHeifetz":"m_qa_page_oldweb","liveStore":"ls_a2_b2_c1_f2","zcmLighting":"zcm"},"userAgent":{"Edge":false,"Wechat":false,"Weibo":false,"QQ":false,"Mobile":false,"Android":false,"iOS":false,"isAppleDevice":false,"Zhihu":false,"isBot":false,"isWebView":false},"trafficSource":""},"config":{"isWindow":1,"canWrite":false,"alertTimeSpan":3600,"tip":"应国家法规对于帐号实名的要求，进行下一步操作前，需要先完成手机绑定。"},"pushNotifications":{"default":{"isFetching":false,"isDrained":false,"ids":[]},"follow":{"isFetching":false,"isDrained":false,"ids":[]},"vote-thank":{"isFetching":false,"isDrained":false,"ids":[]},"currentTab":"default","notificationsCount":{"default":0,"follow":0,"vote-thank":0}},"messages":{"data":{},"currentTab":"common","messageCount":0},"register":{"registerValidateSucceeded":null,"registerValidateErrors":{},"registerConfirmError":null,"sendDigitsError":null,"registerConfirmSucceeded":null},"login":{"loginConfirmError":null,"sendDigitsError":null,"loginConfirmSucceeded":null,"qrcodeLoginToken":"","qrcodeLoginScanStatus":0,"qrcodeLoginError":null,"qrcodeLoginReturnNewToken":false},"active":{"sendDigitsError":null,"activeConfirmSucceeded":null,"activeConfirmError":null},"question":{"followers":{},"concernedFollowers":{},"answers":{},"hiddenAnswers":{},"createdAnswers":{},"collapsedAnswers":{},"notificationAnswers":{},"invitationCandidates":{},"inviters":{},"invitees":{},"similarQuestions":{},"relatedLives":{},"bio":{},"brand":{},"commonAnswerCount":0,"hiddenAnswerCount":0},"comments":{"pagination":{},"collapsed":{},"reverse":{},"reviewing":{},"conversation":{},"parent":{}},"shareTexts":{},"answers":{"voters":{},"copyrightApplicants":{},"favlists":{},"newAnswer":{}},"banner":{},"topics":{"bios":{}},"captcha":{"captchaNeeded":false,"captchaBase64String":null,"captchaValidationMessage":null,"loginCaptchaExpires":false},"sms":{"supportedCountries":[]},"explore":{"recommendations":{}},"articles":{"voters":{}},"favlists":{"relations":{}},"pins":{"voters":{}},"topstory":{"topstorys":{"isFetching":false,"isDrained":false,"afterId":0,"items":[],"next":null},"sidebar":null},"upload":{},"video":{"data":{}},"guide":{"guide":{"isFetching":false,"isShowGuide":false}},"switches":{},"coupon":{"isRedeemingCoupon":false}}"""
print(jsss)

dd = json.loads(jsss)

print(dd)
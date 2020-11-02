# coding=utf-8
def a(s):
    import re
    return re.findall(r"\d+\.?\d*",s)

def process(s):
    if s and "(" in s:
        return s.split("|")[-1].strip()



def process(s):
    from lxml import etree
    html = etree.HTML(s,etree.HTMLParser(encoding="utf-8"))
    text = html.xpath(u'//span[contains(text(),"回复")]/text()')
    if text:
        return text[0]

def process(s):
    from lxml import etree
    html = etree.HTML(s,etree.HTMLParser(encoding="utf-8"))
    text = html.xpath(u'//em[contains(text(),"回答数量：")]/text()')
    if text:
        return text[0]

def process(s):
    import time
    if "发表于" in s:
        s = s.split("发表于")[-1]
        create_time = time.strftime("%Y-%m-%d %H:%M:%S", time.strptime(s,"%Y-%m-%d %H:%M:%S"))
        return create_time

def process(s):
    if "<em>" in s:
        return s.split("<em>")[-1].strip()

def process(s):
    s = s.split("<em>")
    for i in s:
        if u"回答数量：" in i:
            return s.split(u"回答数量：")[-1].strip()



def process(s):
    import re
    if s:
        ret = re.findall("<dt>基本信息：</dt>.*?<dd>(.+?)</d",s,re.S)
        if ret:
            ret.strip()
            if " " in s:
                return s.split(" ")[0]
def process(s):
    import re
    if s:
        ret = re.findall("<dt>基本信息：</dt>.*?<dd>(.+?)</dd>",s,re.S)
        if ret:
            return ret[0]
def process(s):
    import re
    if s and u'男' in s:
        return u'男'
    if s and u'女' in s:
        return u'女'

def process(s):
    if s:
        import re
        ret = re.findall("(\d+)",s)
        if ret:
            return ret[0].strip()

def process(s):
    from lxml import etree
    import re
    html = etree.HTML(s,etree.HTMLParser(encoding="utf-8"))
    doc_list_ele = html.xpath('//div[@class="ys_list"]')
    info_list = []
    for doc_ele in doc_list_ele:
        _d = {}
        name = doc_ele.xpath('.//h3')
        first_class_department = doc_ele.xpath('.//h3/em')
        goodat = doc_ele.xpath('.//p')
        content = doc_ele.xpath(".//following-sibling::p[@class='quest_list_main']")
        date = doc_ele.xpath(".//following-sibling::p[2]")
        if name:
         _d["name"] = name[0].text
        if first_class_department:
            _d["first_class_department"] = first_class_department[0].text
        if goodat:
            _d["goodat"] = goodat[0].xpath('string(.)').strip() or None
        if content:
            _d["content"] = content[0].xpath('string(.)')
        if date:
            ret = re.findall("\d+-\d+-\d+ \d+:\d+",date[0].xpath("string(.)"))
            if ret:
                _d["date"] = "{}:00".format(ret[0])
        info_list.append(_d)
    return info_list




html = """
<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">

        <title>糖尿病患者晚上血糖高怎么办_糖尿病_久久问医手机版</title>

		<meta name="baidu-site-verification" content="wRAn557dE3" />
		<meta name="keywords" content="糖尿病患者晚上血糖高怎么办" />
		<meta name="description" content="我有糖尿病家族史，自己血糖总是在6-7之间，白天还可以，临睡前血糖也不高，有事还低于6之下，但到了早上空腹时就高了，这是什么原因？应该怎么办？" />
		<meta
			content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=0"
			name="viewport">
		<meta content="yes" name="apple-mobile-web-app-capable">
		<meta content="black" name="apple-mobile-web-app-status-bar-style">
		<meta http-equiv="Cache-Control" content="no-cache">
		<meta content="telephone=no" name="format-detection">

		<meta name="applicable-device" content="mobile">
		<link rel="canonical" href="http://ask.9939.com/id/6161455/">
		<link rel="miphtml" href="http://mipask.9939.com/id/6161455.html" />

        <link rel="stylesheet" type="text/css" href="/new/css/reset.css"/>
    	<link rel="stylesheet" type="text/css" href="/new/css/style.css"/>
    	<link rel="stylesheet" type="text/css" href="/new/css/swiper.min.css"/>
    	<style>
		.yzm_code_div{
			display: none;
		}
    	</style>

    </head>
    <body>
    	<!-- ads_top -->

            	            	            	<div class="fixed-ad" id="fixed_ad">
		  <div class="fixed-ad-close"></div>
		  <div class="fixed-ad-con">
		 <script type="text/javascript" src="//w18.9939.com/common/api/resource/oya3g.js?pk=cgzsmzs"></script>
		  </div>
</div>


    	<!-- header start  -->
		<header>
		     <a href="" id="logo"><img src="/new/img/logo1.png"></a>
		     <span>问答详情</span>
		     <a href="javascript:;" id="navBtn"></a>
		</header>
		<!-- header end -->
		<!-- 面包屑 -->
		<article class="shocu artin">
		    <a href="https://wapask.9939.com">久久问医</a>&gt;<a href="https://wapask.9939.com" title="https://wapask.9939.com/department/list.html">科室分类</a>&gt;<a href="https://wapask.9939.com/classid/0.html" title="">全部问题</a>&gt;<a href="https://wapask.9939.com/classid/43.html" title="">糖尿病</a>
		</article>
		<!-- 面包屑 -->
		<!-- <section class="ask_tiwen">
		<a href="https://wapask.9939.com/ask/goAskDoctor"><img src="/new/img/ask_tiwen.png"></a>
		</section> -->
		<section>
			<div class="quest_main">
				<ul>
					<li>
			            <h2 class="topci_h2">糖尿病患者晚上血糖高怎么办</h2>
			            <p class="quest_list_main"><i></i>
			            <span>病情描述(女，56岁)</span></br>
			            我有糖尿病家族史，自己血糖总是在6-7之间，白天还可以，临睡前血糖也不高，有事还低于6之下，但到了早上空腹时就高了，这是什么原因？应该怎么办？</br>
			            			            <p>ywfnc<i class="rwrite">2个回答</i><i class="ritime">2016-06-20 15:07</i></p>

			        </li>
				</ul>
			</div>
		</section>



<!-- 替换广告位 -->




<section class="other_quest">
	<h2>全部答案 <span>因不能面诊，医生的建议仅供参考</span></h2>



	    <div class="ys_list">
	        <span><img src="https://home.9939.com/upload/pic/default_female.jpg" alt="张笑颜" title = "张笑颜"></span>
	        <h3>张笑颜 <em>内分泌科</em></h3>
	        <p>

					        </p>
	        	        <div class="green xtzx"><a href="/ask/doctor/1436559">向他咨询</a></div>
	    		    </div>







	    	    <p class="quest_list_main"><i></i>
            <span>病情分析：</span><br>
            <br>
            				<span>指导意见：</span><br />你好，很高兴为您解答问题。如果经常出现扣税前不高，清晨空腹血糖升高的现象，建议午夜之后测一下血糖，有可能是黎明现象导致的反跳。

        </p>
        <p><i class="ritime">2016-06-20 15:10</i></p>

        			<div class="fenge"></div>






	    <div class="ys_list">
	        <span><img src="https://home.9939.com/upload/pic//201509/200036_avatar_middle.jpg" alt="邢******��" title = "邢******��"></span>
	        <h3>邢******�� <em></em></h3>
	        <p>

					        </p>
	        	    </div>







	    	    <p class="quest_list_main"><i></i>
            <span>病情分析：</span><br>
            <br>
            				<span>指导意见：</span><br />你好，与夜间血糖控制欠佳有关。建议你监测睡前血糖，检查糖化血红蛋白，如果糖化血红蛋白低于6.5％，除了空腹血糖略高外，其他时间血糖控制均满意，也可以维持现在的治疗，并继续定期观察血糖。

        </p>
        <p><i class="ritime">2016-06-20 15:14</i></p>



			<!-- 新加广告位end -->



</section>

<article class="know adv">
		<a href="https://myisheng.9939.com/doctor/26/?9939ask"><img style="width:100%;" src="http://wapask.9939.com/images/ads-1.jpg" alt=""></a>
	</article>
	<article class="know adv">
			<!-- 久久问答搜索推荐图文 -->
	<!-- <script type="text/javascript">
    (function() {
        var s = "_" + Math.random().toString(36).slice(2);
        document.write('<div style="" id="' + s + '"></div>');
        (window.slotbydup = window.slotbydup || []).push({
            id: "u3057907",
            container:  s
        });
    })();
</script> -->
<script type="text/javascript" src="//w18.9939.com/site/res/5u2k.js?jewkbfm=kf"></script>
<!-- 多条广告如下脚本只需引入一次 -->

	</article>







			<section>
				<div class="title-bar tjask_icon">类似问题推荐</div>
				<ul class="list_wenzi tjaskli mb10">
											<li><a href="https://wapask.9939.com/id/6144257.html">糖尿病患者如果脚趾出现积血要怎么办</a> </li>
											<li><a href="https://wapask.9939.com/id/8200254.html">我父亲是糖尿病高血压患者 这几天眼睛大面严重充血 该怎么办呢？</a> </li>
											<li><a href="https://wapask.9939.com/id/8144026.html">2型糖尿病患者血小板很低，口腔流血，该怎么办</a> </li>
											<li><a href="https://wapask.9939.com/id/4396780.html">t糖尿病患者长血瘤怎么办</a> </li>
											<li><a href="https://wapask.9939.com/id/3891289.html">我是糖尿病患者有时侯眼睛布满红血丝 怎么办？</a> </li>
											<li><a href="https://wapask.9939.com/id/3798993.html">1型糖尿病患者在什么时间运动合适，运动后出现低血糖怎么办？</a> </li>
											<li><a href="https://wapask.9939.com/id/8146237.html">糖尿病患者血糖持续升高，下不来，迷糊，恶心，怎么办</a> </li>
											<li><a href="https://wapask.9939.com/id/8105281.html">糖尿病患者血糖高居不下该怎么办</a> </li>
									</ul>
			</section>




		<div class="adv_05">
           	<script type="text/javascript" src="//lmz.9939.com/nixjfaefq.js"></script>
        </div>

				<section>
			<div class="title-bar hotjingyan_icon">相关经验</div>
			<ul class="list_wenzi dian">
								<li><a href="https://wapask.9939.com/exp/1555472153181288.html">糖尿病对牙齿有影响吗？</a> </li>
								<li><a href="https://wapask.9939.com/exp/1374917104181025.html">糖尿病应该怎样预防</a> </li>
								<li><a href="https://wapask.9939.com/exp/1374904985181008.html">有没有简单的方法治疗糖尿病</a> </li>
								<li><a href="https://wapask.9939.com/exp/1374913473180985.html">防治糖尿病必须要做到的三点</a> </li>
								<li><a href="https://wapask.9939.com/exp/1374913320180983.html">妊娠期糖尿病朋友的营养方案</a> </li>

			</ul>
			<div class="see_more">
				<a href="https://wapask.9939.com/jingyan/" title="" class="see_more">查看更多相关经验</a>
			</div>
		</section>


		<!-- 		<section>
			<div class="title-bar hotask_icon">热门回答</div>
			<ul class="list_wenzi hotaskli mb10">
							<li><a href="https://wapask.9939.com/id/8478825.html">小孩几岁了长牙是比较正常的？</a> </li>
							<li><a href="https://wapask.9939.com/id/8478824.html">内痔和直肠脱垂该怎么治疗好？</a> </li>
							<li><a href="https://wapask.9939.com/id/8478826.html">怀孕后做四维该注意什么？</a> </li>
							<li><a href="https://wapask.9939.com/id/8478822.html">鼻涕出现血丝是什么引起的？</a> </li>
							<li><a href="https://wapask.9939.com/id/8478818.html">男性生吃生蚝有什么好处吗？</a> </li>
							<li><a href="https://wapask.9939.com/id/8478823.html">怀孕早期吃生蚝会引起流产吗？</a> </li>

			</ul>

		</section>
		 -->




		<!-- 		<section>
			<div class="title-bar watch">大家都在看</div>
			<div class="main_tab">

				<div class="flicking_main ">
					<div class="tabBoxwenz mb10">
						<ul class="list_wenzi dian">

			              <li><a href="https://m.jb.9939.com/article/2015/1112/314219.shtml">女性产后抑郁症怎么办?有啥危害?</a> </li>

			              <li><a href="https://m.jb.9939.com/article/2015/1112/313255.shtml">我得了痛风怎么办</a> </li>

			              <li><a href="https://m.jb.9939.com/article/2015/1112/313238.shtml">尿酸高引起痛风怎么办</a> </li>

			              <li><a href="https://m.jb.9939.com/article/2015/1112/311013.shtml">宝宝得了厌食症怎么办？</a> </li>

			              <li><a href="https://m.jb.9939.com/article/2015/1112/310387.shtml">糖尿病患者血糖低了怎么办</a> </li>

						</ul>
					</div>

				</div>
			</div>

		</section>
		 -->


				<section>
			<div class="title-bar hotci_icon">相关热词</div>
			<ul class="list_wenzi dian pre50">
									<li><a href="https://wapask.9939.com/top/tnbzz81/">糖尿病症状</a> </li>
									<li><a href="https://wapask.9939.com/top/tnbncsmsg82/">糖尿病能吃什么水果</a> </li>
									<li><a href="https://wapask.9939.com/top/tnbdzqzz83/">糖尿病的早期症状</a> </li>
									<li><a href="https://wapask.9939.com/top/tnbys84/">糖尿病饮食</a> </li>
									<li><a href="https://wapask.9939.com/top/tnbnhdj85/">糖尿病能活多久</a> </li>
									<li><a href="https://wapask.9939.com/top/tnbrcsmsgh86/">糖尿病人吃什么水果好</a> </li>
									<li><a href="https://wapask.9939.com/top/rstnb87/">妊娠糖尿病</a> </li>
									<li><a href="https://wapask.9939.com/top/tnbbfz88/">糖尿病并发症</a> </li>
									<li><a href="https://wapask.9939.com/top/rsqtnb89/">妊娠期糖尿病</a> </li>
									<li><a href="https://wapask.9939.com/top/tnbdyszl90/">糖尿病的饮食治疗</a> </li>
							</ul>
		</section>


		<article class="know adv">
			<!-- <h3 class="reask" style="margin-top: 10px;">大家都在看</h3>

<script type="text/javascript">
	(
		function() {
			document
					.write(unescape('%3Cdiv id="bdcsFrameTitleBox"%3E%3C/div%3E'));
			var bdcs = document.createElement("script");
			bdcs.type = "text/javascript";
			bdcs.async = true;
			bdcs.src = "http://znsv.baidu.com/customer_search/api/rs?sid=11390991775594799180"
					+ "&plate_url="
					+ encodeURIComponent(window.location.href)
					+ "&t="
					+ Math.ceil(new Date() / 3600000)
					+ "&type=3";
			var s = document.getElementsByTagName("script")[0];
			s.parentNode.insertBefore(bdcs, s);
		})();
</script> -->



<!-- <script type="text/javascript" src="/js/jquery.event.drag-1.5.min.js"></script>
<script type="text/javascript" src="/js/jquery.touchSlider.js"></script>
<script type="text/javascript" src="/js/slide.js"></script> -->
		</article>




		<!-- 百度联盟 开始 -->


	    <!-- 百度联盟 结束 -->
		<footer class="footer">
			<div class="f_nav">
				<a href="/">首页</a>
				<a href="https://m.9939.com/Bottom">网站简介</a>
				<a href="https://m.9939.com/Bottom/zlhz">战略合作</a>
				<a href="https://m.9939.com/Bottom/contact">联系我们</a>
				<a href="https://m.9939.com/Bottom/feedback">意见反馈</a>
			</div>
			<div class="f_copy">京ICP备09011420号 <br>久久健康网<a href="https://m.9939.com">m.9939.com</a></div>
		</footer>
<!-- 头部隐藏 -->
		<article class="heabar">
			<div class="heaber_be">
		        <div class="tj_bx1">
		            <ul>
		                <li><a href="https://wapask.9939.com/ask/goAskDoctor" title="问医"><i class="tjd_ico01"></i><span>问医生</span></a></li>
		                <li><a href="http://m.jb.9939.com/" title="疾病"><i class="tjd_ico02"></i><span>查疾病</span></a></li>
		                <li><a href="http://m.9939.com/yiyuan/" title="找医院"><i class="tjd_ico03"></i><span>找医院</span></a></li>
		                <li><a href="http://m.9939.com/yi/" title="药品"><i class="tjd_ico04"></i><span>找药品</span></a></li>
		            </ul>
		        </div>
		        <h3><span>资讯</span></h3>
		        <div class="info">
		            <a href="https://m.9939.com/baby/">母婴</a>
					<a href="https://m.9939.com/lady/">女性</a>
					<a href="https://m.9939.com/man/">男性</a>
					<a href="https://wapask.9939.com/">问答</a>
					<a href="https://m.9939.com/oldman/">老人</a>
					<a href="https://m.9939.com/baojian/">保健</a>
					<a href="https://m.9939.com/js/">健身</a>
					<a href="https://m.9939.com/food/">饮食</a>

					<a href="https://m.9939.com/beauty/">美容</a>
					<a href="https://m.9939.com/zx/">整形</a>
					<a href="https://m.9939.com/fitness/">减肥</a>
					<a href="https://m.9939.com/xinli/">心理</a>
					<a href="https://m.9939.com/tijian/">体检</a>
					<a href="https://m.9939.com/news/">新闻</a>
					<a href="https://m.9939.com/zhongyi/">中医</a>
					<a href="https://m.9939.com/nurse/">护理</a>
					<a href="https://m.9939.com/pianfang/">偏方</a>

					<a href="https://m.9939.com/zhuanti/">专题</a>
					<a href="https://m.9939.com/baby/zhuanti/">热搜</a>
		        </div>

		        <div class="logout" style="display: none;">
		        	<div><a class="lotal" href=""><span id="lotal-username"></span></a></div>
		            <a href="javascript:" class="logout_user">个人中心</a>
		            <a href="javascript:" class="logout_userout">退出</a>
		            <iframe id="remove" src="" style = "display: none;"></iframe>
		        </div>
		        <div class="login">
		            <a href="https://wapask.9939.com/login" class="loginicon">登录</a>
		            <a href="https://wapask.9939.com/login/goregister" class="regicon">注册</a>
		        </div>
		        <span class="arrow"></span>
		    </div>

		</article>
<!-- 头部隐藏 -->
		<script type="text/javascript" src="/new/js/jquery-1.11.0.min.js"></script>
		<script type="text/javascript" src="/new/js/jquery.SuperSlide.2.1.1.js"></script>
		<script type="text/javascript" src="/new/js/index.js"></script>
		<script type="text/javascript" src="/new/js/common.js?v20170926"></script>
		<script type="text/javascript" src="//cpro.baidustatic.com/cpro/ui/cm.js" async="async" defer="defer" ></script>
		<script type="text/javascript">

		function getCookie(name)
		{
		var arr,reg=new RegExp("(^| )"+name+"=([^;]*)(;|$)");
		if(arr=document.cookie.match(reg))
		return unescape(arr[2]);
		else
		return null;
		}

		window.onload=function(){
				var login_url = $('.loginicon').attr('href');
				//login_url += '?'+Math.random();
				$('.loginicon').attr('href',login_url);
	            var userid = window.localStorage.getItem('userid');
	            if(!userid){
	            	userid = getCookie('member_uID');
	            }

	            var username = window.localStorage.getItem('username');
	            if(!username){
	            	username = getCookie('member_username');
	            }

	            var link = "https://wapask.9939.com/doctor/usercenter?userid=" + userid;
	            if (typeof (userid)!="undefined" && parseInt(userid)>0){
	                $('.login').hide();
	                $('#lotal-username').text(username);
	                $('.logout_user').attr('href', link);
	                //$('.logout_userout').attr('href', link);
	                //$('.lotal').attr('href', link);
	                //$(".lotal > span").text(username);
	                //$('.lotal').show();
	                $('.logout').show();
	            } else {
	                $('.login').show();
	            }

	            $(".logout_userout").on('click', function(){
					window.localStorage.removeItem('userid');
					window.localStorage.removeItem('username');
		             //删除 m.9939.com 中的本地缓存(userid)
		            var rd = Math.random();
		            var clear_url = 'https://m.9939.com/remove.php?r='+rd;
		            $("#remove").attr('src',clear_url);
		            var url = 'https://wapask.9939.com/login/logout?userid=' + userid;
		            window.location.href = url;
				});



	        };
		</script>

<!-- 问答页面统计功能代码 -->

<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "https://hm.baidu.com/hm.js?ca9632a494dcdce55cdd58f956aa9f6e";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<script type="text/javascript" src='https://w.cnzz.com/c.php?id=1256546982&l=3'></script>

		<script type="text/javascript">
			$('.doc_huida').click(function() {
				$(this).hide();
			        $('#answer_form').show();

			 });



			$('#chk-phone-btn').click(function() {
			        var phone = $('#phone').val();
			        if(phone == ''){
			            alert('请输入手机号');
			        }else{
			        	//$('.yzm_code_div').show();
			            $.ajax({
			                type: "GET",
			                url: "https://wapask.9939.com/api/send/",
			                data: {mobile:phone},
			                dataType: "html",
			                success: function(data){
			                    //alert(data);
			                    if(data == '发送成功'){
			                        $('#chk-phone-btn').attr('disabled',true);
			                        $('#phone').attr('readonly',true);
			                        alert('请填入手机短信验证码，并初始化您的密码');
			                        $('.yzm_code_div').show();
			                    }else{
			                        alert('error');
			                        $('.yzm_code_div').hide();
			                    }

			                }
			             });
			        }

			 });


			var member_uType = "";

			(function(){

				jQuery("#leftTabBox").slide({autoPlay:true});
				jQuery(".main_tab").slide({
			        titCell:".flicking_con",
			        mainCell:".flicking_main",
			        effect:"left",
			        interTime:"4000",
			        autoPlay:true,
			        autoPage:true
			    });
			})();

			function answer_check(){


				var prohibit_reply = parseInt($('#answer_submit').attr('data-prohibit_reply'));

		        if(prohibit_reply==1){
		            alert('当前问题已关闭,请回复别的问题!');
		            return false;
		        }


		        if (member_uType == 2) {
		        	var _counter = $(".xtzx").length;
		            if (_counter >= 2) {
		                alert('当前问题已有2人回复，请回复别的问题。');
		                return false;
		             }
		        }


				var answer_content = $('#answer_content').val();
				if(answer_content.length <= 0 ){
					alert('字数不能为空');
					return false;
				}

				if(answer_content == '请根据患者提问的内容，给予专业详尽的指导意见。'){
					alert('请输入病情分析');
					return false;
				}

				var answer_suggest = $('#answer_suggest').val();

				if(answer_suggest.length <= 0 ){
					alert('字数不能为空');
					return false;
				}


				if(answer_suggest == '请给出具体的运动，饮食，康复等方面的指导。'){
					alert('请输入指导意见');
					return false;
				}



				$('#answer_form').submit();

			}
		</script>

			            <!-- 新加广告位end -->
    </body>
</html>"""
print(process(html))
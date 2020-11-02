#encoding:utf-8
html = '''
<!DOCTYPE html>
<!--STATUS OK-->
<html>
<head>
<meta http-equiv="X-UA-Compatible" content="IE=Edge" />
<meta http-equiv="content-type" content="text/html;charset=gbk" />
<meta property="wb:webmaster" content="3aababe5ed22e23c" />
<meta name="referrer" content="always" />
<title>吃辣条引起糖尿病酮症酸中毒？这个锅，辣条不背哦！_蝌蚪五线谱_知道日报_百度知道</title>
<link rel="shortcut icon" href="//www.baidu.com/favicon.ico?t=20171027" type="image/x-icon" />
<link rel="icon" sizes="any" mask href="//www.baidu.com/img/baidu.svg" />

<script>
    window.alogObjectConfig = {
        product: '102',
        page: '',
        monkey_page: '',
        speed_page: '',
        speed: {
            sample: ''
        },
        monkey: {
            sample: ''
        },
        exception: {
            sample: ''
        },
        feature: {
            sample: ''
        },
        cus: {
            sample: '',
            custom_metrics: []
        },
        csp: {
            sample: '',
            'default-src': [
                {match: '*bae.baidu.com', target: 'Accept,Warn'},
                {match: '*.baidu.com,*.bdstatic.com,*.bdimg.com,localhost,*.hao123.com,*.hao123img.com', target: 'Accept'},
                {match: /^(127|172|192|10)(\.\d+){3}$/, target: 'Accept'},
                {match: '*', target: 'Accept,Warn'}
            ]
        }
    };

    void function(a,b,c,d,e,f,g){a.alogObjectName=e,a[e]=a[e]||function(){(a[e].q=a[e].q||[]).push(arguments)},a[e].l=a[e].l||+new Date,d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d;var h=!0;if(a.alogObjectConfig&&a.alogObjectConfig.sample){var i=Math.random();a.alogObjectConfig.rand=i,i>a.alogObjectConfig.sample&&(h=!1)}h&&(f=b.createElement(c),f.async=!0,f.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),g=b.getElementsByTagName(c)[0],g.parentNode.insertBefore(f,g))}(window,document,"script","/hunter/alog/alog.min.js","alog"),void function(){function a(){}window.PDC={mark:function(a,b){alog("speed.set",a,b||+new Date),alog.fire&&alog.fire("mark")},init:function(a){alog("speed.set","options",a)},view_start:a,tti:a,page_ready:a}}();
    void function(n){var o=!1;n.onerror=function(n,e,t,c){var i=!0;return!e&&/^script error/i.test(n)&&(o?i=!1:o=!0),i&&alog("exception.send","exception",{msg:n,js:e,ln:t,col:c}),!1},alog("exception.on","catch",function(n){alog("exception.send","exception",{msg:n.msg,js:n.path,ln:n.ln,method:n.method,flag:"catch"})})}(window);
</script>
<script type="text/javascript">
    window.perfConfig = {
        sample: '0.1',
        options: {}
    };
    (function (global) {
        if (Math.random() <= global.perfConfig.sample) {
            var isSupportObserver = !!window.PerformanceObserver;
            var iPerformance = global.iPerformance = function () {
                if (isSupportObserver) {
                    var observer = new PerformanceObserver(function(list) {
                        list.getEntries().forEach(function(entry) {
                            // chrome都支持，safari都不支持，ie和火狐支持mark
                            if (entry.entryType === 'paint' || entry.entryType === 'mark') {
                                let name = entry.name;
                                if (entry.name === 'first-paint') {
                                    name = 'fp';
                                } else if (entry.name === 'first-contentful-paint') {
                                    name = 'fcp';
                                }
                                global.perfConfig.options[name] = entry.startTime + entry.duration;
                            }
                        })
                    });
                    observer.observe({entryTypes: ['paint', 'mark']});
                }
            };
            let performance = global.performance || global.msPerformance || global.webkitPerformance || {};
            // timeOrigin: 文档开始的double时间戳
            iPerformance.startTime = performance.timeOrigin || (+new Date);
            iPerformance.mark = function (name, time) {
                if (isSupportObserver) {
                    performance.mark(name);
                }
                // performance.now(): 从time origin之后到当前调用时经过的时间
                global.perfConfig.options[name] = performance.now() || time || +new Date;
            };

            iPerformance();
        }
    })(window);
</script>

<script>
	!function(document, window){
		var log = {
			list: [],
			host: 'https://' + location.host + '/api/httpscheck',
			log: function(param) {
				var a = [];
		    	for(var k in param) {
		    		a.push(k + '=' + param[k]);
		    	}
		    	var msg = a.join('&');
		    	if(~this.list.indexOf(msg)){
		    		return;
		    	}
		    	this.list.push(msg);
		  		var img = new Image();
		    	var key = '_ik_log_' + (Math.random()*2147483648 ^ 0).toString(36);
		    	window[key] = img;
		    		img.onload = img.onerror = img.onabort = function() {
		        		img.onload = img.onerror = img.onabort = null;
		        		window[key] = null;
			    		img = null;
		    	};
		  		img.src = this.host + '?' + msg;
			}
		};

		function HTTPSWarningLog(){
			this.selector = [
				'link',
				'script',
				'img',
				'embed',
				'iframe'
			];
			this.warningCounter = 0;
			this.init();
		};

		HTTPSWarningLog.prototype = {
			init: function(){
				this.fetch();
			},

			fetch: function(){
				for(var tags = this.selector, i =0, len = tags.length; i < len;i++) {
					this.getTag(tags[i]);
				}
			},

			getTag: function(tag) {
				var domList = document.getElementsByTagName(tag);
				if(!domList.length) {
					return;
				}
				for(var i = 0,len = domList.length;i<len;i++) {
					var el = domList[i];
					var url = el.getAttribute(el.tagName==='LINK' ? 'href' : 'src');
                    if(el.getAttribute('rel') === 'canonical') {
                        continue;
                    }
					if(url && 'https:' === location.protocol && !url.indexOf('http:')){
						this.sendLog(el, el.tagName.toLowerCase(),url);
						this.warningCounter++;
					}
				}
			},

			sendLog: function(el, type, url){
				log.log({
					url: location.href,
					wtype: type,
					wurl: url
				});
			}
		};

		function domReady(fn){
		    if(document.addEventListener) {
		        document.addEventListener('DOMContentLoaded', function() {
		            document.removeEventListener('DOMContentLoaded',arguments.callee, false);
		            fn();
		        }, false);
		    }else if(document.attachEvent) {
		        document.attachEvent('onreadystatechange', function() {
		            if(document.readyState == 'complete') {
		                document.detachEvent('onreadystatechange', arguments.callee);
		                fn();
		            }
		        });
		    }
		};

		domReady(function(){
			new HTTPSWarningLog();
			for(var i=1; i<6; i++) {
				!function(i){
					setTimeout(function(){
						new HTTPSWarningLog();
					}, i*i*i*1000);
				}(i);
			}
		});
	}(document, window);
</script>

<meta name="keywords" content=" 蝌蚪五线谱 知道日报 百度知道 zhidao" />
<meta name="description" content='吃辣条引起糖尿病酮症酸中毒？这个锅，辣条不背哦！' />

<script type="text/javascript">
			!function(){var n={},t={};n.context=function(n,e){var i=arguments.length;if(i>1)t[n]=e;else if(1==i){if("object"!=typeof n)return t[n];for(var o in n)n.hasOwnProperty(o)&&(t[o]=n[o])}},"F"in window||(window.F=n)}();;



			F.context('user', {"isLogin":"1","isRealName":"2","stoken":"42f8dbc5109acf851913dfe3c81ead12","name":"\u5c0f\u745fce","imId":"309ad0a1c9aa6365a15e","id":"","euid":"309a4069236f25705e79a15e","wealth":"","gradeIndex":"2","isMavin":"","encryptedBDUSS":"936exR+6HeVYo0prNsey2w2wDga1MJLiTAtIg4E6tJLllWHWTgICuoqfnr5Mn\/zwbx77PZLmGnpTPvwBBzz1jPrQ\/1uAv0hY9XOawU6WMMeSK3dOzOehqsH+MTiQOo852qR7ZGX35dwQy+mUODGs96H5bSx6+3j\/wS8Rc8wVklTa28MLZWzqUX5TXnaqrjn7M26WIiMjmkzpzOjIyGWcmcaLFYcemzW35xGmfcmE\/YdMZSKPiWlVFNdQXJh05uFu5zidksUZaRuX+6ubTJ\/A6YzcMcG9GCXOcFfaD7g","ECBD":"*"});
			F.context('user')['internalAdmin'] = [];


			            F.context('isQuality', false);
            F.context('now', 1603936319);
		</script>
<script>F.context('sysTaskAutoInit', 1);</script>
<!--[if lte IE 8]>
<script>
                (function(){
                    var e="abbr,article,aside,audio,canvas,datalist,details,dialog,eventsource,figure,footer,header,hgroup,mark,menu,meter,nav,output,progress,section,time,video".split(","),
                    i=e.length;
                    while(i--){document.createElement(e[i])}
                 })();
            </script>
<![endif]-->
<link rel="stylesheet" type="text/css" href="https://iknowpc.bdimg.com/static/common/pkg/common.6ebdc78.css" /><link rel="stylesheet" type="text/css" href="https://iknowpc.bdimg.com/static/common/widget/header-metis/header.39c9ddf.css" /><link rel="stylesheet" type="text/css" href="https://iknowpc.bdimg.com/static/common/widget/set-tag/set-tag.0b3a009.css" /><link rel="stylesheet" type="text/css" href="https://iknowpc.bdimg.com/static/common/widget/task/task-last.1ba3b2d.css" /><link rel="stylesheet" type="text/css" href="https://iknowpc.bdimg.com/static/daily/pkg/module.bd1979a.css" /><link rel="stylesheet" type="text/css" href="https://gss0.bdstatic.com/7051cy792sgCpNKfpU_Y_D3/static/com-brand/pkg/com-brand_f83454b.css" /></head>

<script> alog('speed.set', 'ht', +new Date()); </script>

<body class="daily-view">


<div id="userbar" class="userbar userbar-renew " data="">
<ul class="aside-list">
<li>
<a href="http://www.baidu.com/" class="toindex">百度首页</a>
</li>
<li>
<a href="/ihome" class="user-name" target="_blank" id="user-name">小瑟ce<i class="i-arrow-down"></i></a></li>
</li>
<li alog-alias="userbar-msg" id="userbar-msg"><a class="userbar-msg-a" href="/ihome/notice/center" target="_blank" target="_self">消息<span class="orange-num"><i></i></span></a></li>
<li alog-alias="baidu-msg" id="baidu-msg"><a href="/ichat/chatlist">私信<i class="bd-msg"></i></a></li>
<li class="shop-entrance">
<a href="/shop" title="知道商城">商城<i class="i-house" style="display: none;"></i></a>
<span class="lucky-try" style="display: none"></span>
</li>
</ul>
<div class="sublist-container username-sublist" style="display:none" id="username-sublist">
<div class="sublist-arrow-up"></div>
<ul class="sub-list">
<li><a id="userbar-myinfo" href="/ihome/homepage/recommendquestion" target="_blank">我的主页</a></li>
<li><a id="userbar-my-ask" href="https://zhidao.baidu.com/ihome/homepage/myask" target="_blank">我的提问</a></li>
<li><a id="userbar-my-answer" href="https://zhidao.baidu.com/ihome/homepage/myanwser" target="_blank">我的回答</a></li>
<li><a id="userbar-my-task" href="https://zhidao.baidu.com/ihome/homepage/mytask" target="_blank">我的任务</a></li>
<li><a id="userbar-account" href="http://passport.baidu.com/center" target="_blank">帐号设置</a></li>
<li class="last"><a href="http://passport.baidu.com/?logout&amp;aid=7&amp;u=http%3A//zhidao.baidu.com" id="userbar-logout">退出帐号</a></li>
</ul>
</div>
</div>



<div class="head-wrap">
<header id="header" class="container">

<div class="daily-search-box-wp fixed">
<div class="daily-search-box container-wide">
<div class="logo-wp">
<a href="/" class="zhidao-logo"></a><span>|</span><a href="/daily/" class="daily-logo"></a>
</div>
<form action="/daily/search" name="search-form" method="get" id="search-form" class="search-form">
<input class="hdi" id="kw" maxlength="256" tabindex="1" size="46" name="word" value="" autocomplete="off" placeholder="输入关键字或作者名"/>
<input type="hidden" name="ie" value="gbk">
<button alog-action="g-search-anwser" type="submit" id="search-btn" hidefocus="true"  tabindex="2" class="btn-global">搜索日报</button>
<a href="#" alog-action="g-i-ask" class="i-ask-link" id="ask-btn">我要提问</a>
</form>
</div>
</div>

</header>
</div>
<div id="body" class="container">


<div class="menu-wp">
<div id="menu" class="menu">
<div class="main-menu">
<a href="/daily" class="" data-index="1" data-log="type:2060,action:click,area:main-menu-0,page:daily-all">精选</a><a href="/daily/square" class=" menu-found" data-index="2" data-log="type:2060,action:click,area:main-menu-1,page:daily-all">发现<i class="found-tip" title="有新文章，等你来读"></i></a><a href="/daily/focusdaily" class="" data-index="3" data-log="type:2060,action:click,area:main-menu-2,page:daily-all">收藏/关注</a><a href="/daily/authorcenter" class="authorcenter " data-index="4" data-log="type:2060,action:click,area:main-menu-3,page:daily-all">
<i></i>
作者中心</a>
</div>
</div>
</div>
<div class="container-wide content">
<div class="row clearfix">
<div class="main grid">
<div class="detail-wp">
<div class="detail" id="j-daily-union-dom">
<div class="figure">
<img id="daily-img" src="https://iknow-pic.cdn.bcebos.com/2934349b033b5bb5e2bf0ae73ad3d539b600bcba?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1/quality,q_85" alt="吃辣条引起糖尿病酮症酸中毒？这个锅，辣条不背哦！的头图">
</div>
<h1 id="daily-title" class="title">
吃辣条引起糖尿病酮症酸中毒？这个锅，辣条不背哦！
</h1>
<div class="info">
<span>2018-03-12</span>
<span class="text-line">&nbsp;|&nbsp;</span>
<a href="/daily/author?un=蝌蚪五线谱&amp;ie=gbk" target="_blank" data-log="type:2060,action:click,area:detail-author,page:daily-view"><span class="name">蝌蚪五线谱</span></a>
<span class="original">原创</span>
<input type="text" id="author-id" style="display: none" value="9">
<a href="#" class="focus unfocus" data-log="type:2060,action:click,area:detail-focus,page:daily-view">
<b></b>
收藏(2)</a>
<span class="text-line text-line2">&nbsp;|&nbsp;</span>
<span id="pv" class="pv"></span>
</div>
<div id="daily-cont" class="cont">
<p>辣条，是一种很神奇的食物。80后喜欢它，90后它，00后也喜欢它。虽不是“大自然的馈赠”，但经受住了岁月的洗礼；甚至有冲出中国、走向世界的势头……</p><p><img src="https://iknow-pic.cdn.bcebos.com/91529822720e0cf3cf5a67e20646f21fbe09aa7d?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p><p style="text-align: center;"><sup>辣条（图片来源：amazon.com）</sup></p><p>与此同时，辣条也一直顶着垃圾食品的恶名。最近就有媒体报道，一名少年因为吃了十几包辣条，昏迷、住院。虽然医生很快辟谣，“患者并没有吃那么多辣条”、“昏迷原因是糖尿病酮症酸中毒”，<sup>【1】</sup>但是，这又引出了新的问题——什么是糖尿病酮症酸中毒，它跟辣条有什么关系？</p><p><img src="https://iknow-pic.cdn.bcebos.com/e7cd7b899e510fb3b1c55e8ed533c895d0430cce?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p><p style="text-align: center;"><sup>新闻图片（图片来源：thepaper.cn）</sup></p><p>糖尿病酮症酸中毒（Diabetic ketoacidosis，DKA），这名字乍一看有点唬人，其实拆开来看，无非是三件事：糖尿病、酮症和酸中毒。</p><p>首先是糖尿病。提到糖尿病，很多读者会想到血糖。其实，高血糖只是糖尿病的典型表现之一，糖尿病患者体内，同时存在着多种代谢紊乱。</p><p>人体内的三大营养物质，糖、脂肪和蛋白质，虽然都可以提供能量，但是有着不同的优先级。糖最好，最方便，平常储藏在肝脏内，需要的时候招呼一声就行了，有些组织，比如脑，更是只能利用糖；不过，肝脏内的糖，也就够用十几个小时，如果一整天都没有吃东西，机体便会动员脂肪；至于蛋白质，蛋白质具有多种生理功能，单纯用于供能，是因小失大，所以，不到万不得已，人体不会大量分解蛋白质。</p><p><img src="https://iknow-pic.cdn.bcebos.com/0d338744ebf81a4c7579c5d0db2a6059252da65b?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p><p style="text-align: center;"><sup>三大营养物质可以转化（图片来源：slidesplayer.com）</sup></p><p>正常情况下，胰岛素（insulin）负责降低血糖，一方面促进各组织对血糖的利用，另一方面，把血液中多余的糖分，打包存储到肝脏内；胰高血糖素（Glucagon），负责升高血糖，如果肝脏内的糖可以用，就加速肝糖原的分解，如果肝脏内的糖不够用或者不能用，就只好想些别的法子——动员脂肪，把脂肪分解为甘油和脂肪酸，甘油和脂肪酸可以在肝脏内转换为糖类，供身体利用。</p><p>问题在于，当血糖紊乱的时候，肝脏往往不能正常工作，于是这些脂肪酸，就会变成酮体。<sup>【2】</sup>这就是酮症。</p><p><img src="https://iknow-pic.cdn.bcebos.com/c83d70cf3bc79f3d610dcd29b6a1cd11728b293e?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p><p style="text-align: center;"><sup>酮症（图片来源：dtc.ucsf.edu）</sup></p><p>酮体是一个统称，包括β-羟丁酸、乙酰乙酸和丙酮三种物质。其中，丙酮具有烂苹果味，容易挥发，可随呼吸排出体外；β-羟丁酸、乙酰乙酸，都是强酸。<sup>【3】</sup></p><p>强酸对人体是不利的，不然的话，我们早就像异形一样称霸宇宙了……</p><p>当出现大量强酸时，身体会进行代偿，把酸碱度维持在合适的水平。</p><p>血液内存在弱碱性物质，如碳酸氢根（HCO<sub>3</sub><sup>?</sup>）。碳酸氢根和酸性物质（如氢离子，H<sup>+</sup>）相遇以后，会互相结合，生成二氧化碳和水分。水分是无害的，二氧化碳则可以通过呼吸排出体外，所以在酸中毒早期，患者的呼吸会加快。</p><p style="text-align: center;"><strong>HCO<sub>3</sub><sup>?</sup>+H<sup>+</sup> ? H<sub>2</sub>O+CO<sub>2</sub></strong></p><p>肾脏也可以代偿。肾脏可以分泌、排出酸性物质，同时吸入、回收尿液中的碱性物质。不过，这种吸收，速度比较慢，有一定的限度，而且要满足特定的条件，即渗透压差。把黄瓜泡到盐水里，黄瓜会缩水、变皱。这是因为黄瓜细胞的渗透压比盐水低，黄瓜内的水分子跑到了盐水内。肾脏内的渗透压必须比尿液高，才能保证重新吸收能力。</p><p><img src="https://iknow-pic.cdn.bcebos.com/730e0cf3d7ca7bcb10d6ee36b2096b63f624a87d?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p><p style="text-align: center;"><sup>尿液生成示意图（图片来源：wen31.com）</sup></p><p>最后是细胞。细胞膜会把一部分氢离子运输到细胞内，同时排出钾离子（K<sup>+</sup>）。钾离子，对维持心脏的正常搏动，有着重要意义。</p><p>当然，代偿是万不得已，是已经出现问题时的补救策略，终究有一个限度。如果超出了这个限度，就会出现一系列的失代偿表现。首先，如果酸中毒一直没有缓解甚至恶化，呼吸会受到抑制；其次，在酮症期间，尿液里含有大量未被利用的物质，渗透压反而比肾脏高，于是患者会尿多、尿频，丢失大量水分；血液中的钾离子过多，会引起心跳加速；如果治疗不当，血液中的钾离子大量进入细胞内，则有可能引起心律失常，严重时可以导致心脏骤停。除此之外，血液中大量的酸，还会影响血红蛋白与氧气的解离速度，进而诱发组织缺氧。</p><p>所以，糖尿病酮症酸中毒在早期表现为多尿、口渴和呼吸加深加快，最典型的表现是，呼出的气体有烂苹果味；随着病症加重，因为水分丢失过多、电解质平衡紊乱，会出下心率加快、血压下降；严重时，可引起昏迷，甚至死亡。<sup>【2】</sup></p><p><img src="https://iknow-pic.cdn.bcebos.com/574e9258d109b3dee212cd71c0bf6c81800a4c7d?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p><p style="text-align: center;"><sup>糖尿病酮症酸中毒的临床表现（图片来源：dmnote.tw）</sup></p><p>糖尿病酮症酸中毒是糖尿病最常见的急症，所以对于糖尿病患者来说，一定要学会积极预防。首先，是避免感染。细菌与病毒侵入人体以后，人体会进入“战争状态”，大量调动“物资”、消灭入侵者。为了调动“物资”，人体会分泌胰高血糖素，加重胰岛素不足、引起脂肪分解增加。其次，是定期、足量注射胰岛素，尤其是I型糖尿病患者。I型糖尿病意味着机体分泌的胰岛素绝对不足，一定不要有侥幸心理。只要有条件，就应该学会监测自己的血糖；出现疑似糖尿病酮症酸中毒的症状以后，必须尽快就医。最后，是避免过量饮酒和过量进食。暴饮暴食对一般人，都是有害的，何况是血糖代谢紊乱的糖尿病患者呢？<sup>【4,5】</sup>至于辣条，那不过是暴饮暴食的一各方面而已，白米饭吃多了也是不行的。</p><p><img src="https://iknow-pic.cdn.bcebos.com/11385343fbf2b211afc2ac57c68065380cd78e3e?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p><p style="text-align: center;"><sup>糖尿病酮症酸中毒示意图</sup></p><p>这里也提醒大家：饮酒、吃饭，一定要适量，暴饮暴食切不可取；尤其是现在，长假刚过，大家肚子里都攒了不少油水，更是要注意饮食清淡——老酒虽好，可不要贪杯哦。</p><p><img src="https://iknow-pic.cdn.bcebos.com/d6ca7bcb0a46f21fa299774afa246b600c33ae7d?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p><p style="text-align: center;"><sup>（图片来源于网络）</sup></p><p><sup><strong>参考文献</strong></sup></p><p><sup>【1】吃15包辣条昏迷？少年澄清只吃了四五包，医生称非患病主因_绿政公署_澎湃新闻-The Paper[EB/OL]. [2018-02-08]. http://www.thepaper.cn/newsDetail_forward_1988988.</sup></p><p><sup>【2】陈再英, 钟南山. 内科学[M]. 人民卫生出版社, 2008.</sup></p><p><sup>【3】钱荣立. 糖尿病酮症酸中毒[J]. 中华内分泌代谢杂志, 1993, 9(3): 166–169.</sup></p><p><sup>【4】钱荣立. 糖尿病酮症酸中毒的防治[J]. 内科急危重症杂志, 1996(02): 76–77.</sup></p><p><sup>【5】尹延伟等. 糖尿病酮症酸中毒相关危险因素分析[J]. 临床急诊杂志, 2012(02): 94–96.</sup></p><p><img src="https://iknow-pic.cdn.bcebos.com/ac4bd11373f082029d4eb82647fbfbedaa641bce?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85"></p>
<div class="detail_statement article-source">
<p class="tit clearfix"><span class="left"></span><span class="center">特别声明</span><span class="right"></span></p>
<p class="cont">
本文为自媒体、作者等在百度知道日报上传并发布，仅代表作者观点，不代表百度知道日报的观点或立场，知道日报仅提供信息发布平台。合作及供稿请联系zdribao@baidu.com。</p>
</div>
</div>
<div class="wgt-bottom-union line">
<h2>为您推荐：</h2>
<script type="text/javascript">
        /*百度派－日报－为您推荐*/
        var cpro_id = "u3120033";
    </script>
<script type="text/javascript" src="//cpro.baidustatic.com/cpro/ui/c.js"></script>
</div>
<div class="opt clearfix">
<div class="spt grid-r">
<span id="spt-add" class="spt-add">+1</span>
<span id="spt-btn" class="spt-icon">
<span>点个赞吧</span>
</span>
<span id="spt-num" class="spt-num">赞(<em>0</em>)</span>
</div>
</div>
<div class="author">
<h3>关注作者</h3>
<div class="author-info clearfix">
<a href="/daily/author?un=蝌蚪五线谱&amp;ie=gbk" target="_blank" data-log="type:2060,action:click,area:detail-author2,page:daily-view">
<img src="https://gss0.bdstatic.com/70cFsj3f_gcX8t7mm9GUKT-xh_/zhidaoribao2014/authors/kedo.jpg" alt="头像" width="80" height="80">
</a>
<dl>
<dt>
<a href="/daily/author?un=蝌蚪五线谱&amp;ie=gbk" target="_blank" data-log="type:2060,action:click,area:detail-author2,page:daily-view">蝌蚪五线谱</a>
</dt>
<dd>北京市政府投资建设，北京市科学技术协会承建的大型公益性科普门户网站。</dd>
</dl>
<a class="follow unfollow" data-log="type:2060,action:click,area:detail-follow,page:daily-view">
<b></b>
关注</a>
</div>
</div>
</div>
</div>
<div class="hot-daily-wp">
<div class="hot-daily">
<div class="header clearfix">
<h3 class="grid">知道日报热门文章</h3>
<div class="slide-wp grid">
<a href="javascript:;" class="slide-arrow slide-arrow-l"></a>
<a href="javascript:;" class="slide-dot slide-dot-a"></a>
<a href="javascript:;" class="slide-dot"></a>
<a href="javascript:;" class="slide-dot"></a>
<a href="javascript:;" class="slide-arrow slide-arrow-r"></a>
</div>
</div>
<div class="hot-list-wp">
<ul class="hot-list">
<li class="clearfix " data-id="223287">
<a class="img-wp" href="/daily/view?id=223287" target="_blank"
			    	log="module:daily,page:daily-view,area:hot-list,id:223287,idx:0,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/7af40ad162d9f2d3dae59891b9ec8a136227ccdc?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="光绪被慈禧囚禁后的生活有多惨？" title="光绪被慈禧囚禁后的生活有多惨？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223287" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223287,idx:0,referId:117163">
光绪被慈禧囚禁后的生活有多惨？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223287" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223287,idx:0,referId:117163">
慌乱之时，光绪抓住了袁世凯这根稻草，想要通过他遏制慈禧势力，不想反被出卖，维新变法也走到了尽头。之后，朝廷对外宣称光绪帝患病，实际将他幽禁于西苑瀛台。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%BA%B9%C7%E0%D5%FD%BA%C6&ie=gbk">汗青正浩</a></span>
<span class="browse-count">阅读(46628)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223326">
<a class="img-wp" href="/daily/view?id=223326" target="_blank"
			    	log="module:daily,page:daily-view,area:hot-list,id:223326,idx:1,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/fd039245d688d43fb2eb2e8c6d1ed21b0ef43b09?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="为什么Y染色体传男不传女？" title="为什么Y染色体传男不传女？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223326" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223326,idx:1,referId:117163">
为什么Y染色体传男不传女？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223326" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223326,idx:1,referId:117163">
女性有哪些基因是传给后代世世代代传下去的?
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%CE%F2%BF%D5%BF%C6%D1%A7&ie=gbk">悟空科学</a></span>
<span class="browse-count">阅读(43844)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223330">
<a class="img-wp" href="/daily/view?id=223330" target="_blank"
			    	log="module:daily,page:daily-view,area:hot-list,id:223330,idx:2,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/b17eca8065380cd75ea61d93b144ad3459828110?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="玻璃真的可以存在200万年？" title="玻璃真的可以存在200万年？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223330" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223330,idx:2,referId:117163">
玻璃真的可以存在200万年？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223330" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223330,idx:2,referId:117163">
综艺节目《奔跑吧》在一期节目中提到：一个玻璃瓶降解需要200万年。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%B9%D6%C2%DE%BF%C6%C6%D5&ie=gbk">怪罗科普</a></span>
<span class="browse-count">阅读(43663)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223300">
<a class="img-wp" href="/daily/view?id=223300" target="_blank"
			    	log="module:daily,page:daily-view,area:hot-list,id:223300,idx:3,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/91ef76c6a7efce1b6e3b77b4bf51f3deb48f65b8?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="河狸的生态作用及危害是什么？" title="河狸的生态作用及危害是什么？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223300" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223300,idx:3,referId:117163">
河狸的生态作用及危害是什么？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223300" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223300,idx:3,referId:117163">
河狸，看起来还有点憨厚的样子，实际上它们很凶猛，甚至还造成了人类的死亡。其实世界就是这么奇妙，在可爱的外表下潜藏着致命的危机，河狸修堤筑坝，同样也有对错。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%B6%AF%CE%EF%CB%D9%B5%DD&ie=gbk">动物速递</a></span>
<span class="browse-count">阅读(37880)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223147">
<a class="img-wp" href="/daily/view?id=223147" target="_blank"
			    	log="module:daily,page:daily-view,area:hot-list,id:223147,idx:4,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/503d269759ee3d6dcbd634b553166d224f4adeb8?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="原来人类离灭亡这么近吗？" title="原来人类离灭亡这么近吗？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223147" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223147,idx:4,referId:117163">
原来人类离灭亡这么近吗？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223147" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223147,idx:4,referId:117163">
人类文明出现距今不过1万年。第一次工业革命后科技才得到了爆炸式发展，距今不到200年。与恐龙1亿多年的生存期相比，人类还处于牙牙学语期，但是我们已经数次与灭绝危机擦肩而过了……
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%A1%B6%B4%F3%BF%C6%BC%BC%A1%B7%D4%D3%D6%BE&ie=gbk">《大科技》杂志</a></span>
<span class="browse-count">阅读(31139)</span>
</div>
</div>
</li>
<li class="clearfix last" data-id="223243">
<a class="img-wp" href="/daily/view?id=223243" target="_blank"
			    	log="module:daily,page:daily-view,area:hot-list,id:223243,idx:5,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/c2cec3fdfc039245e3115c719794a4c27d1e2523?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="死于自己发明的发明家有哪些？" title="死于自己发明的发明家有哪些？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223243" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223243,idx:5,referId:117163">
死于自己发明的发明家有哪些？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223243" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223243,idx:5,referId:117163">
发明创造是人类的天赋，有些发明可以让我们战胜自然，例如火和工具；有些可以改变我们的生活方式，例如飞行器；有些发现能让我们更加了解自己所生活的世界，例如元素周期表。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%C1%BF%D7%D3%BF%C6%D1%A7%C2%DB&ie=gbk">量子科学论</a></span>
<span class="browse-count">阅读(26945)</span>
</div>
</div>
</li>
</ul>
<ul class="hot-list" style="display:none;">
<li class="clearfix " data-id="223123">
<a class="img-wp" href="/daily/view?id=223123" target="_blank"
					log="module:daily,page:daily-view,area:hot-list,id:223123,idx:0,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/bd3eb13533fa828bbd732d9ded1f4134970a5a7f?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="为什么鸡那么喜欢吃泡沫？" title="为什么鸡那么喜欢吃泡沫？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223123" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223123,idx:0,referId:117163">
为什么鸡那么喜欢吃泡沫？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223123" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223123,idx:0,referId:117163">
鸡可能一天都在低头刨食，一般主要吃糠、米、麦粒等东西，但是不难发现，散养的鸡一看见泡沫就疯狂了，当地上放置泡沫的时候，鸡就会一股脑的扑过来。这是为什么?
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%D0%C7%C7%F2%C9%CF%B5%C4%BF%C6%D1%A7&ie=gbk" >星球上的科学</a></span>
<span class="browse-count">阅读(26298)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223264">
<a class="img-wp" href="/daily/view?id=223264" target="_blank"
					log="module:daily,page:daily-view,area:hot-list,id:223264,idx:1,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/f636afc379310a55d233628aa74543a9822610bc?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="在五星级酒店拼单拍照的名媛，都亏了吗？" title="在五星级酒店拼单拍照的名媛，都亏了吗？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223264" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223264,idx:1,referId:117163">
在五星级酒店拼单拍照的名媛，都亏了吗？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223264" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223264,idx:1,referId:117163">
贫穷如你我，真的想象不到最壕的五星级酒店能有什么样子，为什么那么贵！
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%C9%CF%C1%F7UpFlow&ie=gbk" >上流UpFlow</a></span>
<span class="browse-count">阅读(26107)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223609">
<a class="img-wp" href="/daily/view?id=223609" target="_blank"
					log="module:daily,page:daily-view,area:hot-list,id:223609,idx:2,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/aa64034f78f0f736f84be97f1a55b319ebc41312?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="美国五大湖，是如何变脏的？" title="美国五大湖，是如何变脏的？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223609" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223609,idx:2,referId:117163">
美国五大湖，是如何变脏的？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223609" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223609,idx:2,referId:117163">
然而现代生活是有代价的。西方国家引领了三次工业革命，在相关技术不成熟的时代走了太多弯路，虽然如今是最重视环保的地区，依旧没能还清先污后治的旧账，代价最为明显。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%B5%D8%C7%F2%D6%AA%CA%B6%BE%D6&ie=gbk" >地球知识局</a></span>
<span class="browse-count">阅读(24042)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223131">
<a class="img-wp" href="/daily/view?id=223131" target="_blank"
					log="module:daily,page:daily-view,area:hot-list,id:223131,idx:3,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/6f061d950a7b0208f69b8f9f72d9f2d3572cc87a?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="琉球王朝的王室还有后裔吗？" title="琉球王朝的王室还有后裔吗？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223131" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223131,idx:3,referId:117163">
琉球王朝的王室还有后裔吗？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223131" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223131,idx:3,referId:117163">
日本有一个特殊的家庭，其姓氏为“尚”，乍一看，这是一个典型的中国姓氏，与日本普遍的双字甚至三字姓氏完全不同。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%BA%B9%C7%E0%D5%FD%BA%C6&ie=gbk" >汗青正浩</a></span>
<span class="browse-count">阅读(20839)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223160">
<a class="img-wp" href="/daily/view?id=223160" target="_blank"
					log="module:daily,page:daily-view,area:hot-list,id:223160,idx:4,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/f636afc379310a55d79f6d8aa74543a982261010?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="真的没什么办法拯救近视眼吗？" title="真的没什么办法拯救近视眼吗？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223160" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223160,idx:4,referId:117163">
真的没什么办法拯救近视眼吗？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223160" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223160,idx:4,referId:117163">
真的没什么办法拯救近视眼吗？？？
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%C9%CF%C1%F7UpFlow&ie=gbk" >上流UpFlow</a></span>
<span class="browse-count">阅读(19415)</span>
</div>
</div>
</li>
<li class="clearfix last" data-id="223279">
<a class="img-wp" href="/daily/view?id=223279" target="_blank"
					log="module:daily,page:daily-view,area:hot-list,id:223279,idx:5,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/b21bb051f819861845fc53fa5aed2e738bd4e611?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="和“对的人”在一起，应该有什么样的感觉？" title="和“对的人”在一起，应该有什么样的感觉？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223279" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223279,idx:5,referId:117163">
和“对的人”在一起，应该有什么样的感觉？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223279" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223279,idx:5,referId:117163">
一段好的亲密关系是如何让人重塑自我、重新找回对爱的信仰的。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=KnowYourself&ie=gbk" >KnowYourself</a></span>
<span class="browse-count">阅读(18406)</span>
</div>
</div>
</li>
</ul><ul class="hot-list" style="display:none;">
<li class="clearfix " data-id="223670">
<a class="img-wp" href="/daily/view?id=223670" target="_blank"
				log="module:daily,page:daily-view,area:hot-list,id:223670,idx:0,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/b219ebc4b74543a9deb85db20e178a82b9011428?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="三峡大坝拦起那么久了，长江里的鱼到底有多大了呢？" title="三峡大坝拦起那么久了，长江里的鱼到底有多大了呢？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223670" target="_blank"
							log="module:daily,page:daily-view,area:hot-list,id:223670,idx:0,referId:117163">
三峡大坝拦起那么久了，长江里的鱼到底有多大了呢？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223670" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223670,idx:0,referId:117163">
三峡大坝是1994年12月开工建设的，到1997年11月时，奔腾不息的万里长江截流成功，三峡变成了一个水平如镜的湖泊！一直以来三峡就以水流湍急著称，大量鱼类栖息在数百千米的三峡中
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%D0%C7%B3%BD%B4%F3%BA%A3%C2%B7%C9%CF%B5%C4%D6%D6%BB%A8%BC%D2&ie=gbk" >星辰大海路上的种花家</a></span>
<span class="browse-count">阅读(16717)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223394">
<a class="img-wp" href="/daily/view?id=223394" target="_blank"
				log="module:daily,page:daily-view,area:hot-list,id:223394,idx:1,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/9e3df8dcd100baa1e4dff9c55710b912c9fc2ed8?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="你吃的突尼斯软籽石榴，是哪的？" title="你吃的突尼斯软籽石榴，是哪的？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223394" target="_blank"
							log="module:daily,page:daily-view,area:hot-list,id:223394,idx:1,referId:117163">
你吃的突尼斯软籽石榴，是哪的？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223394" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223394,idx:1,referId:117163">
金秋十月，是吃石榴的季节。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%C9%CF%C1%F7UpFlow&ie=gbk" >上流UpFlow</a></span>
<span class="browse-count">阅读(16225)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223172">
<a class="img-wp" href="/daily/view?id=223172" target="_blank"
				log="module:daily,page:daily-view,area:hot-list,id:223172,idx:2,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/1ad5ad6eddc451dac0ffbe95a6fd5266d0163246?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="人们都是如何自我治愈的？" title="人们都是如何自我治愈的？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223172" target="_blank"
							log="module:daily,page:daily-view,area:hot-list,id:223172,idx:2,referId:117163">
人们都是如何自我治愈的？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223172" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223172,idx:2,referId:117163">
有没有一个空间，能在你疲惫、崩溃的时候，在无常的世界中给你带来恒常的安心。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=KnowYourself&ie=gbk" >KnowYourself</a></span>
<span class="browse-count">阅读(15847)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223753">
<a class="img-wp" href="/daily/view?id=223753" target="_blank"
				log="module:daily,page:daily-view,area:hot-list,id:223753,idx:3,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/b2de9c82d158ccbf6ffe164409d8bc3eb1354109?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="你三四岁前的记忆去哪里呢？" title="你三四岁前的记忆去哪里呢？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223753" target="_blank"
							log="module:daily,page:daily-view,area:hot-list,id:223753,idx:3,referId:117163">
你三四岁前的记忆去哪里呢？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223753" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223753,idx:3,referId:117163">
记忆是我们最宝贵的财富，记忆是人脑对经验过事物的识记、保持、回忆和再认，它是人类进行思维、想象等活动的基础，这些记忆信息存储在大脑神经元间的突触。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%BF%C6%D1%A7%CC%BD%CB%F7%BE%FA&ie=gbk" >科学探索菌</a></span>
<span class="browse-count">阅读(14310)</span>
</div>
</div>
</li>
<li class="clearfix " data-id="223152">
<a class="img-wp" href="/daily/view?id=223152" target="_blank"
				log="module:daily,page:daily-view,area:hot-list,id:223152,idx:4,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/2e2eb9389b504fc23a2d037bf5dde71190ef6d5a?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="印度儿童失学究竟有多严重？" title="印度儿童失学究竟有多严重？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223152" target="_blank"
							log="module:daily,page:daily-view,area:hot-list,id:223152,idx:4,referId:117163">
印度儿童失学究竟有多严重？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223152" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223152,idx:4,referId:117163">
目前，据联合国儿童基金会发布的《远程学习普及报告》统计，新冠肺炎之下，印度已经关闭了超过150万所学校，影响了2.86亿名学前至中学年龄段的儿童。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%B5%D8%C7%F2%D6%AA%CA%B6%BE%D6&ie=gbk" >地球知识局</a></span>
<span class="browse-count">阅读(14078)</span>
</div>
</div>
</li>
<li class="clearfix last" data-id="223659">
<a class="img-wp" href="/daily/view?id=223659" target="_blank"
				log="module:daily,page:daily-view,area:hot-list,id:223659,idx:5,referId:117163">
<img src="https://iknow-pic.cdn.bcebos.com/35a85edf8db1cb13b4349b6dcd54564e92584b6b?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="秦朝为什么那么快灭亡？" title="秦朝为什么那么快灭亡？" width="214" height="120">
</a>
<div class="daily-cont">
<div class="daily-cont-top">
<h2>
<a href="/daily/view?id=223659" target="_blank"
							log="module:daily,page:daily-view,area:hot-list,id:223659,idx:5,referId:117163">
秦朝为什么那么快灭亡？
</a>
</h2>
<div class="summer">
<a href="/daily/view?id=223659" target="_blank"
						    log="module:daily,page:daily-view,area:hot-list,id:223659,idx:5,referId:117163">
传统观点认为，秦朝之所以短命，主要原因是统治阶层实施暴政，滥用民力，结果造成百姓民不聊生，被迫揭竿而起。从表面来看，这种观点很具有说服力，可仔细分析，却并不完全是这么一回事。
</a>
</div>
</div>
<div class="daily-info">
<span class="fr"><a href="/daily/author?un=%D2%B9%B6%C1%CA%B7%CA%E9&ie=gbk" >夜读史书</a></span>
<span class="browse-count">阅读(10902)</span>
</div>
</div>
</li>
</ul></div>
</div>
</div>
<div class="comment-wp">
<div class="comment">
<div id="comment-header" class="header"></div>
<div id="comment-list" class="comment-list"></div></div>
</div>
</div>
<aside class="aside-wp grid-r">
<div class="wgt-view-replier aside-box">
<dl>
<dt><a href="/daily/author?un=%F2%F2%F2%BD%CE%E5%CF%DF%C6%D7&ie=gbk" target="_blank">蝌蚪五线谱</a></dt>
<dd class="intro">北京市政府投资建设，北京市科学技术协会承建的大型公益性科普门户网站。</dd>
<dd class="face">
<a href="/daily/author?un=%F2%F2%F2%BD%CE%E5%CF%DF%C6%D7&ie=gbk" target="_blank">
<img src="https://gss0.bdstatic.com/70cFsj3f_gcX8t7mm9GUKT-xh_/zhidaoribao2014/authors/kedo.jpg" alt="知道日报作者蝌蚪五线谱的头像" width="80" height="80">
</a>
</dd>
</dl>
<aside class="info">
<ul>
<li><span>4491</span>粉丝</li>
<li class="li2"><span>3839</span>文章</li>
<li><span id="replier-pv"></span>阅读量</li>
</ul>
</aside>
</div>
<div class="aside">
<div class="ad-wp">
</div>
<div class="recommend-author-wp">
<div class="recommend-author">
<h3>热门作者推荐</h3>
<ul>
<li class="clearfix"><dl>
<dt><a href="/daily/author?un=%D3%EE%D6%E6%B9%DB%B2%EC%BC%C7%C2%BC&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank">宇宙观察记录</a></dt>
<dd class="intro">探索宇宙奥秘，普及科学知识。</dd>
<dd class="face"><a href="/daily/author?un=%D3%EE%D6%E6%B9%DB%B2%EC%BC%C7%C2%BC&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank"><img src="https://iknow-pic.cdn.bcebos.com/a1ec08fa513d2697504f27535afbb2fb4316d81b?x-bce-process=image/quality,q_85" alt="知道日报作者宇宙观察记录的头像" width="80" height="80"/></a></dd>
</dl>
</li>
<li class="clearfix"><dl>
<dt><a href="/daily/author?un=%B7%B5%C6%D3&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank">返朴</a></dt>
<dd class="intro">溯源守拙·问学求新</dd>
<dd class="face"><a href="/daily/author?un=%B7%B5%C6%D3&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank"><img src="https://iknow-pic.cdn.bcebos.com/8644ebf81a4c510fa7e316246e59252dd42aa5ed?x-bce-process=image/quality,q_85" alt="知道日报作者返朴的头像" width="80" height="80"/></a></dd>
</dl>
</li>
<li class="clearfix"><dl>
<dt><a href="/daily/author?un=%D0%C7%C7%F2%C9%CF%B5%C4%BF%C6%D1%A7&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank">星球上的科学</a></dt>
<dd class="intro">探索宇宙</dd>
<dd class="face"><a href="/daily/author?un=%D0%C7%C7%F2%C9%CF%B5%C4%BF%C6%D1%A7&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank"><img src="https://iknow-pic.cdn.bcebos.com/c8ea15ce36d3d5392a6294be2a87e950352ab074" alt="知道日报作者星球上的科学的头像" width="80" height="80"/></a></dd>
</dl>
</li>
<li class="clearfix"><dl>
<dt><a href="/daily/author?un=%CA%B3%CE%B6%D2%D5%CE%C4%D6%BE&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank">食味艺文志</a></dt>
<dd class="intro">书斋里的饮馔杂谈，舌尖上的艺文景观</dd>
<dd class="face"><a href="/daily/author?un=%CA%B3%CE%B6%D2%D5%CE%C4%D6%BE&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank"><img src="https://iknow-pic.cdn.bcebos.com/b812c8fcc3cec3fdf6602b54de88d43f879427b0?x-bce-process=image/resize,m_lfit,w_450,h_600,limit_1/quality,q_85" alt="知道日报作者食味艺文志的头像" width="80" height="80"/></a></dd>
</dl>
</li>
<li class="clearfix"><dl>
<dt><a href="/daily/author?un=%B5%D8%C7%F2%D6%AA%CA%B6%BE%D6&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank">地球知识局</a></dt>
<dd class="intro">人文+地理+设计=全球视野新三观</dd>
<dd class="face"><a href="/daily/author?un=%B5%D8%C7%F2%D6%AA%CA%B6%BE%D6&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank"><img src="https://iknow-pic.cdn.bcebos.com/80cb39dbb6fd526693018531a618972bd40736e8?x-bce-process=image/quality,q_85" alt="知道日报作者地球知识局的头像" width="80" height="80"/></a></dd>
</dl>
</li>
<li class="clearfix last"><dl>
<dt><a href="/daily/author?un=%D0%C7%B3%BD%B4%F3%BA%A3%C2%B7%C9%CF%B5%C4%D6%D6%BB%A8%BC%D2&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank">星辰大海路上的种花家</a></dt>
<dd class="intro">种花家的征途在于星辰大海，偶将上下求索.........</dd>
<dd class="face"><a href="/daily/author?un=%D0%C7%B3%BD%B4%F3%BA%A3%C2%B7%C9%CF%B5%C4%D6%D6%BB%A8%BC%D2&ie=gbk" data-log="type:2060,action:click,area:rec-author,page:daily-view" target="_blank"><img src="https://iknow-pic.cdn.bcebos.com/63d9f2d3572c11df1c23ef566d2762d0f603c2d1?x-bce-process=image/quality,q_85" alt="知道日报作者星辰大海路上的种花家的头像" width="80" height="80"/></a></dd>
</dl>
</li>
</ul></div>
</div>
<div class="ad-app-wp">
</div>
</div>
<div id="rel-daily" class="rel-daily">
<header>
<h3><a href="/daily/?period=2618" target="_blank">第<span>2618</span>期</a></h3>
</header><div class="body">
<ul>
<li class="cur">
<a href="/daily/view?id=223753" target="_blank" data-log="type:2060,action:click,area:reldaily,page:daily-view,referId:117163,idx:0">
<img src="https://iknow-pic.cdn.bcebos.com/b2de9c82d158ccbf6ffe164409d8bc3eb1354109?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="你三四岁前的记忆去哪里呢？的头图" width="251" height="185">
<p class="title"><b></b>你三四岁前的记忆去哪里呢？</p>
</a></li>
<li class="">
<a href="/daily/view?id=223394" target="_blank" data-log="type:2060,action:click,area:reldaily,page:daily-view,referId:117163,idx:1">
<img src="https://iknow-pic.cdn.bcebos.com/9e3df8dcd100baa1e4dff9c55710b912c9fc2ed8?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="你吃的突尼斯软籽石榴，是哪的？的头图" width="251" height="185">
<p class="title"><b></b>你吃的突尼斯软籽石榴，是哪的？</p>
</a></li>
<li class="">
<a href="/daily/view?id=218981" target="_blank" data-log="type:2060,action:click,area:reldaily,page:daily-view,referId:117163,idx:2">
<img src="https://iknow-pic.cdn.bcebos.com/7aec54e736d12f2ef697b81e5fc2d56285356839?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="猫从高处落下真的不会摔死吗？的头图" width="251" height="185">
<p class="title"><b></b>猫从高处落下真的不会摔死吗？</p>
</a></li>
<li class="">
<a href="/daily/view?id=220757" target="_blank" data-log="type:2060,action:click,area:reldaily,page:daily-view,referId:117163,idx:3">
<img src="https://iknow-pic.cdn.bcebos.com/78310a55b319ebc429330de79226cffc1e171600?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="你喝的水，或许是某个小行星送到地球来的？的头图" width="251" height="185">
<p class="title"><b></b>你喝的水，或许是某个小行星送到地球来的？</p>
</a></li>
<li class="">
<a href="/daily/view?id=219825" target="_blank" data-log="type:2060,action:click,area:reldaily,page:daily-view,referId:117163,idx:4">
<img src="https://iknow-pic.cdn.bcebos.com/d788d43f8794a4c2f885ee551ef41bd5ad6e392d?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="为什么爱因斯坦认为“一切都是设计好的”？的头图" width="251" height="185">
<p class="title"><b></b>为什么爱因斯坦认为“一切都是设计好的”？</p>
</a></li>
<li class="">
<a href="/daily/view?id=223672" target="_blank" data-log="type:2060,action:click,area:reldaily,page:daily-view,referId:117163,idx:5">
<img src="https://iknow-pic.cdn.bcebos.com/5ab5c9ea15ce36d362a6244e2af33a87e950b12a?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="汽车也压不死，用电钻才能穿透，这种甲虫外壳为什么如此坚硬？的头图" width="251" height="185">
<p class="title"><b></b>汽车也压不死，用电钻才能穿透，这种甲虫外壳为什么如此坚硬？</p>
</a></li>
<li class="">
<a href="/daily/view?id=223070" target="_blank" data-log="type:2060,action:click,area:reldaily,page:daily-view,referId:117163,idx:6">
<img src="https://iknow-pic.cdn.bcebos.com/dbb44aed2e738bd4ce4a034fb18b87d6277ff961?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="“一旋横，两旋拧，三旋打架不要命”，头旋和智商有什么关系？的头图" width="251" height="185">
<p class="title"><b></b>“一旋横，两旋拧，三旋打架不要命”，头旋和智商有什么关系？</p>
</a></li>
<li class="last">
<a href="/daily/view?id=219923" target="_blank" data-log="type:2060,action:click,area:reldaily,page:daily-view,referId:117163,idx:7">
<img src="https://iknow-pic.cdn.bcebos.com/8601a18b87d6277f5901384638381f30e924fcb9?x-bce-process=image/resize,m_lfit,w_800,h_450,limit_1" alt="如果人类把月球上的大量资源运回地球，会发生什么？的头图" width="251" height="185">
<p class="title"><b></b>如果人类把月球上的大量资源运回地球，会发生什么？</p>
</a></li>
</ul>
</div></div>
</aside>
</div>
</div>

<div class="f-contact">合作及供稿请联系：zdribao@baidu.com</div>

</div>


<footer id="footer" class="wgt-footer">
<p>
<a target="_blank" rel="nofollow" href="http://help.baidu.com/question?prod_id=9&class=337">帮助</a>
&nbsp;|&nbsp;<a target="_blank" rel="nofollow" href="javascript:;" id="footer-feedback">意见反馈</a>
&nbsp;|&nbsp;<a target="_blank" rel="nofollow" href="http://help.baidu.com/newadd?prod_id=9&category=1">投诉举报</a>
</p>
<p>
京ICP证030173号-1&nbsp;&nbsp;&nbsp;京网文【2013】0934-983号&nbsp;&nbsp;&nbsp;&nbsp;    &copy;2020Baidu&nbsp;&nbsp;<a rel="nofollow" href="http://www.baidu.com/duty/" target="_blank">使用百度前必读</a>&nbsp;|&nbsp;<a rel="nofollow" href="http://help.baidu.com/question?prod_id=9&class=325&id=2760" target="_blank">知道协议</a>&nbsp;</p>
</footer>



<script type="text/javascript">
window.baidu_hh_hotword={
    id: ['daily-cont'],
    page_url: 'http://zhidao.' + 'baidu.com' + location.pathname + location.search,
    di: "u2374312",
    maxword: 10,
    frequency: 2
}
</script>
<script src="//su.bdimg.com/static/dspui/js/sw.js?v=1"></script>



<script>
    void function(a,b,c,d,e,f){function g(b){a.attachEvent?a.attachEvent("onload",b,!1):a.addEventListener&&a.addEventListener("load",b)}function h(a,c,d){d=d||15;var e=new Date;e.setTime((new Date).getTime()+1e3*d),b.cookie=a+"="+escape(c)+";path=/;expires="+e.toGMTString()}function i(a){var c=b.cookie.match(new RegExp("(^| )"+a+"=([^;]*)(;|$)"));return null!=c?unescape(c[2]):null}function j(){var a=i("PMS_JT");if(a){h("PMS_JT","",-1);try{a=a.match(/{["']s["']:(\d+),["']r["']:["']([\s\S]+)["']}/),a=a&&a[1]&&a[2]?{s:parseInt(a[1]),r:a[2]}:{}}catch(c){a={}}a.r&&b.referrer.replace(/#.*/,"")!=a.r||alog("speed.set","wt",a.s)}}if(a.alogObjectConfig){var k=a.alogObjectConfig.sample,l=a.alogObjectConfig.rand;d="https:"===a.location.protocol?"https://fex.bdstatic.com"+d:"http://fex.bdstatic.com"+d,k&&l&&l>k||(g(function(){alog("speed.set","lt",+new Date),e=b.createElement(c),e.async=!0,e.src=d+"?v="+~(new Date/864e5)+~(new Date/864e5),f=b.getElementsByTagName(c)[0],f.parentNode.insertBefore(e,f)}),j())}}(window,document,"script","/hunter/alog/dp.min.js");
    </script>

<script>
    var _hmt = _hmt || [];
    (function() {
      var hm = document.createElement("script");
      hm.src = "https://hm.baidu.com/hm.js?92f9337283b8a859284c612d2cfeb037";
      var s = document.getElementsByTagName("script")[0];
      s.parentNode.insertBefore(hm, s);
    })();
    </script>
<script type="text/javascript"> window.tt = 1603936319;</script>
</body><script type="text/javascript" src="https://iknowpc.bdimg.com/static/common/lib/mod.75d1f98.js"></script><script nonce="" type="text/javascript">(window.__IKNOW_GLOBAL__ || window).require.resourceMap({"res":{"common:widget\/lib\/jquery\/jquery.origin.js":{"pkg":"common:p3"},"common:widget\/js\/util\/https\/https.js":{"pkg":"common:p6"},"common:widget\/bottom-ask\/bottom-ask.js":{"pkg":"common:p0","deps":["common:widget\/js\/util\/tangram\/tangram.js","common:widget\/js\/util\/event\/event.js","common:widget\/js\/util\/log\/log.js"]},"common:widget\/css\/fonts\/iconfont.js":{"pkg":"common:p0"},"common:widget\/css\/fonts\/iconfont.min.js":{"pkg":"common:p0"},"common:widget\/footer-new\/footer-new.js":{"pkg":"common:p0","deps":["common:widget\/lib\/jquery\/jquery.js","common:widget\/js\/util\/event\/event.js"]},"common:widget\/footer\/footer.js":{"pkg":"common:p0"},"common:widget\/header-metis\/header.js":{"pkg":"common:p0","deps":["common:widget\/lib\/jquery\/jquery.js","common:widget\/js\/ui\/dialog\/dialog.js","common:widget\/js\/util\/template\/template.js","common:widget\/js\/ui\/scrollbar-new\/scrollbar-new.js","common:widget\/js\/util\/store\/store.js"]},"common:widget\/menu\/menu.js":{"pkg":"common:p0","deps":["common:widget\/js\/util\/tangram\/tangram.js","common:widget\/js\/util\/log\/log.js"]},"common:widget\/search-box-new\/search-box-new.js":{"pkg":"common:p0","deps":["common:widget\/js\/util\/tangram\/tangram.js","common:widget\/js\/ui\/suggestion-new\/suggestion-new.js","common:widget\/js\/util\/event\/event.js","common:widget\/js\/util\/form\/form.js","common:widget\/js\/util\/log\/log.js","common:widget\/js\/ui\/dialog\/dialog.js","common:widget\/lib\/jquery.placeholder\/jquery.placeholder.js"]},"common:widget\/set-tag\/set-tag.js":{"pkg":"common:p0","deps":["common:widget\/js\/util\/tangram\/tangram.js","common:widget\/js\/util\/template\/template.js","common:widget\/js\/ui\/scrollbar\/scrollbar.js","common:widget\/js\/ui\/dialog\/dialog.js","common:widget\/lib\/jquery.ui\/jquery.ui.sortable.js"]},"common:widget\/task\/task-last.js":{"pkg":"common:p0","deps":["common:widget\/js\/util\/tangram\/tangram.js","common:widget\/js\/util\/log\/log.js","common:widget\/js\/util\/event\/event.js","common:widget\/js\/ui\/dialog\/dialog.js","common:widget\/js\/util\/https\/https.js","common:widget\/js\/ui\/pop-tip\/pop-tip.js","common:widget\/js\/util\/template\/template.js","common:widget\/js\/logic\/signin-task\/signin-task.js"]},"common:widget\/userbar-renew\/userbar-renew.js":{"pkg":"common:p0","deps":["common:widget\/js\/util\/tangram\/tangram.js","common:widget\/js\/util\/event\/event.js","common:widget\/js\/logic\/login\/login.js","common:widget\/js\/util\/log\/log.js","common:widget\/js\/util\/store\/store.js"]},"com-brand:widget\/js\/ueditor\/ueditor.config.js":{"pkg":"com-brand:p0"},"daily:widget\/detail\/decorate-img.js":{"pkg":"daily:p0","deps":["common:widget\/js\/util\/tangram\/tangram.js"]},"common:widget\/js\/logic\/tip-template\/tipTemplate.es.js":{"pkg":"common:p5","deps":["common:widget\/lib\/jquery\/jquery.js"]},"common:widget\/js\/logic\/usergrade\/threshold.es.js":{"pkg":"common:p5"},"common:widget\/js\/logic\/usergrade\/gradedata.es.js":{"pkg":"common:p5","deps":["common:widget\/js\/logic\/usergrade\/threshold.es.js"]},"common:widget\/js\/ui\/newDialog\/newDialog.es.js":{"pkg":"common:p5","deps":["common:widget\/js\/util\/tangram\/tangram.js"]},"common:widget\/js\/ui\/v-flash\/js\/v-icon.es.js":{"pkg":"common:p5"},"common:widget\/js\/ui\/v-flash\/js\/flash.es.js":{"pkg":"common:p5","deps":["common:widget\/js\/ui\/v-flash\/js\/v-icon.es.js"]},"common:widget\/js\/util\/domToImage\/dom-to-image.es.js":{"pkg":"common:p5"},"common:widget\/js\/util\/monitor\/monitor.es.js":{"pkg":"common:p5","deps":["common:widget\/js\/util\/log\/log.js"]},"common:widget\/js\/util\/observer\/observer.es.js":{"pkg":"common:p5","deps":["common:widget\/js\/util\/observer\/intersection-observer.js","common:widget\/js\/util\/log\/log.js"]}},"pkg":{"common:p0":{"url":"https:\/\/iknowpc.bdimg.com\/static\/common\/pkg\/more.f3a672b.js","has":["common:widget\/bottom-ask\/bottom-ask.js","common:widget\/css\/fonts\/iconfont.js","common:widget\/css\/fonts\/iconfont.min.js","common:widget\/footer-new\/footer-new.js","common:widget\/footer\/footer.js","common:widget\/header-metis\/header.js","common:widget\/menu\/menu.js","common:widget\/search-box-new\/search-box-new.js","common:widget\/set-tag\/set-tag.js","common:widget\/task\/task-last.js","common:widget\/userbar-renew\/userbar-renew.js"]},"common:p5":{"url":"https:\/\/iknowpc.bdimg.com\/static\/common\/pkg\/esmod.84e15b5.js","has":["common:widget\/js\/logic\/tip-template\/tipTemplate.es.js","common:widget\/js\/logic\/usergrade\/threshold.es.js","common:widget\/js\/logic\/usergrade\/gradedata.es.js","common:widget\/js\/ui\/newDialog\/newDialog.es.js","common:widget\/js\/ui\/v-flash\/js\/v-icon.es.js","common:widget\/js\/ui\/v-flash\/js\/flash.es.js","common:widget\/js\/util\/domToImage\/dom-to-image.es.js","common:widget\/js\/util\/monitor\/monitor.es.js","common:widget\/js\/util\/observer\/observer.es.js"]}}});</script><script type="text/javascript" src="https://iknowpc.bdimg.com/static/common/pkg/lib.33719ed.js"></script><script type="text/javascript" src="https://iknowpc.bdimg.com/static/common/pkg/commonjs.5c6c127.js"></script><script type="text/javascript" src="https://iknowpc.bdimg.com/static/daily/pkg/module.5cac358.js"></script><script type="text/javascript" src="https://gss0.bdstatic.com/7051cy792sgCpNKfpU_Y_D3/static/com-brand/pkg/editor_c813b7f.js"></script><script type="text/javascript" src="https://gss0.bdstatic.com/7051cy792sgCpNKfpU_Y_D3/static/com-brand/widget/js/uploader/uploader_b149a46.js"></script><script nonce="" type="text/javascript">
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;			window['__abbaidu_2016_subidgetf'] = function () {
                var currentUrlArray = window.location.href.split("//");
                var start = currentUrlArray[1].indexOf("/");
                if (start == -1) {
                    return 'iknow-pc-home';
				}
                var currentPath = currentUrlArray[1].substring(start);
                if(currentPath.indexOf("?") != -1) {
                    currentPath = currentPath.split("?")[0];
                }
                if (currentPath == "/") {
                    return 'iknow-pc-home';
				}
				if (currentPath.indexOf("/question") === 0) {
					return 'iknow-pc-qb';
				}
				if (currentPath.indexOf("/search") === 0) {
					return 'iknow-pc-search';
				}
				return 'iknow-pc-other';
			}
			window['__abbaidu_2016_cb'] = function (responseData) {
                try {
                    var respJSON = JSON.parse(responseData);

                    var d = new Date();
                    d.setTime(d.getTime()+(60*60*1000));
                    var expires = "expires="+d.toGMTString();
                    document.cookie = 'shitong_key_id=' + respJSON.key_id + '; ' + expires + '; path=/';
                    document.cookie = 'shitong_data=' + respJSON.data + '; ' + expires + '; path=/';
                    document.cookie = 'shitong_sign=' + respJSON.sign + '; ' + expires + '; path=/';
                } catch (err) {
                }
   			};
		}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    F.context('sfrom', '');
    require.async(['common:widget/userbar-renew/userbar-renew']);
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    require.async(['daily:widget/search-box/search-box'], function(o) {
        o.init(1);
    });
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    require.async(['daily:widget/menu/menu'], function (o) {
        o.init(1);
    });
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;	require('daily:widget/detail/decorate-img');

    require.async(['daily:widget/detail/support'], function(ap){
        ap.init({
            id: 117163
        });
    });

    require.async(['daily:widget/detail/detail'], function (obj) {
		obj.init({
			id: 117163,
			title: '吃辣条引起糖尿病酮症酸中毒？这个锅，辣条不背哦！',
			aid: 9,
			focusNum: 2,
			isPreview: '0'
		});
	});
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    require.async(['daily:widget/hot-daily/hot-daily']);
    require.async(['daily:widget/hot-daily/hot-get']);
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    // 初始化 comment
    require.async(['common:widget/js/logic/comment/comment'], function(Comment){
      new Comment({
        threadId: '117163',
        target: '#comment-header',
        targetCon: '#comment-list',
        hasAuthcode: true,
        pageType: 'daily'
      });
    });
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    require.async(['daily:widget/view-replier/view-replier'], function (obj) {
        obj.init({
            id: 9
        });
    });
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    require.async(['daily:widget/rel-daily/rel-daily'], function(obj) {
        obj.init();
    });
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    require.async(['common:widget/js/util/log/log'], function(log){
    	log.init({
    		query: 'body',
    		action: 'click'
    	});
    });
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    require('common:widget/js/logic/ie-prompt/ie-prompt');
    require.async(['common:widget/footer/footer']);
}();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;    require.async(['common:widget/js/util/tangram/tangram','common:widget/js/util/log/log'], function($, log){
        log.send({
            page: 'daily-view',
            area: 'daily-view',
            action: 'pv',
            id: '117163',
            title: '吃辣条引起糖尿病酮症酸中毒？这个锅，辣条不背哦！',
            hasRead: 0,
            sharesource: $.url.getQueryValue(location.href, 'sharesource') || ''
        });
    });
    }();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;								                																	require.async(['common:widget/js/logic/dom-ready/dom-ready'], function(D){ D.init({"isNotPgc":"1"}) });
            }();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;        require.async(["common:widget/js/logic/duration/duration"],function(dur){
            dur.init();
        });
    }();
!function(){var F = (window.__IKNOW_GLOBAL__ || window).F;var require = (window.__IKNOW_GLOBAL__ || window).require;			require.async(['common:widget/js/util/monitor/monitor.es'], function(m) {
				window.iPerformance && m.monitor && m.monitor.init();
			});
		}();
</script>
<script type="text/javascript">
    require.async(['common:widget/lib/jquery/jquery'], function ($) {
        if (!/chrome|firefox|safari|msie 10|rsv:11|msie [89]/i.test(navigator.userAgent)) {
            return;
        }

        window.BaiduHttps = window.BaiduHttps || {};
        window.BaiduHttps.callbacks = function (data) {
            if (data && data.s === 0) {
                window.supportHttps = 1;
                setTimeout(function () {
                    $('a[href^="http://www.baidu.com/s?"]').each(function (index, item) {
                        var link = $(item).attr('href');
                        if (~link.indexOf('?wd=') || ~link.indexOf('&wd=')) {
                            link = link.replace(/^http/, 'https');
                            $(item).attr('href', link);
                        }
                    });
                }, 2000);
            }
        };

        var script = document.createElement('script');
        script.type = 'text/javascript';
        script.src = 'https://www.baidu.com/con?from=zhidao';
        document.body.appendChild(script);
    });
</script>


<script async="" src="https://dlswbr.baidu.com/heicha/mw/abclite-2016-s.js"></script>


</html>

'''
def process(s):
    from lxml import etree
    html = etree.HTML(s, parser=etree.HTMLParser(encoding="utf-8"))
    p = html.xpath(u'//div[@id="daily-cont"]//img')
    if p:
        return u'图片'

print(process(html))
# s = u'郭煦主治医师中山大学附属第一医院妇科1007视频0文章1540语音0问答'
# def process(s):
#     import re
#     if u"视频"in s:
#         s = s.split(u"视频")[0]
#         return s
#
# print(process(s))


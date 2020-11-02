#encoding:utf-8
html = '''
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=gb2312" />
<title>地震会引发心脏病？_心脏病圈_圈子_病友圈_寻医问药网</title>
<meta name="Keywords" content="地震会引发心脏病，心脏病的致病因素"/>
<meta name="Description" content="&nbsp; &nbsp; 上月末，尼泊尔发生了大地震，和汶川地震时候的一个等级，可见地震是很严重的。地震是一个突然发生的，毁灭性很大的自然灾害，人人都很害怕它的来临。除了导致人们直接的损伤以外，还会导致很多疾病，比如：心脏玻很多研究都显示地震和心脏病有" />
<link rel="shortcut icon" type="image/x-icon" href="http://www.xywy.com/favicon.ico" />
<link rel="bookmark" type="image/x-icon" href="http://www.xywy.com/favicon.ico">
<script>
var _hmt = _hmt || [];
(function() {
  var hm = document.createElement("script");
  hm.src = "//hm.baidu.com/hm.js?f954228be9b5d93a74a625d18203e150";
  var s = document.getElementsByTagName("script")[0];
  s.parentNode.insertBefore(hm, s);
})();
</script>
<style>
	.hot-bt{ background:url(http://static.img.xywy.com/quanzi/images/hot.jpg) 80px 10px no-repeat;}
	.new-bt{ background:url(http://static.img.xywy.com/quanzi/images/new.jpg) 80px 10px no-repeat;}
	.group-hot li{ line-height:30px; font-size:14px; color:#666;}
	.group-hot li a{ font-size:14px; color:#666;}
	.avocation{ border-top:1px solid #e5e5e5;}
	.avocation li{ width:315px; border-bottom:1px dashed #e5e5e5; line-height:48px; float:left; margin-left:20px;}
	.avocation li a{ font-size:14px; color:#666;}
	.eys{ background:url(http://static.img.xywy.com/quanzi/images/eys.jpg) 0 18px no-repeat; padding-left:21px; width:25px;}
</style>
</head>
<body>
<link type="text/css" rel="stylesheet" href="http://pub1.wkimg.com/common_login/css/common_login_v2.css" />
<script type="text/javascript" src="http://img.xywy.com/plugin_js/tinker.js"></script>
<script type="text/javascript" src="http://img.xywy.com/home_new/js/home_public.js"></script>
<script type="text/javascript" src="http://home.xywy.com/js/jquery-1.11.1.min.js"></script>
<link rel="stylesheet" type="text/css" href="http://img.xywy.com/home_new/css/reset.css?v=201302210338" />
<link type="text/css" rel="stylesheet" href="http://pub1.wkimg.com/common_login/css/common_login_v2.css" />
<link rel="stylesheet" type="text/css" href="http://img.xywy.com/home_new/css/home_new.css?v=2013022103321153" />
<!--<script type='text/javascript'>var page_xywy_param="club_v2_left_float";</script>
<script type="text/javascript" src="http://a.xywy.com/club_detail.js"></script>
-->

<script>
var domain="http://home.xywy.com/";
var imgdomain="http://home.xywy.com/photos";
document.domain = 'xywy.com';
</script>
<script type="text/javascript" src="http://home.xywy.com/js/login.js" charset="GBK"></script>
<!--统一头部-->
<script type="text/javascript" src="http://pub1.wkimg.com/head/common_nav.js"></script>

<script src="/js/group.js" language="javascript"></script>
<script charset="utf-8" src="/js/kindeditor-4.1.7/kindeditor-min.js"></script>
<script charset="utf-8" src="/js/kindeditor-4.1.7/lang/zh_CN.js"></script>
<script type="text/javascript">
	var editor, resMaskId;
	KindEditor.ready(function(K) {
		editor = K.create('#quickreply', {
			resizeType : 1,
			minWidth : '100%',
			uploadJson : 'http://home.xywy.com/imgupload/upload_json.php',
			allowPreviewEmoticons : false,
			//allowImageUpload : false,
			items : [
				'forecolor', 'hilitecolor', 'bold', 'emoticons','image'], // image
				afterBlur: function(){this.sync();}
		});
	});
	function reply(detailid){
		var uid ='';
		if(uid==''){
			uid = this.getCookie('cookie_user');
		}
		if(uid==''){
			loginPopNew();
		}else {
			var freeze='';
			if(freeze>0){
				showMsg('由于您在健康之家的不当操作，已经被管理员封号，如有问题请联系客服：010-52729953');
			}else {
				var ingroup ='0';
				if(ingroup!=2){
					showMsg('请先加入心脏病圈','http://home.xywy.com/user.php?act=addgroup&gpinyin=xinzangbing&tid='+detailid);
				}else {
					window.location.href='http://home.xywy.com/xinzangbing/'+detailid+'.html#quick_reply';
				}
			}
		}
	}
	function pubtheme(){
		var uid ='';
		if(uid==''){
			uid = this.getCookie('cookie_user');
		}
		if(uid==''){
			loginPopNew();
		}else {
			var freeze='';
			if(freeze>0){
				showMsg('由于您在健康之家的不当操作，已经被管理员封号，如有问题请联系客服：010-52729953');
			}else {
				window.location.href='http://home.xywy.com/group.php?act=pubtheme&pinyinGroup=xinzangbing&first=xzbtl';
			}
		}
	}
    //举报弹框
    function reportPop(){
        Tinker.UI.showMessage('res_box', 'res_close', '', {
            zIndex:100,
            animate:false
        }, function(maskId){
            resMaskId = document.getElementById(maskId);
        });
    }

	function pubreport(){
		var uid ='';
		if(uid==''){
			uid = this.getCookie('cookie_user');
		}
		if(uid==''){
			loginPopNew();
		}else {
			var freeze='';
			if(freeze>0){
				showMsg('由于您在健康之家的不当操作，已经被管理员封号，如有问题请联系客服：010-52729953');
			}else {
                reportPop();
			}
		}
	}
     function report_insert(){
        var reason = $('#reason').val();
        var content = $('#content').val();
        $.ajax({
            type: "POST",
            url: "http://home.xywy.com/group.php?act=report_insert",
            data: "&reason="+reason+"&content="+content,
			success: function(msg){
                if(msg){
                    msg=$.trim(msg);
					if(msg=="0"){
						alert("举报失败！");
					}
					else{
						alert(msg);
						if(msg=="举报成功"){
							try{
								$('#res_box').hide();
								document.body.removeChild(resMaskId);
								resMaskId = null;
							}
							catch(e){}

						}
					}

                }
            }
        });
    }

	function getCookie(name){
		var cookieArr = document.cookie.split('; '),
		cookieValue = '';
		jQuery.each(cookieArr, function(key, value){
			if(decodeURIComponent(value.split('=')[0]) === name){
				cookieValue = decodeURIComponent(value.split('=')[1]);
			}
		});
		return cookieValue;
	}
</script>
<div class="top-wrapper">
    <div id="header" class="wrap">
        <div class="public-hd clearfix">
            <div class="fl public-slogo mt15">
                <div class="fl j-logo"><a href="http://www.xywy.com/" target="_blank"><img src="http://static.img.xywy.com/xy_s_public/images/xy_s_logo.gif" width="132" height="46" alt="" /></a></div>
                <div class="fl t9999 j-descripe"><a href="http://jib.xywy.com">疾病百科</a></div>
            </div>

            <div class="fr public-hd-nav" id="common-hd-nav">
			<style type="text/css">
			body,ul,li,a,div{margin:0;padding:0;}
			ul,li{list-style:none;}
			.wrap{width:980px; margin-left:auto; margin-right:auto;}
			a{ text-decoration:none; outline: none; }
			.top-wrapper{background:#fff;}
			.common-hd-nav a{display:block;height:38px;font-size:12px;}
			.clearfix:after{ visibility: hidden; display: block; font-size: 0; content: " "; clear: both; height: 0; }.clearfix{*zoom:1;}
			.common-hd-nav li{width:125px;float:left;dispaly:inline;margin:24px 0 0 15px;position:relative;text-indent:0;background:url(http://static.img.xywy.com/channel-public/images/nav_ico_new_v2.gif) no-repeat;}
			.common-hd-nav .common-hd-health-nav{background-position:0 0;}
			.common-hd-nav .common-hd-user-nav{background-position:0 -44px;}
			.common-hd-nav .common-hd-drug-nav{background-position:0 -88px;}
			.common-hd-nav .common-hd-doctor-nav{background-position:0 -132px;}
			.common-hd-health-nav a,.common-hd-user-nav a,.common-hd-drug-nav a,.common-hd-doctor-nav a{text-indent:-9999px;background:url(http://static.img.xywy.com/channel-public/images/nav_arrow_down.gif) 110px 17px no-repeat;}
			.common-hd-health-nav .common-hd-arrow-up,.common-hd-user-nav .common-hd-arrow-up,.common-hd-drug-nav .common-hd-arrow-up,.common-hd-doctor-nav .common-hd-arrow-up{background:url(http://static.img.xywy.com/channel-public/images/nav_arrow_up.gif) 110px 17px no-repeat;}
			.common-hd-drop-down{display:none;width:99px;position:absolute;top:-8px;left:24px;border:1px solid #28b4c3;border-bottom-left-radius:5px;border-bottom-right-radius:5px;background:#fff;box-shadow:0 2px 5px 2px rgba(40,180,195,.2)}
			.common-hd-nav span{width:38px;height:38px;position:absolute;left:-1px;top:-39px;display:block;background:url(http://static.img.xywy.com/channel-public/images/item_nav_logo_v2.gif) no-repeat;z-index:9999;}
			.common-hd-drop-down a{display:block;height:24px;line-height:24px;padding-left:20px;color:#666;text-indent:0;}
			.common-hd-drop-down a:hover{color:#fff;text-decoration:none;background:#28b4c3;}
			.common-hd-health-service-menu,.common-hd-user-service-menu,.common-hd-drug-service-menu,.common-hd-doctor-service-menu{position:absolute;}
			.common-hd-health-service-menu span{background-position:0 1px;}
			.common-hd-user-service-menu span{background-position:0 -47px;}
			.common-hd-drug-service-menu span{background-position:0 -95px;}
			.common-hd-doctor-service-menu span{background-position:0 -144px;}

			.j-logo{width:132px; height:46px;}
            .j-descripe{background: url(http://static.img.xywy.com/jbindex/images/qz.gif) no-repeat  6px 4px ;height: 43px;margin: 2px 0 0 8px;width: 186px; }
			.public-main-nav {background-color: #28b4c3;height: 38px;}
			.nav-list li {cursor: pointer;display: inline;float: left;height: 38px;line-height: 38px;margin-right: 1px;overflow: hidden;text-align: center;width: 162px;}
			.nav-list li a{color: #FFFFFF;display: block;font-size: 16px;height: 38px;text-indent: 0;width: 34px; width:162px; text-align:center;}
			.nav-list li a:hover{ text-decoration:none; background:#1ba0af;}
			.nav-list li.current{background:#1ba0af;}
			</style>
			<ul class="common-hd-nav fr">
			<li class="common-hd-health-nav">
			<a href="javascript:void(0)" target="_self">健康知识</a>
			<div class="common-hd-health-service-menu">
			<span></span>
			<div class="common-hd-drop-down" style="display: none;">
			<a target="_blank" href="http://jib.xywy.com/">疾病百科</a>
			<a target="_blank" href="http://zzk.xywy.com/">症状百科</a>
			<a target="_blank" href="http://jck.xywy.com/">检查项目</a>
			<a target="_blank" href="http://zx.xywy.com/mrzx/">整形项目</a>
			<a target="_blank" href="http://www.xywy.com/shoushu">手术项目</a>
			<a target="_blank" href="http://www.xywy.com/muying">母婴百科</a>
			<a target="_blank" href="http://www.xywy.com/caipu/">食疗养生</a>
			<a target="_blank" href="http://www.xywy.com/zixun/">健康资讯</a>
			</div>
			</div>
			</li>
			<li class="common-hd-user-nav">
			<a href="javascript:void(0)" target="_self">用户服务</a>
			<div class="common-hd-user-service-menu">
			<span></span>
			<div class="common-hd-drop-down" style="display: none;">
			<a target="_blank" href="http://club.xywy.com">有问必答</a>
			<a target="_blank" href="http://z.xywy.com/jiahaoshouye.htm">预约转诊</a>
			<a target="_blank" href="http://club.xywy.com/familyDoctor/">家庭医生</a>
			<a target="_blank" href="http://z.xywy.com/dhys.htm">电话咨询</a>
			<a target="_blank" href="http://home.xywy.com/">病友圈</a>
			<a target="_blank" href="http://club.xywy.com/healthShare">健康经验</a>
			<a target="_blank" href="http://www.xywy.com/fangtan/">专家访谈</a>
			<a target="_blank" href="http://club.xywy.com/salon/">线下活动</a>
			</div>
			</div>
			</li>
			<li class="common-hd-drug-nav">
			<a href="javascript:void(0)" target="_self">药品导航</a>
			<div class="common-hd-drug-service-menu">
			<span></span>
			<div class="common-hd-drop-down" style="display: none;">
			<a href="http://yao.xywy.com/" target="_blank">药品网</a>
			<a href="http://wksc.xywy.com/" target="_blank">闻康商城</a>
			</div>
			</div>
			</li>
			<li class="common-hd-doctor-nav">
			<a href="javascript:void(0)" target="_self">医生服务</a>
			<div class="common-hd-doctor-service-menu">
			<span></span>
			<div class="common-hd-drop-down" style="display: none;">
			<a href="http://club.xywy.com/doctorhome/" onmousedown="__sendClickOdm('pc_ucenter', this, ':rightnav+serviceplatform')" target="_blank">医平台首页</a>
			<a href="http://club.xywy.com/zixun/" onmousedown="__sendClickOdm('pc_ucenter', this, ':rightnav+information')" target="_blank">医学资讯</a>
			<a href="http://club.xywy.com/doctorShare/" onmousedown="__sendClickOdm('pc_ucenter', this, ':rightnav+share')" target="_blank">交流分享</a>
			<a href="http://club.xywy.com/zhaopin/" onmousedown="__sendClickOdm('pc_ucenter', this, ':rightnav+joinus')" target="_blank">招聘中心</a>
			<a href="http://club.xywy.com/shouce/" onmousedown="__sendClickOdm('pc_ucenter', this, ':rightnav+manual')" target="_blank">知识手册</a>
			<a href="http://club.xywy.com/doctor/3" onmousedown="__sendClickOdm('pc_ucenter', this, ':rightnav+doctorlife')" target="_blank">中国医生一天</a>
			<a href="http://club.xywy.com/zhuanti/doctor.html#doctor" target="_blank">服务介绍</a>
			</div>
			</div>
			</li>
			</ul>
			<script>
			$('#common-hd-nav').find('li').bind({
			mouseenter: function(){
			$(this).children('a').addClass('common-hd-arrow-up').end().find('.common-hd-drop-down').show();
			},
			mouseleave: function(){
			$(this).children('a').removeClass('common-hd-arrow-up').end().find('.common-hd-drop-down').hide();
			}
			});
			</script>
			</div>

        </div>
    </div>
    <div id="main_nav" class="public-main-nav mt15">
        <div class="wrap">
            <ul class="nav-list clearfix">
                <li>
                    <a class=" nav-index " href="http://home.xywy.com/">首页</a>
                </li>
                <li>
                    <a class=" nav-ks" href="http://home.xywy.com/quanzi/">找疾病圈子</a>
                </li>
                <li>
                    <a class=" nav-bw " href="http://home.xywy.com/doctor/">找专家</a>
                </li>
                <li>
                    <a class=" nav-zm " href="http://home.xywy.com/user/">找患友</a>
                </li>
            </ul>

        </div>
    </div>
</div>
<!--end home-header-->


<div class="group-header rp-bg">
	<div class="w980 bc">
		<div class="group-box clearfix">
			<div class="group fl mt20">
            	<div class="clearfix">
                    <div class="home-user-hd sp-bg fl mr15" style="width:32px; height:25px;">
                        <a href="http://home.xywy.com/xinzangbing/" title="心脏病圈"><img width="32" height="25" alt="心脏病圈" src="http://home.xywy.com/photos/group/2013/04/18/1366271773_1.jpg" class="mt1 ml2"></a>
                    </div>
                    <div class="f16 fl fYaHei fb gray-a normal-a"><a href="http://home.xywy.com/xinzangbing/" title="心脏病圈">心脏病圈</a></div>
                </div>
				<dl>
					<dd class="pt10 lh180 gray group-info oh">了解他人的治疗经验，了解他人的心路历程，寻找他人治疗方法解决自己的疑问，就来冠心病圈。这里聚集了不同状态的冠心病患者，他们分享了自己宝贵经验。</dd>
					<dd class="pt5 f14 graydeep" style="width:600px;">
						<span>患友:<a href="http://home.xywy.com/xinzangbing/user/"><b class="fn green">2269</b></a></span>
						<span class="ml30">专家:<a href="http://home.xywy.com/xinzangbing/doctor/"><b class="fn green">1385</b></a></span>
						<span class="ml30">话题:<a href="http://home.xywy.com/xinzangbing/huati/"><b class="fn green">0</b></a></span>
												<span class="ml30">
						版主:
						                        	<a href="http://home.xywy.com/user/45444632.html" target="_blank" title="星空闪烁"><b class="fn green">星空闪烁</b></a>
                        						</span>
											</dd>
				</dl>
			</div>
			<div class="group-join fr mr30" style="margin-top:70px;">
				<a href="javascript:void(0);" onclick="var uid =''; if(uid==''){ loginPopNew();}else { window.location.href='http://home.xywy.com/user.php?act=addgroup&gpinyin=xinzangbing'};" class="dib sp-bg group-btn group-jbtn"></a>			</div>
		</div><!--end group-box-->
		<div class="group-nav pt25">
			<ul class="clearfix tc f14 gray-a normal-a">
				<li class="fl mr5 "><a class="db sp-bg" href="http://home.xywy.com/xinzangbing/">圈子首页</a></li>
                <li class="fl mr5 current"><a class="db sp-bg" href="http://home.xywy.com/xinzangbing/huati/">话题讨论</a></li>
				<li class="fl mr5 "><a class="db sp-bg" href="http://home.xywy.com/xinzangbing/user/">找同病患友</a></li>
				<li class="fl mr5 "><a class="db sp-bg" href="http://home.xywy.com/xinzangbing/doctor/">找疾病专家</a></li>

				<li class="fl mr5 "><a class="db sp-bg" href="http://home.xywy.com/xinzangbing/xuexi/">疾病学习中心</a></li>			</ul>
		</div>
	</div>
</div><!--end group-header-->
<!-- Baidu Button BEGIN -->
    <!--<script type="text/javascript" id="bdshare_js" data="type=slide&amp;img=0&amp;pos=right&amp;uid=0" ></script>
    <script type="text/javascript" id="bdshell_js"></script>
    <script type="text/javascript">
    document.getElementById("bdshell_js").src = "http://bdimg.share.baidu.com/static/js/shell_v2.js?cdnversion=" + Math.ceil(new Date()/3600000);
    </script>-->

<script>window._bd_share_config={"common":{"bdSnsKey":{},"bdText":"","bdMini":"2","bdMiniList":false,"bdPic":"","bdStyle":"0","bdSize":"16"},"slide":{"type":"slide","bdImg":"0","bdPos":"right","bdTop":"90"}};with(document)0[(getElementsByTagName('head')[0]||body).appendChild(createElement('script')).src='http://bdimg.share.baidu.com/static/api/js/share.js?v=89860593.js?cdnversion='+~(-new Date()/36e5)];
</script>
<!-- Baidu Button END -->
<div class="w980 bc mt15">
	<div class="position pb10 gray-a normal-a deepgray"><br />您现在的位置：<a href="http://home.xywy.com/">首页</a> > <a href="http://home.xywy.com/xinzangbing/">心脏病圈</a> &gt; <a href="http://home.xywy.com/xinzangbing/huati/">话题讨论</a> &gt; <a href="http://home.xywy.com/xinzangbing/xzbtl/">讨论区</a> &gt; 地震会引发心脏病？</div>
	<div class="home-item-bdr home-item-bdrb">
		<div class="eq-height pt1 clearfix">
			<div class="w688 fl">
				<div class="group-main-hd graydeep pl15" style="background:none;">
					<a class="fr mr10 sp-bg go-reply" href="#quick_reply" onclick="reply(393917)"></a>
					<a class="fr mr10 sp-bg go-talk" href="#" onclick="pubtheme()"></a>
					<!--<a class="fr mr10" href="javascript:;" onclick="pubreport()">举报</a>-->
					<span class="mr10">总话题：0</span>
					<span class="mr10">昨日：0</span>
					<span class="mr10">今日：0</span>
				</div>
				<div class="home-item-bdrb mt5 pt2">
					<h1 class="group-talk-title fYaHei f18 fb graydeep tc">地震会引发心脏病？</h1>
				</div>
                				<div class="bm-bdr pt20 pb15 clearfix">
					<div class="fl ml15 group-talk-userinfo">
						<div class="home-user-hd bc sp-bg mr15">
							<a href="http://home.xywy.com/user/52323388.html" title="王莽"><img width="96" height="96" class="mt1 ml2" src="http://home.xywy.com/photos/default/default01.jpg" alt="王莽"></a>
						</div>
                        						<dl class="pt5">
							<dt class="fb gray-a normal-a">
							<a class="dib vm" href="http://home.xywy.com/user/52323388.html" title="王莽">王莽</a>
							<!-- <span class="dib ml5 sp-bg vm user-lv lv-1"></span> -->
							</dt>
							<dd class="pt5 gray">等级1：注册看看</dd>							<dd class="pt5 gray">患友</dd>
                            <dd class="pt5 gray">男，31岁</dd>
							<dd class="pt5 blue-a normal-a"><a href="http://home.xywy.com/xinzangbing/xuexi//" title=""></a></dd>
														<dd class="pt5 clearfix">
							<span class="fl attent attent-btn sp-bg cp" data-userid="52323388" data-type="atten" data-token="4e8f8a93de7a7220a58d0dffeb369ce4"></span>							<a class="fl ml2 sp-bg group-user-msg" title="发私信" href="http://home.xywy.com/user.php?act=dmsg&muid=52323388" target="_blank"></a>
							</dd>
													</dl>
											</div><!--end group-talk-userinfo-->
					<div class="fr group-talk-content">
						<div class="group-talk-text pr15 f14 wordbreak graydeep">
							&nbsp; &nbsp; 上月末，尼泊尔发生了大地震，和汶川地震时候的一个等级，可见地震是很严重的。地震是一个突然发生的，毁灭性很大的自然灾害，人人都很害怕它的来临。除了导致人们直接的损伤以外，还会导致很多疾病，比如：心脏病。很多研究都显示地震和心脏病有着十分密切的联系。<br><br>&nbsp; &nbsp; 在1995年日本阪神大地震后4周，震中附近居民心肌梗死发生率较地震前数年增加3.5倍，其中女性患者所占比例明显增加，超过50%。在汶川地震使住院的心脏病患者恶性室性心律失常发病率增加。地震还可导致心源性猝死发生率上升，多个研究发现，在1981年希腊，1989年澳大利亚纽卡斯尔，1994年以及2001年美国Nisqually等地地震发生后3天猝死发生水平明显上升。　地震作为一种严重的，突发的地质灾害，其对心血管系统的影响是多方面的，既有直接的外伤性创伤，也有内在的急慢性应激所致的内分泌神经精神生理改变，同时也有地震导致的空气水源污染，居住环境改变，基础设施毁坏，社会支持缺失，就医困难等多方面因素。<br><br>&nbsp; &nbsp; 地震月恶性室性心律失常患者的急性心肌缺血都在强震后不久出现，而心力衰竭多与长时间的精神紧张和睡眠不足有关。提示地震可能通过引起急性心肌缺血和心力衰竭，来诱发心脏病患者发生恶性室性心律失常。<br><br><br>	<br><br>
						</div>

						<div class="pt15 pr15 blue-a normal-a">
							<span class="fr gray">2015-05-07 09:54:03</span>
							<a class="dib pl20 sp-bg user-reply cp" onclick="reply(393917);">回复</a>
							<a class="dib mr10" href="javascript:;" onclick="pubreport()">举报</a>
						</div>

					</div><!--end group-talk-content-->
				</div>
                												<div class="bm-bdr pt20 pb15 pr clearfix">
					<div class="fl ml15 group-talk-userinfo">
						<div class="home-user-hd bc sp-bg mr15">
							<a href="http://home.xywy.com/user/52323538.html" title="花满楼"><img width="96" height="96" class="mt1 ml2" src="http://home.xywy.com/photos/default/default.jpg" alt="花满楼"></a>
						</div>
                        						<dl class="pt5">
							<dt class="fb gray-a normal-a">
							<a class="dib vm" href="http://home.xywy.com/user/52323538.html" title="花满楼">花满楼</a>
							<!--<span class="dib ml5 sp-bg vm user-lv lv-1"></span>-->
							</dt>
							<dd class="pt5 gray">等级1：注册看看</dd>							<dd class="pt5 gray">患友</dd>
                            <dd class="pt5 gray">女，31岁</dd>
							<dd class="pt5 blue-a normal-a"><a href="http://home.xywy.com/xinzangbing/xuexi//" title=""></a></dd>
														<dd class="pt5 clearfix">
							<span class="fl attent attent-btn sp-bg cp" data-userid="52323538" data-type="atten" data-token="954279adfe6bb201685c0fa15fafed88"></span>							<a class="fl ml2 sp-bg" title="发私信" date-href="http://home.xywy.com/user.php?act=dmsg&muid=52323538" target="_blank"></a>
							</dd>
													</dl>
											</div><!--end group-talk-userinfo-->
					<div class="fr group-talk-content">
						<div class="group-talk-text pr15 f14 wordbreak graydeep">
							可能是见识过那样的场面以后，就有一些“一朝被蛇咬，十年怕井绳”的感觉，但是自己还是好好控制一下吧！						</div>
						<div class="pt15 pb10 pr15 bm-bdr blue-a normal-a">
							<span class="fr gray">2015-05-07 09:58:29</span>
							<span class="dib pl20 sp-bg graydeep user-reply">0条回复
							<a class="dib mr10" href="javascript:;" onclick="pubreport()">举报</a></span>
						</div>

						<div class="clearfix pt20 pr15">
							<a href="javascript:showReplyDiv(339910,'block');" class="fl sp-bg say-word"></a>													</div>

												<div class="pr pr15 mt15" id="replyDiv339910" style="display:none;">
							<span class="user-reply-arrow sp-bg oh pa"></span>
							<div class="user-reply-box pl15 pb15">
                                                                                                                <div style=" width:512px; height:140px; position:absolute; top:5px; text-align:center; font-size:20px; line-height:80px;"><a href="javascript:void(0);" onClick="loginPopNew()">点击登录</a></div>

								<form action="" method="post" name="replyform" id="replyform" target="add" onsubmit="return themereply(this);">
									<div class="pt15 gray-a normal-a f14" style="display:none;"><a class="dib pl20 sp-bg insert-pic" href="javascript:;">图片</a></div>
									<div class="pt15"><textarea class="user-reply-tarea w500" style="height:50px;" name="content" id="content339910"></textarea></div>
									<div class="tr pt15" style="padding-right:22px;">
										<input type="hidden" name="themeid" value="393917" />
										<input type="hidden" name="replyid" value="339910" />
										<input type="hidden" name="type" value="reply" />
										<button type="submit" class="reply-btn sp-bg cp" name="reply" value="提交"></button>
									</div>
								</form>
							</div>
							<a class="fr gray" href="javascript:showReplyDiv(339910,'none');">隐藏</a>
						</div>
											</div><!--end group-talk-content-->
									</div>
												<div class="page pt20 pb20 tc">
					<div><span>总计: 1条记录</a></span> </div>
				</div>
                <div class="home-item-bdrb quick-reply-bdr">
                <div class="quick-reply-hd pl15 f14 fb graydeep rp-bg">快速回复</div>
                <div class="user-reply-box quick-reply-bd pt15 pb15 clearfix">
                    <div class="home-user-hd sp-bg fl mt10 ml15 mr15"><img width="96" height="96" class="mt1 ml2" src="http://img.xywy.com/home_new/images/96x96.jpg" alt=""></div>
                    <div class="group-patient fl ml15 pr">
                        <a name="quick_reply"></a>
                                                        <div style=" width:512px; height:140px; position:absolute; top:10px; text-align:center; font-size:25px; line-height:140px;"><a href="javascript:void(0);" onClick="loginPopNew()">点击登录</a></div>

                        <form name="" method="post" action="" onsubmit="return themereply(this);">
                            <div class="gray-a normal-a f14" style="display:none;"><a href="javascript:;" class="dib pl20 sp-bg insert-pic">图片</a></div>
                            <div class="pt10"><textarea id="quickreply" name="content" class="user-reply-tarea w500" style="width:510px;height:80px;visibility:hidden;"></textarea></div>
                            <div style="padding-right:28px;" class="pt15 clearfix">
                                <div class="fl graydeep">请遵守<a class="orange" href="http://home.xywy.com/">病友圈</a>言论规则，不得违反国家法律规定</div>
                                <input type="hidden" name="themeid" value="393917" />
                                <input type="hidden" name="replyid" value="0" />
                                <input type="hidden" name="type" value="theme" />
                                <button class="fr reply-btn sp-bg cp" type="submit" value="提交" name="reply"  id="reply" ></button>
                            </div>
                        </form>
                    </div>
                </div>
                            </div>
			</div><!--end w688-->
			<div class="w290 fr pr">
                            	<div class="group-hot bm-bdr pb10">
                    <div class="hot-bt pt15 pl15 f14 fb deepgray">热门话题</div>
                    <ul class="mt10 pl15 pr15 oh">
                                                    <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/916897.html" target="_blank" title="得了肥厚性心肌病吃中药还是吃西药？">得了肥厚性心肌病吃中药还是吃西药？</a></li>
                                                    <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/831178.html" target="_blank" title="肥厚性心肌病患者可摄入高蛋白食物促进心血管健康">肥厚性心肌病患者可摄入高蛋白食物促...</a></li>
                                                    <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/831162.html" target="_blank" title="装了起搏器，左臂少用力，可以替代起搏器治疗肥厚性心肌病的方法">装了起搏器，左臂少用力，可以替代起...</a></li>
                                                    <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/814934.html" target="_blank" title="肥厚化瘀汤专家教您科学饮食使心脏更年轻">肥厚化瘀汤专家教您科学饮食使心脏更...</a></li>
                                                    <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/776647.html" target="_blank" title="肥厚型心肌病患者足不出户看名医">肥厚型心肌病患者足不出户看名医</a></li>
                                                    <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/764301.html" target="_blank" title="冠心病会带来哪些危险呢？怎样治疗冠心病？">冠心病会带来哪些危险呢？怎样治疗冠...</a></li>
                                            </ul>
                </div>

                                <div class="group-hot bm-bdr pb10">
                    <div class="new-bt pt15 pl15 f14 fb deepgray">最新话题</div>
                    <ul class="mt10 pl15 pr15 oh">
                                                        <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/916897.html" target="_blank" title="得了肥厚性心肌病吃中药还是吃西药？">得了肥厚性心肌病吃中药还是吃西药？</a></li>
                                                        <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/831178.html" target="_blank" title="肥厚性心肌病患者可摄入高蛋白食物促进心血管健康">肥厚性心肌病患者可摄入高蛋白食物促...</a></li>
                                                        <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/831162.html" target="_blank" title="装了起搏器，左臂少用力，可以替代起搏器治疗肥厚性心肌病的方法">装了起搏器，左臂少用力，可以替代起...</a></li>
                                                        <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/814934.html" target="_blank" title="肥厚化瘀汤专家教您科学饮食使心脏更年轻">肥厚化瘀汤专家教您科学饮食使心脏更...</a></li>
                                                        <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/776647.html" target="_blank" title="肥厚型心肌病患者足不出户看名医">肥厚型心肌病患者足不出户看名医</a></li>
                                                        <li><a style="color: #000000" href="http://home.xywy.com/xinzangbing/764301.html" target="_blank" title="冠心病会带来哪些危险呢？怎样治疗冠心病？">冠心病会带来哪些危险呢？怎样治疗冠...</a></li>
                                            </ul>
                </div>
                                                                        <div class="group-pic mt10" style="margin-top:0px;margin-left:1px;margin-bottom:1px;"><a href="http://club.xywy.com/familyDoctor/zhuanti/mother" target="_bank"><img  src="http://home.xywy.com/photos/custom/2015/05/06/1430873380_1.jpg" width="290" height="150"></a></div>
                        												<div class="bm-bdr">
					<div class="group-side-hd pt15 pl15 f14 fb deepgray">推荐专家</div>
					<ul class="group-rec-expb clearfix mt10 pl15 pr15 oh">
											<li class="fl w pb20">
							<div class="home-user-hdd sp-bg fl mr15">
								<a href="http://home.xywy.com/doctor/6010305.html" title="尚克福"><img width="68" height="68" class="mt1" alt="尚克福" src="http://home.xywy.com/photos/club/201209/20120907161108.jpg"></a>
							</div>
							<dl class="fl">
								<dt class="gray-a fb normal-a"><a href="http://home.xywy.com/doctor/6010305.html" title="尚克福" class="dib vm">尚克福</a><!--<span class="dib ml5 sp-bg vm user-lv lv-1"></span>--></dt>
								<dd class="pt5 gray" title="周村卫生院">周村卫生院 医师</dd>
																<dd class="pt5 clearfix" id="rightatten6010305">
								<span class="fl attent attent-btn sp-bg cp" data-userid="6010305" data-type="atten" data-token="f54eb18c53fe48cf8630db9bba82941a"></span>								</dd>
															</dl>
						</li>
											<li class="fl w pb20">
							<div class="home-user-hdd sp-bg fl mr15">
								<a href="http://home.xywy.com/doctor/4939132.html" title="徐羽"><img width="68" height="68" class="mt1" alt="徐羽" src="http://home.xywy.com/photos/club/201109/20110908173431.jpg"></a>
							</div>
							<dl class="fl">
								<dt class="gray-a fb normal-a"><a href="http://home.xywy.com/doctor/4939132.html" title="徐羽" class="dib vm">徐羽</a><!--<span class="dib ml5 sp-bg vm user-lv lv-1"></span>--></dt>
								<dd class="pt5 gray" title="河南中医学院第三附属医院">河南中医学院第三附属医院 医师</dd>
																<dd class="pt5 clearfix" id="rightatten4939132">
								<span class="fl attent attent-btn sp-bg cp" data-userid="4939132" data-type="atten" data-token="c4fe146508ab81d6b8550b75cb128270"></span>								</dd>
															</dl>
						</li>
										</ul>
				</div>
																				<span class="pa corners sp-bg"></span>
			</div><!--end w290-->
		</div>
	</div>
	<div class="home-item-bm home-item-bmb rp-bg"></div>
</div><!--end w980-->
<iframe id="add" class="none" name="add">
</iframe>
<script type='text/javascript'>
    var uid ='';
	function themereply(obj){
		var uid ='';
		if(uid==''){
			uid = this.getCookie('cookie_user');
		}
		if(uid==''){
			loginPopNew();
		}else{
			//return true;
                        replysumbit(obj)

		}
                return false;
	}

        function replysumbit(obj){
            $.ajax({
                //contentType: "application/x-www-form-urlencoded; charset=gbk",
                type: "POST",
                url: $(obj).attr('action'),
                data: $(obj).serialize(),
                dataType: 'json',
                success: function(data){
                    if(data.state == 1){
                      showMsg(data.msg,data.url);
                    }else{

                      if((data.msg !== null && data.msg != '') && (data.$url !== null && data.$url != ''))
                        showMsg(data.msg,data.$url);
                      else if((data.msg === null || data.msg == '') && (data.url !==null && data.url != ''))
                        top.location.href = data.url;
                      else if((data.msg !== null && data.msg != '') && (data.url ===null || data.url == ''))
                        showMsg(data.msg);

                    }
                }
            });

        }

</script>
<div class="res_box clearfix none" id="res_box">
	<div class="boxgbk clearfix">
    	<div class="gb fr"><a id="res_close" href="javascript:;">关闭</a></div>
    </div>
    <div class="box_jbht mt20">您要举报的话题为<span>地震会引发心脏病？</span>需要填写以下信息</div>
	<div class="box_cent">
        <div class="box_name clearfix mt10">
            <div class="xm_ty fl"><span class="fr">举报地址：</span></div>
            <div class="xmbox fl pt5">http://home.xywy.com/xinzangbing/393917.html</div>
        </div>

        <div class="box_name clearfix mt10">
            <div class="xm_ty fl"><span class="fr">举报内容：</span></div>
            <div class="xmbox fl"><input type="text" name="reason" id="reason" value="" /></div>
        </div>

        <div class="box_name clearfix mt10">
            <div class="xm_ty fl"><span class="fr">正确内容：</span></div>
            <div class="ndkfbox fl"><textarea name="content" id="content"></textarea></div>
        </div>
        <div class="pt15 pb15 tc"><button type="button" onclick="report_insert()" class="res_btn cp"></button></div>
    </div>
</div>
<div id="loginpop" class="home-login-pop none">
	<div class="pt5 pb5 pl5 pr5">
		<div class="pop-bd pb10">
			<div class="tc f16 fYaHei green fb pop-hd">登录我的病友圈</div>
			<form action="" method="post" name="login">
				<div class="clearfix pt15" style="padding-left:70px;">
					<label class="fl pt2 f14 fYaHei graydeep">账号：</label>
					<input onfocus="statusChange(this, 'focus');" onblur="statusChange(this, 'blur');" type="text" value="请输入用户名" name="login_footer_user" id="login_footer_user" class="fl sp-bg login-name f12 gray">
				</div>
				<div class="clearfix pt15" style="padding-left:70px;">
					<label class="fl pt2 f14 fYaHei graydeep">密码：</label>
					<input onfocus="statusChange(this, 'focus');" onblur="statusChange(this, 'blur');" type="password" value="请输入密码" name="login_footer_pwd" id="login_footer_pwd" class="fl sp-bg login-pwd gray" onkeydown="if(event.keyCode==13) login_footer();">
				</div>
				<div class="clearfix pt15 pl20" style="padding-left:112px;">
					<input type="checkbox" value="" name="autologin" class="fl user-file-radio">
					<span class="fl ml5 graydeep">自动登录</span>
					<span class="fl ml20 gray-a normal-a"><a href="http://sq.xywy.com/uc/reg/getpwd.htm" target="_blank">忘记密码?</a></span>
				</div>
				<div class="clearfix pt15 pl20" style="padding-left:112px;">
					<button type="button" class="fl sp-bg cp pop-btn" onClick="login_footer()"></button>
					<a href="http://passport.xywy.com/member/reg_mobile.htm?cid=null&indicate=home" class="fl ml20 mt5 green f14">免费注册</a>
				</div>
			</form>
		</div>
	</div>
	<span id="popclose" class="pa sp-bg cp login-close" style="top:12px;right:12px;"></span>
</div>
<div class="pub-pop none" id="pubpop">
    <div class="pub-pop-content pb10">
        <div class="pub-pop-hd gray-a normal-a"><a id="pubpopclose" class="fr mr10" href="javascript:;">关闭</a></div>
        <div class="pub-pop-bd mt10 pt10 pb10 clearfix">
            <span class="fl ml30 pub-pop-st"></span>
            <span class="fl ml20 pt10 f14 fb deepgray" id="msg" style="width:250px;"></span>
        </div>
        <div class="pub-pop-bm ml10 mr10 mt10 pt10 tr">
            <a href="javascript:;" class="dib mr10 ok"></a><a href="javascript:;" class="dib cancel"></a>
        </div>
    </div>
</div>
<div class="w980 bc">
<div class=" w home-footer rp-bg mt15">
<script type="text/javascript">
    var common_navFlag = 1;
    var LEFT_FLOAT_YINRU = 1;
</script>
<script src="http://static.js.xywy.com/channel-public/js/public_bottom.js" type="text/javascript"></script>
</div>
</div>
 <a id="gotop" href="#" class="goto-top t9999 none" title="返回顶部">返回顶部</a>
 <script type="text/javascript">
 Tinker.UI.toPlace('gotop', 'top', {animate:true});
 </script>
<div style="display:none">
<script language="javascript" src="http://pub1.wkimg.com/rightpop/rightpopwin.js"></script>
<script language="javascript" src="http://stat.xywy.com/a.js"></script>
<script type="text/javascript">var cnzz_protocol = (("https:" == document.location.protocol) ? " https://" : " http://");document.write(unescape("%3Cspan id='cnzz_stat_icon_1253416370'%3E%3C/span%3E%3Cscript src='" + cnzz_protocol + "s6.cnzz.com/stat.php%3Fid%3D1253416370' type='text/javascript'%3E%3C/script%3E"));</script>
<script src="http://s6.cnzz.com/stat.php?id=5270849&web_id=5270849" language="JavaScript"></script>
</div>
<script>
var mobileNumber = null;
var numberSource = "pc_po_jkzj";
function loginPopNew(url){

$.ajaxSetup({
    cache: true
});

   $('script[src="https://scs.static.xywy.com/ucenter/js/LoginRegister/gbk/web-nonew.js"]').remove();
   if(typeof(url) == 'undefined'){
       url = top.document.location.href;
   }

mobileNumber = {       //必须设置对象，对象中的变量可为空。
　　Mobile : '',
　　needMobile:'',
　　loginSinUp:'on',        //on为普通登录   off为免注册登录
　　loginUserPlace:'',       //普通登陆默认显示手机号(可为空，按需所传)
    ucBack:url
};

    $('body').append('<script type="text\/javascript" src="https:\/\/scs.static.xywy.com\/ucenter\/js\/LoginRegister\/gbk\/web-nonew.js"><\/script>');
}
</script></body>
</html>
'''
def process(s):
    import json
    a = []
    from lxml import etree
    xp = etree.HTML(s, parser=etree.HTMLParser(encoding="utf-8"))
    items = xp.xpath('//div[contains(@class,"bm-bdr pt20 pb15")]')
    for item in items:
        b = {}
        content_list = item.xpath('.//div[contains(@class,"group-talk-text pr15 f14 wordbreak graydeep")]')
        if content_list:
            content = content_list[0].xpath('string(.)')
            b['content'] = content
        time_list = item.xpath('.//span[contains(@class,"fr gray")]')
        if time_list:
            time = time_list[0].xpath('string(.)')
            b['time'] = time
        name_list = item.xpath('.//a[contains(@class,"dib vm")]')
        if name_list:
            name = name_list[0].xpath('string(.)')
            b['name'] = name

        patient_gender_str = item.xpath('.//dl[contains(@class,"pt5")]')
        if patient_gender_str:
            patient_gender = patient_gender_str[0].xpath('string(.)')
            if u'男' in patient_gender:
                b['patient_gender'] = u'男'
            if u'女' in patient_gender:
                b['patient_gender'] = u'女'
        a.append(b)
    return a
    return json.dumps(a,indent= 4,ensure_ascii=False)

print(process(html))



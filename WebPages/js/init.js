// 以下是resize的各项参数
var navbarheight = 0;
var windowheight = 0;
var windowheighthalf = 0;
var chartareaheight = 0;
var chartareawidth = 0;
var tableonlyheight = 0;
var dubwidth = 0;
var dubheight = 0;

// 以下是为了优化体验写死的初始数据，对应正确的2018年统计
var defaultkeys = {
	'boxyear':["2015","2016","2017","2018"],
	'genre':["喜剧","动作","剧情","爱情","奇幻","冒险","悬疑","科幻","犯罪","惊悚","动画",
		"战争","家庭","儿童","恐怖","纪录片","历史","传记","运动"],
	'boxking':["红海行动","唐人街探案2","我不是药神"],
	'actor':["郭政建","梁超","林雪","徐峥","巴多","文松","王千源","郭京飞","董立范","王砚辉"]
};
var defaultvalues = {
	'boxyear':[4196612.14,4362515.96,5316974.59,5561062.03],
	'genre':[1641795.71,1565225.93,1380700.08,597217.19,575158.66,432425.6,413520.89,
		307777.73,233068.14,189451.56,78788.12,74348.55,24833.54,2119.2,2075.93,796.61,
		75.28,5.62,5.62],
	'boxking':[365100,337100,307500],
	'actor':[5,4,4,4,4,4,4,3,3,3]
};

$(document).ready(function(){
	// 移动版菜单初始化
  $(".button-collapse").sideNav({closeOnClick:true});
	// 下拉栏初始化
	$(document).ready(function(){
		$('select').material_select();
  });
	
	// 模态初始化
	$('.modal').modal({
		opacity: .4,
		ending_top: '22%'
	});
	// 自动调整高度的项
	
	reheight();
	
	$(window).resize(()=>{
		reheight();
	});
	
	// SPA显示隐藏元素
	$('#genrediv').hide();
	$('#boxkingdiv').hide();
	$('#logindiv').hide();
	$('#actordiv').hide();
	toboxyear();
});

var reheight = ()=>{
	// 填充固定顶栏留的空白
	navbarheight = $('.navbar-fixed').height();
	$('.stuffnav').height(navbarheight);
	windowheight = $(window).innerHeight() - navbarheight;
	if($(window).width()>993){
		tableonlyheight = windowheight / 3;
		windowheighthalf = 2 * tableonlyheight - 20;
		chartareaheight = windowheighthalf - navbarheight * 2 - 20;
		dubheight = chartareaheight;
		dubwidth = $('.container').width() - 36;
		chartareawidth = dubwidth / 2;
		$('.mobileonly').hide();
		var tableonly = $('.tableonly');
		tableonly.show();
		tableonly.height(tableonlyheight);
	}else{
		windowheighthalf = windowheight;
		chartareaheight = (windowheight - navbarheight * 2 - 18) / 2;
		dubheight = chartareaheight * 2;
		chartareawidth = $('.container').width();
		dubwidth = chartareawidth;
		$('.mobileonly').show();
		$('.tableonly').hide();
	}
	var chartarea=$('.chartarea');
	chartarea.css({'height':chartareaheight,'width':chartareawidth});
	chartarea.height(chartareaheight);
	chartarea.width(chartareawidth);
	$('.chartarea.dubw').width(dubwidth);
	$('.chartarea.dubh').height(dubheight);
	$('.windowheight').height(windowheight);
	$('.windowheighthalf').height(windowheighthalf);
};

function tologin(){
	$('#logindiv').show();
	$('#genrediv').hide();
	$('#boxkingdiv').hide();
	$('#boxyeardiv').hide();
	$('#actordiv').hide();
}

function togenre(){
	$('#logindiv').hide();
	$('#genrediv').show();
	$('#boxkingdiv').hide();
	$('#boxyeardiv').hide();
	$('#actordiv').hide();
	
	// 绘制图表
	if(chartgenre === 0)chartgenre = echarts.init(document.getElementById('cgenre'));
	if(!cgenrebar)cgenrebar = echarts.init(document.getElementById('cgenre-bar'));
	window.addEventListener("resize", function () {
		chartgenre.resize();
		cgenrebar.resize();
	});
	
	chartgenre.setOption(getoptiongenre(defaultkeys.genre,defaultvalues.genre));
	cgenrebar.setOption(getoptiongenrebar(defaultkeys.genre,defaultvalues.genre));
}

function toboxking(){
	$('#logindiv').hide();
	$('#genrediv').hide();
	$('#boxkingdiv').show();
	$('#boxyeardiv').hide();
	$('#actordiv').hide();
	
	// 绘制图表
	if(cbking === 0)cbking = echarts.init(document.getElementById('boxking'));
	if(cbkbar === 0)cbkbar = echarts.init(document.getElementById('boxking-bar'));
	window.addEventListener("resize", function () {
		cbking.resize();
		cbkbar.resize();
	});
	
	cbking.setOption(getoptionbking(defaultkeys.boxking,defaultvalues.boxking));
	cbkbar.setOption(getoptionbkbar(defaultkeys.boxking,defaultvalues.boxking));
}

function toboxyear(){
	$('#logindiv').hide();
	$('#genrediv').hide();
	$('#boxkingdiv').hide();
	$('#boxyeardiv').show();
	$('#actordiv').hide();

	if(boxyear === 0)boxyear = echarts.init(document.getElementById('boxyear'));
	window.addEventListener("resize", function () {
		boxyear.resize();
	});

	boxyear.setOption(getoptionboxyear(defaultkeys.boxyear,defaultvalues.boxyear));
}

function toactor(){
	$('#logindiv').hide();
	$('#genrediv').hide();
	$('#boxkingdiv').hide();
	$('#boxyeardiv').hide();
	$('#actordiv').show();

	// 绘制图表
	if(actorcloud === 0)actorcloud = echarts.init(document.getElementById('actorcloud'));
	if(actorbar === 0)actorbar = echarts.init(document.getElementById('actor-bar'));
	window.addEventListener("resize", function () {
		actorcloud.resize();
		actorbar.resize();
	});

	actorcloud.setOption(getoptionactorcloud(defaultkeys.actor,defaultvalues.actor));
	actorbar.setOption(getoptionactorbar(defaultkeys.actor,defaultvalues.actor));
}

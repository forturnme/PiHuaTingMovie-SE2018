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
var defaultkeys = {'boxyear':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
	'genre':["喜剧","动作","剧情","爱情","奇幻","冒险","悬疑","科幻","犯罪","惊悚","动画",
		"战争","家庭","儿童","恐怖","纪录片","历史","传记","运动"],
	'boxking':["红海行动","唐人街探案2","我不是药神"],
	'actor':["郭政建","梁超","林雪","徐峥","巴多","文松","王千源","郭京飞","董立范","王砚辉"]};
var defaultvalues = {'boxyear':
	[484912.76, 989880.48, 487309.76, 355012.95, 427144.11, 334027.28, 671168.72, 659934.14, 282294.38, 360388.85, 362398.96, 146589.64],
	'genre':[1641795.71,1565225.93,1380700.08,597217.19,575158.66,432425.6,413520.89,307777.73,233068.14,189451.56,78788.12,74348.55,
	24833.54,2119.2,2075.93,796.61,75.28,5.62,5.62],
	'boxking':[365100,337100,307500],
	'actor':[5,4,4,4,4,4,4,3,3,3]};

$(document).ready(function(){
// 	// 移动版菜单初始化
//   $(".button-collapse").sideNav({closeOnClick:true});
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
	
	todownload();
});

var reheight = ()=>{
	// 填充固定顶栏留的空白
	navbarheight = $('.navbar-fixed').height();
	$('.stuffnav').height(navbarheight);
	windowheight = $(window).innerHeight() - navbarheight;
	if($(window).width()>993){
		tableonlyheight = windowheight / 3;
		windowheighthalf = 2 * tableonlyheight - 20;
		chartareaheight = windowheighthalf - navbarheight * 2.2;
		dubheight = chartareaheight;
		dubwidth = $('.container').width() - 36;
		chartareawidth = dubwidth / 2;
		$('.mobileonly').hide();
		var tableonly = $('.tableonly');
		tableonly.show();
		tableonly.height(tableonlyheight);
	}else{
		windowheighthalf = windowheight;
		chartareaheight = (windowheight - navbarheight - 128) / 2;
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

/////////////////////////////////////////////////       新增        ////////////////////////////////////////
//作者：廖儒
function todownload() {//生成报表界面
	$('#download').show();

	if(chartgenre2 === 0)chartgenre2 = echarts.init(document.getElementById('dcgenre'));
	if(cgenrebar2 === 0)cgenrebar2 = echarts.init(document.getElementById('dcgenre-bar'));
	
	chartgenre2.setOption(getoptiongenre(defaultkeys.genre,defaultvalues.genre));
	cgenrebar2.setOption(getoptiongenrebar(defaultkeys.genre,defaultvalues.genre));
	
	cbkbar2 = echarts.init(document.getElementById('dboxking-bar'));
	
	cbkbar2.setOption(getoptionbkbar(defaultkeys.boxking,defaultvalues.boxking));
	
	if(boxyear2 === 0)boxyear2 = echarts.init(document.getElementById('dboxyear'));

	boxyear2.setOption(getoptionboxyear(defaultkeys.boxyear,defaultvalues.boxyear));
	boxyear2.setOption({animation : false});
	
	if(actorbar2 === 0)actorbar2 = echarts.init(document.getElementById('dactor-bar'));

	actorbar2.setOption(getoptionactorbar(defaultkeys.actor,defaultvalues.actor));
	
	$('#download').hide();
	drawboxingyear2();
	drawgenre2();
	drawbking2();
	drawactor2();
}

function toChangefilm()//变更文字内容
{
	var obj=document.getElementById("filmyear2");
	var index=obj.selectedIndex; //序号，取当前选中选项的序号
	var val = obj.options[index].text;
	x=document.getElementById("dfilm");  // 找到元素
	x.innerHTML=(val+"年的票房走势");    // 改变内容
	drawboxingyear2();
}

function toChangegenre()
{
	var obj=document.getElementById("genre-year2");
	var index=obj.selectedIndex; //序号，取当前选中选项的序号
	var val = obj.options[index].text;
	var obj2=document.getElementById("genre-month2");
	var index2=obj2.selectedIndex; //序号，取当前选中选项的序号
	var val2 = obj2.options[index2].text;
	x=document.getElementById("dticai");
	if( index2 === 0)
	x.innerHTML=(val+"年全年的题材份额"); 
	else
	x.innerHTML=(val+"年"+val2+"的题材份额"); 
	drawgenre2();
} 


//导出



function toChangeyear()
{
	var obj=document.getElementById("boxking-year2");
	var index=obj.selectedIndex; //序号，取当前选中选项的序号
	var val = obj.options[index].text;
	var obj2=document.getElementById("boxking-rank2");
	var index2=obj2.selectedIndex; //序号，取当前选中选项的序号
	var val2 = obj2.options[index2].text;
	x=document.getElementById("drank");
	x.innerHTML=(val+"年的票房前"+val2+"名");   
	drawbking2();	// 改变内容
	
}

function toChangeactor()
{
	var obj=document.getElementById("actoryear2");
	var index=obj.selectedIndex; //序号，取当前选中选项的序号
	var val = obj.options[index].text;
	x=document.getElementById("dactor");  // 找到元素
	x.innerHTML=(val+"年的劳模演员");    // 改变内容
	drawactor2();
}

function downl()
{
	$("#w").wordExport('皮划艇报表');
}

function f5()
{
	drawboxingyear2();
	drawgenre2();
	drawbking2();
	drawactor2();
}

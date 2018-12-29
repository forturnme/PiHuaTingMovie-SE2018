var chartgenre2 = 0,cgenrebar2 = 0,cbking2 = 0,cbkbar2 = 0,boxyear2 = 0,actorcloud2 = 0,actorbar2 = 0;//新增报表变量

var chartgenre = 0;
var getoptiongenre=(keys,values)=>{
	var datastr = new Array();
	for(var i=0;i<keys.length;i++){
		datastr.push({value:values[i], name:keys[i]});
	}
	return {
		toolbox: {
			feature: {
				saveAsImage: {}
			}
		},
		tooltip: {
			trigger: 'item',
			formatter: "{a} <br/>{b} : {c} ({d}%)"
		},
		legend: {
			orient: 'vertical',
			left: 'left',
			data: keys,
		},
		series: {
			name: '题材',
			type: 'pie',
			radius : '66%',
			center: ['65%', '60%'],
			data:datastr,
			itemStyle: {
				emphasis: {
					shadowBlur: 10,
					shadowOffsetX: 0,
					shadowColor: 'rgba(0, 0, 0, 0.5)'
				}
			}
		}
	};
};

var cgenrebar = 0;
var getoptiongenrebar=(keys,values)=>{
	return {
		toolbox: {
			feature: {
				saveAsImage: {}
			}
		},
		color: ['#3398DB'],
		tooltip : {
			trigger: 'axis',
			axisPointer : {
				type : 'shadow'
			}
		},
		grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
		},
		xAxis : [
			{
				type : 'category',
				data : keys,
				axisLabel:{
					showMinLabel:true,
					showMaxLabel:true,
					rotate:45,
					interval:0
				},
				axisTick: {
					alignWithLabel: true
				}
			}
		],
		yAxis : [
			{
				name: '票房/万元人民币',
				type : 'value'
			}
		],
		series :[{
			name:'票房/万元人民币',
			type:'bar',
			barWidth: '60%',
			data:values,
			itemStyle: {
				emphasis: {
					shadowBlur: 10,
					shadowOffsetX: 0,
					shadowColor: 'rgba(0, 0, 0, 0.5)'
				}
			}
		}]
	};
};


var cbking=0;
var getoptionbking=(keys,values)=>{
	var datastr = new Array();
	for(var i=0;i<keys.length;i++){
		datastr.push({
			value:values[i], name:keys[i]
		});
	}
	return {
		toolbox: {
			feature: {
				saveAsImage: {}
			}
		},
		tooltip: {
			show: true
		},
		series: [{
			name: '票房/万元人民币',
			type: 'wordCloud',
			size: ['80%', '75%'],
			sizeRange: [10, 40],
			rotationRange: [-90, 90],
			rotationStep: 45,
			gridSize: 2,
			shape: 'pentagon',
			drawOutOfBound: false,
			textPadding: 0,
			autoSize: {
				enable: true,
				minSize: 12
			},
			textStyle: {
				normal: {
					color: '#689f38',
					emphasis: {
						shadowBlur: 5,
						shadowColor: '#333'
					}
				}
			},
			data: datastr
		}]
	};
};

var cbkbar = 0;
var getoptionbkbar=(keys,values)=>{
	return {
		toolbox: {
			feature: {
				saveAsImage: {
					show: true
				}
			}
		},
		color: ['#3398DB'],
		tooltip : {
			trigger: 'axis',
			axisPointer : {
				type : 'shadow'
			}
		},
		grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
		},
		xAxis : [
			{
				type : 'category',
				data : keys,
				axisLabel:{
					showMinLabel:true,
					showMaxLabel:true,
					rotate:45,
					interval:0
				},
				axisTick: {
					alignWithLabel: true
				}
			}
		],
		yAxis : [
			{
				name:'票房/万元人民币',
				type : 'value'
			}
		],
		series :[{
			name:'票房/万元人民币',
			type:'bar',
			barWidth: '60%',
			data:values,
			itemStyle: {
				emphasis: {
					shadowBlur: 10,
					shadowOffsetX: 0,
					shadowColor: 'rgba(0, 0, 0, 0.5)'
				}
			}
		}]
	};
};

// 逐年票房折线图
var boxyear = 0;
var getoptionboxyear=(keys,values)=>{
	return {
		tooltip: {
			trigger: 'axis'
		},
		grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
		},
		toolbox: {
			feature: {
				saveAsImage: {}
			}
		},
		xAxis: {
			type: 'category',
			boundaryGap: false,
			data: keys
		},
		yAxis: {
			name: '票房/万元人民币',
			type: 'value'
		},
		series: [
			{
				name:'总票房/万元人民币',
				type:'line',
				data:values
			}
		]
	};
};

// 演员相关图表
var actorcloud = 0;
var getoptionactorcloud=(keys,values)=>{
	var datastr = new Array();
	for(var i=0;i<keys.length;i++){
		datastr.push({value:values[i], name:keys[i]});
	}
	return {
		toolbox: {
			feature: {
				saveAsImage: {}
			}
		},
		tooltip: {
			show: true
		},
		series: [{
			name: '出演数',
			type: 'wordCloud',
			size: ['85%', '85%'],
			textRotation:[0,90],
			// rotationRange: [46,80],
			textPadding: 0,
			autoSize: {
				enable: true,
				minSize: 14
			},
			textStyle: {
				normal: {
					color: '#ff6f00',
					emphasis: {
						shadowBlur: 5,
						shadowColor: '#333'
					}
				}
			},
			data: datastr
		}]
	};
};

var actorbar = 0;
var getoptionactorbar=(keys,values)=>{
	return {
		toolbox: {
			feature: {
				saveAsImage: {
					show: true
				}
			}
		},
		color: ['#7e57c2'],
		tooltip : {
			trigger: 'axis',
			axisPointer : {
				type : 'shadow'
			}
		},
		grid: {
			left: '3%',
			right: '4%',
			bottom: '3%',
			containLabel: true
		},
		xAxis : [
			{
				type : 'category',
				data : keys,
				data : keys,
				axisLabel:{
					showMinLabel:true,
					showMaxLabel:true,
					rotate:45,
					interval:0
				},
				axisTick: {
					alignWithLabel: true
				}
			}
		],
		yAxis : [
			{
				name: '出演数',
				type : 'value'
			}
		],
		series :[{
			name:'出演数',
			type:'bar',
			barWidth: '60%',
			data:values,
			itemStyle: {
				emphasis: {
					shadowBlur: 10,
					shadowOffsetX: 0,
					shadowColor: 'rgba(0, 0, 0, 0.5)'
				}
			}
		}]
	};
};

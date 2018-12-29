var getdata=(qstr,successfun,failfun)=>{
	$('#modal1').modal('open');
    $.ajax({
        type: 'POST',
        url: 'http://'+SERVER_ADDRESS+':5000/query',
        data: qstr,
		beforeSend:(R)=>{R.setRequestHeader('Connection','Keep-Alive');},
        success: (s)=>{$('#modal1').modal('close');successfun(s);},
        error: (e)=>{$('#modal1').modal('close');failfun(e);}
    });
};

var webalart=(e)=>{//报错的方法
	Materialize.toast('诶呀 服务器好像熟了', 2000);
};

var genresort=(keys,values)=>{
	var dctlst = [];
	for(var i=0;i<keys.length;i++){
		dctlst.push({'key':keys[i],'value':values[i]});
	};
	dctlst.sort((a,b)=>{
		return b.value-a.value;
	});
	var sortedkeys = [];
	var sortedvalues = [];
	for(var i=0;i<keys.length;i++){
		sortedkeys.push(dctlst[i].key);
		sortedvalues.push(dctlst[i].value);
	};
	return {
		'key':sortedkeys,
		'value':sortedvalues
	}
};

var drawboxingyear=()=>{
	var para = document.getElementById('boxyear-year').value;
	if(para == '0'){
		getdata('type=boxing-year&value='+para,
			(s)=>{
				boxyear.setOption(getoptionboxyear(s.key,s.value));
			},
			webalart
		);
	}else{
		getdata('type=boxing-month&value='+para,
			(s)=>{
				boxyear.setOption(getoptionboxyear(s.key,s.value));
			},
			webalart
		);
	};
};

var drawactor=()=>{
	var para = document.getElementById('actoryear').value;
	if(para == '')return;
	getdata('type=actor&value='+para,
		(s)=>{
			actorcloud.setOption(getoptionactorcloud(s.key,s.value));
			actorbar.setOption(getoptionactorbar(s.key,s.value));
		},
		webalart
	);
};

var drawbking=()=>{
	var para1 = document.getElementById('boxking-year').value;
	if(para1 == '')return;
	var para2 = document.getElementById('boxking-rank').value;
	getdata('type=hot&value='+para1,
		(s)=>{
			cbking.setOption(getoptionbking(s.key.slice(0,para2),s.value.slice(0,para2)));
			cbkbar.setOption(getoptionbkbar(s.key.slice(0,para2),s.value.slice(0,para2)));
		},
		webalart
	);
};

var drawgenre=()=>{
	var para1 = document.getElementById('genre-year').value;
	if(para1 == '')return;
	var para2 = document.getElementById('genre-month').value;
	if(para2 == 0){
		getdata('type=genre-year&value='+para1,
			(s)=>{
				ss = genresort(s.key,s.value);
				chartgenre.setOption(getoptiongenre(ss.key,ss.value));
				cgenrebar.setOption(getoptiongenrebar(ss.key,ss.value));
			},
			webalart
		);
	}else if(para2 > 20){
		getdata('type=genre-quarter&value='+para1+'-'+(para2-20),
			(s)=>{
				ss = genresort(s.key,s.value);
				chartgenre.setOption(getoptiongenre(ss.key,ss.value));
				cgenrebar.setOption(getoptiongenrebar(ss.key,ss.value));
			},
			webalart
		);
	}else if(1 <= para2 && para2 <= 12){
		getdata('type=genre-month&value='+para1+'-'+para2,
			(s)=>{
				ss = genresort(s.key,s.value);
				chartgenre.setOption(getoptiongenre(ss.key,ss.value));
				cgenrebar.setOption(getoptiongenrebar(ss.key,ss.value));
			},
			webalart
		);
	}else return;
};

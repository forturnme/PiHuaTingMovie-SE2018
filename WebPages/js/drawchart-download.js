var drawboxingyear2=()=>{
	var para = document.getElementById('filmyear2').value;
	if(para == '0'){
		getdata('type=boxing-year&value='+para,
			(s)=>{boxyear2.setOption(getoptionboxyear(s.key,s.value));
				var picInfo = boxyear2.getDataURL();
				document.getElementById('imgDiv1').innerHTML='<img src="'+picInfo+'" style="width:100%;"/>';
			},
			webalart
		);
	}else{
		getdata('type=boxing-month&value='+para,
			(s)=>{boxyear2.setOption(getoptionboxyear(s.key,s.value));
				var picInfo = boxyear2.getDataURL();
				document.getElementById('imgDiv1').innerHTML='<img src="'+picInfo+'" style="width:100%;"/>';
			},
			webalart
		);
	};
};

var drawactor2=()=>{
	var para = document.getElementById('actoryear2').value;
	if(para == '')return;
	getdata('type=actor&value='+para,
		(s)=>{
			//actorcloud2.setOption({animation: false});
			actorbar2.setOption({animation: false});
			//actorcloud2.setOption(getoptionactorcloud(s.key,s.value));
			actorbar2.setOption(getoptionactorbar(s.key,s.value));
			actorbar2.setOption(getoptionactorbar(s.key,s.value));
			var picInfo2 = actorbar2.getDataURL();
			//var picInfo = actorcloud2.getDataURL();
			document.getElementById('imgDiv4').innerHTML='<img src="'+picInfo2+'" style="width:100%;"/>';
		},
		webalart
	);
};

var drawbking2=()=>{
	var para1 = document.getElementById('boxking-year2').value;
	if(para1 == '')return;
	var para2 = document.getElementById('boxking-rank2').value;
	getdata('type=hot&value='+para1,
		(s)=>{
			//cbking2.setOption({animation: false});
			cbkbar2.setOption({animation: false});
			//cbking2.setOption(getoptionbking(s.key.slice(0,para2),s.value.slice(0,para2)));
			cbkbar2.setOption(getoptionbkbar(s.key.slice(0,para2),s.value.slice(0,para2)));
			var picInfo2 = cbkbar2.getDataURL();
			//var picInfo = cbking2.getDataURL();
			document.getElementById('imgDiv3').innerHTML='<img src="'+picInfo2+'" style="width:100%;"/>';
		},
		webalart
	);
};

var drawgenre2=()=>{
	var para1 = document.getElementById('genre-year2').value;
	if(para1 == '')return;
	var para2 = document.getElementById('genre-month2').value;
	if(para2 == 0){
		getdata('type=genre-year&value='+para1,
			(s)=>{
				chartgenre2.setOption({animation: false});
				cgenrebar2.setOption({animation: false});
				ss = genresort(s.key,s.value);
				// webalart(ss);
				chartgenre2.setOption(getoptiongenre(ss.key,ss.value));
				cgenrebar2.setOption(getoptiongenrebar(ss.key,ss.value));
				var picInfo = chartgenre2.getDataURL();
				var picInfo2 = cgenrebar2.getDataURL();
				document.getElementById('imgDiv2').innerHTML='<img src="'+picInfo+'" style="width:100%;"/> <img src="'+picInfo2+'" style="width:100%;"/>';
			},
			webalart
		);
	}else if(para2 > 20){
		getdata('type=genre-quarter&value='+para1+'-'+(para2-20),
			(s)=>{
				
				chartgenre2.setOption({animation: false});
				cgenrebar2.setOption({animation: false});
				ss = genresort(s.key,s.value);
				// webalart(ss);
				chartgenre2.setOption(getoptiongenre(ss.key,ss.value));
				cgenrebar2.setOption(getoptiongenrebar(ss.key,ss.value));
				var picInfo = chartgenre2.getDataURL();
				var picInfo2 = cgenrebar2.getDataURL();
				document.getElementById('imgDiv2').innerHTML='<img src="'+picInfo+'" style="width:100%;"/> <img src="'+picInfo2+'" style="width:100%;"/>';
			},
			webalart
		);
	}else if(1 <= para2 && para2 <= 12){
		getdata('type=genre-month&value='+para1+'-'+para2,
			(s)=>{
				chartgenre2.setOption({animation: false});
				cgenrebar2.setOption({animation: false});
				ss = genresort(s.key,s.value);
				// webalart(ss);
				chartgenre2.setOption(getoptiongenre(ss.key,ss.value));
				cgenrebar2.setOption(getoptiongenrebar(ss.key,ss.value));
				var picInfo = chartgenre2.getDataURL();
				var picInfo2 = cgenrebar2.getDataURL();
				document.getElementById('imgDiv2').innerHTML='<img src="'+picInfo+'" style="width:100%;"/> <img src="'+picInfo2+'" style="width:100%;"/>';
			},
			webalart
		);
	}else return;
};

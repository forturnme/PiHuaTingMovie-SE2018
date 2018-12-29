// 终于有代码风格了
var dologin=()=>{
	//此处接受服务器提供的盐
	var name=$('#username').val();
	if(name==''){$('#modal-empty').modal('open');return;}
	$('#modal-salt').modal('open');
	var qsalt='username='+name;
	salt=0;
	$.ajax({
		type: 'POST',
		url: 'http://'+SERVER_ADDRESS+':3000/vcode',
		data: qsalt,
		success: (s)=>{
			$('#modal-salt').modal('close');
			salt=s.split('=')[1];
			dohashlogin(salt,qsalt);
		},
		error: (x,i,t)=>{
			$('#modal-salt').modal('close');
			if(x.status==404){$('#modal-logerr').modal('open');return;}
			else{webalart();};
		}
	});
};
var dohashlogin=(salt,qsalt)=>{
	//进行二次散列加密
	var password=$('#password').val();
	if(password==''){$('#modal-empty').modal('open');return;}
	$('#modal-postusr').modal('open');
	var hash1=md5(password);
	var hash2=md5(hash1.toString()+salt.toString());
	var qlogin=qsalt+'&password='+hash2;
	$.ajax({
		type: 'POST',
		url: 'http://'+SERVER_ADDRESS+':3000/jump',
		data: qlogin,
		success: (s)=>{
			$('#modal-postusr').modal('close');
			window.location.href=s;
			return;
		},
		error: (x,i,t)=>{
			$('#modal-postusr').modal('close');
			if(x.status==404){$('#modal-logerr').modal('open');return;}
			else{webalart();};
		}
	});
};
var doregister=()=>{
	var name=$('#username').val();
	if(name==''){$('#modal-empty').modal('open');return;}
	var qsalt='username='+name;
	var password=$('#password').val();
	if(password==''){$('#modal-empty').modal('open');return;}
	var hash1=md5(password);
	var qreg=qsalt+'&password='+hash1;
	$.ajax({
		type: 'POST',
		url: 'http://'+SERVER_ADDRESS+':3000/register',
		data: qreg,
		success: (s)=>{$('#modal-postusr').modal('close');$('#modal-regok').modal('open');},
		error: (x,i,t)=>{
			$('#modal-postusr').modal('close');
			if(x.status==404){$('#modal-regerr').modal('open');return;}
			else{webalart();};
		}
	});
};

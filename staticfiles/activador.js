var event = new Event('change');

function limpiador(depen){
	if(depen.type==="select-one"){
		//console.log(depen.type);
		depen.value='';
		M.FormSelect.init(depen)
		return;
	}
	if(depen.type==="checkbox"){
		depen.checked=false;
		return
	}
	depen.value='';
}
function defaul_value(depenr){
	//M.FormSelect.init()
	console.log("depenr");
	depen = (depenr.querySelectorAll("select").length)===0?depenr.querySelectorAll("input, textarea")[0]:depenr.querySelectorAll("select")[0];
	limpiador(depen);
}

function requiere(depenr){
	//console.log(depenr);
	depen = (depenr.querySelectorAll("select").length)===0?depenr.querySelectorAll("input, textarea")[0]:depenr.querySelectorAll("select")[0];
	//console.log("esto");
	//console.log(depen);
	depen.requiere = true;
	depen.setAttribute("required", "");
	if(depen.type==="select-one"){
		//console.log(depen.type);
		M.FormSelect.init(depen)
	}
}
function requiere_re(depenr){
	//console.log(depenr);
	depen = (depenr.querySelectorAll("select").length)===0?depenr.querySelectorAll("input, textarea")[0]:depenr.querySelectorAll("select")[0];
	//console.log("esto");
	//console.log(depen);
	depen.requiere = true;
	depen.removeAttribute("required");
}
function activar_desactivar(identador,array_desactivar,valores_decomparacion,dependecias_inter=[]){
	identador_res = document.getElementById(identador);
	dato_seleccionado = (typeof(valores_decomparacion)==='boolean') ? identador_res.checked : identador_res.value;
	array_ex = false;
	if(Array.isArray(valores_decomparacion)){
		array_ex = valores_decomparacion.includes(dato_seleccionado);
	}
	if(dato_seleccionado===valores_decomparacion || array_ex){
		for (var i = 0; i < array_desactivar.length; i++){
			document.getElementById(array_desactivar[i]).style.display ='block';
			requiere(document.getElementById(array_desactivar[i]));
		}
	}else{
		for (var i = 0; i < array_desactivar.length; i++){
			defaul_value(document.getElementById(array_desactivar[i]));
			document.getElementById(array_desactivar[i]).style.display = 'None';
			requiere_re(document.getElementById(array_desactivar[i]));
		}
		for (var i = 0; i < dependecias_inter.length; i++){
			defaul_value(document.getElementById(dependecias_inter[i]));
			document.getElementById(dependecias_inter[i]).style.display = 'None';
			requiere_re(document.getElementById(array_desactivar[i]));
		}
	}
}

function activar_desactivar_avansado(identador,array_desactivar,valores_decomparacion,dependecias_inter=[]){
	identador_res = document.getElementById(identador);
	window.addEventListener('load',function(){
		activar_desactivar(identador,array_desactivar,valores_decomparacion,dependecias_inter);
	});
	identador_res.addEventListener('change', function(){
		activar_desactivar(identador,array_desactivar,valores_decomparacion,dependecias_inter);
		console.log("activado");
	});
}
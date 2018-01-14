var express = require('express');
var path = require('path');
var exec= require('child_process').exec;

var app= express();
app.use(express.static(path.join(__dirname,'public')));

app.get('/scanner/:nombre/:num',function(req,res){
	//req.params.num	
	//Proceso de tomar fotos 	
	exec("python TomaFoto.py "+req.params.nombre+" "+req.params.num,function(err,stdout){
 		if(err){console.log(err); }
		console.log(stdout); 			
		});	
});


app.get('*',function(req,res){
	res.send('Operacion invalida');
});



app.listen(8080,function(){
	console.log("Server run on 8080  port");
});
/*
-- Revisar como se comparte la carpeta Publica 100%
-- realizar la toma de Fotos  100%
-------Revisar las multiples fotos Nodejs por su estructura asincronica es complicado, ver si se puede en python
	  ( ejecutar c comando ya programado en python ver carpeta publica) 100%
	respuesta con json desde python. estudiar la estructura json
--Automatizar el proceso 20%
--Pensar el JSON de respuesta donde contendra la ruta de las imagenes
--Ver Task en Python para la lectura de sensores 
	Manejo de sensor de Distancia 10
"en json se entregara errores", el entregara el nombre del sujeto y la cantidad de Fotos a realizar
*/
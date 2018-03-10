var express = require('express');
var path = require('path');
var exec= require('child_process').exec;

var app= express();
app.use(express.static(path.join(__dirname,'public')));

app.get('/scanner/:nombre',function(req,res){
	//req.params.num	
	//Proceso de tomar fotos 
	res.setHeader('Content-Type', 'application/json');	
	exec("python TomaFoto.py "+req.params.nombre+" "+1,function(err,stdout){
		response={}
		
 		if(err){console.log(err); }
		//console.log(stdout);
		for ( i=0; i<1; i++){
	  		response[req.params.nombre]= {"foto1": "/"+req.params.nombre+(i+1)+"-0.jpeg",						
					   "foto2":  "/"+req.params.nombre+(i+1)+"-1.jpeg"}					
		}				
    		res.send(response);		
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
--Pensar el JSON de respuesta donde contendra la ruta de las imagenes 100%
--Ver Task en Python para la lectura de sensores 
	Manejo de sensor de Distancia 10

*/
const settings = {
	async: true,
	crossDomain: true,
	url: 'https://tnql-coords-trial-v2.p.rapidapi.com/v2/api/coords_trial?airport=NRT',
	method: 'GET',
	headers: {
		'X-RapidAPI-Key': 'abd8247158mshdb102c0738044bfp12cebfjsnb1559a432551',
		'X-RapidAPI-Host': 'tnql-coords-trial-v2.p.rapidapi.com'
	}
};

$.ajax(settings).done(function (response) {
	console.log(response);
    // パラメーターの絞り方
	let idinfo = response["results"]["a"][0]["id"];
	let desc1 = response["results"]["a"][0]["description1"];
	let desc2 = response["results"]["a"][0]["description2"];
	let desc3 = response["results"]["a"][0]["description3"];

	const target = document.querySelector("#icon");
	let url = response["results"]["a"][0]["image"];
	
	console.log(url);
	$("#idinfo").append(idinfo);
	$("#desc1").append(desc1);
	$("#desc2").append(desc2);
	$("#desc3").append(desc3);
	
	target.src = url;

});

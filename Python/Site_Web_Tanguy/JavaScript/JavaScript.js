function popup(){
	alert("Tu as réussi à cliquer sur mon nom ! Prêt à voir un site extraordinaire ? Double cliques sur le sous-titre : 'Un vrai crack celui là'")
}

document.getElementById("soustitre").addEventListener("mouseover", function() {
    document.getElementById("soustitre").style.backgroundColor = "purple";
	document.getElementById("soustitre").style.border = "3px dashed #83f52c";
	document.getElementById("boitespeciale").style.backgroundColor = "#83f52c";
	document.getElementById("boitespeciale").style.border = "3px dashed purple";
	
});
    
document.getElementById("soustitre").addEventListener("mouseout", function() {
    document.getElementById("soustitre").style.backgroundColor = "#83f52c";
	document.getElementById("soustitre").style.border = "3px dashed purple";
	document.getElementById("boitespeciale").style.backgroundColor = "purple";
	document.getElementById("boitespeciale").style.border = "3px dashed #83f52c";
});

document.getElementById("boitespeciale").addEventListener("mouseover", function() {
    document.getElementById("boitespeciale").style.backgroundColor = "#83f52c";
	document.getElementById("boitespeciale").style.border = "3px dashed purple";
	document.getElementById("soustitre").style.backgroundColor = "purple";
	document.getElementById("soustitre").style.border = "3px dashed #83f52c";
});

document.getElementById("boitespeciale").addEventListener("mouseout", function() {
    document.getElementById("boitespeciale").style.backgroundColor = "purple";
	document.getElementById("boitespeciale").style.border = "3px dashed #83f52c";
	document.getElementById("soustitre").style.backgroundColor = "#83f52c";
	document.getElementById("soustitre").style.border = "3px dashed purple";
});

function boitetrans(){
	document.querySelector("#transparent").innerHTML= "T'as vu une nouvelle boite est apparu !<p>Et oui je suis un vrai crack, Je sais faire des dingueries comme ça !</p>";
	document.querySelector("#transparent").classList.add("nouvelle");
}
	
function apparence(){
	document.querySelector("#boite1").classList.add("change");
}
	//la fonction apparence ne fonctionne pas. Je ne sais pas pourquoi. Il était censé changer l'apparence de la boite 1 à l'aide de la classe change
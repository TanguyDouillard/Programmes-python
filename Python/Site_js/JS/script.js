

function foncRouge() {
	document.querySelector("#monPara").classList.remove("vert");
	document.querySelector("#monPara").classList.add("rouge");
}

function foncVert() {
	document.querySelector("#monPara").classList.remove("rouge");
	document.querySelector("#monPara").classList.add("vert");
}

function modifMessage() {
	document.querySelector("#monPara").innerHTML="Bravo, t'as cliqué sur le bon boutton"
}

function bigImg(x) {
  x.style.height = "600px";
  x.style.width = "600px";
}

function normalImg(x) {
  x.style.height = "150px";
  x.style.width = "150px";
}

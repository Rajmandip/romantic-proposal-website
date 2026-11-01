for(let i=0;i<150;i++){

let star=document.createElement("div");

star.innerHTML="✦";

star.style.position="absolute";

star.style.left=Math.random()*100+"vw";

star.style.top=Math.random()*100+"vh";

star.style.color="white";

star.style.opacity=Math.random();

document.body.appendChild(star);

}
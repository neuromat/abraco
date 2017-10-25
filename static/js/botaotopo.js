// funcao de ir para o topo
function topo(){
    $("html, body").animate({ scrollTop: 0 }, 500);
}

// mostra o botao somente quando tiver scroll
$(window).scroll(function(e){
	if ($(this).scrollTop() > 100){
	     $("a.top").show();
	} else {
	    $("a.top").hide();
	}
});

$(document).ready(function() {
    $(".menu-hamburger").click(function() {
    	$(this).toggleClass("aberto");
        $(".aMenuAbraco").toggle();
    });
});
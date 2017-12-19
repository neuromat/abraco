$(".panel-title").click(function(){
        a = $(this).find('a').attr('href');
        $(".collapse.in").collapse('hide');
        $(a).collapse('show');
    });

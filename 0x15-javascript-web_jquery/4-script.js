$('#toggle_header').on('click', function(){
    if($('header').hasClass('red')){
        $('header').addClass('green').removeClass('red');
    }
    else {
        $('header').removeClass('green').addClass('red');
    }
});
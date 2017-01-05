$(document).ready(function(){

    $("#filtersidebar").stick_in_parent({offset_top: 70});

    $(".filter-button").click(function(){
        var value = $(this).attr('data-filter');

        if(value == "all")
        {
            //$('.filter').removeClass('hidden');
            $('.filter').show('1000');
        }
        else
        {
//            $('.filter[filter-item="'+value+'"]').removeClass('hidden');
//            $(".filter").not('.filter[filter-item="'+value+'"]').addClass('hidden');
            $(".filter").not('.'+value).hide('3000');
            $('.filter').filter('.'+value).show('3000');

        }
    });

    var selector = ".nav a";

    $(selector).on('click', function(){

      $(selector).removeClass('active');
      $(this).addClass('active');

    });

});

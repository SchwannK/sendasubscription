$(document).ready(function(){

    $("#filtersidebar").stick_in_parent({offset_top: 300});
    $("#gift-browser-sticker").stick_in_parent({offset_top: 54});

    $(".filter-button").click(function(){

        var slider = document.getElementById('slider');
        var slider_values = slider.noUiSlider.get();

        var value = $(this).attr('data-filter');

        if(value == "all")
        {

          $(".filter").filter(function() {
            return parseFloat($(this).attr("price")) >= slider_values[0] && parseFloat($(this).attr("price")) <= slider_values[1];
          }).show('1000');

          $(".filter").filter(function() {
            return parseFloat($(this).attr("price")) < slider_values[0] || parseFloat($(this).attr("price")) > slider_values[1];
          }).hide('1000');

        }
        else
        {
            $(".filter").not('.'+value).hide();
            $('.filter').filter('.'+value).show();

            $(".filter").filter(function() {
              return parseFloat($(this).attr("price")) < slider_values[0] || parseFloat($(this).attr("price")) > slider_values[1];
            }).hide('1000');
        }
    });

    var selector = ".nav a";

    $(selector).on('click', function(){

      $(selector).removeClass('active');
      $(this).addClass('active');

    });

    $(".mCustomScrollbar").mCustomScrollbar({axis:"x"});

});

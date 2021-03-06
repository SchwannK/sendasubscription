var slider = document.getElementById('slider');

noUiSlider.create(slider, {
	start: [0, 400],
	step: 20,
	connect: true,
	tooltips: [wNumb({ decimals: 0 }),  wNumb({ decimals: 0 }) ],
	range: {
		'min': 0,
		'max': 400
	}
});

slider.noUiSlider.on('change', function( values, handle ) {

	var active_cat = $(".filter-button").filter('.active').attr('data-filter');

	if(active_cat=="all") {

		$(".filter").filter(function() {
			return parseFloat($(this).attr("price")) >= values[0] && parseFloat($(this).attr("price")) <= values[1];
		}).show('1000');

		$(".filter").filter(function() {
			return parseFloat($(this).attr("price")) < values[0] || parseFloat($(this).attr("price")) > values[1];
		}).hide('1000');

	} else {

		$(".filter").filter(function() {
			return parseFloat($(this).attr("price")) >= values[0] && parseFloat($(this).attr("price")) <= values[1] && $(this).attr('data-filter') == active_cat;
		}).show('1000');

		$(".filter").filter(function() {
			return parseFloat($(this).attr("price")) < values[0] || parseFloat($(this).attr("price")) > values[1] || $(this).attr('data-filter') != active_cat;
		}).hide('1000');
	}
	
});

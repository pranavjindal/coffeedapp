$( document ).ready(function() {
	var map = new GMaps({
	el: '#map',
	lat: 20.043333,
	lng: -77.028333,
	});
	var locations = $(".location-data");

	locations.each( function( key, value ) {
		var loc_id = $(this).data('id');
		var loc_url = $(this).data('url')
		map.addMarker({
			lat: $(this).data('latitude'),
			lng: $(this).data('longitude'),
			title: $(this).html(),
			click: function(e) {
				window.open(loc_url, "_self");
			}
		}); 
	});
	map.setZoom(2)
	// map.fitZoom();
});
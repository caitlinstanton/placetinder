var initMap = function initMap() {
    var mapDiv = document.getElementById('map');
    var map = new google.maps.Map(mapDiv, {
	center: {lat: 40.71, lng: -74.01},
	zoom: 7
    });

    var marker = new google.maps.Marker({
	position: {lat: 40.71, lng: -74.01},
	map: map
    });

    var circle = new google.maps.Circle({
	strokeColor: '#FF0000',
	strokeOpacity: 0.8,
	strokeWeight: 2,
	fillColor: '#FF0000',
	fillOpacity: 0.35,
	map: map,
	center: marker.getPosition(),
	radius: 32186.9
    });

    map.addListener("click", function(e) {
	marker.setPosition(e.latLng);
	circle.setCenter(e.latLng);
    });
};

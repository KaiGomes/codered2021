var directionsService = new google.maps.DirectionsService();
var map;

function initialize() {

  var center = new google.maps.LatLng(0, 0);
  var myOptions = {
    zoom: 7,
    mapTypeId: google.maps.MapTypeId.ROADMAP,
    center: center
  }

  map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);


  var start = prompt ("Enter start point: ", "16026 Green Manor Drive, Houston, TX");
  var end = prompt("Enter destination", "4800 Calhoun Road, Houston, TX");

  fetch(`/routes/${start}/${end}`)
  .then(response => response.json())
  .then(json => {
    // var parser = new DOMParser();;
    // var doc = parser.parseFromString(html, "text/html");
    var val = JSON.stringify(json);
    // doc.querySelector('scores').innerHTML = json;
    document.getElementById('scores').innerHTML = val;
    console.log('GET response:');
    console.log(val);
});

  plotDirections(start, end);
}

function plotDirections(start, end) {

  var method = 'DRIVING';

  var request = {
    origin: start,
    destination: end,
    travelMode: google.maps.DirectionsTravelMode[method],
    provideRouteAlternatives: true
  };

  directionsService.route(request, function(response, status) {

    if (status == google.maps.DirectionsStatus.OK) {

      var routes = response.routes;
      var colors = ['red', 'green', 'blue', 'orange', 'yellow', 'black'];
      var directionsDisplays = [];

      // Reset the start and end variables to the actual coordinates
      start = response.routes[0].legs[0].start_location;
      end = response.routes[0].legs[0].end_location;

			// Loop through each route
      for (var i = 0; i < routes.length; i++) {
        var directionsDisplay = new google.maps.DirectionsRenderer({
          map: map,
          directions: response,
          routeIndex: i,
          draggable: true,
          polylineOptions: {

            strokeColor: colors[i],
            strokeWeight: 4,
            strokeOpacity: .3
          }}, false)

      const routeVar = document.getElementsByClassName("route");
      for (let j = 0; j < routes.length; j++) {
        routeVar[j].setAttribute('id', j);
        document.getElementById(j).innerHTML = 'Route<span class="numSpan"></span>';
      }

      for (let j = 0; j < routes.length; j++) {
        const spanVar = document.getElementsByClassName("numSpan");
        routeVar[j].setAttribute('id', 'none');
        spanVar[j].setAttribute('id',j);
        document.getElementById(j).innerHTML =" " + (j + 1) + "Append JSON here?";
      }

        // Push the current renderer to an array
        directionsDisplays.push(directionsDisplay);

        // Listen for the directions_changed event for each route
        google.maps.event.addListener(directionsDisplay, 'directions_changed', (function(directionsDisplay, i) {

          return function() {

            var directions = directionsDisplay.getDirections();
            var new_start = directions.routes[0].legs[0].start_location;
            var new_end = directions.routes[0].legs[0].end_location;

            if ((new_start.toString() !== start.toString()) || (new_end.toString() !== end.toString())) {

              // Remove every route from map
              for (var j = 0; j < directionsDisplays.length; j++) {

                directionsDisplays[j].setMap(null);
              }

              // Redraw routes with new start/end coordinates
              plotDirections(new_start, new_end);
            }
          }
        })(directionsDisplay, i)); // End listener
      } // End route loop
    }
  });
}

initialize();

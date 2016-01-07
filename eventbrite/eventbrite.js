var submitForm = function submitForm(e) {
    type = $("#type").val();
    location = $("#where").val();

    var token = 'JYHSYPNUFM546GH2YJSO';
    var $events = $("#events");
    
    $.get('https://www.eventbriteapi.com/v3/'+location+'/'+type+'/search/?token='+token+'&expand=venue', function(res) {
	if (res.events.length) {
	    var s = "<ul class='eventList'>";
	    for(var i=0;i<res.events.length;i++) {
		var event = res.events[i];
		console.dir(event);
		
		s += "<li><a href='" + event.url + "'>" + event.name.text + "</a> - " + "<br>" + event.start.local + "<br>" + "</li>";
	    }
	    s += "</ul>";
	    $events.html(s);
	    
	    

	} else {
	    $events.html("<p>Sorry, there are no upcoming events.</p>");
	}
    });
}

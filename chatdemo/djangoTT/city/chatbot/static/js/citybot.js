var text= $('#chatcontent');


$('#message').keypress(function() {
	if (event.which == 13) {
		
		var userinput = $('#message').val();
		var res = $('<div>');
		res.text('You: ' + userinput);
		res.appendTo(text);
		$('#message').val('');

		//Get the response from views and db
		$.ajax( {

		url: '/chatbot/citybot/',
		data: {
			'input': userinput, 
		},
		method: 'POST',
		success: function(data) {
			//What to do when getting the data back from views
			var newres = $('<div>');
			newres.text('Bot: ' + data['reply']);
			newres.appendTo(text);
		}
		})
	
	}
})

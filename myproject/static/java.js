function addToQueue(elem) {
	alert (elem.id);
	$.post('ajaxqueue/' + $('#userNumber').text() + '/' +'userCenter/'+ elem.id)
}

function upvote(elem) {
	alert(elem.id);
	$.post('upvote/' + $('#userNumber').text() + '/' + 'userCenter/' + elem.id)

}

function downvote(elem) {
	alert(elem.id);
	$.post('downvote/' + $('#userNumber').text() + '/' + 'userCenter/' + elem.id)
}

function loadQueue() {
	$.ajax({
        url: "/returnqueue/{user}/{queue}",
        cache: false,
        dataType: "json",
        success: function(data) {
			$('#queue').empty('');
			for (i = 0; i < data.queue.length; i++) {
				console.log(data.queue[0].title);
				$('#queue').append('<li class=\"queueitem\">\r\n\t\t\t\t\t\t<div class = "counters"><img class="upvote" src="static/upvote.png" onClick="upvote(this)" id = "' + i + '"></img><img class="downvote" src="static/downvote.png" onClick="downvote(this)" id = "' + i + '"></img><span class="upCount">' + data.queue[i].upvote + '</span></div><span class="userAdd"></span><img src=\"http:\/\/images.grooveshark.com\/static\/albums\/70_album.png\" height=\"70px\" width=\"70px\">\r\n\t\t\t\t\t\t<span class =\"songName\">' + data.queue[i].title + '<\/span>\r\n\t\t\t\t\t\t<span class =\"songArtist\">' + data.queue[i].artist + '<\/span>\r\n\t\t\t\t\t<\/li>');
			}
		}
	});
}

setInterval("loadQueue()", 1000 );
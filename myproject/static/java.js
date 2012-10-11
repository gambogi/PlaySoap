function addToQueue(elem) {
	alert (elem.id);
	$.post('ajaxqueue/' + $('#username').text() + '/' +'abc/'+ elem.id)
}

function loadQueue() {
	$.ajax({
        url: "/returnqueue/{user}/{queue}",
        cache: false,
        dataType: "json",
        success: function(data) {
			$('div.songQueueItems').empty('');
			for (i = 0; i < data.queue.length; i++) {
				console.log(data.queue[0].title);
				$('div.songQueueItems').append('<li class=\"queueitem\">\r\n\t\t\t\t\t\t<img src=\"http:\/\/images.grooveshark.com\/static\/albums\/70_album.png\" height=\"70px\" width=\"70px\">\r\n\t\t\t\t\t\t<div class =\"songName\">' + data.queue[i].title + '<\/div>\r\n\t\t\t\t\t\t<div class =\"songArtist\">' + data.queue[i].artist + '<\/div>\r\n\t\t\t\t\t<\/li>');
			}
		}
	});
}

setInterval("loadQueue()", 4000 );
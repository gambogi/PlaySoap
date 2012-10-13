function addToQueue(elem) {
	alert (elem.id);
	$.post('ajaxqueue/' + $('#userNumber').text() + '/' +'abc/'+ elem.id)
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
				$('#queue').append('<li class=\"queueitem\">\r\n\t\t\t\t\t\t<span class="upvote"></span><span class="downvote"></span><span class="userAdd"></span><img src=\"http:\/\/images.grooveshark.com\/static\/albums\/70_album.png\" height=\"70px\" width=\"70px\">\r\n\t\t\t\t\t\t<span class =\"songName\">' + data.queue[i].title + '<\/span>\r\n\t\t\t\t\t\t<span class =\"songArtist\">' + data.queue[i].artist + '<\/span>\r\n\t\t\t\t\t<\/li>');
			}
		}
	});
}

setInterval("loadQueue()", 1000 );
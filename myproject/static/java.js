queue = "userCenter"
function addToQueue(elem) {
	$.post('ajaxqueue/' + $('#userNumber').text() + '/' + queue + '/'+ elem.id)
}

function upvote(elem) {
	$.post('upvote/' + $('#userNumber').text() + '/' + queue + '/' + elem.id)

}

function downvote(elem) {
	$.post('downvote/' + $('#userNumber').text() + '/' + queue + '/' + elem.id)
}

function changeQueue(queueName) {
	queue = queueName
}

function loadQueue() {
	$.ajax({
        url: "/returnqueue/0/" + queue,
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
queue = "userCenter"
service = "play"
function addToQueue(elem) {
	$.post('ajaxqueue/' + service + '/' + $('#userNumber').text() + '/' + queue + '/'+ elem.id)
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

function login() {
  // $('#loginform').ajaxForm({
  //       url : '/login',
  //       dataType : 'json',
  //       success : function (response) {
  //           alert("The server says: " + response);
  //       }
  //   });
	var username = $("input#username").val();
	var password = $("input#password").val();   
	var dataString = 'username=' + username + '&password=' + password; 
		  $.ajax({
    		type: "POST",
    		url: "/login",
    		data: dataString,
    		success: function(data) {
    			$('#loginDIV').empty('');
    			console.log(data)
    			$('#userNumber').text(data.userNumber)
      			changeService("play");
    		}
  		});
}

function changeService(serviceName) {
	service = serviceName
	$.ajax({
        url: "/returnLibrary/" + service + "/" + $('#userNumber').text() + "/" + queue + "/" + "0",
        dataType: "json",
        success: function(data) {
			$('#song-headers').empty('');
			$('#song-headers').append('<tr><th>NAME</th><th>ARTIST</th><th>ALBUM</th></tr>')
			for (i = 0; i < data.library.length; i++) {
				console.log(data.library[0].title);
				$('#song-headers').append('<tr id="' + i + '" ' + 'onClick="addToQueue(this)" class="Songs"><td>' + data.library[i].title + '</td><td>' + data.library[i].artist + '</td><td>' + data.library[i].album + "</td></tr>");
			}
		}
	});

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
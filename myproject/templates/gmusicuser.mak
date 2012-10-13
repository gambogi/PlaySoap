<html>
<link rel="stylesheet" type="text/css" href="static/play.css" />
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<script src="static/java.js"></script>
<body>
	<div id="topGoogleBar">
			<ul id="topleftbarlist">
				<li>Play</li>
				<li>Spotify</li>
				<li>GS</li>
			</ul>
			<ul id="toprightbarlist">
				<li id="username">${username}</li>
				<li id="userNumber">${userNumber}</li>
				<li>Logout</li>
			</ul>
	</div>
	<div id="logoAndQueueButtons">
		<img src="static/logo.png"/>
		<ul id="rightQueueButtons">
			<li><a href="#" class="buttons">Lounge</a></li>
			<li><a href="#" class="buttons">UserCenter</a></li>
			<li><a href="#" class="buttons">SOAP</a></li>
			<div class="clear"></div>
			</ul>
		<div class="clear"></div>
	</div>
	<div id="main">
	<div id="leftList">
		<ul id="leftListUL">
			<li>Home</li>
			<li>Songs</li>
			<li>Artists</li>
			<li>Albums</li>
			<li>Genres</li>
			<li>Playlists</li>
		</ul>
	</div>
	<div id="rightSongList">
		<table id="song-headers">
			<tr>
				<th>NAME</th>
				<th>ARTIST</th>
				<th>ALBUM</th>
			</tr>
			%  for idx,item in enumerate(items):
			<tr id=${idx} onClick="addToQueue(this)" class="Songs">		
					<td>${item["title"]}</td>
					<td>${item["artist"]}</td>
					<td>${item["album"]}</td>
			</tr>
			%endfor
		</table>
		</div>
	</div>
		<div id="footer">
			<div id="songqueue">
				<ul id="queue">
				</ul>
			</div>
			<ul id="leftControls"</ul>
				<li><img src="static/play.png"/></li>
				<li><img src="static/next.png"/></li>
			</ul>
</html>

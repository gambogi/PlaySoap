<html>
<link rel="stylesheet" type="text/css" href="static/play.css" />
<body>
	<div id="topGoogleBar">
			<ul id="topleftbarlist">
				<li>Play</li>
				<li>Spotify</li>
				<li>GS</li>
			</ul>
			<ul id="toprightbarlist">
				<li>Username</li>
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
				<td></td>
				<th>NAME</th>
				<th>ARTIST</th>
				<th>ALBUM</th>
			</tr>
			%  for item in items:
			<tr class="Songs">
				<td><img src="static/play.png"/></td>
				<td>${item["title"]}</td>
				<td>${item["artist"]}</td>
				<td>${item["album"]}</td>
			</tr>
			%endfor
		</table>
		</div>
		<div id="footer">
			<div id="songqueue">
				<ul id="queue">
					<li class="queueitem">
						<img src="http://images.grooveshark.com/static/albums/70_album.png" height="70px" width="70px">
						<div class ="songName">AAAAAAAAAAAAAAA</div>
						<div class ="songArtist">Artist</div>
					</li>
					<li class="queueitem">
						<img src="http://images.grooveshark.com/static/albums/70_album.png" height="70px" width="70px">
						<div class ="songName">Test</div>
						<div class ="songArtist">Artist</div>
					</li>
				</ul>
			</div>
			<ul id="leftControls"</ul>
				<li><img src="static/play.png"/></li>
				<li><img src="static/next.png"/></li>
			</ul>
</html>

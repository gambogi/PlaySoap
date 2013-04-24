<html>
<link rel="stylesheet" type="text/css" href="static/play.css" />
<script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
<script src="static/java.js"></script>
<body>
	<div id="topGoogleBar">
			<ul id="topleftbarlist">
				<li onClick="changeService('play')">Play</li>
				<!--<li onClick="changeService('spotify')">Spotify</li>-->
				<li onClick="changeService('hactar')">Hactar</li>
			</ul>
			<ul id="toprightbarlist">
				<li id="username">NOTLOGGEDIN</li>
				<li id="userNumber">NOTLOGGEDIN</li>
				<!--<li>Logout</li>-->
			</ul>
	</div>
	<div id="logoAndQueueButtons">
		<img src="static/logo.png"/>
		<ul id="rightQueueButtons">
			<li><a href="#" class="buttons" onClick="changeQueue('southside')">SouthSide</a></li>
			<li><a href="#" class="buttons" onClick="changeQueue('northside')">NorthSide</a></li>
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
			<div id ="loginDIV">
				<strong>NOTE:</strong> If using a google account with two-factor authentication, you must create an application password for soap. This is the <strong>only</strong> known way you can login. 
			<form  action="" id="loginform">
				<fieldset>
    			<div>
      				Username: <input type="text" name="username" id="username"/>
    			</div>
    			<div>
      				Password: <input type="password" name="password" id="password"/>
    			</div>
   				<input type="button" value="Submit" id="submitForm" onClick="login()" />
   				</fieldset>
  			</form>
  		</div>
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

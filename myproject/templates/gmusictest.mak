<html>
<head>
<script src="//ajax.googleapis.com/ajax/libs/prototype/1.7.1.0/prototype.js"></script>
</head>
<body>
<a href="javascript:void loadTab( 'usercenter' )">Tab 1</a> |
<a href="javascript:void loadTab( 'lounge' )">Tab 2</a> |
<a href="javascript:void loadTab( 'research' )">Tab 3</a>
<div id="content" style="padding:5px;border:2px solid black;">
</div>
<script>
function loadTab( tab ) { 
  new Ajax.Updater( 'content', tab, { method: 'post' } );
}
loadTab( 'usercenter' );
</script>
</body>
</html>

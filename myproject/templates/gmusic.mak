 <html xmlns="http://www.w3.org/1999/xhtml">
<table>
%  for idx,item in enumerate(items):
	% if (idx < 5):
    <tr>
      <th>Name</th>
      <td>${item["name"]}</td>
	 	<th>Artist</th>
		<td>${item["artist"]}</td>
		<th>Song ID</th>
		<td>${item["id"]}</td>
		<th>Song Stream URL</th>
		<td>${item["songURL"]}</td>$
	</tr>
	% endif
%	endfor
</table>
</html>

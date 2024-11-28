<!DOCTYPE html>
<html lang="en" dir="ltr">
<meta http-equiv="Content-Type" content="text/html; charset=utf-8">
<meta name="robots" content="noindex">
<title>Export - localhost:5432 - Adminer</title>
<link rel="stylesheet" type="text/css" href="?file=default.css&amp;version=4.8.1">
<script src='?file=functions.js&amp;version=4.8.1' nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE="></script>
<link rel="shortcut icon" type="image/x-icon" href="?file=favicon.ico&amp;version=4.8.1">
<link rel="apple-touch-icon" href="?file=favicon.ico&amp;version=4.8.1">

<body class="ltr nojs">
<script nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE=">
mixin(document.body, {onkeydown: bodyKeydown, onclick: bodyClick});
document.body.className = document.body.className.replace(/ nojs/, ' js');
var offlineMessage = 'You are offline.';
var thousandsSeparator = ',';
</script>

<div id="help" class="jush-pgsql jsonly hidden"></div>
<script nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE=">mixin(qs('#help'), {onmouseover: function () { helpOpen = 1; }, onmouseout: helpMouseout});</script>

<div id="content">
<p id="breadcrumb"><a href="?pgsql=localhost%3A5432">PostgreSQL</a> &raquo; <a href='?pgsql=localhost%3A5432&amp;username=postgres' accesskey='1' title='Alt+Shift+1'>localhost:5432</a> &raquo; Export
<h2>Export</h2>
<div id='ajaxstatus' class='jsonly hidden'></div>
<div class='error'>Too big POST data. Reduce the data or increase the 'post_max_size' configuration directive.</div>

<form action="" method="post">
<table cellspacing="0" class="layout">
<tr><th>Output<td><label><input type='radio' name='output' value='text' checked>open</label><label><input type='radio' name='output' value='file'>save</label><label><input type='radio' name='output' value='gz'>gzip</label>
<tr><th>Format<td><label><input type='radio' name='format' value='sql' checked>SQL</label><label><input type='radio' name='format' value='csv'>CSV,</label><label><input type='radio' name='format' value='csv;'>CSV;</label><label><input type='radio' name='format' value='tsv'>TSV</label>
<tr><th>Database<td><select name='db_style'><option><option>USE<option>DROP+CREATE<option selected>CREATE</select><label><input type='checkbox' name='routines' value='1' checked>Routines</label><tr><th>Tables<td><select name='table_style'><option><option>DROP+CREATE<option selected>CREATE</select><label><input type='checkbox' name='auto_increment' value='1' checked>Auto Increment</label><label><input type='checkbox' name='triggers' value='1' checked>Triggers</label><tr><th>Data<td><select name='data_style'><option><option>TRUNCATE+INSERT<option selected>INSERT</select></table>
<p><input type="submit" value="Export">
<input type="hidden" name="token" value="55524:724916">

<table cellspacing="0">
<script nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE=">qsl('table').onclick = dumpClick;</script>
<thead><tr><th style='text-align: left;'><label class='block'><input type='checkbox' id='check-databases' checked>Database</label><script nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE=">qs('#check-databases').onclick = partial(formCheck, /^databases\[/);</script></thead>
<tr><td><label class='block'><input type='checkbox' name='databases[]' value='Penjualan' checked>Penjualan</label>
<tr><td><label class='block'><input type='checkbox' name='databases[]' value='porto_be_fast' checked>porto_be_fast</label>
<tr><td><label class='block'><input type='checkbox' name='databases[]' value='postgres' checked>postgres</label>
<tr><td><label class='block'><input type='checkbox' name='databases[]' value='template0' checked>template0</label>
<tr><td><label class='block'><input type='checkbox' name='databases[]' value='template1' checked>template1</label>
</table>
</form>
</div>

<form action='' method='post'>
<div id='lang'>Language: <select name='lang'><option value="en" selected>English<option value="ar">العربية<option value="bg">Български<option value="bn">বাংলা<option value="bs">Bosanski<option value="ca">Català<option value="cs">Čeština<option value="da">Dansk<option value="de">Deutsch<option value="el">Ελληνικά<option value="es">Español<option value="et">Eesti<option value="fa">فارسی<option value="fi">Suomi<option value="fr">Français<option value="gl">Galego<option value="he">עברית<option value="hu">Magyar<option value="id">Bahasa Indonesia<option value="it">Italiano<option value="ja">日本語<option value="ka">ქართული<option value="ko">한국어<option value="lt">Lietuvių<option value="ms">Bahasa Melayu<option value="nl">Nederlands<option value="no">Norsk<option value="pl">Polski<option value="pt">Português<option value="pt-br">Português (Brazil)<option value="ro">Limba Română<option value="ru">Русский<option value="sk">Slovenčina<option value="sl">Slovenski<option value="sr">Српски<option value="sv">Svenska<option value="ta">த‌மிழ்<option value="th">ภาษาไทย<option value="tr">Türkçe<option value="uk">Українська<option value="vi">Tiếng Việt<option value="zh">简体中文<option value="zh-tw">繁體中文</select><script nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE=">qsl('select').onchange = function () { this.form.submit(); };</script> <input type='submit' value='Use' class='hidden'>
<input type='hidden' name='token' value='115986:660034'>
</div>
</form>
<form action="" method="post">
<p class="logout">
<input type="submit" name="logout" value="Logout" id="logout">
<input type="hidden" name="token" value="55524:724916">
</p>
</form>
<div id="menu">
<h1>
<a href='https://www.adminer.org/' target="_blank" rel="noreferrer noopener" id='h1'>Adminer</a> <span class="version">4.8.1</span>
<a href="https://www.adminer.org/#download" target="_blank" rel="noreferrer noopener" id="version"></a>
</h1>
<script src='?file=jush.js&amp;version=4.8.1' nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE="></script>
<script nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE=">
bodyLoad('17');
</script>
<form action="">
<p id="dbs">
<input type="hidden" name="pgsql" value="localhost:5432"><input type="hidden" name="username" value="postgres"><span title='database'>DB</span>: <select name='db'><option value=""><option>Penjualan<option>porto_be_fast<option>postgres<option>template0<option>template1</select><script nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE=">mixin(qsl('select'), {onmousedown: dbMouseDown, onchange: dbChange});</script>
<input type='submit' value='Use' class='hidden'>
<input type='hidden' name='dump' value=''></p></form>
<p class='links'><a href='?pgsql=localhost%3A5432&amp;username=postgres&amp;sql='>SQL command</a>
<a href='?pgsql=localhost%3A5432&amp;username=postgres&amp;import='>Import</a>
<a href='?pgsql=localhost%3A5432&amp;username=postgres&amp;dump=' id='dump' class='active '>Export</a>
</div>
<script nonce="ZTEzMDBiODdlYTQwYjNjZTE3NDQ0NjkwYWZiOWFmNmE=">setupSubmitHighlight(document);</script>

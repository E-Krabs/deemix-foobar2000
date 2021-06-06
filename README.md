# deemix-foobar2000
Converts foobar2000 curropted txt list to deezer album url
<hr>
<h3>Getting Started</h3><br>
<p>foobar out file will look like this:</p><br>
<pre>
ARTIST-NAME1/Album1<br>

ARTIST-NAME2/Album2<br>

ARTIST-NAME3/Album3<br>

ARTIST-NAME4/Album4
</pre>
<p>First, place your out file in your user directory.</p>
<pre>C:/User/Name/foo-out.txt</pre>
<p>Then, run <code>strip.py</code>. You will be prompted to enter the name of your foo-out file.</p><br>
<pre>
>>> File name (foobar.txt):<br>
>>> foo-out.txt<br>
</pre>
<p>Your foo-out file will now look like this:</p><br>
<pre>
ARTIST-NAME1/Album1<br>
ARTIST-NAME2/Album2<br>
ARTIST-NAME3/Album3<br>
ARTIST-NAME4/Album4
</pre>
<hr>
<h3>Main.py</h3>
<p>Next, run <code>main.py</code>. A file will appear called <code>links.txt</code> in your user directory.</p><br>
<h3>The Transfromation Process:</h3><br>
<pre>ARTIST-NAME1/Album1</pre>
<pre>ARTIST+NAME1%2FAlbum1</pre>
<pre>https://html.duckduckgo.com/html/?q=site%3Adeezer.com+ARTIST+NAME1%2FAlbum1</pre>
<pre>https://www.deezer.com/en/album/306125</pre>

# deemix-foobar2000 | Under Construction (still)
Converts foobar2000 corrupted txt list to deezer album url. It's gonna run into some errors (maybe (idk)).

<h3>Requirements</h3>
<ul>
  <li>Python3</li>
  <li>requests</li>
  <li>bs4</li>
  <strike><li>lxml</li></strike>
 </ul>
<h3>Getting Started</h3>
<p>Installing Requirements:</p>
<pre>pip install bs4</pre>
<pre>pip install requests</pre>
<strike><pre>pip install lxml</pre></strike><br>
<p>foobar out file will look like this:</p>

ARTIST-NAME1/Album1<br>

ARTIST-NAME2/Album2<br>

ARTIST-NAME3/Album3<br>

ARTIST-NAME4/Album4

<p>First, place your out file in your user directory.</p>
<pre>C:/User/Name/foobar.txt</pre>
<p>Then, run <code>strip.py</code>. You will be prompted to enter the name of your foobar out file.</p><br>
<pre>
>>> File name (foobar.txt):<br>
>>> foo-out.txt<br>
</pre>
<p>A file called <code>strip.txt</code> will appear. It will look like this (No spaces in between):</p><br>

ARTIST-NAME1/Album1<br>
ARTIST-NAME2/Album2<br>
ARTIST-NAME3/Album3<br>
ARTIST-NAME4/Album4

<hr>
<h3>Main.py</h3>
<p>Next, run <code>main.py</code>. A file will appear called <code>links.txt</code> in your user directory.</p><br>
<h3>The Transfromation Process</h3>
<pre>ARTIST-NAME1/Album1</pre>
<pre>ARTIST+NAME1%2FAlbum1</pre>
<pre>https://api.deezer.com/search/album/?q=ARTIST-NAME1%20Album1&index=0&limit=2&output=xml</pre>
<pre>https://www.deezer.com/en/album/306125</pre>
<hr>
<h3>How it Works</h3>
<p>Strips empty lines from foobar out file. Then, encodes url. Scrapes api.deezer.com/search/album/. Writes <code>href</code> to file.</p>
<h1><b><i>Le Fin</i></b></h1>
<p>P.S. I have no idea how the foobar out file looks. I'm going off <a href="https://www.reddit.com/r/deemix/comments/nsvghm/how_replace_this_text_artistnamealbum_by_the/">this Reddit comment.

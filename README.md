# deemix-foobar2000 | Under Construction
Converts foobar2000 corrupted txt list to deezer album url (or track). It's gonna run into some errors (maybe).<br>
Its still not done sry.

<h3>Requirements</h3>
<ul>
  <li><a href="https://www.python.org/downloads/">Python3</a></li>
  <li><a href="https://pypi.org/project/requests/">requests</a></li>
  <li><a href="https://pypi.org/project/beautifulsoup4/">bs4</a></li>
  <li><a href="https://pypi.org/project/Unidecode/">unidecode</a></li>
  <strike><li>lxml</li></strike>
 </ul>
<h3>Getting Started</h3>
<p>Installing Requirements:</p>
<pre>pip install bs4</pre>
<pre>pip install requests</pre>
<pre>pip install unidecode</pre>
<strike><pre>pip install lxml</pre></strike><br>
<p>Your original foobar out file should look like this:</p>
<img src="https://raw.githubusercontent.com/NEDb-tk/deemix-foobar2000/main/images/foobar.PNG">

<p>First, cd to the deemix-foobar2000-main directory (or your virtualenv). Next, place your <code>foobar.txt</code> in this directory.</p>
<pre>C:/User/Name/Downloads/deemix-foobar2000-main/foobar.txt</pre>
<p>Then, run <code>strip.py</code>. You will be prompted to enter the name of your foobar out file.</p><br>
<pre>
>>>File name (foobar.txt):
foobar.txt <-- type <code>foobar.txt</code> or whatever the text file is named.
</pre>
<p>A file called <code>strip.txt</code> will appear. It will look like this (No spaces in between):</p><br>
<img src="https://raw.githubusercontent.com/NEDb-tk/deemix-foobar2000/main/images/strip.PNG">

<hr>
<h3>Main.py</h3>
<p>Next, run <code>main.py</code> from the directory stated above.<br>
<img src="https://raw.githubusercontent.com/NEDb-tk/deemix-foobar2000/main/images/command.PNG">  

A file will appear called <code>links.txt</code> in this directory.</p><br>
<img src="https://github.com/NEDb-tk/deemix-foobar2000/blob/main/images/links.PNG">

<h3>The Transfromation Process</h3>
<pre>ARTIST-NAME1/Album1</pre>
<pre>ARTIST%20NAME1%20Album1</pre>
<pre>https://api.deezer.com/search/album/?q=ARTIST%20NAME1%20Album1&index=0&limit=2&output=xml</pre>
<pre>https://www.deezer.com/en/album/306125</pre>
<hr>
<h3>How it Works</h3>
<p>Strips empty lines from foobar out file. Then, encodes url. Scrapes api.deezer.com/search/album/. Writes <code>link</code> to file.</p>
<p>To download all the albums/tracks in `links.txt`, use the <a href="https://www.reddit.com/r/deemix/comments/hmrhhs/download_links/">Deemix CLI</a>.
<p>Thanks <a href="https://developers.deezer.com/api">Deezer API</a> and <a href="https://www.reddit.com/r/deemix/">Deemix</a>!
  <center><h2><b><i>Le Fin</i></b></h2></center>

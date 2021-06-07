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
<h1><b><i>Le Fin</i></b></h1>
<p>P.S. I have no idea how the foobar out file looks. I'm going off <a href="https://www.reddit.com/r/deemix/comments/nsvghm/how_replace_this_text_artistnamealbum_by_the/">this Reddit comment.

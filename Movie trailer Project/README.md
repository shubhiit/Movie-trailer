<h2> About the Project</h2>
<ul><li>This project includes a web page which will contain a number of movies and user will be able to watch the trailer of these movies and add/remove movies as per his/her choices.</li></ul>
<h2> Software and Installation</h2>
<ul><li>To use this project one should have a webbrowser and python installed in his/her system.</ul></li>
<h4> How to install python(if not already):</h4>
<ul><li> Open this <a href="https://www.python.org/downloads/">link</a> and download Python then follow the steps as mentioned in the installer to install it. At each step choosing default settings will be a wiser decision.</ul></li>
<h2>Usage</h2>
<ol>
<li>As python is installed in your system, it will have an IDLE. We will use this IDLE to run this project.</li>
<li>So open the downloaded files on IDLE by right click on file and choose `edit with IDLE` and then run them on IDLE by click `Run` present in IDLE window, to check they are error free.If they are error free then go to further steps.</li>
<li>Want to add trailers of your favorite movie do as follows.-<ul>
<li>Create new objects of Movie class in details.py file with providing the required details of movies as follows.</li>
` obj1 = movie.Movie(name, storyline, URL of trailer,URL of poster) `<br/>
Remember to pass the details as <strong>strings</strong>.
<li>Add this object to the earlier made list, taken as argument by function open_movies_page() in details.py. Add as many objects you want.</li>
</ul>
<li>To remove a movie , remove it's object from the list and comment out or delete the object of that movie.</li>
<li>As you have added your favorite moviesto the list, save the changes and run the details.py on IDLE and if there are no errors then a webpage will load in your web browser and that's it.</li>
<li>To watch the trailers click on the poster of movie and sit back and watch trailers of your favorite movies.</li>
</ol>
<h2>How to remove errors:</h2>
<ul><li>If you counter any error while running details.py, IDLE will be pointing out where the error lies, remove the specified error using python knowledge or intellect of yours.</li></ul>
<h2>Basic steps to create this project from scratch:</h2>
<ol>
<li>Create a  python file and in this file create a class "Movie"and define init function of the class and define variables in it.</li>
<li>Define a show trailer method in the class such that it open the url of the trailer enter by the programmer, use required imports and functions to achieve the same.</li>
<li>Create another file and import movie.py file in it and then create the required number of objects of the class.</li>
<li>Create a python file providing frontend code to improve the presentation of web page and methods also then import that file to the file created in step 3 and then run the required functions and the web page is ready to use.</li>
</ol>

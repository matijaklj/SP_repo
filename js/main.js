var user;
postForm = {};

function login(event) {
    var usersFile = "json/users"; // name of the .json file with the user info

    var oReq = new XMLHttpRequest();
    oReq.addEventListener("load", userHandlerJson);
    oReq.open("GET", usersFile+".json");
    oReq.responseType = "text";
    oReq.send();

    event.preventDefault();
}

function userHandlerJson(event) {
    var usersJson = JSON.parse(this.responseText);

    var u = document.getElementById("username").value;
    var p = document.getElementById("password").value;
    console.log(u + " " + p);

    for (var i = 0; i < usersJson.length; i++) {
        if((usersJson[i].username == u || usersJson[i].email == u) && usersJson[i].password == p) {
            window.location = "home.html";
            return;
        }
    }
    console.log("wrong username or password!!!");
}

function getLocation() {

    if (postForm.loc == null && navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        //x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    var x = document.getElementById("new-post-tags");

    x.innerHTML += "<a class=\"buttn\" href=\"http://maps.google.com/?q="+ position.coords.latitude +","+ position.coords.longitude +"\"><div class=\"sprite sprite-location\"></div>lokacija</a>"

    postForm.loc = "http://maps.google.com/?q="+ position.coords.latitude +","+ position.coords.longitude;

    document.getElementById("add-location").setAttribute("disabled");
}

function submitPost(event) {
    var filename = "json/post1"; //name od the .json file with posts

    var text = document.getElementById("post-input").value;
    var loc = "";

    if(postForm.loc != null) loc = postForm.loc;

    if(text == "" && loc == "") {
        alert("Cant post empty post!");
        return;
    }

    createArticlePost("img/users/janez/cover-image.jpg", "img/users/janez/profile-image.jpg", "Janez Novak", text, loc, function(post) {
        document.getElementById("newsfeed").insertBefore(post, document.getElementById("newsfeed").firstChild);
    });

    document.getElementById("post-input").value = "";

    formPost = {};
     document.getElementById("new-post-tags").innerHTML = "";
/*
    var xmlhttp = new XMLHttpRequest();   // new HttpRequest instance
    xmlhttp.addEventListener("load", postHandlerJson);
    xmlhttp.open("POST", "json/action");
    xmlhttp.setRequestHeader("Content-Type", "application/json;charset=UTF-8");
    xmlhttp.onreadystatechange = function () {
        if (xmlhttp.readyState == 4 && xmlhttp.status == 200) {
            alert(xmlhttp.responseText);
        }
    }
    xmlhttp.send(JSON.stringify({"cover-image": "img-json/cover1.jpg",
                                "profile-image": "img-json/profile-image1.jpg",
                                "username": "Mister X",
                                "text": text,
                                "location": loc}));
*/
/* // this is for reading posts
    var filename = "json/post1"; //name od the .json file with posts

    var oReq = new XMLHttpRequest();
	oReq.addEventListener("load", postHandlerJson);
	oReq.open("GET", filename+".json");
	oReq.responseType = "text";
	oReq.send();

	event.preventDefault();
*/
}

function readPosts(event) {
    var filename = "json/posts"; //name od the .json file with posts

    var oReq = new XMLHttpRequest();
	oReq.addEventListener("load", postHandlerJson);
	oReq.open("GET", filename+".json");
	oReq.responseType = "text";
	oReq.send();

	event.preventDefault();
}

function postHandlerJson(event) {
    var postJson = JSON.parse(this.responseText);

    for (var i = 0; i < postJson.length; i++) {
        coverImage = postJson[i]["cover-image"];
    	profileImage = postJson[i]["profile-image"];
        username = postJson[i]["username"];
        text = postJson[i]["text"];
        loc = postJson[i]["location"];

        createArticlePost(coverImage, profileImage, username, text, loc, function(post) {
            document.getElementById("newsfeed").insertBefore(post, document.getElementById("newsfeed").firstChild);
        });
    }
}

function createArticlePost(coverImage, profileImage, username, text, loc, callback) {
    checkText(text, function(text) {

        var art = document.createElement("article");
        art.className += "post";
        var div1 = document.createElement("div");
        div1.className += "cover-image";
        var cover_img = document.createElement("img");
        cover_img.className += "cover-image";
        cover_img.setAttribute("src", coverImage);
        cover_img.setAttribute("alt", "cover photo");
        div1.appendChild(cover_img);
        art.appendChild(div1);

        var div2 = document.createElement("div");
        div2.className += "profile-image-div";
        var profile_img = document.createElement("img");
        profile_img.className += "profile-image";
        profile_img.setAttribute("src", profileImage);
        profile_img.setAttribute("alt", "profile photo");
        div2.appendChild(profile_img);
        art.appendChild(div2);

        var h2 = document.createElement("h2");
        h2.className += "profile-name";
        h2.innerHTML = username;
        art.appendChild(h2);

        var div3 = document.createElement("div");
        div3.className += "post-text";
        var p = document.createElement("p");
        p.innerHTML = text;
        div3.appendChild(p);
        art.appendChild(div3);

        if(loc != "") {
            var tags = document.createElement("div");
            tags.className += "tags";
            var a = document.createElement("a");
            a.setAttribute("href", loc);
            var span = document.createElement("span");
            span.className += "buttn";
            var icon = document.createElement("div");
            icon.className += "sprite sprite-location";
            span.appendChild(icon);
            span.innerHTML += " Location";
            a.appendChild(span);
            tags.appendChild(a);

            art.appendChild(tags);
        }

        if(callback != null) callback(art);
    });
}

function checkText(text, callback) {

    text = text.replace(/(^|\s)(#[a-z\d-]+)/gi, "$1<a href='#'>$2</a>");
    text = text.replace(/(^|\s)(@([a-z\d-]+))/gi, "$1<a href=\"#$3\">$2</a>");

    if(callback != null) callback(text);
}

function collapseMenu(event) {
    //console.log(document.getElementById("collapse-menu").getAttribute("href") );
    if(document.getElementById("collapse-menu").getAttribute("href")  == "#dropdown-menu")
        document.getElementById("collapse-menu").setAttribute("href", "#")
    else
        document.getElementById("collapse-menu").setAttribute("href", "#dropdown-menu");;

    //document.getElementById("show-menu").className = "header-link-colapsed buttn";
    //document.getElementById("collapse-menu").className = "header-link-colapsed buttn no-display";

}
function showMenu(event) {
    document.getElementById("collapse-menu").className = "header-link-colapsed buttn";
    document.getElementById("show-menu").className = "header-link-colapsed buttn no-display";

}

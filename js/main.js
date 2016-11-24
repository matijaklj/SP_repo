var user;

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
    var x = document.getElementById("res");

    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(showPosition);
    } else {
        x.innerHTML = "Geolocation is not supported by this browser.";
    }
}

function showPosition(position) {
    x.innerHTML = "<a href=\"http://maps.google.com/?q="+ position.coords.latitude +","+ position.coords.longitude +"\">@lokacija</a>"
}

function submitPost(event) {
    var filename = "json/post1"; //name od the .json file with posts

    var oReq = new XMLHttpRequest();
	oReq.addEventListener("load", postHandlerJson);
	oReq.open("GET", filename+".json");
	oReq.responseType = "text";
	oReq.send();

	event.preventDefault();
}

function postHandlerJson(event) {
    var postJson = JSON.parse(this.responseText);
	coverImage = postJson["cover-image"];
	profileImage = postJson["profile-image"];
    username = postJson["username"];
    text = postJson["text"];
    loc = postJson["location"];

    if(loc == "") console.log(loc);


    createArticlePost(coverImage, profileImage, username, text, loc, function(post) {
        document.getElementById("newsfeed").insertBefore(post, document.getElementById("newsfeed").firstChild);
    });

}

function createArticlePost(coverImage, profileImage, username, text, loc, callback) {
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
        var icon = document.createElement("img");
        icon.className += "icon";
        icon.setAttribute("src", "icon/location.png");
        span.appendChild(icon);
        span.innerHTML += " Location";
        a.appendChild(span);
        tags.appendChild(a);

        art.appendChild(tags);
    }

    if(callback != null) callback(art);
}

var session = null;

function handle_click_response (data) {
    if (data) {
	$("#viewport").attr ("src", data);
    }
}

function process_click (x, y, other) {
    if (typeof (other) == "undefined") {
	other = "";
    }
    $.get ("process_click.cgi", {'src': $("#viewport").attr("src"),
				 'session': session,
				 'x': x,
				 'y': y,
				 'other': other},
	   handle_click_response);
}

function viewport_click (evt) {
    var x = evt.offsetX;
    var y = evt.offsetY;

    process_click (x, y);
}

function left (evt) {
    process_click (0, 0, "left");
}
function right (evt) {
    process_click (0, 0, "right");
}

function get_cookie(c_name) {
    var i,x,y,ARRcookies = document.cookie.split(";");
    for (i = 0;i < ARRcookies.length; i++) {
	x = ARRcookies[i].substr(0, ARRcookies[i].indexOf("="));
	y = ARRcookies[i].substr(ARRcookies[i].indexOf("=")+1);
	x = x.replace(/^\s+|\s+$/g, "");
	if (x == c_name) {
	    return unescape(y);
	}
    }
}

function set_cookie(c_name,value,exdays) {
    var exdate = new Date();
    exdate.setDate(exdate.getDate() + exdays);
    var c_value = escape(value) + ((exdays==null) ? "" : "; expires="+exdate.toUTCString());
    document.cookie = c_name + "=" + c_value;
}

function init () {
    session = get_cookie ("session");
    if (session == null || session == "") {
	session = (new Date()).getTime () + "";
	set_cookie ("session", session);
    }

    $("#viewport").click (viewport_click);
    $("#left").click (left);
    $("#right").click (right);
}

$(document).ready (init);

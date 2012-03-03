function handle_click_response (data) {
    $("#viewport").attr ("src", data);
}

function process_click (evt) {
    var x = evt.offsetX;
    var y = evt.offsetY;

    $.get ("process_click.cgi", {'src': $("#viewport").src,
				 'x': x,
				 'y': y},
	   handle_click_response);
}

function init () {
    $("#viewport").click (process_click);
}

$(document).ready (init);

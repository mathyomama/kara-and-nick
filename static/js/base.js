function resize_invitation() {
	var $inner = $('.invitation-inner');
	// 70 pixels for the navbar height and bottom-margin and 20 for whole-container bottom-padding
	$('.invitation-outer').css('min-height', String($(window).height() - 70 - 20) + 'px');
	$inner.css('height', 'auto');
	$inner.css('height', String($('.invitation-outer').height() - 30) + 'px');
}

function old_resize_invitation() {
	var $inner = $('.invitation-inner');
	console.log("BEFORE MIN-HEIGHT");
	print_height();
	// 70 pixels for the navbar height and bottom-margin and 20 for whole-container bottom-padding
	$('.invitation-outer').css('min-height', String($(window).height() - 70 - 20) + 'px');
	console.log("BEFORE AUTO HEIGHT");
	print_height();
	$inner.css('height', 'auto');
	console.log("BEFORE RESIZE");
	print_height();
	$inner.css('height', String($('.invitation-outer').height() - 30) + 'px');
	console.log("AFTER");
	print_height();
}

$(document).ready(function() {
	$(window).resize(resize_invitation);
});

window.onload = function() {
	resize_invitation();
}

function print_height() {
	console.log("$(window).height() : " + $(window).height() + "\n",
			"$(document).height() : " + $(document).height() + "\n",
			"$(html).height() : " + $("html").height() + "\n",
			"$(.whole-container).height() : " + $(".whole-container").height() + "\n",
			"$(.invitation-outer).height() : " + $(".invitation-outer").height() + "\n",
			"$(.invitation-inner).height() : " + $(".invitation-inner").height() + "\n");
}

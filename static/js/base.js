function resize_invitation() {
	var $inner = $('.invitation-inner');
	// 70 pixels for the navbar height and bottom-margin and 20 for whole-container bottom-padding
	$('.invitation-outer').css('min-height', String($(window).height() - 70 - 20) + 'px');
	$inner.css('height', 'auto');
	$inner.css('height', String($('.invitation-outer').height() - 30) + 'px');
	var $flourish_br= $('#flourish-corner-br');
	var $flourish_bl= $('#flourish-corner-bl');
    //$flourish_br.css('margin_right','-13px');
    //$flourish_bl.css('margin_left','-13px');
    $flourish_br.css('bottom','-12px');
    $flourish_bl.css('bottom','-12px');
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
	$(".invitation-inner").animate({opacity:"1.0"},"slow");
	$(window).resize(resize_invitation);

	$("nav li li a, .navbar-brand").click(function(evt){
		var link = $(this).attr("href");
		setTimeout(function() { window.location.href = link; }, 10000);
		$(".invitation-inner").animate({opacity:"0.0"},"slow");
	});
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

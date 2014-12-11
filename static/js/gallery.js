$(document).ready(function() {
	$(".gallery-image").click(function(e) {

		// This function is for formatting the html for the img tag and changing it in the modal
		function change_image(src) {
			var img = "<img src=\"" + src + "\" class=\"modal-img\" width=100\% />";
			$("#gallery-modal .modal-image").html("").html(img);
		}

		// This function removes the img tag in the modal
		function remove_image() {
			$("#gallery-modal .modal-image").html("");
		}

		var len = $(".gallery-image").length;
		var src = $(this).data("src");
		var index = $(this).index(".gallery-image");

		function prev() {
			if (index === 0) {
				index = len - 1;
			} else {
				index -= 1;
			}
			var src = $($(".gallery-image").get(index)).data("src");
			change_image(src);
		}

		function next() {
			if (index === len - 1) {
				index = 0;
			} else {
				index += 1;
			}
			var src = $($(".gallery-image").get(index)).data("src");
			change_image(src);
		}

		// The browser is told to change the image when the modal is being shown
		$("#gallery-modal").on("show.bs.modal", function(){
			change_image(src);
		});

		// The browser is told to remove the image when the modal has been closed
		$("#gallery-modal").on("hidden.bs.modal", function(){
			remove_image();
		});

		$("#gallery-modal").keydown(function(e) {
			if (e.which == 37) {
				prev();
			} else if (e.which == 39) {
				next();
			}
		});

		$(".prev").click(function(e) {
			prev();
		});

		$(".next").click(function(e) {
			next();
		});

		// This event is triggered on when the gallery thumbnail is clicked. This should happen last
		// so that the events for the modal appearing are set up before this event occurs.
		$("#gallery-modal").modal();

		return 0;
	});
});

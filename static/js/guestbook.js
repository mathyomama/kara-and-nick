$(function() {
	
	// Need to setup some cookie stuff for ajax to work
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = $.trim(cookies[i]);
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}
	
	// More cookie and csrf stuff
	function csrfSafeMethod(method) {
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	function fix_side() {
		var $side_menu = $('#side-menu');
		// first reset the div so that the height and width are natural
		$side_menu.removeClass('fixed').css({
			"width": "auto",
			"height": "auto",
		});
		var div_height = $side_menu.height();
		// The 90 is from the top and bottom margins for the invitation and body
		var height = $("body").height() - 90, width = +$side_menu.width() + 30;
		console.log(height, width);
		if (height > div_height) {
			$side_menu.addClass('fixed').css({
				"width": width,
				"height": height,
			});
		}
	}

	// This will retrieve the data from the forms and even accounts for the checkbox nuance
	function get_form_data() {
		var inputs = $('form').find('.form-group').find('input, textarea');
		var data = {};
		inputs.each(function(index, input) {
			var $input = $(input);
			if ($input.attr('type') === 'checkbox') {
				data[$input.attr('name')] = $input.is(':checked');
			} else {
				data[$input.attr('name')] = $input.val();
			}
		});
		return data;
	}

	// Takes the jqXHR object and renders the form errors from it
	function render_form_errors(jqXHR) {
		// clear all errors by removing them
		$('.error').remove();
		var errors = $.parseJSON(jqXHR.responseText);
		$.each(errors, function(key, value) {
			$(document.createElement("p"))
			.addClass("error text-danger")
			.text(value)
			.prependTo($('#' + key + " div.error-message"));
		});
	}

	$('body').on('hidden.bs.modal', '.modal', function() {
		$(this).removeData('bs.modal');
	});

	$(window).resize(function(e) {
		e.preventDefault();
		resize_invitation();
		fix_side();
	});

	$('.clickable').click(function(e) {
		$(this).find('a')[0].click();
	});

	fix_side();

	// A function for returning the first "n" words
	$.addTemplateFormatter("firstNWords", function(value, count) {
		return value.split(/\s/).slice(0, count + 1).join(" ") + " ... ";
	});

	// This is the create a person function and it takes form data from the server
	function create_note(data) {
		var path = window.location.pathname,
			search = window.location.search;
		if ((path === "/guestbook/" && (search === "" || search === "?page=1")) || (path === "/guestbook/page/1/")) {
			$('#entries').loadTemplate($('#entry-template'), data, {prepend: true});
			$('.clickable').filter(':first').click(function(e) {
				$(this).find('a')[0].click();
			});
		} else if (/\/guestbook\/\w+\/edit\//.test(path)) {
			$("tbody").loadTemplate($('#edit-entry-template'), data, {prepend: true});
		}
	}

	// This is the update a person function and it takes form data from the server
	function update_note(data) {
		var container = $('#' + data['old_id']);
		container.find('td').filter(function(index) {
			if (index < 3) {
				return $(this);
			}
		}).each(function(index, elem) {
			var $elem = $(elem);
			var field = $elem.attr('class').split(' ')[0];
			if (field === "note") {
				$elem.text(data[field].split(/\s/).slice(0, 16).join(" ") + " ...");
			} else {
				$elem.text(data[field]);
			}
		});
		container.attr('id', data['id']);
	}

	// This is the delete a person function and it takes form data from the server
	function delete_note(data) {
		$('#' + data['old_id']).remove();
	}

	// This event is run after a new modal is loaded
	$('body').on('loaded.bs.modal', '.modal', function() {
		// These two function need to be run every time a new form pops up on the modal.
		var csrftoken = getCookie('csrftoken');

		$.ajaxSetup({
			beforeSend: function(xhr, settings) {
				if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
					xhr.setRequestHeader("X-CSRFToken", csrftoken);
				}
			}
		});

		// This will set up the event on the submit button so that the data reaches the server and approriate actions follow based on the status of the response
		$('#guestbook-form').submit(function(e) {
			e.preventDefault();
			var data = get_form_data();
			var form_url = $(this).attr('action');
			$.post(form_url, data, function(data) {
				action = data['status'];
				if (action === 'create') {
					create_note(data);
				} else if (action === 'update') {
					update_note(data);
				} else if (action === 'delete') {
					delete_note(data);
				}
				resize_invitation();
				$('#form-modal').modal('hide');
			}).fail(function(jqXHR, textStatus, errorThrown) {
				render_form_errors(jqXHR);
			});
		});
	});
});

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

	// This is a template formatter so that booleans show up on the template (mostly for create_person)
	$.addTemplateFormatter("booleanToString", function(value, template) {
		return String(value);
	});

	// This is the create a person function and it takes form data from the server
	function create_person(data) {
		$('#submissions').loadTemplate($('#submission-template'), data, {append: true});
	}

	// This is the update a person function and it takes form data from the server
	function update_person(data) {
		var container = $('#' + data['old_id']);
		container.find('div.rsvp-row').each(function(index, elem) {
			var $elem = $(elem);
			var field = $elem.attr('class').split(' ')[1];
			$elem.find('p').text(data[field]);
		});
		container.attr('id', data['id']);
	}

	// This is the delete a person function and it takes form data from the server
	function delete_person(data) {
		$('#' + data['old_id']).remove();
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

	// This event is triggered when the modal is hidden and will remove the data tied to that modal so a new one can take it's place
	$('body').on('hidden.bs.modal', '.modal', function() {
		$(this).removeData('bs.modal');
	});

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
		$('#person-form').submit(function(e) {
			e.preventDefault();
			var data = get_form_data();
			var form_url = $(this).attr('action');
			$.post(form_url, data, function(data) {
				data['updates'] = data['updates'] ? "yes" : "no";
				action = data['status'];
				if (action === 'create') {
					create_person(data);
				} else if (action === 'update') {
					update_person(data);
				} else if (action === 'delete') {
					delete_person(data);
				}
				resize_invitation();
				$('#form-modal').modal('hide');
			}).fail(function(jqXHR, textStatus, errorThrown) {
				render_form_errors(jqXHR);
			});
		});
	});
});

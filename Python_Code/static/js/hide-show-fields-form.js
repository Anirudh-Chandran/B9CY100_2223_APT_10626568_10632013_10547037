$("#user_type").change(function() {
			if ($(this).val() == "hospital") {
				$('#hospital_name').show();
				$('#h_name').attr('required','');
				$('#h_name').attr('data-error', 'This field is required.');
			} else {
				$('#hospital_name').hide();
				$('#h_name').removeAttr('required');
				$('#h_name').removeAttr('data-error');
				$('#vendor_name').hide();
				$('#v_name').removeAttr('required');
				$('#v_name').removeAttr('data-error');
			}
		});
		$("#user_type").trigger("change");
		
